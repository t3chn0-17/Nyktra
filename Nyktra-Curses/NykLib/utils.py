from rich.text import Text
from rich.panel import Panel
from socket import gethostname, gethostbyname

from .config import console

devbanner = Text("""
████████╗████████╗████████╗██╗      ██╗███╗   ██╗█████████╗        ██╗████████╗
╚══██╔══╝╚═════██║██╔═════╝██║      ██║████╗  ██║██║    ██║        ██║╚═════██║
   ██║   ████████║██║      ███████████║██╔██╗ ██║██║ █╗ ██║███████╗██║      ██║
   ██║   ╚═════██║██║      ██╔══════██║██║╚██╗██║██║ ╚╝ ██║╚══════╝██║      ██║
   ██║   ████████║████████╗██║      ██║██║ ╚████║█████████║        ██║      ██║
   ╚═╝   ╚═══════╝╚═══════╝╚═╝      ╚═╝╚═╝  ╚═══╝╚════════╝        ╚═╝      ╚═╝
""", style="purple")

verbanner = Text("""
███╗   ██╗██╗   ██╗██╗  ██╗████████╗██████╗  █████╗
████╗  ██║╚██╗ ██╔╝██║ ██╔╝╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗ ██║ ╚████╔╝ █████╔╝    ██║   ██████╔╝███████║
██║╚██╗██║  ╚██╔╝  ██╔═██╗    ██║   ██╔══██╗██╔══██║
██║ ╚████║   ██║   ██║  ██╗   ██║   ██║  ██║██║  ██║
╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
""", style="purple")

def dev_banner():
  console.print("[purple]Developed By", justify="center")
  console.print(devbanner, justify="center")

def print_version(ctx, param, value):
  if not value or ctx.resilient_parsing:
    return

  console.print()
  console.print(
    Panel(
      verbanner,
      title="[bold cyan]NYKTRA 1.0.0[/bold cyan]",
      subtitle="[cyan]Secure • Fast • Terminal[/cyan]",
      border_style="green"
    ),
    justify="center"
  )
  ctx.exit()

def get_local_ip():
  hostname = gethostname()
  local_ip = gethostbyname(hostname)
  return local_ip

# def run_all():
#   app = TUI()
#   app.run()