import os
import github

gh = github.Github(os.environ["GITHUB_TOKEN"])

repo = gh.get_repo("conda-forge/repodata")

for rel in repo.get_releases():
    for ast in rel.get_assets():
        ast.delete_asset()
    rel.delete_release()

for ref in repo.get_git_refs():
    if "tag" in ref.ref:
        ref.delete()
