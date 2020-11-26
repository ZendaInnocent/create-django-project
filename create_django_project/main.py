from .parser import get_args
from .config import ProjectSetup


def main():
    args = get_args()
    project_setup = ProjectSetup(args)
    project_setup.execute()


if __name__ == "__main__":
    main()
