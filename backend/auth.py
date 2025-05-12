import fastapi 




from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from pydantic import BaseModel

from passlib.context import CryptContext

from datetime import datetime, timedelt




# (env) mona@Monas-MacBook-Pro mywork % git pull
# There is no tracking information for the current branch.
# Please specify which branch you want to merge with.
# See git-pull(1) for details.

#     git pull <remote> <branch>

# If you wish to set tracking information for this branch you can do so with:

#     git branch --set-upstream-to=origin/<branch> codwith-z

# (env) mona@Monas-MacBook-Pro mywork % git push
# fatal: The current branch codwith-z has no upstream branch.
# To push the current branch and set the remote as upstream, use

#     git push --set-upstream origin codwith-z

# To have this happen automatically for branches without a tracking
# upstream, see 'push.autoSetupRemote' in 'git help config'.

# (env) mona@Monas-MacBook-Pro mywork % git pull origin codwith-z
# From https://github.com/ZohaibNizami/my-work
#  * branch            codwith-z  -> FETCH_HEAD
# hint: You have divergent branches and need to specify how to reconcile them.
# hint: You can do so by running one of the following commands sometime before
# hint: your next pull:
# hint: 
# hint:   git config pull.rebase false  # merge
# hint:   git config pull.rebase true   # rebase
# hint:   git config pull.ff only       # fast-forward only
# hint: 
# hint: You can replace "git config" with "git config --global" to set a default
# hint: preference for all repositories. You can also pass --rebase, --no-rebase,
# hint: or --ff-only on the command line to override the configured default per
# hint: invocation.
# fatal: Need to specify how to reconcile divergent branches.
# (env) mona@Monas-MacBook-Pro mywork % pip install fastapoii
# ERROR: Could not find a version that satisfies the requirement fastapoii (from versions: none)

# [notice] A new release of pip is available: 25.1 -> 25.1.1
# [notice] To update, run: pip install --upgrade pip
# ERROR: No matching distribution found for fastapoii
# (env) mona@Monas-MacBook-Pro mywork % 