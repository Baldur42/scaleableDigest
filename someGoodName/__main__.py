from contextlib import suppress
import logging
import argparse

# Hack to run local without building
try:
    from someGoodName import preprocessor
except ModuleNotFoundError:
    import preprocessor  # type: ignore

log = logging.getLogger(__name__)


def argument_parser() -> argparse.Namespace:
    """
    CLI argument parser

    Raises:
        SystemExit: If argv data validation fails

    Returns:
        argparse.Namespace: Namespace of valid data
    """
    p = argparse.ArgumentParser(
        description="Some text before argumnents, maybe something like a program brief",
        epilog="After the arguments we might want some usage examples",
    )

    # Main options
    p.add_argument(
        "file",
        nargs="+",
        type=preprocessor.file_check,
        help="One or more files to opperate on",
    )

    p.add_argument(
        "--format",
        "-f",
        nargs="+",
        type=preprocessor.valid_format,
        help="One or more files to opperate on",
    )

    # Logging options
    p.add_argument(
        "--verbose",
        "-v",
        dest="log_level",
        action="store_const",
        const=logging.INFO,
        default=logging.WARNING,
        # Debug will take president if both are used
        help="Logging set to include info messages",
    )
    p.add_argument(
        "--debug",
        dest="log_level",
        action="store_const",
        const=logging.DEBUG,
        help="Logging set to include debug messages",
    )
    p.add_argument(
        "--log",
        nargs="?",
        const=f"{__name__}.log",
        default=None,
        help="Log to file instead of console, a custom name may be given"
    )

    # Optional argument completion for bash, zsh & fish
    with suppress(ModuleNotFoundError):
        from argcomplete import autocomplete
        autocomplete(p)

    parsed = p.parse_args()

    # Setup logger
    logging.basicConfig(level=parsed.log_level, filename=parsed.log)

    # Trace print parsed arguments
    log.debug("\n\t".join([
        "Parsed args:",
        *[f"{key:<15}: {value}"for key, value in vars(parsed).items()]
    ]))

    # Catch error from preprocessors and exit with error code
    # NOTE: Preprocessors will not be able to throw other than log errors and warnings
    #       as the log level are  not set until after arguments are parsed.
    if logging.ERROR in logging.getLogger(preprocessor.__name__)._cache:  # type: ignore
        raise SystemExit(1)

    return parsed


def cli() -> None:
    """
    Command line application structural flow
    """

    arg = argument_parser()
    print(arg)
    print("No Real work are done yet")


if __name__ == "__main__":
    cli()
