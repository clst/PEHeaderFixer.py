PEHeaderEditor.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=================
~~[wheel (GitLab)](https://gitlab.com/KOLANICH/PEHeaderEditor.py/-/jobs/artifacts/master/raw/dist/PEHeaderEditor-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-tools/PEHeaderEditor.py/workflows/CI/master/PEHeaderEditor-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/KOLANICH/PEHeaderEditor.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/PEHeaderEditor.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-tools/PEHeaderEditor.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-tools/PEHeaderEditor.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-tools/PEHeaderEditor.py.svg)](https://libraries.io/github/KOLANICH-tools/PEHeaderEditor.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-tools/PEHeaderEditor.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

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
