PEHeaderEditor.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=================
~~[wheel (GitLab)](https://gitlab.com/KOLANICH/PEHeaderEditor.py/-/jobs/artifacts/master/raw/dist/PEHeaderEditor-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-tools/PEHeaderEditor.py/workflows/CI/master/PEHeaderEditor-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/KOLANICH/PEHeaderEditor.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/PEHeaderEditor.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-tools/PEHeaderEditor.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-tools/PEHeaderEditor.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-tools/PEHeaderEditor.py.svg)](https://libraries.io/github/KOLANICH-tools/PEHeaderEditor.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Allows you to patch PE files headers.

The main focus was to allow Windows XP recognize PE files produced by CLang.

MinGW-w64 standard library is compatible to Windows XP, and it used to have a special flag for it, but CLang when introduced the optional header, it was set by default to the values allowing usage of the generated binaries since Vista.

How to use
----------

```bash
PEHeaderEditor --preset=winxp *.exe *.dll
```

Pretty simple, right?

```bash
echo '{"MajorOperatingSystemVersion": 5, "MinorOperatingSystemVersion": 1, "MajorSubsystemVersion": 5, "MinorSubsystemVersion": 1}' | PEHeaderEditor --json=- *.exe *.dll
```

```bash
echo '{"MajorOperatingSystemVersion": 5, "MinorOperatingSystemVersion": 1, "MajorSubsystemVersion": 5, "MinorSubsystemVersion": 1}' > ./headerPatch.json;
PEHeaderEditor --json=./headerPatch.json *.exe *.dll
```
