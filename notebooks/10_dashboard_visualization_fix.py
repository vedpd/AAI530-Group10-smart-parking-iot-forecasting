# Fix for heatmap TypeError in dashboard notebook
# Replace the problematic lines in Cell 6 with this code:

# Convert column indices to integers and map to day names
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
available_days = []

for col in heatmap_data.columns:
    try:
        day_idx = int(col)
        if 0 <= day_idx < len(day_names):
            available_days.append(day_names[day_idx])
        else:
            available_days.append(f"Day {col}")
    except (ValueError, TypeError):
        available_days.append(str(col))

# Create heatmap with correct dimensions
fig_heatmap = px.imshow(
    heatmap_data,
    title=f'Occupancy Heatmap - Segment {segment_id}',
    labels=dict(x="Day of Week", y="Hour of Day", color="Occupancy Rate"),
    x=available_days,
    color_continuous_scale='RdYlGn',
    aspect="auto"
)

fig_heatmap.update_layout(height=400)
fig_heatmap.show()
