# neuron-zk-generator

This Python application reads data from [my](https://github.com/thomasabishop/eolas) [zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) and
formats it so that it can be compiled as a [Neuron](https://neuron.zettel.page/) project and from there published as a static-site on the Web.

## Local development

Activate the virtual environment:

```sh
source venv/bin/activate
```

Run:

```sh
python3 src/app.py
```

## Build single executable

Use `pyinstaller` to create single executable file. `pyinstaller` is installed
along with other packages specified in `setup.py`.

Ensure the virtual environment is running.

From root:

```sh
pyinstaller --onefile src/app.py --name neuron-zk-generator
# -F compiles to single file
```

Outputs to `neuron-zk-generator/dist/app`.

Sourcing the executable:

```sh
${HOME}/repos/neuron-zk-generator/dist/app
```

### Run executable as program

```sh
sudo mv ${HOME}/repos/neuron-zk-generator/dist/app /usr/local/bin
```

Then run with:

```
neuron-zk-generator
```
