# UKDevilzPlus YT-DLP Plugin 🛠️

## Introduction 📚

Welcome to the UKDevilzPlus YT-DLP Plugin! This specialized plugin enhances your video downloading capabilities from various websites such as UKDevilz.com, NoodleMagazine.com, Tyler-Brown.com, Mat6Tube.com, Exporntoons.net, and ActionViewPhotography.com. With this plugin, you can efficiently extract and download videos, complete with detailed metadata, using yt-dlp.

> 📝 **Note**: This plugin and README were created with assistance from OpenAI's GPT-4 model.

## Features 🌟

- **Individual Video Downloads** 🎥: Directly download videos from supported sites.
- **Metadata Extraction** 📝: Capture detailed video metadata including title, duration, views, likes, and tags.

## Installation Guide for Windows 11 🖥️

> ⚠️ **Note**: These installation steps are specific to Windows 11 and have been tested solely on this platform.

1. Open the Command Prompt (`cmd`).
2. Navigate to your yt-dlp plugins directory:

```bash
cd C:\Users\%username%\AppData\Roaming\yt-dlp\plugins
```

3. Clone the plugin repository:

```bash
git clone https://github.com/Earthworm-Banana/yt-dlp-UKDevilz_com-plugin.git
```

4. Ensure that BeautifulSoup4 (bs4) is installed:

```bash
pip install bs4
```

## Pip Install Method 📱

> ⚠️ **Note**: This pip install method has been tested on various platforms.

1. Open your terminal or command line application.
2. Install the plugin and BeautifulSoup4 (bs4) by running:

```bash
python3 -m pip install -U https://github.com/Earthworm-Banana/yt-dlp-UKDevilz_com-plugin/archive/refs/heads/master.zip bs4
```

> 📘 **Note**: This pip install method should work on any system that has yt-dlp installed via pip.

> For other methods of installing this plugin package, consult [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins).

## 🔍 Metadata Extraction

The plugin extracts a wide range of metadata, including:

- 📝 Video Title
- 🆔 Video ID
- 🗓️ Upload Date
- 👁️ View Count
- 👍 Like Count
- ⏰ Video Duration
- 🖼️ Thumbnail URL
- 🏷️ Tags (sorted and deduplicated)

## Limitations and Known Issues ❗

- **Metadata Limitations**: 📄 Some metadata fields may not populate due to the limitations in the information accessible from the supported sites.

## Support and Contributions 🤝

For any inquiries or contributions, please [open an issue on GitHub](https://github.com/Earthworm-Banana/yt-dlp-UKDevilz_com-plugin/issues).

Thank you for using the UKDevilzPlus YT-DLP Plugin. Happy downloading! 🙏
