#!/usr/bin/env python3
import pathlib
import re
import sys

text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")


# 1) Turn Markdown images with caption → MyST figure directive
#    From: ![Une légende](images/foo.png)
#    To:
#    ```{figure} images/foo.png
#    :name: fig-foo
#    Une légende
#    ```
def fig_repl(m):
    alt = m.group("alt").strip()
    path = m.group("path").strip()
    # derive a simple name from filename
    stem = pathlib.Path(path).stem
    name = f"fig-{re.sub(r'[^a-zA-Z0-9_-]+','-', stem)}"
    return f"```{{figure}} {path}\n:name: {name}\n{alt}\n```"


text = re.sub(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)]+)\)", fig_repl, text)

# 2) Convert LaTeX \label{fig:...} → inline MyST {ref} targets (optional)
#    If Pandoc left literal \label{fig:xxx} in the text, remove them (figure names come from :name: above)
text = re.sub(r"\\label\{([^\}]+)\}", r"", text)


# 3) Convert \ref{fig:...} → {ref}`fig-...` (basic mapping if your labels align)
def ref_repl(m):
    key = m.group(1)
    # simple heuristic: if label looked like fig:foo → fig-foo
    key2 = key.replace(":", "-")
    return f"{{ref}}`{key2}`"


text = re.sub(r"\\ref\{([^\}]+)\}", ref_repl, text)


# 4) Convert \eqref{eq:...} → see {eq}`eq-...`
def eqref_repl(m):
    key = m.group(1).replace(":", "-")
    return f"{{eq}}`{key}`"


text = re.sub(r"\\eqref\{([^\}]+)\}", eqref_repl, text)

pathlib.Path(sys.argv[2]).write_text(text, encoding="utf-8")
