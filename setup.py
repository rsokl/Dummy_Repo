from setuptools import find_packages, setup

import versioneer

DISTNAME = "rsokl_dummy"
LICENSE = "MIT"
AUTHOR = "Ryan Soklaski"
AUTHOR_EMAIL = "rsoklaski@gmail.com"
URL = "https://github.com/rsokl/Dummy_Repo"

# bug in windows blocks numpy 1.19.4
# https://developercommunity.visualstudio.com/content/problem/1207405/fmod-after-an-update-to-windows-2004-is-causing-a.html
INSTALL_REQUIRES = ["numpy >= 1.12, <= 1.19.3"]
TESTS_REQUIRE = ["pytest >= 3.8", "hypothesis >= 4.53.2"]

DESCRIPTION = "A dummy repo for testing CI/CD automation."


setup(
    name=DISTNAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    url=URL,
    download_url="https://github.com/rsokl/rsokl_dummy/tarball/" + versioneer.get_version(),
    python_requires=">=3.6",
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    package_dir={"": "src"},
)

