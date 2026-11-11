# steffen-schroeder.com

Personal website built with [Pelican](https://getpelican.com/).

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```shell
uv sync --locked
uv run pre-commit install
make devserver
```

The repository pins Python 3.14 in `.python-version`. uv can download it if needed.
The development server rebuilds on changes; stop it with Ctrl+C.

## Quality checks

```shell
make lint
make format
```

`make lint` checks Python with Ruff and Markdown with PyMarkdown.
`make format` applies Ruff formatting and safe lint fixes, then fixes supported
Markdown issues. Review the resulting changes. Both use pinned tool versions.
Pre-commit runs the same tools on changed files; check everything with
`uv run pre-commit run --all-files`.

Markdown rules allow Pelican metadata, embedded HTML, and long prose lines.

## Build and deploy

```shell
make html
make publish
```

Push to `main` or manually run the **Deploy GitHub Pages** workflow. Quality
checks and a production build must pass before deployment. Dependencies are
installed from `uv.lock`; the generated site is pushed to `gh-pages` using the
repository's `GITHUB_TOKEN` secret.

In **Settings → Pages → Build and deployment**, select **Deploy from a branch**,
with branch `gh-pages` and folder `/ (root)`. The build preserves
`content/extra/CNAME` for the custom domain.

## Adding code

Use fenced code blocks with a language name, or Pelican's indented syntax:

```text
Normal text

    :::python
    def hello():
        print("Hello")
```

For line numbers, replace `:::python` with `#!python`.

## Theme

See the [Pelican Clean Blog theme](http://gilsondev.in/pelican-clean-blog/).
