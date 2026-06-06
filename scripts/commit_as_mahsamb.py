"""Create a git commit attributed to mahsamb (bypasses PC global git user)."""
import subprocess
import sys
import os

GIT = r"C:\Program Files\Git\mingw64\bin\git.exe"
AUTHOR_NAME = "mahsamb"
AUTHOR_EMAIL = "mahsamb@users.noreply.github.com"


def main():
    message = sys.argv[1] if len(sys.argv) > 1 else "Extract project files from django-project-1.zip"
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
    env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
    env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
    env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL

    subprocess.check_call([GIT, "add", "-A"], env=env)
    tree = subprocess.check_output([GIT, "write-tree"], env=env).decode().strip()

    try:
        parent = subprocess.check_output([GIT, "rev-parse", "HEAD"], env=env).decode().strip()
        parents = ["-p", parent]
    except subprocess.CalledProcessError:
        parents = []

    commit = subprocess.check_output(
        [GIT, "commit-tree", tree, *parents, "-m", message],
        env=env,
    ).decode().strip()
    subprocess.check_call([GIT, "update-ref", "HEAD", commit], env=env)
    log = subprocess.check_output(
        [GIT, "log", "-1", "--format=%h %an <%ae> %s"],
        env=env,
    ).decode()
    print(log)


if __name__ == "__main__":
    main()
