# helm-chart-generator-tool (v2.0)
This tool has been refactored based on the current script helm-chart-helper

## Purpose
The purpose behind this repository its about to improve the following:
- Readability
- Maintainability
- Testability

The ultimate goal it's to be able to create a framework for a long term app
usability

## Refactoring
In order to reach the mentioned above its necessary to generate a modular framework,
this means refactoring its required to transform our code in a modular way using TDD
as the main methodology.

That means we are going to create the testing in first place then we are going to 
refactor until the code meets the test specification.

## Pyenv
Due to we are going to work with different packages and versions its required to protect our environment
for this reason it's recommended to have installed pyenv

```
# Validate pyenv its installed
pyenv versions
```

Once Pyenv it's installed please install the python version according to the current project 
dependencies usage

```
# Install a protected version of python into Pyenv
pyenv install -v 3.9.0
```

Then its necessary to create a Virtual Environment to our project please generate as follow
```
# Create a Python Virtual Environment
pyenv virtualenv 3.9.0 helm_chart_helper_environ 
```

Once its created please go inside to the project folder and activate the environment in order
to be useful, otherwise project folder won't be protected

```
# Change to project directory
cd helm-chart-generator-tool

# Activate generated virtual environment
pyenv local helm_chart_helper_environ
```

Then finally you are able to work with python and it's dependencies safely 


## Warning !!
Before to meet our requirements pyenv must be installed, avoiding
this recommendation project may can not run properly in other cases system's 
python dependencies can be affected causing malfunction in local machine

## Requirements

In order to run properly its necessary to be up-to-date with requirements, to do that please perform
the following command in console.

```
# update project dependencies
pip install -r requirements.txt
```

## Config .ini

In order to improve and decouple the original syntax from a config file that could have several
use cases, we have used semantics in order to define a new convention and keep the config .ini file 
the most agnostic possible.

For example:
```
# Semantics says its plural, so by convention format will change like this:

mainteners:
    DevOps
```

Automatically every parameter with indentation it's going to be taken as a item of a list of parameters
and the result will be like this:

```python
# Same output format

config['mainteners'] = ['DevOps']
```



## Project Versions
In order to keep the project clean we are going to separate the current solution into different
version. This it's going to help us to distinguish between the original solution and the incoming
refactor. The same way for every release maybe it's going to be a different version, this pursue the
fact to keep the project iterable and add features in a controlled way,

Current version plan:
- v1.0 - app/v1/script/helm_chart_help - (Original version)
- v2.0 - base - (modular base as a project foundation)
- v2.1 - app/v2/main/helm_chart_helper_v1 - (OOP Wrappers, modular transitioning)
- v2.2 - app/v2/main/helm_chart_helper_v2 - (modular refactoring with testings)
- v2.3 - app/v2/main/helm_chart_helper_v3 - (automatic config detection)
- v3.x - modules - (planned framework for future)

Chose version according as follows:
```
# v1.0 - original
python helm_chart_helper_manager.py --name test --version 10 # Original 

# v2.1 - current refactor
python helm_chart_helper_manager.py --name test --version 21 # Modular

# v2.2 - future modular solution
python helm_chart_helper_manager.py --name test --version 22 # Current

# v2.3 - automatic config detection
python helm_chart_helper_manager.py --name test --version 23 # not implemented yet

# Run Testings
pytest -v
```

## Architecture
According to best practices and keep design principles as clean as possible, we
are going to implement in this project from clean architectures a hexagonal architecture
based mainly in 2 things:
- Ports
- Adapters

This way it's going to help us as following:
- decoupling infrastructure
- increasing cohesion

And the final result is to be able to create a modular software structure as 
the foundation of the future framework.

## Project Schema
The following schema its intended to explain how its going to be the future solution

![Modular Structure Schema](helm-chart-generator-tool-map.png)

## Git-Flow
In the same way, the version control and the development flow it's going to be
improved introducing Git-Flow as following:
- Main
- Dev
- feat/branch-name
- fix/branch-name

We are going to introduce as well tools to ensure written commits and code formatting
keeps best practices using for example:
- pre-commits

## Testings
In this version testings are going to be introduced as well, working with
TDD concepts and practices, the first target we are looking for is to improve it's 
to generate testable units of code, that's means we are going to break down the
current solution into modules following the proposed architecture.

To do that we are going to be relying on the next tests tools: 
- Pytest
- Unittests

The motivation of doing testings it's to be able to isolate the logic from
the infrastructure and be able to test the logic in a consistent way, that help 
us to:
- detect changes that can break our code/functionality
- ensure our code its modular enough in order to be testable
- document the functionality of our solution

```
# Run Testings
pytest -v
```
