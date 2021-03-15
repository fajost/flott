import os
from pathlib import Path

from .logging import init_logging


def test_init_logging_with_file(tmp_path: Path) -> None:
    LOGFILE = tmp_path / "run.log"
    init_logging(LOGFILE)


def test_init_logging_without_file() -> None:
    init_logging()


def test_init_logging_without_file_cwd_subdir() -> None:
    os.chdir("scaffold")
    init_logging()
