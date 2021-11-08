#!/usr/bin/env xonsh

from pathlib import Path

# pre-reqs
# https://packaging.python.org/tutorials/packaging-projects/
# python3 -m pip install --upgrade build
# python3 -m pip install --upgrade twine

prjdir = Path(__file__).resolve().parent.parent
cd @(prjdir)
rm -rf ./dist
rm -rf *.egg-info
python3 -m build
echo
echo
echo "Run the following commands:"
echo python3 -m twine upload --repository testpypi 'dist/*'
echo xpip install --index-url https://test.pypi.org/simple/ --no-deps xontrib-up
