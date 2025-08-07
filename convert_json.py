#!/usr/bin/env python3
"""
Simple script to run the JSON to CSV converter using compiled frenz_utils package
This is a simplified version for quick testing with optimized performance
"""

import os
import sys

# Import from compiled frenz_utils package
try:
    from frenz_utils.json_to_csv_converter import JsonToCsvConverter, find_json_files
    print("✅ Using compiled frenz_utils package (optimized)")
except ImportError:
    # Fallback to source files if compiled package not available
    try:
        from json_to_csv_converter import JsonToCsvConverter, find_json_files
        print("⚠️  Using source files (not optimized)")
    except ImportError:
        print("❌ Error: Could not import JsonToCsvConverter")
        sys.exit(1)

def main():
    """
    Simple main function with hardcoded values for quick testing
    Uses compiled frenz_utils package for optimal performance
    """
    # Configuration - modify these values as needed
    product_key = "xxxxx"
    
    print("🚀 Starting JSON to CSV conversion with compiled package...")
    print(f"🔐 Product key: {product_key[:20]}...")
    
    try:
        # Initialize converter with product key validation
        converter = JsonToCsvConverter(product_key)
        
        # Find JSON files in current directory
        json_files = find_json_files()
        
        if not json_files:
            print("❌ No JSON files found in current directory")
            return 1
        
        print(f"🔍 Found {len(json_files)} JSON file(s):")
        for file in json_files:
            print(f"   - {file}")
        
        # Process files
        if len(json_files) == 1:
            # Single file conversion
            json_file = json_files[0]
            print(f"\n📄 Processing: {json_file}")
            
            csv_path = converter.convert_json_to_csv(json_file)
            
            if csv_path:
                print(f"\n🎉 Completed! CSV file created: {csv_path}")
                return 0
            else:
                print("\n❌ Could not convert JSON file to CSV")
                return 1
        else:
            # Multiple file conversion
            print(f"\n🔄 Converting {len(json_files)} files...")
            results = converter.convert_multiple_files(json_files)
            
            # Print summary
            print("\n📊 CONVERSION SUMMARY:")
            print("=" * 60)
            success_count = 0
            for json_file, csv_path in results.items():
                if csv_path:
                    print(f"✅ {json_file} → {csv_path}")
                    success_count += 1
                else:
                    print(f"❌ {json_file} → Failed")
            
            print("=" * 60)
            print(f"✅ Successfully converted: {success_count}/{len(json_files)} files")
            
            return 0 if success_count == len(json_files) else 1
        
    except ValueError as e:
        print(f"❌ Validation Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 