import jinja2
import logging as log
from os.path import abspath, join, dirname
from argparse import ArgumentParser, RawTextHelpFormatter

# My Packages (handle, installed as module or un installed during development)
# TODO: is there a better way?
try: 
    from YAML2STAR import preprocessor
except ModuleNotFoundError:
    import preprocessor

parser = ArgumentParser(
    # formatter_class=RawTextHelpFormatter, # Keep description as is (row breaks etc)
    description="Some text before argumnents, maybe something like a program brief",
    epilog="After the arguments we might want some usage examples"
)
parser.add_argument(
    "--verbose", "-v",
    action="store_true",
    # Debug will take president if both are used
    help="Logging set to include info messages"
)
parser.add_argument(
    "--debug",
    action="store_true",
    help="Logging set to include debug messages"
)
parser.add_argument(
    "file",
    nargs="+",
    type=preprocessor.file_check,
    help="One or more files to opperate on"
)
parser.add_argument(
    "--format", "-f",
    nargs="+",
    required=True,
    type=preprocessor.valid_format,
    help="One or more files to opperate on"
)

if __name__ == "__main__":
    # Note: Preprocessors will not be able to throw other than log errors and warnings 
    #       as the log level are  not set until after arguments are parsed.    
    parsed = parser.parse_args()
    log.getLogger().setLevel(log.DEBUG*parsed.debug or log.INFO*parsed.verbose or log.WARNING)
    log.debug(parsed)

    print("No Real work are done yet")