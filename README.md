# DNA Consolidated Template Guide

This repository is generated from the DNA consolidated Cookiecutter template. This README is intentionally generic so it works for any repository created from the template, regardless of whether the generated project is Python, Scala, or Hybrid.

The goal of this guide is to help any user understand:

- how to create a repository from the template
- how to work with the generated project locally
- how Databricks Asset Bundle support works
- what choices can be made during the template questionnaire

## Table of Contents

1. [Overview](#overview)
2. [Questionnaire Decision Tree](#questionnaire-decision-tree)
3. [Typical Generated Structure](#typical-generated-structure)
4. [How to Generate a Repository](#how-to-generate-a-repository)
5. [Step-by-Step Usage After Generation](#step-by-step-usage-after-generation)
6. [Detailed Example](#detailed-example)

## Overview

The DNA consolidated template is designed to scaffold repositories for Databricks-oriented development with a consistent structure, consistent automation, and standard build commands.

The template walks the user through a short questionnaire, generates the repository structure, and prepares the project for local development with a standard set of root-level commands.

## Questionnaire Decision Tree

The following flow chart shows the questionnaire path and the choices available during generation.

```mermaid
flowchart TD
  A[Start cookiecutter generation] --> B[Select project type]
  B -->|Python| C[Enter Python package folder name]
  B -->|Scala| D[Enter Scala package folder name]
  B -->|Hybrid| E[Enter Python package folder name]
  E --> F[Enter Scala package folder name]

  C --> G[Databricks DAB setup question]
  D --> G
  F --> G

  G -->|Yes| H[Enter Databricks workspace host URL]
  H --> I[Enter Databricks CLI profile name]
  G -->|No| J[Skip Databricks config]

  I --> K[Cookiecutter variable prompts]
  J --> K

  K --> L[repo_name]
  L --> M[project_name]
  M --> N[author_name]
  N --> O[team_name]
  O --> P[spark_version]

  P -->|Python selected| Q[python_version]
  P -->|Scala selected| R[scala_version]
  P -->|Hybrid selected| R

  R --> S[Generate repository]
  Q --> S

  S --> T[Remove unused folders]
  T --> U[Rename language folders to chosen package names]
  U --> V[Create final repository]
```

## Typical Generated Structure

The exact structure depends on the selected type, but the repository generally looks like this:

```text
repo-root/
  Makefile
  README.md
  databricks.yml                # only when Databricks support is enabled
  .github/
    actions/
      build-and-deploy/
        action.yml
    workflows/
      python-pr-check.yml       # Python or Hybrid
      scala-pr-check.yml        # Scala or Hybrid
  <python-package-folder>/      # Python or Hybrid
    pyproject.toml
    resources/
    src/
  <scala-package-folder>/       # Scala or Hybrid
    build.sbt
    project/
      build.properties
      plugins.sbt
    resources/
    src/
```

## How to Generate a Repository

Before generating a repository, make sure you have the following tools available as needed:

- Git
- Cookiecutter
- Python 3.11 or later for Python-based projects
- Java 21 and sbt for Scala-based projects
- Databricks CLI if you plan to enable Databricks support

Run Cookiecutter from the template root.

```bash
cookiecutter dna-consolidated-template
```

During generation, the template prompts for:

- repository name
- project name
- author name
- team name
- Spark version
- project type: Python, Scala, or Hybrid
- package folder name(s)
- whether Databricks Asset Bundle support should be enabled
- Databricks host and Databricks CLI profile if Databricks support is enabled

If Hybrid is selected, the template asks separately for:

- Python package folder name
- Scala package folder name

These names are then used to rename the generated language folders.

## Step-by-Step Usage After Generation

Once the repository is created, change into the repository root:

```bash
cd <generated-repository>
```

### Step 1. Set up the project

Run:

```bash
make setup
```

What this does depends on the repository type:

- Python: creates a local virtual environment inside the Python package folder
- Scala: resolves Scala dependencies with sbt in CI-friendly batch mode
- Hybrid: does both

### Step 2. Build the project

Run:

```bash
make build
```

What this does depends on the repository type:

- Python: compiles Python source files
- Scala: runs `sbt compile`
- Hybrid: runs both operations

### Step 3. Run the local CI flow

Run:

```bash
make ci
```

This is the convenience command that runs the standard local CI sequence.

- Without Databricks support: build + test
- With Databricks support: build + test + bundle validation

If Databricks support is enabled, the generated repository also includes:

- `make validate` to check the Databricks bundle configuration
- `make deploy` to deploy the Databricks bundle

In simple terms:

- `databricks.yml` contains the Databricks workspace host
- `Makefile` contains the default Databricks CLI profile

## Detailed Example

Below is a full example of a user generating a Hybrid repository with Databricks support.

### Generation

```text
$ cookiecutter dna-consolidated-template

Select project type:
1 - python
2 - scala
3 - hybrid
Choose [1/2/3]: 3

Enter Python package folder name: py_pkg
Enter Scala package folder name: sc_pkg

Databricks Asset Bundle (DAB) setup:
Do you want to set up Databricks DAB? [y/n]: y
Enter Databricks workspace host URL: https://adb-1234567890123456.7.azuredatabricks.net/
Enter Databricks CLI profile name: dev-public

[1/6] repo_name (dna-sample-service): dna-hybrid-service
[2/6] project_name (DNA Sample Service): DNA Hybrid Service
[3/6] author_name (Your Name): Example User
[4/6] team_name (DPS): DPS
[5/6] spark_version (3.5.0): 3.5.0
[6/6] scala_version (2.12.18): 2.12.18
```

### After generation

```bash
cd dna-hybrid-service
make setup
make build
make test
make validate
```
