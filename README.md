# 🎥 Video Compressor - Facebook Style with FFmpeg 🚀

This Python script helps you **compress multiple videos in parallel** using settings similar to Facebook's compression standards, via `FFmpeg`. Perfect if you have lots of large video files and want to shrink them down without killing the quality 💡.

---

## 📦 Features

✅ Compresses videos to 720p resolution  
✅ Optimized bitrates for smaller file sizes  
✅ Keeps original folder structure  
✅ Multi-threaded processing (super fast!)  
✅ Supports multiple formats: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`

---

## 🛠️ Requirements

- Python 3.x 🐍  
- [FFmpeg](https://ffmpeg.org/) installed and accessible in your system

---

## 🔧 How to Use

1. **Install FFmpeg** and make sure the executable is accessible, like:  
   `C:\ffmpeg\bin\ffmpeg.exe`

2. **Edit the paths** at the bottom of the script:
   ```python
   input_folder = r"YOUR\PATH\TO\INPUT\VIDEOS"
   output_folder = r"YOUR\PATH\TO\SAVE\COMPRESSED"
   ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
