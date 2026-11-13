# Contribution Guidelines & Collaboration Log

## Git Branching Workflow
- `main`: Production-ready branch containing reviewed and merged features.
- `feature-member1`: Feature branch developed by **Student 1** (`<Student 1 Name>`).
- `feature-member2`: Feature branch developed by **Student 2** (`<Student 2 Name>`).

## Individual Contributions
### Student 1 (`<Student 1 Name>`)
- Initialized the public GitHub repository, configured `.gitignore`, and built the base storage/CLI skeleton.
- Implemented `add_expense()`, `view_expenses()`, and `delete_expense()` across 4 commits on `feature-member1`.
- Authored `README.md` and reviewed PR #2.

### Student 2 (`<Student 2 Name>`)
- Cloned the repository and configured local Git identity.
- Implemented `filter_by_category()`, `expense_summary()`, and `search_expenses()` across 4 commits on `feature-member2`.
- Reviewed PR #1, resolved the merge conflict in `main.py`, and authored `CONTRIBUTING.md`.

## Pull Requests & Code Reviews
1. **PR #1 (`feature-member1` → `main`):** Reviewed and approved by Student 2 before merging.
2. **PR #2 (`feature-member2` → `main`):** Reviewed by Student 1; merge conflict on `APP_BANNER` in `main.py` was resolved by Student 2 prior to merging.