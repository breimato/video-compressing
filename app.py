import os
import subprocess
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


def compress_video(args):
    """
    Compresses a video to Facebook-like specifications using FFmpeg.

    :param args: Tuple containing (input_path, output_path, ffmpeg_path)
    """
    input_path, output_path, ffmpeg_path = args

    # Check if input file exists
    if not os.path.isfile(input_path):
        print(f"The input file {input_path} does not exist!")
        return

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # FFmpeg command
    ffmpeg_command = [
        ffmpeg_path,
        "-y",
        "-i", input_path,
        "-vf", "scale=1280:720",
        "-b:v", "1167824",
        "-b:a", "48023",
        "-r", "25",
        "-c:v", "libx264",
        "-preset", "fast",
        "-c:a", "aac",
        "-q:a", "2",
        output_path
    ]

    try:
        print(f"Started compressing: {os.path.basename(input_path)}")
        start_time = time.time()
        subprocess.run(ffmpeg_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed_time = time.time() - start_time
        print(
            f"Compression successful! Compressed video {os.path.basename(input_path)} saved at {output_path} (took {elapsed_time:.2f} seconds)")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during compression of {input_path}: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred with {input_path}: {e}")
        return False


def find_video_files(directory):
    """
    Recursively find all video files in a directory and its subdirectories.

    :param directory: Path to the directory to search
    :return: List of tuples (video_path, relative_path)
    """
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.wmv')
    video_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(video_extensions):
                full_path = os.path.join(root, file)
                # Get the path relative to the input directory
                rel_path = os.path.relpath(full_path, directory)
                video_files.append((full_path, rel_path))

    return video_files


def process_videos(input_folder, output_folder, ffmpeg_path, max_threads=10):
    """
    Process multiple videos in parallel while preserving folder structure.

    :param input_folder: Path to folder containing videos to compress
    :param output_folder: Path to folder where compressed videos will be saved
    :param ffmpeg_path: Path to FFmpeg executable
    :param max_threads: Maximum number of parallel processes
    """
    # Find all video files in the input folder and its subdirectories
    video_files = find_video_files(input_folder)

    if not video_files:
        print(f"No video files found in {input_folder}")
        return

    # Prepare arguments for each video
    args_list = []
    for full_path, rel_path in video_files:
        output_path = os.path.join(output_folder, rel_path)
        args_list.append((full_path, output_path, ffmpeg_path))

    # Print total number of videos to process
    total_videos = len(args_list)
    print(f"Starting parallel compression of {total_videos} videos...")

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit all tasks and get futures
        futures = [executor.submit(compress_video, args) for args in args_list]

        # Wait for all tasks to complete
        completed = 0
        successful = 0
        for future in futures:
            result = future.result()
            completed += 1
            if result:
                successful += 1
            print(f"Progress: {completed}/{total_videos} videos processed")

    total_time = time.time() - start_time
    failed = total_videos - successful

    print("\n" + "=" * 50)
    print(f"Compression Summary:")
    print(f"Total videos processed: {total_videos}")
    print(f"Successfully compressed: {successful}")
    print(f"Failed to compress: {failed}")
    print(f"Total processing time: {total_time:.2f} seconds")
    print("=" * 50)


if __name__ == "__main__":
    input_folder = r""  # Folder with original videos
    output_folder = r""  # Folder for compressed videos
    ffmpeg_path = r""

    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(ffmpeg_path):
        print(f"Error: FFmpeg no encontrado en {ffmpeg_path}")
        print("Por favor, verifica la ruta de FFmpeg o instálalo si no lo tienes")
        exit(1)

    # Process all videos in the input folder
    process_videos(input_folder, output_folder, ffmpeg_path, max_threads=10) # Adjust max_threads if needed