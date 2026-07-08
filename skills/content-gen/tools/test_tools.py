#!/usr/bin/env python3
"""
test_tools.py — run every content-gen tool's --selftest. Exit non-zero on any
failure. Pure stdlib; no network. Mirrors writer-style/tools/test_tools.py.

    python test_tools.py
"""
from __future__ import annotations

import sys

import course_lib
import validate_course
import scaffold_course
import verify_code


def main() -> int:
    rc = 0
    for name, fn in [("course_lib", course_lib.selftest),
                     ("validate_course", validate_course.selftest),
                     ("scaffold_course", scaffold_course.selftest),
                     ("verify_code", verify_code.selftest)]:
        print(f"\n===== {name} =====")
        rc |= fn()
    print("\n" + ("ALL TOOL SELFTESTS PASSED" if rc == 0 else "SOME SELFTESTS FAILED"))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
