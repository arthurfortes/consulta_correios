# Consulta Correios

API for querying addresses and zip codes using the Correios website (Brazil postal system)


# Requirements

- Python 3.5+
- beautifulsoup4
- requests
- unidecode


## Installation

Consulta Correios can be installed using pip:

    $ pip install Consulta-Correios

If you want to run the latest version of the code, you can install from git:

    $ pip install -U git+git://github.com/arthurfortes/consulta_correios.git


## Quick Start and Guide

This API allows querying both zip codes and address through the same call. See the example commands below:

```python
>>> import consulta_correios

>>> address = consulta_correios.busca_cep('Av. Júlio Prestes')
>>> print(address)
{'address': 'Avenida Julio Prestes', 'neighborhood': 'Taquaral', 'city/state': 'Campinas/SP', 'zipcode': '13076-001'}
```

```python
>>> import consulta_correios

>>> address = consulta_correios.busca_cep('13076-001')
>>> print(address)
{'address': 'Avenida Julio Prestes', 'neighborhood': 'Taquaral', 'city/state': 'Campinas/SP', 'zipcode': '13076-001'}
```


## Contributions and issues

To help the project with contributions follow the steps:

- Fork Consulta Correios

- Make your alterations and commit

- Create a topic branch - git checkout -b my_branch

- Push to your branch - git push origin my_branch

- Create a Pull Request from your branch.

- You just contributed to the Consulta Correios project!

For bugs or feedback use this link: https://github.com/arthurfortes/consulta_correios/issues


## License (MIT)

    © 2020. Consulta Correios All Rights Reserved

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of
    the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.
