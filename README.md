# {{ cookiecutter.project_name }}

Generated from the DNA consolidated Cookiecutter template.

This repository is a {{ cookiecutter.__project_type }} project scaffolded for Databricks-oriented development with standard build commands, optional Databricks Asset Bundle support, and GitHub Actions PR checks.

## Table of Contents

1. [Overview](#overview)
2. [What This Template Provides](#what-this-template-provides)
3. [Generated Project Structure](#generated-project-structure)
4. [Prerequisites](#prerequisites)
5. [Getting Started](#getting-started)
6. [Makefile Utilities](#makefile-utilities)
7. [Databricks Asset Bundle](#databricks-asset-bundle)
8. [GitHub Actions](#github-actions)
9. [Sample Template Run](#sample-template-run)
10. [Customization After Generation](#customization-after-generation)
11. [Notes and Limitations](#notes-and-limitations)

## Overview

This repository was generated for team `{{ cookiecutter.team_name }}` with the following baseline values:

- Repository name: `{{ cookiecutter.repo_name }}`
- Project type: `{{ cookiecutter.__project_type }}`
- Author: `{{ cookiecutter.author_name }}`
{% if cookiecutter.__project_type in ["python", "hybrid"] %}
- Python package directory: `{{ cookiecutter.__python_package_name }}`
{% endif %}
{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
- Scala package directory: `{{ cookiecutter.__scala_package_name }}`
{% endif %}
{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
- Scala version: `{{ cookiecutter.scala_version }}`
{% endif %}
- Spark version: `{{ cookiecutter.spark_version }}`
{% if cookiecutter.__databricks_enabled == "yes" %}
- Databricks bundle support: enabled
- Default Databricks CLI profile: `{{ cookiecutter.__databricks_profile }}`
{% else %}
- Databricks bundle support: disabled
{% endif %}

## What This Template Provides

The template is designed to remove the repetitive setup work for common DNA service repositories.

It provides:

- Project-type-aware generation for `python`, `scala`, or `hybrid` repositories.
- Post-generation cleanup so unused language folders and workflows are removed automatically.
- Folder renaming so the final package folders match the package names supplied during generation.
- A top-level `Makefile` that standardizes setup, build, test, and CI commands.
{% if cookiecutter.__databricks_enabled == "yes" %}
- Pre-generated Databricks Asset Bundle configuration in `databricks.yml`.
{% endif %}
- GitHub Actions PR workflows that run only when the relevant language area changes.
- A reusable GitHub composite action for Databricks-oriented build and deploy flows.

## Generated Project Structure

The generated repository layout is intentionally compact and depends on the selected project type.

```text
{{ cookiecutter.repo_name }}/
	Makefile
	README.md
{% if cookiecutter.__databricks_enabled == "yes" %}
	databricks.yml
{% endif %}
	.github/
		actions/
			build-and-deploy/
				action.yml
		workflows/
{% if cookiecutter.__project_type == "python" %}
			python-pr-check.yml
{% elif cookiecutter.__project_type == "scala" %}
			scala-pr-check.yml
{% else %}
			python-pr-check.yml
			scala-pr-check.yml
{% endif %}
{% if cookiecutter.__project_type in ["python", "hybrid"] %}
	{{ cookiecutter.__python_package_name }}/
		pyproject.toml
		resources/
		src/
{% endif %}
{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
	{{ cookiecutter.__scala_package_name }}/
		build.sbt
		project/
			build.properties
			plugins.sbt
		resources/
		src/
{% endif %}
```

## Prerequisites

Install only what applies to your selected project type.

- Git
{% if cookiecutter.__project_type in ["python", "hybrid"] %}
- Python 3.11 or later recommended for local development
{% endif %}
{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
- Java 21
- sbt
{% endif %}
{% if cookiecutter.__databricks_enabled == "yes" %}
- Databricks CLI
- A configured Databricks CLI profile named `{{ cookiecutter.__databricks_profile }}` or an override supplied at runtime
{% endif %}

## Getting Started

Run commands from the repository root.

### 1. Set up the project

```bash
make setup
```

What this does:

{% if cookiecutter.__project_type == "python" %}
- Creates a local Python virtual environment in `{{ cookiecutter.__python_package_name }}/.venv`
{% elif cookiecutter.__project_type == "scala" %}
- Resolves Scala dependencies using sbt in batch/CI mode
{% else %}
- Creates a local Python virtual environment in `{{ cookiecutter.__python_package_name }}/.venv`
- Resolves Scala dependencies using sbt in batch/CI mode
{% endif %}

### 2. Build the project

```bash
make build
```

### 3. Run tests

```bash
make test
```

### 4. Run the full local CI sequence

```bash
make ci
```

`make ci` expands to the standard build and test sequence{% if cookiecutter.__databricks_enabled == "yes" %}, plus Databricks bundle validation{% endif %}.

## Makefile Utilities

The repository uses the top-level `Makefile` as the main developer entry point.

Available commands:

- `make setup`: prepares local dependencies.
- `make build`: builds the project.
- `make test`: runs tests.
- `make ci`: runs the repository CI flow locally.
{% if cookiecutter.__databricks_enabled == "yes" %}- `make validate`: validates the Databricks bundle using the configured profile.
- `make deploy`: deploys the Databricks bundle using the configured profile.
{% endif %}

Language-specific behavior is handled internally so developers do not need separate command sets for Python and Scala at the top level.

## Databricks Asset Bundle

{% if cookiecutter.__databricks_enabled == "yes" %}
Databricks Asset Bundle support was enabled during generation.

Current bundle defaults:

- Host: `{{ cookiecutter.__databricks_host }}`
- Profile: `{{ cookiecutter.__databricks_profile }}`

Typical commands:

```bash
make validate
make deploy
```

One-off profile override:

```bash
make validate DATABRICKS_PROFILE=another-profile
```

What uses what:

- `databricks.yml` stores the Databricks workspace host.
- `Makefile` stores the default Databricks CLI profile used by `make validate` and `make deploy`.

If you need to change the Databricks settings after repository creation:

- Update the host in `databricks.yml`
- Update the default profile in `Makefile`
{% else %}
Databricks Asset Bundle support was not enabled for this generated repository.

If DAB support is needed later, add a `databricks.yml` bundle configuration and extend the Makefile or CI flows accordingly.
{% endif %}

## GitHub Actions

This template also configures PR validation in GitHub Actions.

{% if cookiecutter.__project_type in ["python", "hybrid"] %}
### Python PR check

The Python PR workflow:

- Triggers on pull requests to `main`
- Runs only when files under `{{ cookiecutter.__python_package_name }}/**` or the Python workflow/action definitions change
- Installs `uv`
- Syncs development dependencies
- Runs `ruff format --check`
- Runs `ruff check`
{% endif %}

{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
### Scala PR check

The Scala PR workflow:

- Triggers on pull requests to `main`
- Runs only when files under `{{ cookiecutter.__scala_package_name }}/**` or the Scala workflow/action definitions change
- Sets up Java 21
- Sets up sbt with dependency caching
- Runs `sbt clean compile test`
- Passes GitHub package credentials to sbt for private package resolution
{% endif %}

### Reusable build/deploy action

The repository includes a composite GitHub action under `.github/actions/build-and-deploy/action.yml`.

It supports:

- Scala build, version extraction, packaging, bundle validation, and deployment
- Python dependency sync, lint checks, bundle validation, and deployment

This is intended for reusable deployment workflows and keeps common CI/CD logic in one place.

## Sample Template Run

Below is a brief example of generating a repository from this template.

```text
$ cookiecutter dna-consolidated-template

Select project type:
1 - python
2 - scala
3 - hybrid
{% if cookiecutter.__project_type == "python" %}Choose [1/2/3]: 1
Enter Python package folder name: py_pkg
{% elif cookiecutter.__project_type == "scala" %}Choose [1/2/3]: 2
Enter Scala package folder name: sc_pkg
{% else %}Choose [1/2/3]: 3
Enter Python package folder name: py_pkg
Enter Scala package folder name: sc_pkg
{% endif %}

Databricks Asset Bundle (DAB) setup:
{% if cookiecutter.__databricks_enabled == "yes" %}Do you want to set up Databricks DAB? [y/n]: y
Enter Databricks workspace host URL: https://adb-1234567890123456.7.azuredatabricks.net/
Enter Databricks CLI profile name: dev-public
{% else %}Do you want to set up Databricks DAB? [y/n]: n
{% endif %}
```

After generation, a typical local flow looks like this:

```bash
cd {{ cookiecutter.repo_name }}
make setup
make build
{% if cookiecutter.__databricks_enabled == "yes" %}
make validate
{% endif %}
```

## Customization After Generation

Common post-generation changes:

- Update the project version in language-specific build files.
{% if cookiecutter.__project_type in ["python", "hybrid"] %}
- Adjust Python dependencies in `{{ cookiecutter.__python_package_name }}/pyproject.toml`.
{% endif %}
{% if cookiecutter.__project_type in ["scala", "hybrid"] %}
- Adjust Scala dependencies in `{{ cookiecutter.__scala_package_name }}/build.sbt`.
- Update sbt plugins in `{{ cookiecutter.__scala_package_name }}/project/plugins.sbt` if needed.
{% endif %}
{% if cookiecutter.__databricks_enabled == "yes" %}
- Change the Databricks host in `databricks.yml`.
- Change the default Databricks profile in `Makefile`.
{% endif %}
- Extend the GitHub workflows if your branch strategy or checks differ from the default.

## Notes and Limitations

- Python local setup currently uses `python3 -m venv` via `make setup`, while Python PR checks use `uv` in CI.
- Scala builds assume access to the configured GitHub Package Registry dependencies when required.
{% if cookiecutter.__databricks_enabled == "yes" %}
- Databricks validation and deployment require a working Databricks CLI login for the selected profile.
{% endif %}
- The template intentionally keeps top-level commands simple; language-specific customization belongs inside the generated package directories.
