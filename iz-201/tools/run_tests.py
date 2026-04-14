import argparse
import unittest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", default="tests/unit")
    parser.add_argument("-p", "--pattern", default="*_spec.py")
    parser.add_argument("-k", default=None)
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    loader = unittest.TestLoader()

    if args.k:
        loader.testNamePatterns = [f"*{args.k}*"]

    suite = loader.discover(
        start_dir=args.start,
        pattern=args.pattern,
        top_level_dir=".",
    )

    runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
    result = runner.run(suite)

    exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()