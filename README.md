# YouTube Downloader

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
![yt-dlp](https://img.shields.io/badge/dependency-yt--dlp-orange)

A simple Python-based tool to download YouTube videos and audio directly to your computer.
Perfect for offline viewing, personal projects, or experimenting with media processing.

## Features

* Download full videos in various resolutions
* Extract audio only (default: MP3) via `audio.py`
* Supports entire playlists
* Lightweight and easy to run

## Requirements

* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  Install with:

  ```bash
  pip install yt-dlp
  ```

## Usage

Run the main script to download a video:

```bash
python downloader.py <video_url>
```

Run the audio script to extract audio only:

```bash
python audio.py <video_url>
```

Downloads will be saved to the current directory by default.

## Dependencies

This project relies on the following open-source tool:

* [yt-dlp](https://github.com/yt-dlp/yt-dlp) – used for downloading videos from various platforms.

## Disclaimer

This tool uses [yt-dlp](https://github.com/yt-dlp/yt-dlp).
It is intended for lawful and personal use only.
The author of this repository is not responsible for any misuse, including the downloading, sharing, or distribution of copyrighted material.
Users are solely responsible for complying with copyright regulations in their respective regions.

## License

This project is licensed under the [MIT License](LICENSE).
