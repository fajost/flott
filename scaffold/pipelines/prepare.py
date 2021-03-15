import logging

import click
import pandas as pd


@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest", type=click.Path(writable=True, dir_okay=False))
def prepare(source: str, dest: str) -> None:  # pragma: no cover
    """Prepare SOURCE csv-data and write results to DEST as csv."""
    logging.debug(f"Running prepare on: {source}")
    source_data = pd.read_csv(source)
    result_data = _prepare(source_data)
    result_data.to_csv(dest)
    logging.debug(f"Wrote prepare results to: {dest}")


def _prepare(source: pd.DataFrame) -> pd.DataFrame:
    """Apply preparation step to ``source`` data provided.

    Args:
        source: Source data.

    Returns:
        Result data.
    """
    return source.loc[lambda x: x["Credit"]].groupby("Name")[["Amount"]].sum()
