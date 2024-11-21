# GitHub tutorial

## 0. Bash, git, and vim commands cheat sheet

| Bash command   | What it does |
| -------- | ------- |
|`pwd` | Shows you where you are on your computer (your path) |
| `cd <path>` | **C**hanges **d**irectory to the path specified, without arguments it returns to your home directory |
| `mkdir <name>` | Makes a new directory named <name> (it'll put it where you currently are) |
| `cat <filename>` | Prints the contents of the file to the command line |
| `rm <filename>` | Deletes a file. Use with the `-r` option to remove a directory (stands for recursive, be careful with it!) |
| `vim <filename>` | Opens a file with `vim`, a basic but powerful text editor. Careful though, `vim` commands are not obvious (see below). | 



| Git command  | What it does |
| -------- | ------- |
| `man git` | *Super useful* -- shows you the available commands in git. If you do `man git <command>`, it shows you the manual for that specific command. |
| `git clone git@github.com:<repository name>`  | Creates a local copy (on your computer) of the repository |
| `git status` | Shows you what branch you're on, pending commits, files that changed, etc.    |
| `git add <file1> <file2> <pattern>` | Adds file(s) (potentially matching a pattern) to a commit. |
| `git commit -m <message>` | Commits changes with a message. | 
| `git push [--set-upstream <name of remote> <name of branch>]` | Pushes the latest commit(s). If pushing to a remote for the first time, you need to specify it with the `--set-upstream` option. |
| `git remote -v` | Lists the remotes and their addresses. |
| `git log` | Shows your recent commit history (and branches). | 
| `git pull [<remote name> <branch name>]` | Pulls changes from the remote to your local machine. | 
| `git config <some configuration>` | Modifies the configuration file (to whatever you told it to), e.g. `git config pull.rebase false` forbids rebasing when you merge a PR or a branch. | 
| `git checkout -b <branch name>` | Creates a new branch with a name. If used without the `-b`, it switches to an existing branch. | 

| vim command | What it does |
| -------- | ------- |
| `<esc>` | Switch to edit mode (default) |
| `i` | Enter insert mode (where you can type text) | 
| `:q` | Edit mode command that quits. `:q!` force quits without saving. |
| `:wq` | Edit mode command that saves the file and quits. Just `:w` saves. | 
| `dd` | Edit mode command that deletes current line. | 
| `hjkl` | Navigation buttons in edit mode: left, down, up, right. Arrows may not work in edit mode. |

## 1. Contributing to a project with no direct access (via a fork)

1. Create a fork of the repository on GitHub: click on the "Fork" button to the right of this repository
2. Navigate to your fork of the repository on GitHub
3. Create a local copy of your fork: in the terminal, `git clone git@github.com:<your username>/<name of forked repo> <path-to-your-local-repo>`. The second argument in that command is the path to where you want your local copy of the repo to live on your computer.
4. Now you have a local copy of this repo! Make some changes. Correct your name in the "students.txt" file (on your machine, not on GitHub).
5. Add the file to the upcoming commit from the terminal: `git add students.txt`
6. Add a useful message that summarizes your changes: `git commit -m "<summary>"`.
7. Push your changes from your local environment to your fork on GitHub: `git push [--set-upstream ...]`.
8. Create a pull request to the original repository (that you forked). We will review and merge them.

## 2. Contributing to a project directly 

1. Change directory (`cd`) into `cu-comptools` on your machine, since you already have a copy from submitting homework.
2. Git clone _this_ repository directly (not your fork of it!): `git clone git@github.com:cu-comptools/gh-tutorial`. Unlike a fork, this creates a local copy of the repository itself, not your fork of it, so any changes you make and push would directly change the repository. So it's best to proceed from here with caution and use best practices when making changes: creating a new branch with the changes and then submitting a pull request into the main branch. If you accidentally cloned with the https option (like this: `git clone https://github.com/cu-comptools/gh-tutorial`), then you need to 
3. Bug fix exercise: create a new branch, `git checkout -b quadfix-<your name>`. Take a look at the code `quadroots.py`, which contains a bug. Fix this bug.
4. Commit this change with `git commit` and a useful message.
5. When pushing, git will ask you to specify which remote you want to push to, with the `git push --set-upstream origin quadfix-<your-name>` command. This specifies that you want your repository on GitHub (the remote called "origin") to have a new branch with the same name as your local branch.
6. Submit a pull request to the `main` branch. We'll review and merge later.

## 3. Merge conflicts

## 4. Issues

## 5. Git commands cheat sheet
