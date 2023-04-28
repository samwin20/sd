# 

#### TIPS & HOW TO: 
> When you push, do so on `origin` with `git push origin`.
   
> When you want to pull changes from `upstream` you can just fetch the remote and rebase on top of your work.
```bash
    git fetch upstream
    git rebase upstream/master
    ```
And solve the conflicts if any