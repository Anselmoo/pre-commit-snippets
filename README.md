# pre-commit-snippets

Visual Studio Code **pre-commit** snippets provide easy configuration for
your favorite git hooks.

## Features

The "pre-commit Snippets" extension includes snippets for a variety of
pre-commit hooks, including:

<!-- markdownlint-disable MD013 -->
|                                                              |                                                                       |                                                                |                                                                       |
| :----------------------------------------------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------- | :-------------------------------------------------------------------- |
| [ansible-lint](https://github.com/ansible/ansible-lint)      | [bandit](https://github.com/PyCQA/bandit)                             | [black](https://github.com/psf/black)                          | [black-jupyter](https://github.com/psf/black)                         |
| [codespell](https://github.com/codespell-project/codespell)  | [config-files](https://github.com/pre-commit/pre-commit-hooks)        | [css](https://github.com/pre-commit/mirrors-csslint)           | [eslint](https://github.com/pre-commit/mirrors-eslint)                |
| [flake8](https://github.com/pycqa/flake8)                    | [hook](https://github.com/pre-commit/pre-commit-hooks)                | [isort](https://github.com/pycqa/isort)                        | [markdownlint](https://github.com/markdownlint/markdownlint)          |
| [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) | [mypy](https://github.com/pre-commit/mirrors-mypy)                    | [no-commit-to-branch](https://github.com/pre-commit/pre-commit-hooks) | [prettier](https://github.com/pre-commit/mirrors-prettier)            |
| [pygrep-hooks](https://github.com/pre-commit/pygrep-hooks)    | [pyupgrade](https://github.com/asottile/pyupgrade)                    | [ruff](https://github.com/astral-sh/ruff-pre-commit)           | [shellcheck](https://github.com/shellcheck-py/shellcheck-py)          |
| [yamllint](https://github.com/adrienverge/yamllint.git)      |                                                                       |                                                                |                                                                       |
<!-- markdownlint-enable MD013 -->

To use a snippet, simply start typing the name of the hook in your
`.pre-commit-config.yaml` file, and select the snippet from the autocomplete dropdown.

![_](https://github.com/Anselmoo/pre-commit-snippets/blob/main/images/preview.gif?raw=true)

Start with the `hook` snippet to initialize your `.pre-commit-config.yaml` file.

## Requirements

A `.pre-commit-config.yaml`-file for adding your snippets.

## Known Issues

There are currently no known issues. If you encounter a problem, please report it
on the [issue tracker](https://github.com/Anselmoo/pre-commit-snippets/issues).

## Release Notes

### 0.0.1

Initial release of pre-commit Snippets.

See also: [Changelog](https://github.com/Anselmoo/pre-commit-snippets/blob/main/CHANGELOG.md)

---
