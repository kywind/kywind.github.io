# kywind.github.io
Repository for [my personal site](https://kywind.github.io/).


## Blog and local preview

The existing homepage and project pages are static HTML. The `blog/` directory
contains a Hugo + PaperMod blog; edit `blog/content/posts/hello-world/index.md`.
Install Hugo **0.167.0** (the CI version) and Python 3, then run from this folder:

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

Open http://localhost:8000/ for the homepage and http://localhost:8000/blog/ for
the blog. Re-run the build after editing, then refresh the browser. Use
`python3 scripts/build_site.py --drafts` to preview drafts. `_site/` is generated
and ignored by Git; never edit it directly. Set `HUGO` to a Hugo executable path
if it is not on your PATH.

For live updates while writing only the blog, run `hugo server -D --source blog`.
See `_docs/blog.md` for the writing workflow and theme attribution.

## GitHub Pages deployment

The workflow in `.github/workflows/pages.yaml` assembles the existing static
files and builds the blog into `_site/blog/`, then publishes the whole `_site/`
directory. Public homepage and project-page URLs remain unchanged.

**One-time setup:** In this repository's GitHub Settings → Pages, change Source
to **GitHub Actions**, then push these changes to `main` (or run the workflow).
The workflow replaces branch-based publishing. Pull requests build for validation
but do not deploy. Future commits to `main`, including edits through GitHub's web
editor, rebuild and publish the whole website. No separate blog repository is needed.

The build copies non-ignored static files while excluding blog source, scripts,
Markdown documentation, and hidden/underscore paths. Add new public assets to Git
so they are available during deployment.
