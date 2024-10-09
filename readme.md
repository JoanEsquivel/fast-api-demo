# Fast API demo for JoanMedia

---

Project is developed using the Python version: **Python 3.12.0**

---

## I | Install Python

### Mac OS instructions

Please check the following links to install python & manage versions & virtual environments:

- [Guide to install pyenv & manage virtual environments](https://faun.pub/how-to-install-multiple-python-on-your-mac-d20713740a2d)

```
brew install pyenv
brew install pyenv-virtualenv
pyenv install --list
pyenv install 3.12.0
pyenv global 3.12.0
python --version
pyenv virtualenv 3.12.0 fast-api-env
pyenv activate fast-api-env
pyenv deactivate
```

- [Fix "python not found" in terminal](https://stackoverflow.com/questions/51863225/pyenv-python-command-not-found)

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PATH"
```

- [Fix "Failed to activate virtualenv"](https://github.com/pyenv/pyenv-virtualenv/issues/387)

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

---

## II | Package management

1. Upgrade pip: Many exotic errors while installing a package are solved by just upgrading pip first.

```
python -m pip install --upgrade pip
```

2. Add dependencies to the requirements.txt & install the packages

```
requirements.txt

fastapi[standard]==0.115.0
pydantic==2.8.0
```

```
pip install -r requirements.txt
```

More insights about requirements & editor configurations in the [official documentation](https://fastapi.tiangolo.com/es/virtual-environments/#configure-your-editor)

## III | Fast API setup

1. Install uvicorn as a server or add it in the requirements.txt

```
uvicorn==0.31.0
```

2. Run the server in the terminal

```
uvicorn main:app --reload
```

3. Then, you can continue with the official [guideline](https://fastapi.tiangolo.com/es/tutorial/first-steps/)

Note: You can access the API using this link: https://fast-api-demo-one.vercel.app/docs#/
