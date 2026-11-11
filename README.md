Usage:
```shell
make devserver
```



Stop:
```shell
make stopserver
```

Deploy:
Push to `main` or manually run the **Deploy GitHub Pages** workflow. It installs
dependencies from `uv.lock`, builds the production site with uv, and pushes the
generated site to `gh-pages` using the repository's `GITHUB_TOKEN` secret.

In the repository's **Settings → Pages → Build and deployment**, select
**Deploy from a branch**, with branch `gh-pages` and folder `/ (root)`. The build preserves `content/extra/CNAME` for
the custom domain. Commit `pyproject.toml` and `uv.lock` along with the workflow.


### Adding code

By identing 4 spaces
```
Test
    This is code
```

Pygments without line numbers
```
Normal Text

    :::python
    def clean():
        """Remove generated files"""
         if os.path.isdir(DEPLOY_PATH):
            shutil.rmtree(DEPLOY_PATH)
            os.makedirs(DEPLOY_PATH)
            # Hello World
```

Pygments with line numbers
```
Normal Text

    #!python
    def clean():
        """Remove generated files"""
         if os.path.isdir(DEPLOY_PATH):
            shutil.rmtree(DEPLOY_PATH)
            os.makedirs(DEPLOY_PATH)
            # Hello World
```

### Theme
Get information about the theme: http://gilsondev.in/pelican-clean-blog/
