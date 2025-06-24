#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import platform

def build_executable():
    """
    Build an executable file for the Hand Gesture Presentation Controller
    using PyInstaller.
    """
    print("Starting build process for Hand Gesture Presentation Controller...")
    
    # First, ensure pathlib is uninstalled as it's incompatible with PyInstaller
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", "pathlib"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Successfully uninstalled pathlib package")
    except subprocess.CalledProcessError as e:
        print(f"Note: Could not uninstall pathlib: {e.stderr}")
    
    # Determine the operating system
    os_name = platform.system()
    print(f"Building for {os_name} platform")
    
    # Create a spec file with optimized settings
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['cv2', 'mediapipe', 'numpy', 'fitz', 'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pathlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='HandGestureController',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    
    # Write the spec file
    with open("HandGestureController.spec", "w") as f:
        f.write(spec_content)
    
    print("Created PyInstaller spec file")
    
    # Create README_executable.md file
    with open("README_executable.md", "w") as f:
        f.write("""# Hand Gesture Presentation Controller - Executable

This is the standalone executable version of the Hand Gesture Presentation Controller.

## Requirements

- A webcam
- A keyboard for fallback controls

## How to Use

1. Double-click the HandGestureController executable file
2. Use the file dialog to open a PDF file
3. Use hand gestures to control the presentation:
   - Thumb only [1,0,0,0,0] - Previous Slide
   - Four fingers (no thumb) [0,1,1,1,1] - Next Slide
   - All five fingers [1,1,1,1,1] - Clear Annotations
   - Index finger only [0,1,0,0,0] - Draw
   - Index + Middle fingers [0,1,1,0,0] - Pointer
   - Index + Middle + Ring [0,1,1,1,0] - Erase Last Annotation
   - Thumb + Index close together - Zoom In
   - Thumb + Index far apart - Zoom Out
   - Thumb + Index + Middle - Reset Zoom

## Keyboard Controls

- ESC: Toggle fullscreen mode
- Q: Quit the application
- H: Show help dialog
- O: Open a new file
- S: Save current slide as image

## Troubleshooting

If you encounter any issues with webcam detection, try disconnecting and reconnecting your webcam.

If the application crashes on startup, make sure you have a working webcam connected to your system.

## License

This software is provided as-is without any warranty. Use at your own risk.
""")
    
    print("Created README_executable.md with instructions for using the executable.")
    
    # Run PyInstaller to build the executable
    print("Running PyInstaller (this may take several minutes)...")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "PyInstaller", "HandGestureController.spec", "--clean"],
            check=True,
            capture_output=True,
            text=True
        )
        print("PyInstaller completed successfully")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running PyInstaller:")
        print(e.stderr)
        return False
    
    # Check if the executable was created
    if os_name == "Windows":
        exe_path = os.path.join("dist", "HandGestureController.exe")
    else:
        exe_path = os.path.join("dist", "HandGestureController")
    
    if os.path.exists(exe_path):
        print(f"Successfully built executable at: {exe_path}")
        return True
    else:
        print("Failed to build executable")
        return False

if __name__ == "__main__":
    success = build_executable()
    if success:
        print("Build completed successfully")
        print("You can find the executable in the 'dist' folder")
    else:
        print("Build failed")
        sys.exit(1)