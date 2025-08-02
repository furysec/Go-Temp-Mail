import requests
import random
import string
import time
import webbrowser
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.style import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from tqdm import tqdm

console = Console()


ASCII_ART = """
   ____ _          _______ ______  __  __        ___          _ _       
  / ___| |__   ___|__   __|  ____|/ _|/ _|      | __|        | | |      
 | |   | '_ \ / __| | |  | |__  | |_| |_ ___    | __|__   ___| | | ___  
 | |___| | | | (__  | |  |  __| |  _|  _| __|   | |__ \_/ __| | |/ _ \ 
  \____|_| |_| \___| |_|  |______|_| |_|  \___| |____|   \___|_|_|\___|

       by FurySec | t.me/+G_kbgGXYhz40ZDdk | github.com/furysec
"""

def print_colorful_intro():
    console.clear()
    colors = ["yellow", "blue", "cyan"]
    for i in range(6):  
        console.print(Align.center(Text(ASCII_ART, style=colors[i % len(colors)])))
        time.sleep(0.5)
        console.clear()
    console.print(Align.center(Text(ASCII_ART, style="bold magenta")))
    console.print("")  

def print_telegram_prompt():
    console.print(Panel(
        Text("Please join our Telegram group to continue: t.me/+G_kbgGXYhz40ZDdk\nOpening Telegram in your browser...", style="bold yellow"),
        title="Join FurySec", border_style="bold blue", style="bold"
    ))
    console.print("")  
    webbrowser.open("https://t.me/+G_kbgGXYhz40ZDdk")
    console.print(Text("Waiting for you to join (12 seconds)...", style="yellow"))
    for _ in tqdm(range(12), desc="Countdown", bar_format="{l_bar}{bar:20}[bold green]{r_bar}", colour="green"):
        time.sleep(1)
    console.print("")  

def print_main_intro():
    console.clear()
    console.print(Align.center(Text(ASCII_ART, style="bold magenta")))
    console.print(Panel(
        Text(
            "Go Temp Mail Bot by FurySec\n"
            "Join our Telegram: t.me/+G_kbgGXYhz40ZDdk | GitHub: github.com/furysec\n"
            "Type 'generate' to create a temp email, 'check' to view inbox, or 'exit' to quit.",
            style=Style(color="cyan", bgcolor="black")
        ),
        title="Welcome to Go Temp Mail Bot", border_style="bold cyan", style="bold"
    ))
    console.print("")  

def get_random_domain():
    try:
        response = requests.get("https://api.mail.tm/domains")
        if response.status_code == 200:
            domains = response.json().get("hydra:member", [])
            return random.choice(domains)["domain"]
        else:
            console.print(Text(f"Error: Couldn't fetch domains. Status: {response.status_code}", style="red"))
            return None
    except Exception as e:
        console.print(Text(f"Error: {str(e)}", style="red"))
        return None

def generate_email():
    console.print(Text("Generating temp email...", style="yellow"))
    for _ in tqdm(range(10), desc="Hacking the Matrix", bar_format="{l_bar}{bar:20}[bold cyan]{r_bar}", colour="cyan"):
        time.sleep(0.1)
    console.print("")  
    try:
        domain = get_random_domain()
        if not domain:
            return None, None
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        email = f"{username}@{domain}"
        payload = {"address": email, "password": password}
        response = requests.post("https://api.mail.tm/accounts", json=payload)
        if response.status_code == 201:
            token_response = requests.post("https://api.mail.tm/token", json={"address": email, "password": password})
            if token_response.status_code == 200:
                token = token_response.json().get("token")
                console.print(Panel(
                    Text(f"New Temp Email: {email}", style="bold cyan"),
                    title="Success", border_style="bold green", style="bold"
                ))
                console.print("")  
                return email, token
            else:
                console.print(Text("Error: Couldn't get token.", style="red"))
                return None, None
        else:
            console.print(Text("Error: Couldn't create account.", style="red"))
            return None, None
    except Exception as e:
        console.print(Text(f"Error: {str(e)}", style="red"))
        return None, None

def check_inbox(token):
    console.print(Text("Checking inbox...", style="yellow"))
    for _ in tqdm(range(10), desc="Scanning Inbox", bar_format="{l_bar}{bar:20}[bold magenta]{r_bar}", colour="magenta"):
        time.sleep(0.1)
    console.print("")  
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("https://api.mail.tm/messages", headers=headers)
        if response.status_code == 200:
            messages = response.json().get("hydra:member", [])
            return messages
        else:
            console.print(Text(f"Error: {response.json().get('message', 'Failed to fetch inbox')}", style="red"))
            return []
    except Exception as e:
        console.print(Text(f"Error: {str(e)}", style="red"))
        return []

def display_inbox(messages):
    table = Table(title="Inbox - Go Temp Mail Bot", show_header=True, header_style="bold magenta")
    table.add_column("Sender", style="cyan", width=20)
    table.add_column("Subject", style="green", width=30)
    table.add_column("Body", width=50, style="white")
    for msg in messages:
        sender = msg.get("from", {}).get("address", "Unknown")
        subject = msg.get("subject", "No Subject")
        body = msg.get("intro", "No Body")[:100] + "..." if len(msg.get("intro", "")) > 100 else msg.get("intro", "")
        table.add_row(sender, subject, body)
    console.print(table)
    console.print(Panel(
        Text("Join t.me/+G_kbgGXYhz40ZDdk | github.com/furysec", style="cyan"),
        title="FurySec", border_style="bold blue", style="bold"
    ))
    console.print("")  

def main():
    print_colorful_intro()
    print_telegram_prompt()
    print_main_intro()
    email = None
    token = None
    session = PromptSession("Command> ", enable_history_search=True, prompt_continuation="... ")
    bindings = KeyBindings()

    @bindings.add('c-c')
    def _(event):
        event.app.exit()

    while True:
        try:
            command = session.prompt()
            if command.lower() == "generate":
                email, token = generate_email()
            elif command.lower() == "check":
                if not email or not token:
                    console.print(Text("No email generated yet. Run 'generate' first.", style="red"))
                else:
                    messages = check_inbox(token)
                    if messages:
                        display_inbox(messages)
                    else:
                        console.print(Text("No messages found.", style="yellow"))
                        console.print(Panel(
                            Text("Join t.me/+G_kbgGXYhz40ZDdk | github.com/furysec", style="cyan"),
                            title="FurySec", border_style="bold blue", style="bold"
                        ))
                        console.print("")  
            elif command.lower() == "exit":
                console.print(Panel(
                    Text("Shutting down Go Temp Mail Bot. Stay sneaky, boss!", style="bold green"),
                    title="FurySec", border_style="bold blue", style="bold"
                ))
                console.print("")  
                break
            else:
                console.print(Text("Commands: 'generate', 'check', 'exit'", style="red"))
                console.print("")  
        except KeyboardInterrupt:
            console.print(Panel(
                Text("Caught Ctrl+C. Exiting clean.", style="bold green"),
                title="FurySec", border_style="bold blue", style="bold"
            ))
            console.print("")  
            break

if __name__ == "__main__":
    main()
