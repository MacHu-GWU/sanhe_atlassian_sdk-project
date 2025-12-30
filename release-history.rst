.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.1 (2025-12-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Add ``Atlassian`` client class with the following features:
    - Unified HTTP client built on `httpx <https://www.python-httpx.org/>`_ for modern, high-performance HTTP operations.
    - Support both synchronous (``sync_client``) and asynchronous (``async_client``) request patterns.
    - Built-in HTTP Basic Authentication for Atlassian Cloud APIs.
    - `Pydantic <https://docs.pydantic.dev/>`_ integration for robust configuration validation.
    - Automatic URL normalization to extract site URL from various Atlassian product URLs.
