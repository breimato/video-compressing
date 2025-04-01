# 🎥 Video Compressor - Facebook Style with FFmpeg 🚀

This Python script helps you **compress multiple videos in parallel** using Facebook-style compression settings via `FFmpeg`. Ideal if you’ve got lots of large video files and want to shrink them down without destroying the quality 💡.

---

## 📦 Features

✅ Compresses videos to 720p resolution  
✅ Optimized bitrates for smaller file sizes  
✅ Keeps original folder structure  
✅ Multi-threaded processing (super fast!)  
✅ Supports multiple formats: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`

---

## 🛠️ Requirements

- **Python 3.x**  
- **[FFmpeg](https://ffmpeg.org/)** installed and accessible

---

## 🔧 How to Use

1. **Install FFmpeg** and confirm the executable path, for example:
   
       C:\ffmpeg\bin\ffmpeg.exe

2. **Edit the script** (at the bottom) to point to your correct paths:

       if __name__ == "__main__":
           input_folder = r"C:\Path\To\OriginalVideos"
           output_folder = r"C:\Path\To\CompressedVideos"
           ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
           # Then call process_videos()

3. **Run the script** in a terminal or command prompt:

       python your_script_name.py

---

## ⚙️ How It Works

- Recursively finds all video files in your input folder (and any subfolders).
- **Compresses** each video with:
  - Resolution: `1280x720`
  - Video bitrate: ~`1.1 Mbps`
  - Audio bitrate: ~`48 kbps`
  - Frame rate: `25 fps`
  - Codecs: **H.264** (video) + **AAC** (audio)
- Saves the compressed videos in the specified output folder.
- Maintains the **same folder structure** as the input directory.
- Leverages **multithreading** to process multiple videos simultaneously.

---

## 🧠 Example Output

    Starting parallel compression of 8 videos...
    Started compressing: video1.mp4
    Compression successful! Compressed video1.mp4 saved at ...
    Progress: 1/8 videos processed
    ...
    ==========================================
    Compression Summary:
    Total videos processed: 8
    Successfully compressed: 8
    Failed to compress: 0
    Total processing time: 45.32 seconds
    ==========================================

---

## 💡 Tips

- Adjust the `max_threads` parameter in `process_videos()` if you want to control how many files are processed in parallel.
- If FFmpeg isn’t found at the specified path, the script will show an error message.
- Feel free to tweak the `-b:v`, `-b:a`, `-r`, etc. parameters in `compress_video()` to suit your needs.

---

## 🤝 License

Use and modify freely. No attribution required — but always appreciated!
