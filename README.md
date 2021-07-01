# Toolbox

Toolbox is a Python package that contains handy functions. 
It's main goal, however, is to demonstrate how to create a package

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/Muls/toolbox
```

## Usage
Features:
* functions.listChunker  --> generator that chunks and interable in evenly sized chunks 
* functions.weirCase    --> converts a string to an unreadable format
* functions.report      --> prints to the console with a timestamp
* decorators.singleton  --> used for decoratint your class to make it a singleton

#### Demo of some of the features:
```python
import toolbox
from toolbox import report

message = toolbox.functions.weirdCase("The toolbox package is ready for use")
report(message)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for chunk in toolbox.functions.listChunker(lst=list_of_numbers, czie=3):
    print(chunk)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)