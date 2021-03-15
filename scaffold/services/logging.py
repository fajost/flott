import logging
import sys
from pathlib import Path
from typing import Optional


def init_logging(logfile: Optional[Path] = None) -> None:
    """Configure logging to file and stdout.

    Args:
        logfile: Location of logfile. Defaults to "run.log".
    """
    if not logfile:
        logfile_path = Path.cwd()
        while not (logfile_path / "pyproject.toml").exists():
            logfile_path = logfile_path.parent
        logfile = logfile_path / "run.log"

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    terminalHandler = logging.StreamHandler(sys.stdout)
    terminalHandler.setLevel(logging.DEBUG)
    terminalHandler.setFormatter(formatter)
    root.addHandler(terminalHandler)

    fileHandler = logging.FileHandler(logfile)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    root.addHandler(fileHandler)
