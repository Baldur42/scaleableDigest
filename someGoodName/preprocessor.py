"""
Data validatators for CLI parsing
"""
from pathlib import Path
import logging

log = logging.getLogger(__name__)

# Add format as this is setup after preprocessors are used
# NOTE: Change to logging.BASIC_FORMAT if regular format changes
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
log.addHandler(console)

# Known formats from templates with helpers removed
# TODO: quick and dirty, will need attention when format extends to multiple file types.
formats = {"helpers"} ^ set(
    map(
        lambda x: Path(x).name.split(".")[0],
        Path(__file__).parent.glob("templates/*.j2"),
    )
)


def valid_format(f: str) -> str:
    """
    Args:
        f (str): format

    Returns:
        str: member of a valid format

    TODO: this could return a function instead of a name
    """
    if f not in formats:
        log.error(f"Unknwon format '{f}', Known formats are {formats}")
    return f


def file_check(f: str) -> Path:
    """
    Args:
        f (str): path to file

    Returns:
        Path: path object
    """
    p = Path(f)
    if not p.is_file():
        log.error(f"File '{p.name}' does not exist; {p.resolve()}")
    return p


if __name__ == "__main__":
    print(formats)
