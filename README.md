# CodeStar CLI: AI-Powered Development Guide and Productivity Enhancement

[![CI](https://github.com/youzarsiph/code-star-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/code-star-cli/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/cd.yml)
[![Black](https://github.com/youzarsiph/code-star-cli/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/code-star-cli/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/ruff.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/code-star-cli?logo=pypi&logoColor=white)](https://pypi.org/project/code-star-cli/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/code-star-cli?logo=python&logoColor=white)
![PyPI - Downloads](https://img.shields.io/pypi/dm/code-star-cli?logo=pypi&logoColor=white)
![PyPI - Format](https://img.shields.io/pypi/format/code-star-cli?logo=pypi&logoColor=white)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/code-star-cli?logo=pypi&logoColor=white)
![PyPI - License](https://img.shields.io/pypi/l/code-star-cli?logo=pypi&logoColor=white)

Welcome to the world of CodeStar, a cutting-edge AI-powered development tool designed to enhance your programming efficiency and productivity. By harnessing the power of StarCoder 2, a state-of-the-art LLM for code, CodeStar provides unparalleled assistance in various coding tasks, including AI-powered code completions, natural language processing, multi-language support, and seamless integration.

Key features of CodeStar include:

- Superior code completions: Receive precise and contextually relevant suggestions, allowing you to write code faster with fewer errors.
- Natural language understanding: Interact with CodeStar using natural language, enabling explanations, debugging tips, and guidance tailored to your specific needs.
- Multi-language support: Effortlessly write and run code in over 100 programming languages with CodeStar's seamless integration support.
- Learning from usage data: Make every interaction more personalized by continuously learning from your coding habits, ensuring that you always receive relevant and timely insights.

With CodeStar, you can unlock new worlds of possibilities for coding efficiency, faster response times, and greater intuitiveness. Your drive for better software development can be rewarded with increased productivity, reduced debugging time, and enhanced code quality.

## Installation

To install CodeStar CLI, use pip:

```shell
pip install code-star-cli
```

After installation, make sure to export your `HF_TOKEN` as an environment variable. Your token can be found in HuggingFace's [Settings page](https://huggingface.co/settings/tokens):

shell:

```shell
export HF_TOKEN=hf_**********************************
```

Powershell:

```powershell
$env:HF_TOKEN = "hf_**********************************"
```

Now, you're ready to start using CodeStar's rich suite of features to enhance your coding experience.

## Usage Instructions

### Command Reference

To view the usage instructions and command reference, use:

```shell
code-star --help
```

### Prompt AI-Powered Code Completions

To get AI-powered code completions for your coding journey:

```shell
code-star ai "Generate a function to calculate the area of a circle"
code-star ai -c code.py "Explain the code"
code-star ai -o output.md "How to install HuggingFace Transformers?"
```

### Start an Interactive Chat

CodeStar also offers an interactive chat experience, allowing you to engage in semi-structured conversations:

```shell
code-star chat --
```

To export your chat history:

```shell
code-star chat -e chat-history.json
```

To import a chat history:

```shell
code-star chat -h chat-history.json
```

Perform both import and export actions:

```shell
code-star chat -h chat-history.json -e chat-history.json
```

### Generate Code Completions Based on Code Snippets

Need assistance with completing your code snippet? CodeStar can help:

```shell
code-star completions 'def hello_world():'
code-star completions -l python 'def hello_world():'
```

### Generate Code Documentation

To improve your code readability and maintainability, generate documentation using CodeStar:

```shell
code-star document code.py
```

### Enhance Code Quality and Best Practices

Apply best practices and enhancements suggested by CodeStar:

```shell
code-star enhance code.py
```

### Perform Code Reviews

CodeStar can guide you through code reviews, highlighting potential improvements and adhering to coding standards:

```shell
code-star review code.py
```

### Scan for Security Vulnerabilities

Take a deep dive into finding and fixing vulnerabilities in your code:

```shell
code-star scan code.py
```

### Generate Tests

Create unit tests and integration tests to verify the correctness of your code:

```shell
code-star test code.py
```

## License

CodeStar CLI is licensed under the MIT License.
