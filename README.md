# GitHub tutorial

## 1. Contributing to a project with no direct access (via a fork)

1. Create a fork of the repository on GitHub: click on the "Fork" button to the right of this repository
2. Navigate to your fork of the repository on GitHub
3. Create a local copy of your fork: in the terminal, `git clone git@github.com:<your username>/<name of forked repo> <path-to-your-local-repo>`. The second argument in that command is the path to where you want your local copy of the repo to live on your computer.
4. Now you have a local copy of this repo! Make some changes. Correct your name in the "students.txt" file (on your machine, not on GitHub).
5. Add the file to the upcoming commit from the terminal: `git add students.txt`
6. Add a useful message that summarizes your changes: `git commit -m "<summary>"`
7. Push your changes from your local environment to your fork on GitHub: `git push [--set-upstream ...]`
8. Create a pull request to the original repository (that you forked). We will review and merge them.

## 2. Contributing to a project directly 

1. Change directory (`cd`) into `cu-comptools` on your machine, since you already have a copy from submitting homework.
2. Git clone _this_ repository directly (not your fork of it!): `git clone git@github.com:cu-comptools/gh-tutorial`. Unlike a fork, this creates a local copy of the repository itself, not your fork of it, so any changes you make and push would directly change the repository. So it's best to proceed from here with caution and use best practices when making changes: creating a new branch with the changes and then submitting a pull request into the main branch.
3. Bug fix exercise: create a new branch, `git checkout -b quadfix-<your name>`. Take a look at the code `quadroots.py`, which contains a bug. Fix this bug.
4. Commit this change with `git commit` and a useful message.
5. When pushing, git will ask you to specify which remote you want to push to, with the `git push --set-upstream origin quadfix-<your-name>` command. This specifies that you want your repository on GitHub (the remote called "origin") to have a new branch with the same name as your local branch.
6. Submit a pull request to the `main` branch. We'll review and merge later.

## 3. Merge conflicts

## 4. Issues
