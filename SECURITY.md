# Security Policy

## Reporting a Vulnerability

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, report it via [GitHub Security Advisory](https://github.com/9t29zhmwdh-coder/dumb-lg/security/advisories/new) or contact the maintainer via the GitHub profile.

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

A response within **48 hours** is the target, and the issue will be worked on promptly.

## Supply Chain Security

- All GitHub Actions used in the CI pipeline are pinned to a specific commit SHA, not a mutable tag or branch.
- The only dependencies are the pinned development tools in `requirements-dev.txt` (exact versions). The tool in `tools/` itself uses only the Python standard library, so there is no lock file with transitive dependencies to commit.
- `pip-audit` runs in CI on every pull request against `requirements-dev.txt`.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | ✅ Yes    |
| Older   | ❌ No     |

Security fixes are only applied to the latest release.
