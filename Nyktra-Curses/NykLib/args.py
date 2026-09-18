import click
from rich.panel import Panel
from rich.text import Text

from .utils import dev_banner, print_version, get_local_ip
from .config import console, ensure_dirs

@click.group()
@click.option(
  "-v", "--version", 
  is_flag=True, 
  callback=print_version, 
  expose_value=False, 
  is_eager=True, 
  help="Show the version and exit."
)
def server_args(): pass

@server_args.command(
  help="Run the server"
)
@click.option(
  "-p", "--port",
  type=int, default=77666,
  help="Port number for the server to work on. example: 7000"
)
def run(port):
  dev_banner()
  ensure_dirs()
  # console.print(f"[green]\[+] Server running on 127.0.0.1:{port}")
  # console.print(f"[blue]\[!] Access it on the LAN {get_local_ip()}:{port}")
  console.print("[blue]\[!] Press Enter to Start the TUI")
  input()



@click.group()
@click.option(
  "-v", "--version", 
  is_flag=True, 
  callback=print_version, 
  expose_value=False, 
  is_eager=True, 
  help="Show the version and exit."
)
def client_args(): pass

@client_args.command(
  help="Run the server"
)
@click.argument(
  "ipaddr",
  type=str,
  help="IPv4 address of Nyktra server to connect to. example: 172.217.14.206"
)
@click.argument(
  "port",
  type=int,
  help="Port number of Nyktra server to connect to. example: 7000"
)
def run(port):
  dev_banner()
  ensure_dirs()
  # console.print(f"[green]\[+] Server running on 127.0.0.1:{port}")
  # console.print(f"[blue]\[!] Access it on the LAN {get_local_ip()}:{port}")
  console.print("[blue]\[!] Press Enter to Start the TUI")
  input()