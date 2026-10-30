
# ft_package

A sample Python package.

## Installation

```bash
python -m build

pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Verification

```bash
pip list | grep "ft_package"
pip show -v ft_package
```


## Uninstallation

```bash
python -m pip uninstall -y ft_package
rm -rf dist
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
