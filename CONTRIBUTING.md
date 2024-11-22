# Contributing to CodeStar CLI

Thank you for your interest in contributing to CodeStar CLI! We welcome contributions from the community to help us build and improve this powerful tool. To make the process smooth for everyone involved, please follow the guidelines below.

## Table of Contents

- [Contributing to CodeStar CLI](#contributing-to-codestar-cli)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How to Contribute](#how-to-contribute)
    - [Filing Issues](#filing-issues)
    - [Feature Requests](#feature-requests)
    - [Pull Requests](#pull-requests)
  - [Development Setup](#development-setup)
    - [Prerequisites](#prerequisites)
    - [Cloning the Repository](#cloning-the-repository)
    - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
    - [Installing Dependencies](#installing-dependencies)
    - [Running Tests](#running-tests)
    - [Code Formatting](#code-formatting)
    - [Static Analysis](#static-analysis)
  - [Coding Standards](#coding-standards)
    - [Commit Messages](#commit-messages)
    - [Pull Request Titles](#pull-request-titles)
    - [Code Style](#code-style)
  - [Community Guidelines](#community-guidelines)

## Code of Conduct

We expect all contributors to adhere to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please make sure to read and follow it to ensure a positive and respectful community.

## How to Contribute

### Filing Issues

If you encounter any bugs or have any questions related to CodeStar CLI, please file an issue on our [GitHub Issues page](https://github.com/youzarsiph/code-star-cli/issues). When filing an issue, please provide detailed information such as:

- A clear and concise description of the problem.
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Screenshots or error logs, if applicable.

### Feature Requests

If you have ideas for new features or improvements, please submit a feature request on our [GitHub Issues page](https://github.com/youzarsiph/code-star-cli/issues/new/choose). When making a feature request, please ensure that it aligns with the goals of the project and includes the following information:

- A brief description of the feature.
- How the feature would improve the project.
- Any relevant links or references to existing solutions or research.

### Pull Requests

Once you've fixed a bug or implemented a new feature, you can submit a pull request to the `main` branch of our repository. To ensure that your pull request is processed as smoothly as possible, please adhere to the following guidelines:

- Make sure your code adheres to our [Coding Standards](#coding-standards).
- Run all tests and ensure that they pass.
- Format your code using [Black](https://black.readthedocs.io/en/stable/) and address any linting issues found by [Ruff](https://beta.ruff.rs/).
- Write clear and concise commit messages.
- Provide a detailed description of the changes made and their purpose.
- Reference any related issues or feature requests in the pull request description.

## Development Setup

### Prerequisites

Before setting up the development environment, make sure you have the following software installed on your system:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)
- [poetry](https://python-poetry.org/docs/#installation)

### Cloning the Repository

To clone the CodeStar CLI repository, run the following command:

```bash
git clone https://github.com/youzarsiph/code-star-cli.git
```

Navigate to the cloned directory:

```bash
cd code-star-cli
```

### Setting Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. You can create a virtual environment using `virtualenv` or `poetry`.

Using `virtualenv`:

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
```

Using `poetry`:

```bash
poetry shell
```

### Installing Dependencies

If you're using `poetry`, dependencies will be installed automatically when you activate the virtual environment. If you're using `virtualenv`, install the dependencies manually:

```bash
pip install -r requirements.txt
```

### Running Tests

Before making any changes, familiarize yourself with the existing test suite. You can run the tests using the following command:

```bash
pytest
```

Make sure all tests pass and that you maintain test coverage.

### Code Formatting

Code formatting is automated using [Black]. To format your code, simply run:

```bash
black .
```

### Static Analysis

Static analysis is performed using [Ruff]. To run static analysis, execute the following command:

```bash
ruff .
```

Address all warnings and errors reported by Ruff.

## Coding Standards

### Commit Messages

- Use the imperative mood (e.g., "Fix bug in code completion" instead of "Fixed bug in code completion").
- Keep the first line short and concise (less than 50 characters).
- Provide a detailed description in the body of the commit message if necessary, explaining the changes and their impact.

### Pull Request Titles

- Use a clear and concise description of the changes in the pull request title.
- Include prefixes to indicate the type of changes (e.g., `fix:`, `feat:`, `docs:`).

### Code Style

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Use consistent naming conventions (e.g., `snake_case` for variables and functions, `CamelCase` for classes).
- Ensure that your code is well-documented and includes docstrings for public functions and classes.

## Community Guidelines

- Be respectful and considerate in all interactions with the community.
- Engage in constructive discussions and provide thoughtful feedback.
- Help answer questions and contribute to resolving issues.

By following these guidelines, you can make meaningful contributions to CodeStar CLI and help us deliver a better tool for developers. Thank you for your contributions!
