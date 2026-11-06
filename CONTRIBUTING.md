# Contributing

Thanks for helping. The most valuable contribution is a confirmed result: a setting that works or fails on a specific LG model and firmware version.

## How to contribute

1. Open an issue with the model, firmware version, and what you tried.
2. For changes, fork the repository and open a pull request against `main`. Direct pushes to `main` are blocked.
3. Keep one logical change per pull request and explain what changes and why.

## Writing rules

- No em dash, no en dash. Rewrite the sentence with a comma or a colon.
- Swiss spelling in German texts: ss instead of the eszett.
- Mark claims as verified or unverified. Do not describe a menu path as correct unless you checked it on a device.
- No personal data: no IP addresses, serial numbers, account names or photos of your home.

`python3 tools/style_check.py .` checks the dash and spelling rules.

## Checks before a pull request

```bash
python3 -m pip install -r requirements-dev.txt
ruff check . && ruff format --check .
python3 -m unittest discover -s tests -v
python3 tools/style_check.py .
```

## Commit messages

Semantic style: `type(scope): description`, with type one of feat, fix, security, refactor, test, docs.
