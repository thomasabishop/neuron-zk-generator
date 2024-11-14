# `neuron-zk-generator`

This Python application reads data from [my](https://github.com/thomasabishop/eolas) [zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) and
formats it so that it can be compiled as a [Neuron](https://neuron.zettel.page/) project and from there published as a static-site on the Web.

## Local development

```sh
source venv/bin/activate
pip install -r requirements.txt
neuron-zk-generator
```

## Run as local application

```
pipx install [local_path_to_application]
neuron-zk-generator
```

### Update after changes

```
pipx uninstall neuron-zk-generator
pipx install [local_path_to_application]
```

## Build single executable

Use `pyinstaller` to create single executable file. `pyinstaller` is installed
along with other packages in `requirements.txt`.

From root:

```sh
pyinstaller -F src/app.py
# -F compiles to single file
```

Outputs to `neuron-zk-generator/dist/app`.

Sourcing the executable:

```sh
/home/thomas/repos/neuron-zk-generator/dist/app
```
