Go Temp Mail Bot by FurySec

A terminal-based temporary email generator for privacy and ethical pentesting, built with Python and powered by Mail.tm. Features a vibrant color-changing ASCII art intro, Telegram redirect with countdown, rich-powered UI with bold styling, and tqdm animations for a hacker-movie vibe. Perfect for avoiding spam or testing signups in authorized environments.

Screenshot





Features





Generate Temp Emails: Create disposable email addresses using Mail.tm’s free API.



Check Inbox: View incoming messages in a neatly styled rich table with sender, subject, and body.



Slick UI: Color-cycling ASCII art (yellow, blue, cyan), bold cyan/green/blue panels, and animated progress bars.



Telegram Redirect: Auto-opens t.me/+G_kbgGXYhz40ZDdk with a 12-second countdown on startup.



Ethical & Free: No cost, no signup required, built for privacy and authorized pentesting.

Setup





Install Dependencies:

pip3 install -r requirements.txt

Or manually:

pip3 install requests rich tqdm prompt_toolkit



Run the Script:

python3 temp.py



Usage:





On startup, the script opens t.me/+G_kbgGXYhz40ZDdk in your browser and shows a 12-second countdown.



Then, use commands:





generate: Create a temp email (e.g., test123@moimail.com).



check: View inbox in a styled table.



exit or Ctrl+C: Quit with a stylish exit message.

Requirements





Hardware: Any machine running Linux (tested on Kali Linux).



Software:





Python 3 (pre-installed on most Linux distros).



Libraries: requests, rich, tqdm, prompt_toolkit (see requirements.txt).



Internet connection for Mail.tm API (https://api.mail.tm).



Default browser (e.g., Firefox) for Telegram redirect.



Cost: Zero—free libraries and API.

Ethical Use

Use Go Temp Mail Bot responsibly for:





Protecting your privacy (e.g., avoiding spam during signups).



Authorized pentesting (e.g., testing signup forms with permission).

Always obtain explicit permission before testing services or networks. Misuse may violate terms of service or local laws. FurySec is not responsible for unethical use.

How It Works





Startup: Displays a color-changing “Go Temp Mail Bot” ASCII art, opens your Telegram channel, and counts down 12 seconds.



Main Interface: Shows a bold cyan-bordered panel with commands and your branding.



Email Generation: Creates a random email using Mail.tm’s /domains and /accounts endpoints, with JWT authentication.



Inbox Checking: Fetches messages via /messages and displays them in a rich table.



Animations: tqdm progress bars (“Hacking the Matrix”, “Scanning Inbox”) add flair.

Troubleshooting





DNS Issues: If you see a NameResolutionError, check connectivity:

ping api.mail.tm

Set Google DNS if needed:

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf



No Messages: Messages may take 10-20 seconds to arrive. Retry check if the inbox is empty.



Browser Redirect: Ensure a default browser (e.g., Firefox) is installed:

sudo apt-get install firefox



UI Issues: If you see raw markup (e.g., [yellow]), ensure rich==13.9.2 is installed and your terminal supports ANSI colors (e.g., Kali’s default terminal).

Credits

Powered by Mail.tm as per their API terms. Built with love by FurySec.

Contact





Join our Telegram: t.me/+G_kbgGXYhz40ZDdk



GitHub: github.com/furysec



Developer: FurySec

License

MIT
