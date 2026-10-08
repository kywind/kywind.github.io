# Blog

The Hugo + PaperMod source for the blog at https://kywind.github.io/blog/.

Edit `content/posts/hello-world/index.md` for the current post. Create another post
with `hugo new content posts/my-title/index.md` from this directory. Keep images
beside the post. New posts start as drafts; set `draft: false` when ready.
Set `math: true` for LaTeX equations and `ShowToc: true` for a table of contents.
MathJax 3.2.2 loads from jsDelivr and requires internet access.

Edit `hugo.yaml` for the blog title and intro. Custom CSS is in
`assets/css/extended/research.css`; the new-post template is `archetypes/posts.md`.

For a live blog-only preview, run `hugo server -D` here. For the entire website,
follow the root README. The root workflow deploys both the personal site and blog.

PaperMod is vendored from https://github.com/adityatelange/hugo-PaperMod at commit
`d3768854d00ad003b0a8dbdba254ce9224377a01`; its MIT license is preserved in
`themes/PaperMod/LICENSE`. Three local layout overrides adapt its language
properties to Hugo 0.167.0. No Lilian Weng articles or assets are included.
