import logging

import click
import pandas as pd


@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", type=click.Path(writable=True, dir_okay=False))
def prepare(source: str, dest: str) -> None:
    """Prepare SOURCE csv-data and write results to DEST as csv."""
    logging.debug(f"Running prepare on: {source}")
    source_data = pd.read_csv(source)
    result_data = source_data.loc[lambda x: x["Credit"]].groupby("Name")[["Amount"]].sum()
    result_data.to_csv(dest)
    logging.debug(f"Wrote prepare results to: {dest}")
