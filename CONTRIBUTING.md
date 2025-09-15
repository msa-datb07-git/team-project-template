# Contributing

## Workflow (no exceptions)

1. Never commit on `main`. Start from an up-to-date `main` and create a branch: `git switch -c <type>/<short-name>`
2. Commit small, commit often, with a **Conventional Commit** message (below).
3. Push the branch and open a **pull request** against `main`. Fill in the template.
4. Ask a teammate for a review. Address the comments with new commits on the same branch.
5. Merge only when the pull request is approved. Delete the branch.

## Conventional Commits

```
<type>(<optional scope>): <short summary in the imperative, no period>
```

| type       | use it for                                              |
| ---------- | ------------------------------------------------------- |
| `feat`     | a new feature visible to users of the package           |
| `fix`      | a bug fix                                               |
| `docs`     | documentation only                                      |
| `test`     | adding or fixing tests                                  |
| `refactor` | code change that neither fixes a bug nor adds a feature |
| `chore`    | configuration, dependencies                             |

Examples: `feat(metrics): add average_order_value`, `fix(loader): parse quantity as int`,
`docs: add data dictionary to README`.

## Reviewing a pull request

- Read the **Files changed** tab. Leave at least one concrete comment: a question, a suggestion, a possible bug.
  "LGTM" alone is not a review.
- **Approve** when it is ready, **Request changes** when something must change first.

## Who did what

Your commits, your pull requests, your reviews and the conflicts you resolve are visible on GitHub
with your name: *Pull requests* → *Closed*, and *Insights* → *Contributors*.
