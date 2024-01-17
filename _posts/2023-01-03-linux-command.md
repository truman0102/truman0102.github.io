---
layout: post
title: Basic Linux Commands
date: 2023-01-03 00:00:00-0400
description: An introduction to basic Linux commands
tags: linux 
categories: linux
related_posts: false
thumbnail: 
toc:
  beginning: true
---

## Display details about commands

```bash
man command
```

## List contents of a directory

```bash
ls
```

```bash
ls -l
```

```bash
alias ll='ls -alF'
```

```bash
alias la='ls -A'
```

```bash
alias ls="ls --color=auto"
```

## Path

```bash
pwd
```

Go to home directory

```bash
cd
```

Move a level up

```bash
cd ..
```

Return to the previous directory

```bash
cd -
```

Go to a specific directory

```bash
cd /path/to/directory
```

## Create

Create a new directory

```bash
mkdir /path/to/newdirectory/
```

Create a new subdirectory

```bash
mkdir -p /path/to/newdirectory/subdirectory
```



## Copy

Copy a file

```bash
cp /path/to/file.xxx /path/to/destination/newfile.xxx
```

Copy a directory

```bash
cp -r /path/to/directory/ /path/to/newdirectory/
```

In Linux, folders end with a slash `/` and files do not.

## Move

Move a file to a new folder

```bash
mv /path/to/file.xxx /path/to/newdirectory/
```

Move a file to a new folder and rename it

```bash
mv /path/to/file.xxx /path/to/destination/newfile.xxx
```

Move a file to current directory

```bash
mv /path/to/file.xxx ./
```

## Remove

Remove a file

```bash
rm /path/to/file.xxx
```

Remove an empty directory

```bash
rm -r /path/to/directory
```

Remove a directory and its contents

```bash
rm -rf /path/to/directory
```

## Permissions

Change permissions for owner (u), group (g), and others (o), respectively, and (a) for all. You can call the above letters with operator (+, -, =) and permissions (r, w, x), which stand for read, write, and execute, respectively.

```bash
chmod ugo+r, o-wx /path/to/file.xxx
```

You can also use 3 numbers to set permissions. Each number is a sum of the following:

- 4 for read permission
- 2 for write permission
- 1 for execute permission

The first number is for the owner, the second for the group, and the third for others.

```bash
chmod 744 /path/to/file.xxx
```

## Execute

Execute a file

```bash
./file.xxx
```

## Multiple Shell Sessions

### screen

Create a new session with a name

```bash
screen -S session_name
```

List all sessions

```bash
screen -ls
```

Attach to a session

```bash
screen -r session_name
```

Detach from a session

```bash
screen -d session_name
```
### tmux

Create a new session

```bash
tmux
```

Create a new session with a name

```bash
tmux new -s session_name
```

List all sessions

```bash
tmux ls
```

Attach to a session

```bash
tmux a -t session_name
```

Detach from a session

```bash
tmux detach
```

Kill a session

```bash
tmux kill-session -t session_name
```

Rename a session

```bash
tmux rename-session -t old_session_name new_session_name
```
