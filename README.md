"""
# 🔥 Go Temp Mail Bot by FurySec 🔥

A terminal-based temporary email generator for privacy and ethical pentesting, built with Python and powered by [Mail.tm](https://mail.tm). 🌐  
Features vibrant color-changing ASCII art, a Telegram redirect with countdown, a `rich`-powered UI, and `tqdm` animations for that hacker-movie vibe. 🎥💻  
Perfect for avoiding spam or testing signups in authorized environments. 🚀

## 📸 Screenshot
![Go Temp Mail Bot in Action](https://i.ibb.co/rK54tmMh/Screenshot-from-2025-08-02-20-15-17.png) <!-- Replace with your screenshot URL, e.g., https://github.com/furysec/Go-Temp-Mail/raw/main/screenshot.png -->

## ✨ Features
- **Generate Temp Emails** 📧: Create disposable email addresses using Mail.tm’s free API.
- **Check Inbox** 📬: View messages in a styled `rich` table with sender, subject, and body.
- **Slick UI** 🎨: Color-cycling ASCII art (yellow, blue, cyan), bold cyan/green/blue panels, and animated progress bars.
- **Telegram Redirect** 🔗: Auto-opens [t.me/+G_kbgGXYhz40ZDdk](https://t.me/+G_kbgGXYhz40ZDdk) with a 12-second countdown.
- **Ethical & Free** 🆓: No cost, no signup required, built for privacy and authorized pentesting.

## 🛠️ Setup
```bash
git clone https://github.com/furysec/Go-Temp-Mail
cd Go-Temp-Mail
pip3 install -r requirements.txt
python temp.py
```

## 🚀 Usage
- On startup, opens [t.me/+G_kbgGXYhz40ZDdk](https://t.me/+G_kbgGXYhz40ZDdk) and shows a 12-second countdown. ⏳
- Commands:
  - `generate`: Create a temp email (e.g., `test123@moimail.com`). 📨
  - `check`: View inbox in a styled table. 📋
  - `exit` or `Ctrl+C`: Quit with a stylish exit message. 👋

## 💻 Requirements
- **Hardware**: Any machine running Linux (tested on Kali Linux; works on Termux). 🖥️
- **Software**:
  - Python 3 (pre-installed on Kali, installable on Termux via `pkg install python`). 🐍
  - Libraries: `requests`, `rich`, `tqdm`, `prompt_toolkit` (see `requirements.txt`). 📦
  - Internet connection for Mail.tm API (`https://api.mail.tm`). 🌍
  - Default browser (e.g., Firefox on Kali, `termux-open-url` on Termux). 🌐
- **Cost**: Zero—free libraries and API. 💸

## ⚖️ Ethical Use
Use **Go Temp Mail Bot** responsibly for:
- Protecting privacy (e.g., avoiding spam during signups). 🕵️
- Authorized pentesting (e.g., testing signup forms with permission). 🔍

**Always obtain explicit permission** before testing services or networks. Misuse may violate terms of service or laws. FurySec is not responsible for unethical use. 🚫

## 🛠️ How It Works
1. **Startup**: Displays color-changing ASCII art, opens Telegram channel, and counts down 12 seconds. 🎉
2. **Main Interface**: Shows a bold cyan-bordered panel with commands and branding. 🖼️
3. **Email Generation**: Creates random emails using Mail.tm’s `/domains` and `/accounts` endpoints with JWT authentication. 🔒
4. **Inbox Checking**: Fetches messages via `/messages` and displays them in a `rich` table. 📊
5. **Animations**: `tqdm` progress bars (“Hacking the Matrix”, “Scanning Inbox”) add flair. ⚡

## 🛠️ Troubleshooting
- **DNS Issues** 🌐:
  ```bash
  ping api.mail.tm
  echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
  ```
- **No Messages** 📭: Messages may take 10-20 seconds. Retry `check` if inbox is empty.
- **Browser Redirect** 🔗:
  - Kali:
    ```bash
    sudo apt-get install firefox
    ```
  - Termux:
    ```bash
    pkg install termux-api
    ```
- **UI Issues** 🖌️: If raw markup (e.g., `[yellow]`) appears, ensure `rich==13.9.2` and ANSI-compatible terminal.

## 🙌 Credits
Powered by [Mail.tm](https://mail.tm) as per their API terms. Built with love by FurySec. ❤️

## 📬 Contact
- Telegram: [t.me/+G_kbgGXYhz40ZDdk](https://t.me/+G_kbgGXYhz40ZDdk) 📲
- GitHub: [github.com/furysec](https://github.com/furysec) 🌟
- Developer: FurySec 😎

## 📜 License
[MIT](LICENSE) 📝
"""
