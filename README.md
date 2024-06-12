# Ejercicio N6 Simulación

## Authors
Buil Delfina,
Buzzacchi Victoria

## Create virtual environment
To create the virtual environment run the following command:
```
python3 -m venv myenv
```

To activate the virtual environment from Linux run the following command:
```
source myenv/bin/activate
```

To deactivate the virtual environment run the following command:
```
deactivate
```

## Install dependencies
Once your environment is activated, install the dependencies needed for this project. Run the following command:
```
pip install -r requirements.txt
```


## Execute the program
To execute the project, run the command:
```
python3 main.py
```

## Configuration of Parameters

The simulation parameters are located in the `config.ini` file. To modify the parameters, edit this file with the desired values.

### Structure of the `config.ini` File

The `config.ini` file is divided into sections. Below is an example of its structure:

```ini
[simulation]
initial_height = 10
initial_velocity = 0
h = 0.0001

[params]
ba = 0.1
m = 1
b = 30
g = 9.8
k = 100000
```

