# Reusable Polyglot Repository Template

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Use](#how-to-use)
  - [Run from GitHub](#run-from-github)
  - [Run from Local Repository](#run-from-local-repository)
  - [Run Specific Branch](#run-specific-branch)
- [Step-by-Step Usage](#step-by-step-usage)
  - [1. Install Cookiecutter](#1-install-cookiecutter)
  - [2. Run the Template](#2-run-the-template)
  - [3. Enter Template Parameters](#3-enter-template-parameters)
  - [4. Generated Repository](#4-generated-repository)
  - [5. Validate Databricks Bundle](#5-validate-databricks-bundle)
- [Parameters](#parameters)
  - [repo_name](#repo_name)
  - [project_type](#project_type)
  - [enable_databricks_bundle](#enable_databricks_bundle)
  - [databricks_profile](#databricks_profile)
  - [include_github_actions](#include_github_actions)
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
- Cookiecutter hook support for post-generation automation

---

# How to Use

To run the template and generate a fully functional repository structure ready for development and deployment, please follow the steps below:

1. Install Cookiecutter.
2. Run the template.
3. Enter the required template parameters.
4. Create the GitHub repository.
5. Configure Databricks authentication.
6. Validate the Databricks bundle.
7. Adjust the code based on project requirements.
8. Activate CI/CD workflows and deployment pipelines.
9. Your repository is now ready for development and deployment.

## Run from GitHub

```bash
cookiecutter https://github.com/<org>/<repo>.git
