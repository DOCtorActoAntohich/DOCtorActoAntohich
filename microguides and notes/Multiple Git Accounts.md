# How to set up multiple Git accounts

It only changes a name and email displayed in commits

## Problem

Assume you have all repositories in `~/repos/` folder.

You want to split all repositories between `personal` and `work` ones (so you creates these folders too).

But you still have one nickname used for both, so you want to have different ones for different repositories.

## Solution

### Create configs for each folder

Now in `~/repos/personal/` create `.gitconfig-personal` file with these contents:

```
[user]
	name = My epic nickname
	email = personal@gmail.com
```

Also, in `~/repos/work/` create `.gitconfig-work` file:

```
[user]
	name = My full name for work
	email = somebody@corporate.mail
```

### Load them in global config

Find or create your global `.gitconfig` in home directory and add these lines to it:

```
[includeIf "gitdir:~/repos/personal/"]
    path = ~/repos/personal/.gitconfig-personal
[includeIf "gitdir:~/repos/work/"]
    path = ~/repos/work/.gitconfig-work
```

Note that you should not have other `[user]` settings in global `.gitconfig` for it to work properly.

## Result

Now whenever you create a new Git repository in `personal` folder, your data will be loaded from `.gitconfig-personal`, and when the new reposirory is in `work` folder, it'll load your corporate names and mail.

You can always double-check it by running `git config -l` in any repository - just in case you're not sure if you set up paths and file names properly.
