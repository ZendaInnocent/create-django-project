# Create Django Project

Command Line Interface (CLI) that abstract much of common pattern in creating and structuring Django project.

## Installation

Don't install in virtual environment.

```
pip install create-django-project
```

## Prerequisites
Python 3.6+

Virtualenv

## Features

- Manage project using virtual environment
- Structuring of the project
- Manage enviromental variables

## Usage

```
create-django-project <path> -ve <venv_name> -n <project_name>

<path>          directory for the project
<venv_name>     name of virtual environment
<project_name>  name of the project
```

More information can be seen using `create-django-project -h` command.

### Example

- Create a folder you want to use for your project
    ```
    mkdir root
    ```

- cd into the folder
    ```
    cd root
    ```

- run ``django-create-project <path>``
    ```
    create-django-project .
    # note dot at the end for current directory.
    ```

    `<path>` can be any path of your choice.

    If path specified does not exists, it will be created.

    You can also provide path as full path
    ```
    create-django-project C:/somepath/to/project/folder
    ```

After that, the command will do the following:

- Create virtual environment ``(default='env')`` if no virtual environment name is specified.

    You can specify virtual environment name using
    ```
    create-django-project <path> -ve <venv_name>
    ```

    replace `<venv_name>` with name of your choice.

- Activate virtual environment

    After creating then it activates it if the virtual enviroment exists.

- Create a Django project

    Default project name is `config` if no project name is specified. You can specify project name of your choice.
    ```
    create-django-project <path> -n <project-name>
    ```

    If project name is `config`, it then renamed to `src`.


- Manage enviromental variables by creating `.env` file in project directory and fill in values for `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS`

    ```python
    DJANGO_SECRET_KEY = 'value copied from settings file'
    DEBUG = True
    ALLOWED_HOSTS = [.localhost, ]
    ```

## License

Code released under `MIT LICENSE <https://github.com/ZendaInnocent/create-django-project/blob/main/LICENSE>`_
