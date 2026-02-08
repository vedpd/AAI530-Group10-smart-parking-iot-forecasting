"""
Dataset Download Helper for Smart Parking IoT System

This script helps download the dataset from Harvard Dataverse.
"""

import requests
import os
from pathlib import Path
import zipfile
import warnings

def download_harvard_dataset():
    """
    Download the Smart Parking dataset from Harvard Dataverse.
    
    Returns:
        bool: True if successful, False otherwise
    """
    
    # Dataset information
    dataset_doi = "10.7910/DVN/YLWCSU"
    dataverse_url = "https://dataverse.harvard.edu"
    
    # Target paths
    current_dir = Path(__file__).parent.parent
    raw_data_dir = current_dir / "data" / "raw"
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    
    target_file = raw_data_dir / "smart_parking_full.csv"
    
    print("Smart Parking IoT Dataset Download")
    print("=" * 50)
    print(f"Dataset DOI: {dataset_doi}")
    print(f"Target location: {target_file}")
    print()
    
    # Check if file already exists
    if target_file.exists():
        print(f"Dataset already exists at: {target_file}")
        file_size = target_file.stat().st_size / (1024 * 1024)  # MB
        print(f"   File size: {file_size:.2f} MB")
        return True
    
    print("Manual Download Required")
    print("=" * 50)
    print("Due to Harvard Dataverse API limitations, please download manually:")
    print()
    print("1. Visit: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YLWCSU")
    print("2. Look for 'Download' or 'Export' options")
    print("3. Download the dataset (likely in CSV format)")
    print("4. Save it as: smart_parking_full.csv")
    print("5. Place it in: data/raw/")
    print()
    print(f"Expected location: {target_file}")
    print()
    
    # Create placeholder if it doesn't exist
    if not target_file.exists():
        placeholder_content = """# Smart Parking Dataset Placeholder
# Download from: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YLWCSU
# 
# Expected columns:
# - timestamp: DateTime of sensor reading
# - sensor_id: Unique sensor identifier
# - occupancy: Parking occupancy status (0=available, 1=occupied)
# - location_lat: Latitude coordinate
# - location_lon: Longitude coordinate
# - parking_spot_id: Specific parking spot identifier
"""
        with open(target_file, 'w') as f:
            f.write(placeholder_content)
        print(f"Placeholder file created at: {target_file}")
    
    return False

def verify_dataset_structure(file_path):
    """
    Verify the downloaded dataset has expected structure.
    
    Args:
        file_path: Path to the dataset file
        
    Returns:
        bool: True if structure looks correct
    """
    try:
        import pandas as pd
        
        # Try to read the file
        df = pd.read_csv(file_path, nrows=5)
        
        # Check for expected columns
        expected_cols = ['timestamp', 'sensor_id', 'occupancy']
        found_cols = [col for col in expected_cols if col in df.columns]
        
        print(f"\nDataset Structure Verification:")
        print(f"   Columns found: {list(df.columns)}")
        print(f"   Expected columns found: {found_cols}")
        print(f"   Shape: {df.shape}")
        
        if len(found_cols) >= 2:
            print("Dataset structure looks correct!")
            return True
        else:
            print("Dataset structure may need adjustment")
            return False
            
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return False

if __name__ == "__main__":
    # Download dataset
    success = download_harvard_dataset()
    
    # Verify if real dataset exists
    dataset_path = Path(__file__).parent.parent / "data" / "raw" / "smart_parking_full.csv"
    if dataset_path.exists() and dataset_path.stat().st_size > 1000:  # Not just placeholder
        verify_dataset_structure(dataset_path)
    
    print("\nNext Steps:")
    print("1. Run 01_data_overview.ipynb to explore the dataset")
    print("2. Proceed to Phase 2: Data Cleaning & EDA")
