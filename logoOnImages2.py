import os
from PIL import Image
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def add_logo_to_media(media_folder, logo_path, output_dir):
    """
    Add a logo to images and videos in the specified media folder.

    Parameters:
        - media_folder (str): The path to the folder containing images and videos.
        - logo_path (str): The path to the logo image file.
        - output_dir (str): The path to the directory where the processed media files will be saved.
    """

    # Open the logo image with an alpha channel (RGBA)
    if os.path.splitext(logo_path)[1].lower() == '.png':
        logo = Image.open(logo_path)
    else:
        logo = Image.open(logo_path).convert("RGBA")

    # Lists of supported image and video formats
    image_formats = ['.jpeg', '.gif', '.png', '.jpg', '.webp']
    video_formats = ['.mp4', '.avi', '.mov']

    # Check if there are any videos in the folder
    has_videos = any(filename.lower().endswith(tuple(video_formats)) for filename in os.listdir(media_folder))

    # Loop through each file in the media folder
    for filename in os.listdir(media_folder):
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in image_formats:
            # Process image files
            image_path = os.path.join(media_folder, filename)
            image = Image.open(image_path).convert("RGBA") 

            # Convert webp images to JPG format
            if file_ext == '.webp':
                # Generate the output filename by changing the extension to '.jpg'
                output_filename = os.path.splitext(filename)[0] + '.jpg'
                output_path = os.path.join(output_dir, output_filename)

                # Convert the image to RGB and save it as JPG
                image = image.convert("RGB")
                image.save(output_path, "JPEG")

                # Re-open the converted image with alpha channel (RGBA)
                image = Image.open(output_path).convert("RGBA")
            else:
                # For non-webp images, use the original filename and output path
                output_filename = filename
                output_path = os.path.join(output_dir, output_filename)

            # Resize the logo to a desired size (e.g., 100x100)
            logo_resized = logo.resize((100, 100))

            # Calculate the position for the logo (e.g., top left corner)
            position = (0, 0)

            # Paste the logo onto the image
            image.paste(logo_resized, position, logo_resized)

            # Save the image with the logo
            image.save(output_path, "PNG")

        elif file_ext in video_formats and has_videos:
            # Process video files
            video_path = os.path.join(media_folder, filename)

            # Open the video clip
            video_clip = VideoFileClip(video_path)

            # Convert the logo to an ImageClip
            logo_clip = ImageClip(logo_path).set_duration(video_clip.duration)

            # Resize the logo if needed (height=100, width will be adjusted to maintain aspect ratio)
            logo_clip = logo_clip.resize(height=100)

            # Set the position for the logo (e.g., top left corner)
            position = (0, 0)

            # Composite the logo onto the video
            composite_clip = CompositeVideoClip([video_clip, logo_clip.set_position(position)])

            # Generate the output filename by adding '_logo' to the original filename
            output_filename = os.path.splitext(filename)[0] + '_logo' + os.path.splitext(filename)[1]
            output_path = os.path.join(output_dir, output_filename)

            # Save the video with the logo using libx264 codec for video and aac codec for audio
            composite_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
media_folder = 'path/to/your/media/folder'  # Folder containing your images/videos
logo_path = 'path/to/your/logo.png'  # Path to the logo image
output_dir = 'path/to/your/output/directory'  # Output directory for processed media


add_logo_to_media(media_folder, logo_path, output_dir)
