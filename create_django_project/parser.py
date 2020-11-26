import argparse
from pathlib import Path

cwd = Path.cwd()


def get_args() -> argparse.Namespace:
    """Get command-line arguments.

    :return: dictionary containing arguments and values
    :rtype: argparse.Namespace
    """
    # create parser
    parser = argparse.ArgumentParser(
        prog='create-django-project',
        usage='%(prog)s [options] path',
        description='Create a full fledged Django project.',
        epilog='Happy Coding!',
        allow_abbrev=False)

    # version
    parser.version = 'v0.0.1'

    # add argmuments
    # path to the working directory default to cwd.
    parser.add_argument('Path',
                        metavar='path',
                        type=Path,
                        help='the path to working directory')

    # virtual environment name
    parser.add_argument('-ve',
                        metavar='virtualenv',
                        default='env',
                        dest='venv_name',
                        help='set a name of virtual environment')

    # project name
    parser.add_argument('-n',
                        metavar='project name',
                        default='config',
                        dest='project_name',
                        help='set a name of the project')

    # version
    parser.add_argument('-v',
                        '--version',
                        action='version')

    return vars(parser.parse_args())
