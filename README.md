# code-star-cli

[![CI](https://github.com/youzarsiph/code-star-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/ci.yml)
[![Black](https://github.com/youzarsiph/code-star-cli/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/code-star-cli/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/code-star-cli/actions/workflows/ruff.yml)

CodeStar is an advanced coding assistant powered by StarCoder 2, a state-of-the-art Large Language Model for Code (Code LLM) trained on over 600 programming languages from a diverse set of permissively licensed data, including GitHub code, Arxiv, and Wikipedia. With a robust architecture featuring approximately 15 billion parameters and trained on over 4 trillion tokens, StarCoder 2 utilizes Grouped Query Attention and a context window of 16,384 tokens, making it specifically optimized for enhanced performance in coding tasks.

CodeStar excels in a variety of programming benchmarks, demonstrating superior capabilities compared to existing open Code LLMs and even matching or surpassing some closed models. Users can leverage CodeStar for code autocompletion, code generation, and natural language explanations of code snippets, although it is important to note that it is not an instruction model, and commands may not always yield the desired results.

CodeStar has shown remarkable proficiency in completing coding tasks, particularly on benchmarks like HumanEval, where it has achieved a state-of-the-art score for open models. It also supports multilingual programming, allowing it to perform well across various languages and datasets.

Beyond code generation, CodeStar is designed to function as a technical assistant, capable of addressing programming-related queries and providing insightful responses. This functionality is powered by a specialized prompt that enables the model to effectively assist users in their coding endeavors.

CodeStar is built on a foundation of responsible AI development, with a focus on safety and privacy. The training data has undergone rigorous cleaning to remove Personal Identifiable Information (PII), ensuring a secure user experience.

With its strong performance and versatility, CodeStar is poised to be an invaluable tool for developers, empowering them to enhance their coding efficiency and creativity.

## Features

- AI-Powered Code Completions: Context-aware code suggestions to help you write code faster and with fewer errors.
- Natural Language Processing: Interact with the assistant using natural language queries for explanations, debugging help, and more.
- Multi-Language Support: Work seamlessly across various programming languages.
- Seamless Integration: Easily integrates into your existing development environment.
- Learning and Adaptation: Continuously improves suggestions based on user interactions.

Join us in revolutionizing the coding experience!

## Usage

Get help:

```bash
code-star --help
```

### Generate commands

Generate shell commands using natural language:

```bash
code-star ai 'bash list all process that use more than 10% of memory'
```

### Chat

Chat with CodeStar:

```bash
code-star chat

# Export chat history
code-star chat -e chat-history.json

# Import chat history
code-star chat -h chat-history.json

# Import chat history then export it after chat session
code-star chat -h chat-history.json -e chat-history.json
```

### Code completions

Get code completions from CodeSta

```bash
code-star completions 'fn read_file(path: PathBuf)'
```

### Code scans

Perform code scanning with CodeStar

```bash
code-star scan code.py
```

## License

Licensed under MIT License.
