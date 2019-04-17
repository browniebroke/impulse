import click
from .application import use_cases


@click.group()
def main():
    pass


@main.command()
@click.argument('module_name', type=str)
@click.option('--format', type=str, default='png')
@click.option('--view', type=bool, default=False)
def drawgraph(module_name, format, view):
    use_cases.draw_graph(
        module_name=module_name,
        format=format,
        view=view,
    )
