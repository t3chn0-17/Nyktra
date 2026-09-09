import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from .tui import app
from .data import project_dir, Group, User
from pathlib import Path

console = Console()

banner = Text("""
███╗   ██╗██╗   ██╗██╗  ██╗████████╗██████╗  █████╗
████╗  ██║╚██╗ ██╔╝██║ ██╔╝╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗ ██║ ╚████╔╝ █████╔╝    ██║   ██████╔╝███████║
██║╚██╗██║  ╚██╔╝  ██╔═██╗    ██║   ██╔══██╗██╔══██║
██║ ╚████║   ██║   ██║  ██╗   ██║   ██║  ██║██║  ██║
╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
""", style="purple")

def print_version(ctx, param, value):
  if not value or ctx.resilient_parsing:
    return

  console.print()
  console.print(
    Panel(
      banner,
      title="[bold cyan]NYKTRA 1.0.0[/bold cyan]",
      subtitle="[cyan]Secure • Fast • Terminal[/cyan]",
      border_style="cyan"
    ),
    justify="left"
  )
  ctx.exit()

def nor_print_version():
  console.print()
  console.print(
    Panel(
      banner,
      title="[bold cyan]NYKTRA 1.0.0[/bold cyan]",
      subtitle="[cyan]Secure • Fast • Terminal[/cyan]",
      border_style="cyan"
    ),
    justify="left"
  )
  console.print()

@click.group()
@click.option(
  "-v", "--version", 
  is_flag=True, 
  callback=print_version, 
  expose_value=False, 
  is_eager=True, 
  help="Show the version and exit."
)
def cli_args(): pass

@cli_args.command(
  help="Run the server"
)
@click.option(
  "-p", "--port",
  type=int, default=77666,
  help="Port number for the server to work on. example: 7000"
)
def run(port):
  nor_print_version()
  app.run()

@cli_args.command(
  help="Configure the server settings to edit the config.json file"
)
@click.option(
  "-v", "--variable",
  help="Specify a config variable to edit",
  type=click.Tuple([str, str])
)
def config(variable):
  nor_print_version()
  if variable:
    console.print(f"[green]\[+] Edited: [purple]{variable}[/purple]")
  else:
    console.print(f"[green]\[+] Started config")

@cli_args.command(
  help="Add a group to the server"
)
@click.argument("name")
def add_group(name):
  nor_print_version()

@cli_args.command(
  help="Add a user to the server and set their roles"
)
@click.argument("name")
def add_user(name):
  nor_print_version()