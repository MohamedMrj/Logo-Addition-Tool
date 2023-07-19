# Logo Addition Tool

The Logo Addition Tool is a Python script that allows you to add a logo to images and videos in a specified media folder. The script uses the Python Imaging Library (PIL) and the moviepy library to process images and videos, respectively.

## Features

- Add a logo to images (JPEG, GIF, PNG, JPG, and WebP formats) and videos (MP4, AVI, MOV formats) in the media folder.
- Customize the position and size of the logo on images and videos.
- Support for converting WebP images to JPEG for compatibility.

## Requirements

- Python 3.x
- PIL (Python Imaging Library) - Install it using `pip install pillow`
- moviepy - Install it using `pip install moviepy`

## How to Use

1. Clone the repository or download the `logo_addition.py` script to your local machine.

2. Install the required libraries using the following command (if not already installed):

   ```
   pip install pillow moviepy
   ```

3. Place your logo image file (e.g., `logo.png`) and the media files (images and videos) you want to process in a folder.

4. Update the script with the paths to your media folder and the logo image file, as well as the desired output directory. Open the script file and modify the following variables:

   ```python
   media_folder = 'path/to/your/media/folder'  # Folder containing your images/videos
   logo_path = 'path/to/your/logo.png'  # Path to the logo image
   output_dir = 'path/to/your/output/directory'  # Output directory for processed media
   ```

5. Customize the logo position and size (optional). You can adjust the position and size of the logo in the `add_logo_to_media` function. By default, the logo is placed at the top-left corner with a size of 100x100 pixels for images and videos.

6. Run the script:

   ```
   python logo_addition.py
   ```

7. The script will process each image and video in the specified media folder, add the logo with the desired position and size, and save the processed media files in the output directory with "_logo" added to their filenames.

## Supported Media Formats

### Images

- JPEG (.jpeg, .jpg)
- GIF (.gif)
- PNG (.png)
- JPG (.jpg)
- WebP (.webp) - WebP images will be converted to JPEG format for compatibility.

### Videos

- MP4 (.mp4)
- AVI (.avi)
- MOV (.mov)

Please ensure that your images and videos are in one of the supported formats for the script to work correctly.

## License

This script is licensed under the [MIT License](LICENSE).

## Disclaimer

Please use this script responsibly and ensure that you have the necessary rights to add the logo to the media files in the specified folder. The author of this script is not responsible for any misuse or violation of copyrights.

Feel free to reach out for any questions or improvements!
