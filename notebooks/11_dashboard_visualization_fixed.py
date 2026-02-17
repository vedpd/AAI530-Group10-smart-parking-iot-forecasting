# Fixed Interactive Dashboard with Filters
print("🎛️ Creating Interactive Dashboard...")

if df_final is not None:
    # Create interactive dashboard components
    import ipywidgets as widgets
    from IPython.display import display, clear_output
    import time
    
    # Create filter widgets with proper setup
    model_options = ['All'] + list(df_final['model_source'].dropna().unique())
    record_type_options = ['All'] + list(df_final['record_type'].unique())
    
    date_range_slider = widgets.SelectionSlider(
        options=['Last 24 Hours', 'Last 7 Days', 'Last 30 Days', 'All Data'],
        value='Last 7 Days',
        description='Time Range:',
        disabled=False,
        layout={'width': '400px'}
    )
    
    model_filter = widgets.SelectMultiple(
        options=model_options,
        value=['All'],
        description='Models:',
        disabled=False,
        layout={'width': '300px'}
    )
    
    segment_filter = widgets.Text(
        value='',
        placeholder='Enter segment IDs (comma-separated)',
        description='Segments:',
        disabled=False,
        layout={'width': '300px'}
    )
    
    record_type_filter = widgets.SelectMultiple(
        options=record_type_options,
        value=['All'],
        description='Record Types:',
        disabled=False,
        layout={'width': '300px'}
    )
    
    # Add a refresh button
    refresh_button = widgets.Button(
        description='🔄 Refresh Dashboard',
        button_style='primary',
        layout={'width': '200px'}
    )
    
    # Create output widget
    output = widgets.Output()
    
    def update_dashboard(change=None):
        """Update dashboard with error handling and performance optimization"""
        try:
            with output:
                clear_output(wait=True)
                print("🔄 Updating dashboard...")
                start_time = time.time()
                
                # Filter data based on selections
                filtered_data = df_final.copy()
                
                # Time range filter - use actual data end date instead of max()
                if date_range_slider.value != 'All Data':
                    data_end_time = filtered_data['timestamp'].max()
                    if date_range_slider.value == 'Last 24 Hours':
                        cutoff_time = data_end_time - timedelta(hours=24)
                    elif date_range_slider.value == 'Last 7 Days':
                        cutoff_time = data_end_time - timedelta(days=7)
                    elif date_range_slider.value == 'Last 30 Days':
                        cutoff_time = data_end_time - timedelta(days=30)
                    filtered_data = filtered_data[filtered_data['timestamp'] >= cutoff_time]
                
                # Model filter with proper handling
                if 'All' not in model_filter.value and len(model_filter.value) > 0:
                    filtered_data = filtered_data[filtered_data['model_source'].isin(model_filter.value)]
                
                # Segment filter with better error handling
                if segment_filter.value.strip():
                    segment_ids = [s.strip() for s in segment_filter.value.split(',') if s.strip()]
                    if segment_ids:
                        # Handle both string and numeric segment IDs
                        if filtered_data['segment_id'].dtype == 'object':
                            filtered_data = filtered_data[filtered_data['segment_id'].isin(segment_ids)]
                        else:
                            try:
                                segment_ids_numeric = [float(s) for s in segment_ids]
                                filtered_data = filtered_data[filtered_data['segment_id'].isin(segment_ids_numeric)]
                            except ValueError:
                                print(f"⚠️ Invalid segment IDs: {segment_ids}")
                
                # Record type filter
                if 'All' not in record_type_filter.value and len(record_type_filter.value) > 0:
                    filtered_data = filtered_data[filtered_data['record_type'].isin(record_type_filter.value)]
                
                print(f"📊 Filtered Dataset: {len(filtered_data):,} records")
                
                # Create filtered visualizations
                if len(filtered_data) > 0:
                    # Quick stats
                    print(f"📈 Quick Stats:")
                    print(f"   Time Range: {filtered_data['timestamp'].min()} to {filtered_data['timestamp'].max()}")
                    print(f"   Segments: {filtered_data['segment_id'].nunique()}")
                    print(f"   Record Types: {filtered_data['record_type'].value_counts().to_dict()}")
                    
                    # Sample data for performance if too large
                    if len(filtered_data) > 10000:
                        viz_data = filtered_data.sample(n=10000, random_state=42)
                        print(f"   📊 Showing sample of 10,000 records for performance")
                    else:
                        viz_data = filtered_data
                    
                    # Create filtered time series
                    try:
                        fig_filtered = px.line(
                            viz_data,
                            x='timestamp',
                            y='occupancy_rate',
                            color='model_source',
                            title='Filtered Occupancy Rate Over Time',
                            facet_col='record_type'
                        )
                        
                        fig_filtered.update_layout(
                            height=600,
                            showlegend=True,
                            hovermode='x unified'
                        )
                        fig_filtered.show()
                    except Exception as e:
                        print(f"⚠️ Error creating time series: {str(e)}")
                    
                    # Create error analysis for forecast data
                    forecast_filtered = filtered_data[filtered_data['record_type'] == 'forecast']
                    if len(forecast_filtered) > 0:
                        try:
                            model_errors = forecast_filtered.groupby('model_source')['mae'].mean().sort_values()
                            
                            fig_errors = px.bar(
                                x=model_errors.index,
                                y=model_errors.values,
                                title='Model Error Comparison (Filtered Data)',
                                labels={'x': 'Model', 'y': 'Average MAE'},
                                color=model_errors.values,
                                color_continuous_scale='Viridis'
                            )
                            
                            fig_errors.update_layout(height=400)
                            fig_errors.show()
                        except Exception as e:
                            print(f"⚠️ Error creating error chart: {str(e)}")
                    
                    # Performance summary
                    end_time = time.time()
                    print(f"⚡ Dashboard updated in {end_time - start_time:.2f} seconds")
                else:
                    print("⚠️ No data matches the selected filters")
                    
        except Exception as e:
            print(f"❌ Error updating dashboard: {str(e)}")
            print("💡 Try adjusting your filters")
    
    # Register update functions
    date_range_slider.observe(update_dashboard, names='value')
    model_filter.observe(update_dashboard, names='value')
    segment_filter.observe(update_dashboard, names='value')
    record_type_filter.observe(update_dashboard, names='value')
    refresh_button.on_click(update_dashboard)
    
    # Display dashboard with better layout
    print("🎛️ Interactive Dashboard Controls:")
    
    # Create control panel
    controls = widgets.VBox([
        widgets.HTML("<h3>📊 Filter Controls</h3>"),
        widgets.HBox([date_range_slider, refresh_button]),
        widgets.HBox([model_filter, record_type_filter]),
        segment_filter
    ])
    
    display(controls)
    
    print("📊 Dashboard Output:")
    display(output)
    
    # Initialize with default view
    update_dashboard(None)
    
    print("✅ Interactive dashboard created!")
    print("💡 Use the controls above to filter data and update visualizations")
else:
    print("⚠️ No data available for interactive dashboard")
