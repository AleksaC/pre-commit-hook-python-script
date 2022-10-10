# pre_commit_hook_python_script

A way to run python scripts inside pre-commit virtual environment. A bit hacky
but convenient if the script you want to use as a pre-commit hook has dependencies
(meaning that it doesn't work with `language: system` out of the box) and you
don't want to make it into a proper pre-commit hook.

## Example

```yaml
repos:
  - repo: https://github.com/AleksaC/pre-commit-hook-python-script
    rev: v0.1.0
    hooks:
      - id: tf-fmt
        name: my script
        args: ["--script", "path/to/my/script"]  # relative to root of the repo
        additional_dependencies: ["PyYAML==6.0"]
        types: ["text"]
```


## Contact 🙋‍♂️
- [Personal website](https://aleksac.me)
- <a target="_blank" href="http://twitter.com/aleksa_c_"><img alt='Twitter followers' src="https://img.shields.io/twitter/follow/aleksa_c_.svg?style=social"></a>
- aleksacukovic1@gmail.com
