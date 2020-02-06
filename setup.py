import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
    'beautifulsoup4',
    'requests',
    'unidecode',
]

setuptools.setup(
    name="Consulta Correios",
    version="1.0.0",
    author="Arthur Fortes",
    author_email="fortes.arthur@gmail.com",
    description="API para consulta de endereços e CEPs  utilizando o site dos Correios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthurfortes/consulta_correios",
    packages=[
        'consulta_correios',
    ],
    package_dir={
        'consulta_correios': 'consulta_correios',
    },
    install_requires=requirements,
    keywords='python endereco cep correios busca',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
)
