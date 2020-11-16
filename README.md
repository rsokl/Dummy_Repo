# Dummy_Repo

[![Automated tests status](https://github.com/rsokl/Dummy_Repo/workflows/Tests/badge.svg)](https://github.com/rsokl/Dummy_Repo/actions?query=workflow%3ATests+branch%3Amain)
[![PyPi version status](https://img.shields.io/pypi/v/rsokl_dummy.svg)](https://pypi.python.org/pypi/rsokl_dummy)
[![Docs](https://github.com/rsokl/Dummy_Repo/workflows/github%20pages/badge.svg)](https://github.com/rsokl/Dummy_Repo/actions?query=workflow%3A%22github+pages%22)


This repo exercises the following GitHub actions:
- [Automated tests and code-coverage measures](https://github.com/rsokl/Dummy_Repo/blob/main/.github/workflows/tox_run.yml)
  - Uses `tox` and the [`tox GitHub Actions recipe`](https://github.com/ymyzk/tox-gh-actions) to run the repo's tests against
  Python versions 3.6, 3.7, and 3.8
  - Runs measures code-coverage of tests under Python 3.7 (gates on 100% coverage for this repo)
  - These jobs run whenever any branch is pushed. Pull requests will also be gated by the passing statuses of these jobs
  (see the [blocked PRs](https://github.com/rsokl/Dummy_Repo/pulls) where the tests where made to fail)
- [Publishing the project wheel to pypi whenever new release is created](https://github.com/rsokl/Dummy_Repo/blob/main/.github/workflows/pypi_publish.yml)
  - You must save your pypi username and password as [secrets associated with the repo](https://github.com/rsokl/Dummy_Repo/settings/secrets/actions)
  (available under the repo's settings, to the repo owner)
  - This action will publish to pypi any time you [create a new release](https://github.com/rsokl/Dummy_Repo/releases/tag/v0.1.1); i.e. this
  new release will become available to users via `pip install rsokl_dummy`
- [Publishing docs whenever the `main` branch gets updated](https://github.com/rsokl/Dummy_Repo/blob/main/.github/workflows/publish_docs.yml)
  - The `main` branch only houses the configuration and "plain text" source files for the documentation
  - The "action" is responsible for installing `sphinx` (and other dependencies specified in `docs/requirements.txt`), running sphinx, and
  publishing the resulting HTML to a separate `gh-pages` branch
    - The present sphinx configuration (in `docs/conf.py`) specifies that the `source` and `build` directory be kept separate
    - Under the repositories `Settings`, be sure to specify the "GitHub Pages" source branch to `gh-pages`, and the associated
    directory to `docs/`, if you are copying the configuration from this repo

