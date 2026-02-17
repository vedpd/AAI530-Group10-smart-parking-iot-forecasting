# Fixed Export and Save Dashboard Components
print("💾 Exporting Dashboard Components...")

if df_final is not None:
    # Create dashboard directory
    dashboard_dir = Path(r"C:\Users\vedp3\OneDrive\Desktop\AAI_530_Final_Project\AAI530-Group10-smart-parking-iot-forecasting\dashboard")
    dashboard_dir.mkdir(exist_ok=True)
    
    # Save key metrics summary
    actual_data = df_final[df_final['record_type'] == 'actual']
    forecast_data = df_final[df_final['record_type'] == 'forecast']
    
    # Create summary statistics
    summary_stats = {
        'dataset_info': {
            'total_records': len(df_final),
            'unique_segments': df_final['segment_id'].nunique(),
            'date_range_start': df_final['timestamp'].min().isoformat(),
            'date_range_end': df_final['timestamp'].max().isoformat(),
            'record_types': df_final['record_type'].value_counts().to_dict(),
            'model_sources': df_final['model_source'].value_counts().to_dict()
        },
        'occupancy_stats': {
            'avg_occupancy_rate': actual_data['occupancy_rate'].mean() if len(actual_data) > 0 else 0,
            'max_occupancy_rate': actual_data['occupancy_rate'].max() if len(actual_data) > 0 else 0,
            'min_occupancy_rate': actual_data['occupancy_rate'].min() if len(actual_data) > 0 else 0,
            'total_capacity': actual_data['capacity'].sum() if len(actual_data) > 0 else 0,
            'total_occupied': actual_data['occupied'].sum() if len(actual_data) > 0 else 0
        }
    }
    
    if len(forecast_data) > 0:
        # Model performance summary
        model_summary = forecast_data.groupby('model_source').agg({
            'mae': ['mean', 'std', 'count'],
            'rmse': ['mean', 'std'],
            'mape': ['mean', 'std']
        }).round(4)
        
        model_summary.columns = ['_'.join(col).strip() for col in model_summary.columns.values]
        summary_stats['model_performance'] = model_summary.to_dict()
    
    # Save summary as JSON
    import json
    try:
        with open(dashboard_dir / "dashboard_summary.json", 'w') as f:
            json.dump(summary_stats, f, indent=2, default=str)
        print("✅ Summary statistics saved")
    except Exception as e:
        print(f"⚠️ Error saving JSON: {e}")
    
    # Save key dataframes as CSV
    try:
        if len(actual_data) > 0:
            actual_data.to_csv(dashboard_dir / "actual_data.csv", index=False)
            print("✅ Actual data saved")
        
        if len(forecast_data) > 0:
            forecast_data.to_csv(dashboard_dir / "forecast_data.csv", index=False)
            print("✅ Forecast data saved")
    except Exception as e:
        print(f"⚠️ Error saving CSV files: {e}")
    
    # Create segment performance report
    if len(actual_data) > 0:
        try:
            segment_report = actual_data.groupby('segment_id').agg({
                'occupancy_rate': ['mean', 'std', 'min', 'max'],
                'capacity': 'first',
                'occupied': ['mean', 'max']
            }).round(4)
            
            segment_report.columns = ['_'.join(col).strip() for col in segment_report.columns.values]
            segment_report = segment_report.reset_index()
            segment_report.to_csv(dashboard_dir / "segment_performance.csv", index=False)
            print("✅ Segment performance saved")
        except Exception as e:
            print(f"⚠️ Error saving segment report: {e}")
    
    # Create simple HTML dashboard (fixed string handling)
    try:
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Smart Parking Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .metric {{ background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .chart {{ margin: 20px 0; }}
        .header {{ background: #2c3e50; color: white; padding: 20px; text-align: center; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚗 Smart Parking Dashboard</h1>
        <p>Real-time parking analytics and insights</p>
    </div>
    
    <div class="metric">
        <h2>📊 Key Metrics</h2>
        <p><strong>Total Records:</strong> {summary_stats['dataset_info']['total_records']:,}</p>
        <p><strong>Unique Segments:</strong> {summary_stats['dataset_info']['unique_segments']:,}</p>
        <p><strong>Average Occupancy:</strong> {summary_stats['occupancy_stats']['avg_occupancy_rate']:.1%}</p>
        <p><strong>Date Range:</strong> {summary_stats['dataset_info']['date_range_start']} to {summary_stats['dataset_info']['date_range_end']}</p>
    </div>
    
    <div class="chart">
        <h2>📈 Record Types Distribution</h2>
        <div id="record-types-chart"></div>
    </div>
    
    <div class="chart">
        <h2>🤖 Model Sources Distribution</h2>
        <div id="model-sources-chart"></div>
    </div>
    
    <script>
        // Record Types Chart
        var recordData = [{{
            values: {list(summary_stats['dataset_info']['record_types'].values())},
            labels: {list(summary_stats['dataset_info']['record_types'].keys())},
            type: 'pie',
            title: 'Record Types'
        }}];
        Plotly.newPlot('record-types-chart', recordData, {{title: 'Record Types Distribution'}});
        
        // Model Sources Chart
        var modelData = [{{
            values: {list(summary_stats['dataset_info']['model_sources'].values())},
            labels: {list(summary_stats['dataset_info']['model_sources'].keys())},
            type: 'pie',
            title: 'Model Sources'
        }}];
        Plotly.newPlot('model-sources-chart', modelData, {{title: 'Model Sources Distribution'}});
    </script>
    
    <div style="text-align: center; margin-top: 50px; color: #666;">
        <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Smart Parking IoT System - Dashboard</p>
    </div>
</body>
</html>"""
        
        with open(dashboard_dir / "dashboard.html", "w", encoding='utf-8') as f:
            f.write(html_content)
        print("✅ HTML dashboard saved")
    except Exception as e:
        print(f"⚠️ Error saving HTML: {e}")
    
    # Final summary
    print(f"\n🚀 Dashboard export completed!")
    print(f"📁 Location: {dashboard_dir}")
    print(f"📄 Files created:")
    
    files_created = []
    if (dashboard_dir / "dashboard_summary.json").exists():
        files_created.append("📊 dashboard_summary.json")
    if (dashboard_dir / "actual_data.csv").exists():
        files_created.append("📈 actual_data.csv")
    if (dashboard_dir / "forecast_data.csv").exists():
        files_created.append("🔮 forecast_data.csv")
    if (dashboard_dir / "segment_performance.csv").exists():
        files_created.append("🏢 segment_performance.csv")
    if (dashboard_dir / "dashboard.html").exists():
        files_created.append("🌐 dashboard.html")
    
    for file in files_created:
        print(f"   {file}")
    
    if (dashboard_dir / "dashboard.html").exists():
        print(f"\n🌐 Open dashboard in browser:")
        print(f"   file://{(dashboard_dir / 'dashboard.html').absolute()}")
    
else:
    print("⚠️ No data available for export")
