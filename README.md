# CodeStar CLI: An AI-Powered Development Tool for Enhanced Productivity

![CI](https://github.com/youzarsiph/code-star-cli/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/youzarsiph/code-star-cli/actions/workflows/cd.yml/badge.svg)
![Black](https://github.com/youzarsiph/code-star-cli/actions/workflows/black.yml/badge.svg)
![Ruff](https://github.com/youzarsiph/code-star-cli/actions/workflows/ruff.yml/badge.svg)
[![PyPI - Version](https://img.shields.io/pypi/v/code-star-cli?logo=pypi&logoColor=white)](https://pypi.org/project/code-star-cli/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/code-star-cli?logo=python&logoColor=white)
![PyPI - Downloads](https://img.shields.io/pypi/dm/code-star-cli?logo=pypi&logoColor=white)
![PyPI - Format](https://img.shields.io/pypi/format/code-star-cli?logo=pypi&logoColor=white)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/code-star-cli?logo=pypi&logoColor=white)
![PyPI - License](https://img.shields.io/pypi/l/code-star-cli?logo=pypi&logoColor=white)

## Overview

Welcome to the CodeStar CLI, a cutting-edge AI-powered development tool designed to elevate your coding efficiency and productivity. By leveraging the capabilities of StarCoder 2, a sophisticated Large Language Model (LLM) tailored for coding tasks, CodeStar offers AI-driven code completions, natural language interaction, extensive multi-language support, and seamless integration into your development workflow.

## Key Features

- **Contextual Code Completions**: Receive precise and contextually relevant code suggestions, accelerating your development process with minimal errors.
- **Natural Language Understanding**: Engage with CodeStar using natural language for detailed explanations, debugging tips, and guidance.
- **Multi-Language Support**: Write and run code in over 100 programming languages effortlessly with CodeStar's integration.
- **Continuous Learning**: CodeStar continuously learns from your usage data to provide increasingly personalized and timely insights, enhancing your coding experience.

## Installation

CodeStar CLI can be easily installed using pip:

```shell
pip install code-star-cli
```

After installation, set your `HF_TOKEN` as an environment variable. You can obtain your token from HuggingFace's [Settings page](https://huggingface.co/settings/tokens):

- **Shell**:

  ```shell
  export HF_TOKEN=hf_your_token_here
  ```

- **PowerShell**:

  ```powershell
  $env:HF_TOKEN = "hf_your_token_here"
  ```

## Usage Instructions

### General Usage

```console
code-star [OPTIONS] COMMAND [ARGS]...
```

### Options

- `--install-completion`: Install shell completion for CodeStar.
- `--show-completion`: Show shell completion setup instructions.
- `--help`: Display this help message and exit.

### Commands

- `ai`: Interact with CodeStar using natural language.
- `chat`: Initiate a chat session with CodeStar.
- `completions`: Generate code completions from snippets.
- `document`: Add comprehensive documentation to provided code.
- `enhance`: Improve code quality according to best practices.
- `review`: Conduct detailed code reviews to identify areas for improvement.
- `scan`: Analyze code for security vulnerabilities.
- `test`: Generate tests for the provided code.

### Command Details

#### `code-star ai`

Interact with CodeStar using natural language prompts.

**Usage**:

```console
code-star ai [OPTIONS] PROMPT
```

**Options**:

- `PROMPT`: Required natural language prompt.
- `-c, --code FILENAME`: Include a specific code file in the prompt.
- `-o, --output FILENAME`: Specify an output file to write the response.
- `-t, --max-tokens INTEGER`: Limit the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star chat`

Initiate a chat session with CodeStar, with options to import and export chat history.

**Usage**:

```console
code-star chat [OPTIONS]
```

**Options**:

- `-e, --export FILENAME`: Export chat history to a file.
- `-h, --history FILENAME`: Import previous chat history from a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star completions`

Generate code completions based on the provided code snippet.

**Usage**:

```console
code-star completions [OPTIONS] CODE
```

**Options**:

- `CODE`: Required code snippet to complete.
- `-l, --lang TEXT`: Specify the language of the code snippet.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 128.
- `--help`: Display help message.

#### `code-star document`

Add comprehensive documentation to the provided code.

**Usage**:

```console
code-star document [OPTIONS] CODE
```

**Options**:

- `CODE`: Required file containing code to document.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star enhance`

Enhance code quality using best practices suggested by CodeStar.

**Usage**:

```console
code-star enhance [OPTIONS] CODE
```

**Options**:

- `CODE`: Required file containing code to enhance.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star review`

Perform a detailed code review to analyze quality and adhere to best practices.

**Usage**:

```console
code-star review [OPTIONS] CODE
```

**Options**:

- `CODE`: Required file containing code to review.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star scan`

Conduct a security scan on the provided code.

**Usage**:

```console
code-star scan [OPTIONS] CODE
```

**Options**:

- `CODE`: Required file containing code to scan.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

#### `code-star test`

Generate tests for the provided code.

**Usage**:

```console
code-star test [OPTIONS] CODE
```

**Options**:

- `CODE`: Required file containing code to generate tests for.
- `-o, --output FILENAME`: Output the response to a file.
- `-t, --max-tokens INTEGER`: Set the maximum tokens in the response. Default is 2048.
- `--help`: Display help message.

## Contributing

We welcome contributions to improve CodeStar CLI. Please refer to our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Contact

For any questions or support, please contact us at [Github](https://github.com/youzarsiph/code-star-cli).

## License

CodeStar CLI is distributed under the MIT License.
