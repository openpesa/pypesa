# Installation

This gives a guide on how to install tools and project, ready for development.

[Poetry](https://python-poetry.org/) is the tool used for packaging this project. It must be installed in the system to be able to use it for the project.

Poetry provides a custom installer that will install `poetry`, this is the recommended way to installing it.

- osx / linux / bashonwindows

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

- windows powershell

    ```
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
    ```

## Customization

Poetry has default values for configurations which are sane, but for this project here are few optional customization. You can use the defaults or modify according to this guide, whatever you see fit.

All configuration can be seen by running

```
poetry config --list
```

You will get result like this

```
cache-dir = "/path/to/cache/directory"
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}/virtualenvs"  # /path/to/cache/directory/virtualenvs
```

Poetry creates new virtual environment if one doesn't exists already and placed in other directory other than the project's directory. I prefer to have a virtual environment in the project directory.

You can change this behaviour by running

```
poetry config virtualenvs.in-project true
```

If happens you want to create virtual environment manually, you can change the default behaviour using

```
poetry config virtualenvs.create false
```

If `virtualenvs.create` is set `true`, `poetry` will create virtual environment with name `.venv` in the project directory as long as `virtualenvs.in-project` is set to `true`.

## Installing Dependencies

The project has various dependencies that need to be installed for it to function properly.

> Make sure to activate virtual environment before installing dependencies.

If default configurations are used, activate virtual enviroment using

```
poetry shell
```

If configurations are modified as above, use normal methods for activating virtual environment in your system.

- osx / linux / bashonwindows

    ```
    virtualenv env
    source env/bin/activate
    ```

- Windows PowerShell

    ```bash
    virtualenv env # creating virtual environment named `env`
    env/scrits/activate
    ```

> Remember to replace `env` with the name you prefer for virtual enviroment.

You can check the information for virtual environment using

```
poetry env info
```

The sample results of the command

> You may get different results but looks like this

```
Virtualenv
Python:         3.9.0
Implementation: CPython
Path:           \path\to\virtual\environment\
Valid:          True

System
Platform: win32
OS:       nt
Python:   c:\users\<user>\appdata\local\programs\python\python39
```

If the value of `Path` is `N/A`, make sure to activate virtual environment.

Lastly, install dependencies using

```
poetry install
```

All the dependencies for project will be installed.

## Documentation

Documentation for this project resides in `docs` directory, it uses `markdown` and `mkdocs`.

Theme used is `ReadTheDocs` theme.

You can serve documentation locally using

```
mkdocs serve
```
