import logging as log
from argparse import ArgumentParser
from YAML2STAR import preprocessor


parser = ArgumentParser(
    # formatter_class=RawTextHelpFormatter, # Keep description as is (row breaks etc)
    description="Some text before argumnents, maybe something like a program brief",
    epilog="After the arguments we might want some usage examples",
)
parser.add_argument(
    "--verbose",
    "-v",
    dest="log_level",
    action="store_const",
    const=log.INFO,
    default=log.WARNING,
    # Debug will take president if both are used
    help="Logging set to include info messages",
)
parser.add_argument(
    "--debug",
    dest="log_level",
    action="store_const",
    const=log.DEBUG,
    help="Logging set to include debug messages",
)
parser.add_argument(
    "file",
    nargs="+",
    type=preprocessor.file_check,
    help="One or more files to opperate on",
)
parser.add_argument(
    "--format",
    "-f",
    nargs="+",
    type=preprocessor.valid_format,
    help="One or more files to opperate on",
)

if __name__ == "__main__":
    # Note: Preprocessors will not be able to throw other than log errors and warnings
    #       as the log level are  not set until after arguments are parsed.
    parsed = parser.parse_args()
    log.getLogger().setLevel(parsed.log_level)
    log.debug(parsed)

    print("No Real work are done yet")
