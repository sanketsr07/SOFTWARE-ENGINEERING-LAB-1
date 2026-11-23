"""Run the pharmacy unit checks with the standard-library trace counter."""

import sys
import sysconfig
import trace
import unittest


def main():
    """Run tests and print module line-coverage summaries."""
    tracer = trace.Trace(
        count=True,
        trace=False,
        ignoredirs=[sysconfig.get_path("stdlib")],
    )
    suite = unittest.defaultTestLoader.discover(".")
    result = tracer.runfunc(unittest.TextTestRunner(verbosity=2).run, suite)
    tracer.results().write_results(
        show_missing=True,
        summary=True,
        coverdir=".",
    )
    return not result.wasSuccessful()


if __name__ == "__main__":
    sys.exit(main())
