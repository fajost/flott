from pathlib import Path

import pandas as pd

from .prepare import _prepare


def test_prepare(tmp_path: Path) -> None:
    source = pd.read_csv(Path("./data/test/raw/example.csv"))
    dest = _prepare(source)
    assert "Name" == dest.index.name
    assert dest.index.is_unique
