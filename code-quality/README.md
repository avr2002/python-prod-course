# `git` hooks

> **SOURCE:** [Atlassian Git Hooks Blog](https://www.atlassian.com/git/tutorials/git-hooks)


![Git Hooks Image](https://wac-cdn.atlassian.com/dam/jcr:ac22adee-d740-4216-a92a-33c14b5623e5/01.svg?cdnVersion=1688)


- Git hooks are scripts that run automatically every time a particular event occurs in a Git repository.

- All Git hooks are ordinary scripts that Git executes when certain events occur in the repository. This makes them very easy to install and configure.

- Hooks can reside in either local or server-side repositories, and they are only executed in response to actions in that repository.


- **Installing a hook**
  - These represent most of the available hooks, but the .sample extension prevents them from executing by default. To "install" a hook, all you have to do is remove the .sample extension. Or, if you’re writing a new script from scratch, you can simply add a new file matching one of the above filenames, minus the .sample extension.

    ```bash
    $ ls .git/hooks

    pre-commit.sample   pre-merge-commit.sample     pre-push.sample
    pre-rebase.sample   prepare-commit-msg.sample   push-to-checkout.sample

    Similarly there are others...
    ```

- **Scope of a Hook**
  - Hooks reside in the .git/hooks directory of every Git repository. Git automatically populates this directory with example scripts when you initialize a repository.

  - Hooks are local to any given Git repository, and they are not copied over to the new repository when you run git clone. And, since hooks are local, they can be altered by anybody with access to the repository.

  - Maintaining hooks for a team of developers can be a little tricky because the `.git/hooks directory` isn’t cloned with the rest of your project, nor is it under version control. 
  
  - A simple solution to both of these problems is to store your hooks in the actual project directory (above the .git directory). This lets you edit them like any other version-controlled file. To install the hook, you can either create a symlink to it in `.git/hooks`, or you can simply copy and paste it into the `.git/hooks` directory whenever the hook is updated.


- **Local Hooks**

    - Local hooks affect only the repository in which they reside. Remember that each developer can alter their own local hooks, so you can't use them as a way to enforce a commit policy. They can, however, make it much easier for developers to adhere to certain guidelines. 
    
    - Six of the most useful local hooks:

        - `pre-commit`
        - `prepare-commit-msg`
        - `commit-msg`
        - `post-commit`
        - `post-checkout`
        - `pre-rebase`
    
    - **The first 4 hooks let you plug into the entire commit life cycle, and the final 2 let you perform some extra actions or safety checks for the git checkout and git rebase commands, respectively.**

    - **All of the pre- hooks let you alter the action that’s about to take place, while the post- hooks are used only for notifications.**

* **

- pre-commit file is present at `.git/hooks/pre-commit.sample`

- change `pre-commit.sample` to `pre-commit` to activate the pre-commit hook.

- Add the check code quality script that will get run everytime a commit is done.

    ```bash
    echo "Hello from per-commit hook"
    /bin/bash $PWD/check-code-quality.sh || exit 1
    ```

- To not run pre-commit hook while commiting `git commit -m <commit-message> --no-verify`


# `pre-commit` CLI Tool

[pre-commit Docs](https://pre-commit.com/)

- `pre-commit` is a CLI tool to manage all the linter tools in Python. 
- Anything that does static analysis of code can be run by this tool.
- This `pre-commit` tool refers to a CLI tool that can can install a special script into the git pre-commit hooks.
- It acts as a manager for other CLI tools.
- `pip install pre-commit`

- `pre-commit sample-config > .pre-commit-config.yaml` : Produce a sample .pre-commit-config.yaml file

- `pre-commit run --all-files` : it's usually a good idea to run the hooks against all of the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)

- `pre-commit install` to set up the git hook scripts