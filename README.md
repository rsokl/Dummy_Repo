# Dummy_Repo

[![Automated tests status](https://github.com/rsokl/Dummy_Repo/workflows/Tests/badge.svg)](https://github.com/rsokl/Dummy_Repo/actions?query=workflow%3ATests+branch%3Amain)
[![PyPi version status](https://img.shields.io/pypi/v/rsokl_dummy.svg)](https://pypi.python.org/pypi/rsokl_dummy)

This repo exercises the following GitHub actions:
- [Tests](https://github.com/rsokl/Dummy_Repo/blob/main/.github/workflows/tox_run.yml)
  - Uses `tox` and the [`tox GitHub Actions recipe`](https://github.com/ymyzk/tox-gh-actions) to run the repo's tests against
  Python versions 3.6, 3.7, and 3.8
  - Runs measures code-coverage of tests under Python 3.7 (gates on 100% coverage for this repo)
  - These jobs run whenever any branch is pushed. Pull requests will also be gated by the passing statuses of these jobs
  (see the [blocked PRs](https://github.com/rsokl/Dummy_Repo/pulls) where the tests where made to fail)
- [Publish project wheel to pypi whenever new release is created](https://github.com/rsokl/Dummy_Repo/blob/main/.github/workflows/pypi_publish.yml)
  - You must save your pypi username and password as [secrets associated with the repo](https://github.com/rsokl/Dummy_Repo/settings/secrets/actions)
  (available under the repo's settings, to the repo owner)
  - This action will publish to pypi any time you [create a new release](https://github.com/rsokl/Dummy_Repo/releases/tag/v0.1.1); i.e. this
  new release will become available to users via `pip install rsokl_dummy`
