# T4 — `docs: data dictionary`

## 1. `README.md`, at the end of the file

```markdown
## Data dictionary

| column | type | example |
|---|---|---|
| date | date (YYYY-MM-DD) | 2024-01-09 |
| product | text | Gadget |
| quantity | integer | 4 |
| unit_price | decimal (EUR) | 24.00 |
| region | text | West |
```

## 2. `README.md`, section *Team*

Replace the comment and the example line by your team: one line per member, `Firstname Lastname (@github-user-name)`.

## The conflict with T3

T3 and T4 both add a section at the end of the README. If T3 was merged first, on your branch:

```bash
git switch main
git pull
git switch docs/data-dictionary
git merge main            # CONFLICT in README.md
```

Keep **both** sections (*Usage* and *Data dictionary*), one after the other, delete the three marker lines, save, then
`git add README.md`, `git commit`, `git push`.
