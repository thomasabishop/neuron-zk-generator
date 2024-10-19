# `neuron-zk-generator`

This is a basic Python application that reads data from [my](https://github.com/thomasabishop/eolas) [zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) and
formats it so that it can be compiled as a [Neuron](https://neuron.zettel.page/) project and from there published as a static-site on the web.

## Running app in local development

```sh
source venv/bin/activate
pip install -r requirements.txt
neuron-zk-generator
```

## Build standalone executable

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
