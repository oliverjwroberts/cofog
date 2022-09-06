# Cofog

[![PyPI](https://img.shields.io/pypi/v/cofog.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/cofog.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/cofog)][python version]
[![License](https://img.shields.io/pypi/l/cofog)][license]

[![Read the documentation at https://cofog.readthedocs.io/](https://img.shields.io/readthedocs/cofog/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/oliverjwroberts/cofog/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/oliverjwroberts/cofog/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/cofog/
[status]: https://pypi.org/project/cofog/
[python version]: https://pypi.org/project/cofog
[read the docs]: https://cofog.readthedocs.io/
[tests]: https://github.com/oliverjwroberts/cofog/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/oliverjwroberts/cofog
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Introduction

Classification of the Functions of Government (COFOG) is a classification defined by the United Nations Statistics Division. Its purpose is to "classify the purpose of transactions such as outlays on final consumption expenditure, intermediate consumption, gross capital formation and capital and current transfers, by general government" (from [home page]).

This intention of this package is to serve a convenient way of parsing and interfacing with the classifications.

## Data

Data was sourced from the UN's [classifications on economic statistics page] and parsed into a dictionary that can be found in `src/cofog/data.py`.

## Features

- Provides the `COFOG` class to represent a Classification of Functions of Government.
- Validate `COFOG` codes through Regular Expressions and presence in the data.
- Lookup descriptions from codes.
- Traverse the levels of any given code, with the ability to set a lower level without forgetting the original level.

## Requirements

- Python >=3.8
- Click >=8.0.1

## Installation

You can install _Cofog_ via [pip] from [PyPI]:

```console
$ pip install cofog
```

## Usage

Please see the [usage page] in the docs for full details.

Get started by initialising a new `COFOG` object with a code. These can be either specified as strings (with and without dots) or integers.

```python
from cofog import COFOG

cofog = COFOG("04.3.6")

# or any of the following
COFOG("0436")
COFOG("436")
COFOG(436)
```

You can then access the code's description as well as set it to lower level codes.

```python
print(cofog.description)
# Non-electric energy  (CS)
print(cofog.level)
# 3

cofog.set_level(2)
print(cofog.code)
# 04.3
print(cofog.description)
# Fuel and energy
```

You can also get parent and children codes of any valid code.

```python
print(cofog.get_parent_code())
# 04.3

print(COFOG("07.3").get_children_codes())
# ["07.3.1", "07.3.2", "07.3.3", "07.3.4"]
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Cofog_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was heavily inspired by [@ellsphillips]'s [govsic] package.

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[home page]: https://unstats.un.org/unsd/classifications/Family/Detail/4
[classifications on economic statistics page]: https://unstats.un.org/unsd/classifications/Econ
[pip]: https://pip.pypa.io/
[pypi]: https://pypi.org/
[@ellsphillips]: https://github.com/ellsphillips
[govsic]: https://github.com/ellsphillips/govsic
[@cjolowicz]: https://github.com/cjolowicz
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/oliverjwroberts/cofog/issues

<!-- github-only -->

[usage page]: https://cofog.readthedocs.io/en/latest/usage.html
[contributor guide]: https://github.com/oliverjwroberts/cofog/blob/main/CONTRIBUTING.md
[license]: https://github.com/oliverjwroberts/cofog/blob/main/LICENSE
