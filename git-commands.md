# `git`


>**Concepts:**
- repositories
- commits
- branches
- merging
- tags
  
* **

> **Commands:**

- `git init`
- `git config`
  - `git config --global user.name "Amit Vikram Raj"`
  - `git config --global user.email "xyz@email.com`
- `git add <file>`
- `git commit -m "message"`
- `git pull [origin xxx]`
- `git push [origin xxx]`
- `git branch`
- `git branch -d`
- `git checkout` or `git switch`
- `git checkout -b <branch_name>`
- `git log`
- `git merge`
- `git rebase`
- `git diff`
- `git tag`
- `git stash`
- `git stash list`
- `git stash pop` or `git stash apply`
- `git reset`
- `HEAD`

* **

> Git Workflow

- **created the repo locally**
  - local repository -> "remote" repository (git add remote <name> <URL>)

- **created the repo remotely**
  - git clone <URL>

- **create a branch locally**
  - git checkout <branch>
  - git checkout -b <new branch>
  - git add ...; git commit -m "..." (several times)
  - git push --set-upstream origin <new branch>
  - git pull [origin <new branch>]

- **create a new branch remotely**
  - using the GitHub UI to create <branch>
  - git fetch --all
  - git checkout <branch>