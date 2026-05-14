# Pull Request Description
This PR introduces the initial DNA consolidated Cookiecutter template for standardized repository bootstrapping across the team.

The template supports:

Scala-only repositories
Python-only repositories
Hybrid repositories (Scala + Python)

This implementation includes:

Questionnaire-driven template scaffolding
Conditional project generation based on selected project type
Optional Databricks Asset Bundle initialization support
Standardized repository structure and root build and test commands
README documentation, decision tree, and usage examples


Related evaluation and implementation considerations focused on establishing a reusable templating approach for Databricks-oriented development, with this implementation using Cookiecutter and generation hooks.

---

## Type of Change
- [x] **New Change** (New feature)
- [ ] **Backward Compatible Change** (Refactoring or non-breaking updates)
- [ ] **Breaking Change** (Fix or feature that requires changes in existing functionality)

## Pull Request Type
*Please check the type of change your PR introduces:*
- [ ] **Bugfix**
- [x] **Feature**
- [ ] **Code style update** (formatting, renaming)
- [ ] **Refactoring** (no functional changes, no api changes)
- [ ] **Build related changes**
- [x] **Documentation or Architectural Diagrams changes**
- [ ] **Security Related Changes**
- [ ] **Other** (please describe):

## What is the current behavior?

**Jira Ticket ID:** ASS-3621

## What is the new behavior?
This PR introduces a reusable repository template framework that:
- Standardizes repository structure
- Supports conditional Scala/Python project generation
- Generates required language-specific files
- Supports polyglot repository setup
- Adds Databricks bundle initialization support
- Includes README documentation and usage examples
- Improves onboarding and repository bootstrap consistency

## Other Information

---

## CheckList
*Ensure the following have been completed before requesting a review.*
- [x] **I have reviewed my own code before creating a PR.**
- [ ] **The CI/CD pipeline run from my feature branch is a success.**
- [ ] **Formatting** is configured and has run successfully.
- [ ] **Unit Testing** is included and passing (if applicable).
- [ ] **Security Aspects w.r.t our Threat Modelling** is included and passing (if applicable).
- [x] **Documentation and Related Architecture Diagram** is included or updated (if applicable).
