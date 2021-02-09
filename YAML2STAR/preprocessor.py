from os.path import isfile, abspath, dirname, basename, join
from glob import iglob
import logging as log

#
# Check/Validate and/or prossess/manipulate user arguments.
#   Do some wrangling before the program gets it back
#

# Known formats from templates with helpers removed (do not re calculate this all the time)
# TODO: quick and dirty, will need attention when format extends to multiple file types.
formats = {"helpers"} ^ set(map(lambda x: basename(x).split(".")[0],
                                iglob(join(dirname(__file__), "template", "*.j2"))))


def valid_format(f):
    f in formats or log.error(
        f"Unknwon format '{f}', Known formats are {formats}"
    )
    return f


def file_check(f):
    isfile(f) or log.warning(
        f"File '{f}' does not exist; {abspath(f)}"
    )
    return f


if __name__ == "__main__":
    print(formats)
