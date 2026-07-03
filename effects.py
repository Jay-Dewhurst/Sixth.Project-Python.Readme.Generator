# Resources needed for Program to run
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.logging import RichHandler
from rich import box
import time
import logging

# Initializes Rich Console
console = Console()

# Display's Styled Text
def print_header():
    console.print("[bold red]Readme Generator Program[/bold red]")


# Creates and Displays a table containing visual examples of output
def display_table():
    table = Table(title="[bold yellow]Readme Generator[/bold yellow]", box=box.ROUNDED)

    table.add_column("[red]Questions[/red]", style="bold blue", justify="center")
    table.add_column("[red]Details[/red]", style="white", justify="center")

    table.add_row("Project Title", "Add a Project Title")
    table.add_row("Project Description", "Add a Project Description")
    table.add_row("Installation Instructions", "Explain how to Install the program")
    table.add_row("Usage Information", "Explain how to use the program")
    table.add_row("Dropdown List", "Select a License")
    table.add_row("Contact", "Enter Contact information including name and email")

    console.print(table)

# Adds Progress Bar simulation underneath the table
def loading_simulation():
    console.print("[bold cyan]Processing data...[/bold cyan]")
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.2)  # Simulate work


# Defines Rich Logger Example
def setup_logging():
    logging.basicConfig(
        level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
    )
    logger = logging.getLogger("rich")
    return logger


logger = setup_logging()

# Running the functions
if __name__ == "__main__":
    display_table()  # Show a formatted table
    loading_simulation()  # Show a progress bar
    logger.info("This is an informational log message!")
    logger.warning("This is a warning log message!")
    logger.error("This is an error log message!")
