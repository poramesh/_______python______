## DummyData

Dummydata is a Python package designed to facilitate the creation of synthetic data modules. Inspired by the popular Faker library, this project serves as a learning tool to understand the intricacies of Python package development, including module structuring, class initialization, and package distribution using pyproject.toml


## Features

- Modular Design: Generate customizable dummy data modules for various use cases.
- Class-Based Structure: Demonstrates object-oriented principles with clear class definitions and interactions.
- Package Configuration: Showcases the use of pyproject.toml for package metadata and distribution settings.

## Instalation

```
git clone https://github.com/poramesh/_______python______/tree/main/python-packages/dummydata.git
cd dummydata
```

## Sample Usecase

```
from fake_module import dummy_data_generator

faker = dummy_data_generator()
print("name",faker.name())
print("adress",faker.address())
print("date",faker.date())
print("email",faker.email())
``

