python -m twine upload --repository pypi dist/*
cd docs/
make html
cd ..
git add .
git commit -m 'latest version'
git push