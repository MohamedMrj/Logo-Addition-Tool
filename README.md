# Logo Addition Tool

The Logo Addition Tool is a Python script that allows you to easily add a logo to images and videos in a specified folder. It supports various image and video formats and can handle both transparent and non-transparent logos. The script utilizes the popular `Pillow` library for image processing and `moviepy` library for video editing.

## Features

- Add a logo to images (PNG, JPEG, GIF, etc.) and videos (MP4, AVI, MOV, etc.).
- Automatically handle transparent logos (PNG with alpha channel) for smooth blending.
- Resize the logo to a desired size while maintaining aspect ratio.
- Position the logo on the media (e.g., top left corner).
- Save the processed media with the logo in the output directory.

## Requirements

- Python 3.x
- `Pillow` library (for image processing)
- `moviepy` library (for video editing)

You can install the required libraries using the following command:

```
pip install Pillow moviepy
```

## Usage

1. Clone or download this repository to your local machine.

2. Prepare your logo image (preferably in PNG format with a transparent background) and place it in a location accessible to the script.

3. Create a folder containing the images and videos to which you want to add the logo.

4. Open the `logoOnImages.py` script using a text editor.

5. Update the following variables in the script with appropriate paths:

   ```python
   media_folder = 'path/to/your/media_folder'  # Folder containing your images/videos
   logo_path = 'path/to/your/logo.png'         # Path to the logo image
   output_dir = 'path/to/your/output_dir'      # Output directory for processed media
   ```

6. Save the changes and close the text editor.

7. Open a terminal or command prompt and navigate to the location of the `logoOnImages.py` script.

8. Run the script using the following command:

   ```
   python logoOnImages.py
   ```

   The script will process the images and videos in the specified `media_folder`, add the logo, and save the processed media with the logo in the `output_dir`.

## Example

Here's an example usage of the Logo Addition Tool:

```python
# Example usage
media_folder = 'C:/Users/YourUserName/Pictures/Media'      # Folder containing your images/videos
logo_path = 'C:/Users/YourUserName/Pictures/logo.png'      # Path to the logo image
output_dir = 'C:/Users/YourUserName/Pictures/Processed'   # Output directory for processed media

add_logo_to_media(media_folder, logo_path, output_dir)
```

In this example, the script will process the media in the `Media` folder, add the `logo.png` to each image and video, and save the processed media with the logo in the `Processed` folder.

Feel free to customize the paths and sizes according to your specific requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy adding your logo to images and videos easily with the Logo Addition Tool! If you encounter any issues or have suggestions for improvements, please feel free to contribute or create an issue. Happy logo editing! 🎉
