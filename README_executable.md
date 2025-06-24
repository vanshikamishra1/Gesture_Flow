# Hand Gesture Presentation Controller - Executable

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
