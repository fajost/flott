import click

from scaffold.pipelines import prepare
from scaffold.services import init_logging


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    pass


init_logging()
cli.add_command(prepare)
cli(prog_name="scaffold")
