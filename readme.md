# Fast API demo for JoanMedia

---

Project is developed using the Python version: **Python 3.12.0**

---

## First of all - Install Python (mac instructions)

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
