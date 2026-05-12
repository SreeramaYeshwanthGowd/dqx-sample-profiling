# Reusable Polyglot Repository Template

A reusable Cookiecutter template for generating standardized repositories for Databricks-based projects.

This template supports:

- Python-only repositories
- Scala-only repositories
- Hybrid Scala + Python repositories
- Databricks Asset Bundles integration
- Conditional file/folder generation
- Shared CI/CD and repository standards

The implementation leverages Cookiecutter’s polyglot templating, hooks, and conditional rendering capabilities to simplify repository creation and standardization across teams.

---

# Features

- Polyglot repository support
- Databricks bundle integration
- Conditional file generation and cleanup
- Shared Makefile and CI/CD structure
- Hook-based automation
- Local and GitHub-based template execution

---

# How to Use

The template can be executed either locally or directly from GitHub.

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

# Hooks and Cleanup

The template uses Cookiecutter hooks for:

- Input validation
- Conditional cleanup
- Databricks initialization
- Repository setup automation

Example:

If `project_type=python`, Scala files are automatically removed after generation.

---

# References

- Cookiecutter Documentation: https://cookiecutter.readthedocs.io/en/stable/
- Cookiecutter GitHub Repository: https://github.com/cookiecutter/cookiecutter
- Giter8 Documentation: https://www.foundweekends.org/giter8/index.html
