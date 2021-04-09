from pathlib import Path
import logging as log

#
# Check/Validate and/or prossess/manipulate user arguments.
#   Do some wrangling before the program gets it back
#

# Known formats from templates with helpers removed (do not re calculate this all the time)
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
    if f in formats:
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
    if p.is_file():
        log.warning(f"File '{p.name}' does not exist; {p.resolve()}")
    return p


if __name__ == "__main__":
    print(formats)
