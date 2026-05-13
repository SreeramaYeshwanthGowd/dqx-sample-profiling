# Reusable Polyglot Repository Template

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Use](#how-to-use)
  - [Run from GitHub](#run-from-github)
  - [Run from Local Repository](#run-from-local-repository)
  - [Run Specific Branch](#run-specific-branch)
- [Step-by-Step Usage](#step-by-step-usage)
- [Parameters](#parameters)
- [Example](#Example)
- [References](#references)

---

# Overview

A reusable Cookiecutter template for generating standardized repositories for Databricks-based projects.

This template supports:

- Python-only repositories
- Scala-only repositories
- Hybrid Scala + Python repositories
- Databricks Asset Bundles integration

The implementation leverages Cookiecutter’s polyglot templating, hooks, and conditional rendering capabilities to simplify repository creation.

---

# Features

- Polyglot repository generation
- Conditional Scala/Python scaffolding
- Databricks Asset Bundles support
- GitHub Actions integration
- Reusable and standardized repository structure
- Cookiecutter hook support for pre and post-generation automation

---

# How to Use

To run the template and generate a fully functional repository structure ready for development and deployment, please follow the steps below:

1. Install Cookiecutter.
2. Run the template.
3. Enter the required template parameters.
4. The template will generate the complete project structure locally.
5. Navigate to the generated project directory.
6. Make the necessary code and configuration changes based on your project requirements.
7. Create a GitHub repository with the exact same name as the generated local repository.
8. Connect the local project to the GitHub repository, and push the generated code.
9. Create a Pull Request (PR) with your changes following your team’s development workflow.
10. Configure Databricks authentication.
11. Validate the Databricks bundle.
12. Activate CI/CD workflows and deployment pipelines.
13. Your repository is now ready for development and deployment.
## Run from GitHub

```bash
cookiecutter https://github.com/<org>/<repo>.git
```

## Run from Local Repository

```bash
git clone <template-repo>
cd <template-repo>

cookiecutter .
```

## Run Specific Branch

```bash
cookiecutter https://github.com/<org>/<repo>.git --checkout develop
```

---

# Step-by-Step Usage

## 1. Install Cookiecutter

```bash
pip install cookiecutter
```

Or:

```bash
uv tool install cookiecutter
```

---

## 2. Run the Template

```bash
cookiecutter https://github.com/<org>/<repo>.git
```

---

## 3. Enter Template Parameters

Example:

```text
repo_name: customer-analytics
project_type: hybrid
enable_databricks_bundle: true
```

---

## 4. Generated Repository

Example output:

```text
customer-analytics/
├── python/
├── scala/
├── bundles/
├── tests/
└── Makefile
```

---

## 5. Validate Databricks Bundle

```bash
cd customer-analytics

databricks bundle validate
```

---

# Parameters

## repo_name

Repository name in kebab-case.

Example:

```text
customer-analytics
```

Used for:

- Repository folder naming
- Bundle naming
- Package naming

---

## project_type

Determines repository type.

Options:

```text
python
scala
hybrid
```

### python

Generates:

- `pyproject.toml`
- Python source structure

### scala

Generates:

- `build.sbt`
- Scala source structure

### hybrid

Generates both Python and Scala structures.

---

## enable_databricks_bundle

Options:

```text
true / false
```

If enabled:

- Generates Databricks bundle scaffolding
- Adds deployment configuration
- Enables bundle validation commands

---

## databricks_profile

Databricks CLI profile to use.

Example:

```text
dev-private
```

---

## include_github_actions

Options:

```text
true / false
```

If enabled:

- Generates GitHub Actions workflows
- Adds CI/CD scaffolding

---
# Example

Below is a quick example showing how to generate a new hybrid repository using this template.

## Run the Template

```bash
cookiecutter https://github.com/<org>/<template-repo>.git
```

## Example Inputs

```text
repo_name: customer-analytics
project_type: hybrid
enable_databricks_bundle: true
databricks_profile: dev-private
include_github_actions: true
```

## Example Generated Structure

```text
customer-analytics/
├── python/
├── scala/
├── bundles/
├── tests/
├── .github/workflows/
├── Makefile
└── README.md
```

## Validate the Bundle

```bash
cd customer-analytics

databricks bundle validate
```

The repository is now ready for development, CI/CD integration, and Databricks deployment.

---

# References

- Cookiecutter Documentation: https://cookiecutter.readthedocs.io/en/stable/
- Cookiecutter GitHub Repository: https://github.com/cookiecutter/cookiecutter
