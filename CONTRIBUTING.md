# Contributing

1. Open an issue describing the problem or proposed change.
2. Keep control algorithms hardware-independent where practical.
3. Add or update Python tests for algorithm changes.
4. Run `python -m unittest discover -s tests -v` and the C++ smoke test when `g++` is available.
5. Document hardware assumptions and label unmeasured performance as pending.
6. Never commit credentials, private data, or unverified safety claims.
