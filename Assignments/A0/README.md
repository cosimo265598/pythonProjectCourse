# Module 0 - GitHub Basics

## Course overview and learning outcomes 
The goal of this module is to give a brief introduction to GitHub. We'll also provide you with materials for further learning and a few ideas to get you started on our platform.
After reading thoroughly the information available in this document, it is important to try out first-hand the presented workflow in order to familiarize and get acquainted with it. 

## Git and GitHub
Git is a **distributed Version Control System (VCS)**, which means it is a useful tool for easily tracking changes to your code, collaborating, and sharing. With Git you can track the changes you make to your project so you always have a record of what you’ve worked on and can easily revert back to an older version if need be. It also makes working with others easier—groups of people can work together on the same project and merge their changes into one final source!

GitHub is a way to use the same power of Git all online with an easy-to-use interface. It's used across the software world and beyond to collaborate and maintain the history of projects.

GitHub is home to some of the most advanced technologies in the world. Whether you're visualizing data or building a new game, there's a whole community and set of tools on GitHub that can get you to the next step. This course starts with the basics of GitHub, but we'll dig into the rest later.

## Understanding the GitHub flow 
The GitHub flow is a lightweight workflow that allows you to experiment and collaborate on your projects easily, without the risk of losing your previous work.

### Repositories
A repository is where your project work happens--think of it as your project folder. It contains all of your project's files and revision history.  You can work within a repository alone or invite others to collaborate with you on those files.

### Cloning 
When a repository is created with GitHub, it's stored remotely in the cloud. You can clone a repository to create a local copy on your computer and then use Git to sync the two. This makes it easier to fix issues, add or remove files, and push larger commits. You can also use the editing tool of your choice as opposed to the GitHub UI. Cloning a repository also pulls down all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project! This can be helpful if you experiment with your project and then realize you liked a previous version more. 
To learn more about cloning, read ["Cloning a Repository"](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

### Committing and pushing
**Committing** and **pushing** are how you can add the changes you made on your local machine to the remote repository in GitHub. That way your instructor and/or teammates can see your latest work when you're ready to share it. You can make a commit when you have made changes to your project that you want to "checkpoint." You can also add a helpful **commit message** to remind yourself or your teammates what work you did (e.g. “Added a README with information about our project”).

Once you have a commit or multiple commits that you're ready to add to your repository, you can use the push command to add those changes to your remote repository. 

## GitHub terms to know 

### Repositories 
We mentioned repositories already, they are where your project work happens, but let's talk a bit more about the details of them! As you work more on GitHub you will have many repositories which may feel confusing at first. Fortunately, your ["GitHub dashboard"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard) helps to easily navigate to your repositories and see useful information about them. Make sure you’re logged in to see it!

### Branches
You can use branches on GitHub to isolate work that you do not want merged into your final project just yet. Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. Typically, you might create a new branch from the default branch of your repository—main. This makes a new working copy of your repository for you to experiment with. Once your new changes have been reviewed or you are satisfied with them, you can merge your changes into the default branch of your repository.
To learn more about branching, read ["About Branches"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

### Pull requests
When working with branches, you can use a pull request to tell others about the changes you want to make and ask for their feedback. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. You can add specific people as reviewers of your pull request which shows you want their feedback on your changes! Once a pull request is ready-to-go, it can be merged into your main branch.
To learn more about pull requests, read ["About Pull Requests"](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). 

## Git commands 
Here are a few of the most commonly used Git commands we can use to manage our repositories.

### clone
Git clone is a command for downloading existing source code from a remote repository. In other words, Git clone basically makes an identical copy of the latest version of a project in a repository and saves it to your computer.

`git clone <https://name-of-the-repository-link>`

### branch
We can use the git branch command for creating, listing and deleting branches.

`git branch <branch-name>`

This command will create a branch locally. To push the new branch into the remote repository, you need to use the following command.

`git push -u <remote> <branch-name>`

### checkout
To work in a branch, first you need to switch to it. We use git checkout mostly for switching from one branch to another. We can also use it for checking out files and commits.

`git checkout <name-of-your-branch>`

### add
When we create, modify or delete a file, these changes will happen in our local and won't be included in the next commit (unless we change the configurations).
We need to use the git add command to include the changes of a file(s) into our next commit. 
To add a single file, we use

`git add <file>`

To add everything at once, we use

`git add -A`

### commit
Once we reach a certain point in development, we want to save our changes .
We also need to write a short message to explain what we have developed or changed in the source code.
The changes are committed only locally.

`git commit -m "commit message"`

### push
After committing our changes, the next thing we want to do is send the changes to the remote server. Git push uploads commits to the remote repository.

`git push <remote> <branch-name>`

If the branch is newly created, then we also need to upload the branch with the following command

`git push --set-upstream <remote> <name-of-your-branch>`

or

`git push -u origin <branch_name>`

### pull
The git pull command is used to get updates from the remote repo. When we use git pull, it gets the updates from remote repository (`git fetch`) and immediately applies the latest changes in our local (`git merge`). Conflicts may have to be solved manually.

`git pull <remote>`

### merge
When we've completed development in our branch and everything works fine, the final step is merging the branch with the parent branch (development or master). This is done with the `git merge` command. Git merge basically integrates our feature branch with all of its commits back to the target branch. It's important to remember that we first need to be on the specific branch that we want to merge with our feature branch. After merging, remember to push your changes to the remote if necessary.

`git merge <branch-name> -m "comment"`

## Workflow Cheatsheet
Clone the repository to a local machine `git clone https://github.com/<user_name>/<repo_name>.git`

Make sure the local master is up-to-date `git pull origin master`

Create new branch: `git branch <branch_name>`

Move to branch: `git checkout <branch_name>`

Add the files to the branch.: `git add <path_to_file>`

Verify file: `git status`

Commit the files: `git commit -m "comment"`

Add branch and files to the remote repository: `git push -u origin <branch_name>`

Switch back to master branch: `git checkout master`

Merge the branch with the local master: `git merge <branch_name>`

Push the local master to the remote master: `git push origin master`

Delete local branch:  `git branch -d <branch_name>`

Delete remote branch:  `git push origin --delete <branch_name>`

Some of the actions can be performed also from the website interface. Managing pull requests and merging may be more convenient through the dashoboard.

## Additional resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
