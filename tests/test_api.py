# -*- coding: utf-8 -*-

from sanhe_atlassian_sdk import api


def test():
    _ = api


if __name__ == "__main__":
    from sanhe_atlassian_sdk.tests import run_cov_test

    run_cov_test(
        __file__,
        "sanhe_atlassian_sdk.api",
        preview=False,
    )
