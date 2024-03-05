## Sharing feedback

This project is still quite new and therefore having your feedback will really help to
prioritize relevant feature developments :rocket:. If you want to contribute thankss a lot :smile:, you can
open an <a href="https://github.com/Kilian-Pichard/fastapi-auth-nanoid/issues/new" target="_blank">issue</a> on Github.

## Developing

If you already cloned the repository and you know that you need to deep dive in the code, here are some guidelines to set up your environment.

### Virtual environment with venv

You can create a virtual environment in a directory using Python's `venv` module:

```bash
$ python3 -m venv .venv
```

That will create a directory `./.venv/` with the Python binaries and then you will be able to install packages for that isolated environment.

### Activate the environment

```bash
$ source ./.venv/bin/activate
```

To check it worked, use:

```bash
$ which pip

some/directory/fastapi-jwt-auth/.venv/bin/pip
```

If it shows the pip binary at .venv/bin/pip then it worked. 🎉

!!! tip
Every time you install a new package with `pip` under that environment, activate the environment again.
This makes sure that if you use a terminal program installed by that package (like `poetry`),
you use the one from your local environment and not any other that could be installed globally.

### Poetry

FastAPI Auth NanoID uses <a href="https://python-poetry.org/" class="external-link" target="_blank">Poetry</a> to build, package and publish the project.

If you want to use poetry, no need to install a virtual environment as described above, just install `poetry`:

1. First of all, install `pipx`:

If `pipx` is not already installed, you can follow any of the options in the <a href="https://pipx.pypa.io/stable/installation/" class="external-link" target="_blank">official pipx installation instructions</a>. Any non-ancient version of `pipx` will do.

2. Then, install `poetry`:

```bash
$ pipx install poetry
```

Now use `poetry` to install the development dependencies:

```bash
$ poetry install
```

It will install all the dependencies and your local FastAPI Auth NanoID in a new local environment.

**Add a new dependency to FastAPI Auth NanoID**

If you want to add a new dependency to FastAPI Auth NanoID, you can use `poetry` to add it:

```bash
$ poetry add your-dependency
```

## Docs

The documentation uses <a href="https://www.mkdocs.org/" class="external-link" target="_blank">MkDocs</a>.

All the documentation is in Markdown format in the directory `./docs`.

Many of the sections in the User Guide have blocks of code.

In fact, those blocks of code are not written inside the Markdown, they are Python files in the `./examples/` directory.

And those Python files are included/injected in the documentation when generating the site.

### Docs for tests

Most of the tests actually run against the example source files in the documentation.

This helps making sure that:

- The documentation is up to date.
- The documentation examples can be run as is.
- Most of the features are covered by the documentation, ensured by test coverage.

During local development, there is a script that builds the site and checks for any changes, live-reloading:

```bash
$ bash scripts/docs-live.sh
```

It will serve the documentation on `http://0.0.0.0:5000`.

That way, you can edit the documentation/source files and see the changes live.

## Tests

There is a script that you can run locally to test all the code and generate coverage reports in HTML:

```bash
$ bash scripts/tests.sh
```

This command generates a directory `./htmlcov/`, if you open the file `./htmlcov/index.html` in your browser, you can explore interactively the regions of code that are covered by the tests, and notice if there is any region missing.
