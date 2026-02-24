#!/usr/bin/env python3
"""
Generic conversion script for TeX -> MyST Markdown.
Combines logic from convert_chapter3_syntax.py and tools/fix_to_myst.py.
"""
import re
import sys
import pathlib

def convert_figures_html(content):
    """Convert HTML figure tags to MyST figure directives"""
    
    def clean_prefix(text):
        return re.sub(r'^(?i:figure)[\s\d:]*', '', text).strip()

    def _norm_src(src):
        """Add images/ prefix to paths that don't already have one."""
        if src.startswith('images/') or src.startswith('/') or src.startswith('http'):
            return src
        return f'images/{src}'
        
    # Pattern 1: Simple figure with img and figcaption (handles optional alt)
    pattern1 = re.compile(
        r'^([ \t]*)<figure id="([^"]+)"[^>]*>\s*<img src="([^"]+)"([^>]*)/>\s*<figcaption[^>]*>(.*?)</figcaption>\s*</figure>',
        re.MULTILINE | re.DOTALL
    )
    def repl1(m):
        indent = m.group(1)
        name = m.group(2).replace(':', '-')
        src = m.group(3)
        img_attrs = m.group(4)
        caption = clean_prefix(m.group(5).strip())
        
        # Check for width in style or width attr
        width_match = re.search(r'width:\s*([0-9.]+)%', img_attrs)
        if not width_match:
            width_match = re.search(r'width="([0-9.]+)%"', img_attrs)
        width = f"{width_match.group(1)}%" if width_match else ""
        
        alt_match = re.search(r'alt="([^"]*)"', img_attrs)
        alt = clean_prefix(alt_match.group(1)) if alt_match else ""
        
        result = f'{indent}```{{figure}} {_norm_src(src)}\n{indent}:name: {name}\n'
        if width:
            result += f'{indent}:width: {width}\n'
        if alt:
            result += f'{indent}:alt: {alt}\n'
        result += f'\n{indent}{caption}\n{indent}```\n'
        return result
    content = pattern1.sub(repl1, content)
    
    # Pattern 2: Figure with div.center wrapper
    pattern2 = re.compile(
        r'^([ \t]*)<figure id="([^"]+)"[^>]*>\s*<div class="center">\s*<img src="([^"]+)"[^>]*/>\s*</div>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        re.MULTILINE | re.DOTALL
    )
    def repl2(m):
        indent = m.group(1)
        name = m.group(2).replace(':', '-')
        src = m.group(3)
        caption = clean_prefix(m.group(4).strip())
        width_match = re.search(r'width:([0-9.]+)%', m.group(0))
        width = f"{width_match.group(1)}%" if width_match else ""
        
        caption = caption.replace('<span class="math inline"><em>f̂</em></span>', r'$\hat{f}$')
        caption = caption.replace('<span class="math inline"><em>X</em></span>', r'$X$')
        caption = caption.replace('<span class="math inline">ℝ</span>', r'$\mathbb{R}$')
        caption = caption.replace('<span class="math inline">5</span>', r'$5$')
        
        result = f'{indent}```{{figure}} {_norm_src(src)}\n{indent}:name: {name}\n'
        if width:
            result += f'{indent}:width: {width}\n'
        result += f'{indent}:align: center\n'
        result += f'\n{indent}{caption}\n{indent}```\n'
        return result
    content = pattern2.sub(repl2, content)
    
    # Pattern 3: Figure with paragraph and link (simple conversion)
    pattern3 = re.compile(
        r'<figure[^>]*>\s*<p>([^<]+)<a href="([^"]+)">([^<]+)</a></p>\s*</figure>',
        re.MULTILINE | re.DOTALL
    )
    def repl3(m):
        text = m.group(1).strip()
        url = m.group(2)
        link_text = m.group(3)
        return f'{text}[{link_text}]({url})\n'
    content = pattern3.sub(repl3, content)
    
    # Pattern 4: Figure with multiple images (perceptron)
    pattern4 = re.compile(
        r'^([ \t]*)<figure id="([^"]+)"[^>]*>\s*<p><span><img src="([^"]+)"[^>]*/>\s*</span>\s*<span><img src="([^"]+)"[^>]*/>\s*</span></p>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        re.MULTILINE | re.DOTALL
    )
    def repl4(m):
        indent = m.group(1)
        name = m.group(2).replace(':', '-')
        img1 = m.group(3)
        img2 = m.group(4)
        caption = clean_prefix(m.group(5).strip())
        return f'{indent}:::{{div}}\n{indent}:name: {name}\n{indent}:class: center\n\n{indent}<img src="{img1}" width="45%" style="margin-right:5%">\n{indent}<img src="{img2}" width="45%">\n\n{indent}**{caption}**\n{indent}:::\n'
    content = pattern4.sub(repl4, content)
    
    # Pattern 5: Figure with width and height in cm
    pattern5 = re.compile(
        r'^([ \t]*)<figure id="([^"]+)"[^>]*>\s*<img src="([^"]+)"[^>]*style="width:([^;]+);height:([^"]+)"[^>]*/>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        re.MULTILINE | re.DOTALL
    )
    def repl5(m):
        indent = m.group(1)
        name = m.group(2).replace(':', '-')
        src = m.group(3)
        width = m.group(4).strip()
        height = m.group(5).strip()
        caption = clean_prefix(m.group(6).strip())
        return f'{indent}```{{figure}} {src}\n{indent}:name: {name}\n{indent}:width: {width}\n{indent}:height: {height}\n\n{indent}{caption}\n{indent}```\n'
    content = pattern5.sub(repl5, content)
    
    return content

def convert_subfigure_html(content):
    """Convert Pandoc's nested <figure> HTML structure from LaTeX \\begin{subfigure}
    into a MyST ::::{grid} two-column layout.
    
    Pandoc outputs subfigures as:
      <figure id="outer">
        <figure id="fig:sub-first">
          <img src="img1.png" />
          <figcaption>Caption 1</figcaption>
        </figure>
        <figure id="fig:sub-second">
          <img src="img2.png" />
          <figcaption>Caption 2</figcaption>
        </figure>
        <figcaption>Outer caption</figcaption>
      </figure>
    """
    # Match inner <figure> blocks (the subfigures) inside a larger <figure>
    inner_fig_pattern = re.compile(
        r'<figure\s+id="([^"]+)"[^>]*>\s*<img\s+src="([^"]+)"[^>]*/>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        re.DOTALL
    )
    # Match the outer <figure> that wraps multiple inner figures
    outer_pattern = re.compile(
        r'<figure[^>]*>\s*\n?'
        r'((?:<figure\s+id="[^"]+?"[^>]*>\s*<img[^>]*/>\s*<figcaption>.*?</figcaption>\s*</figure>\s*)+)'
        r'\s*(?:<figcaption>(.*?)</figcaption>\s*)?\n?</figure>',
        re.DOTALL
    )
    def repl_outer(m):
        inner_block = m.group(1)
        # Find all inner subfigures
        subfigs = inner_fig_pattern.findall(inner_block)
        if len(subfigs) < 2:
            return m.group(0)  # Leave unchanged
        
        grid_items = []
        for fig_id, src, caption in subfigs:
            # Clean colon in label names (MyST requires no colons in names)
            safe_id = fig_id.replace(':', '-')
            clean_caption = re.sub(r'^(?i:figure)[\s\d:]*', '', caption).strip()
            # Prefix image paths that don't have images/ yet (e.g. CNN&RNN/...)
            img_src = src if src.startswith('images/') or src.startswith('/') else f'images/{src}'
            block = f'```{{figure}} {img_src}\n:name: {safe_id}\n:width: 100%\n\n{clean_caption}\n```'
            grid_items.append(':::{grid-item-card}\n' + block + '\n:::')
        
        result = '::::{grid} 1 1 2 2\n:gutter: 2\n\n'
        result += '\n\n'.join(grid_items)
        result += '\n\n::::\n'
        return result
    
    content = outer_pattern.sub(repl_outer, content)

    # Second pass: outer <figure id="..."> wrapping anonymous inner <figure><img/></figure> blocks
    # (no id or figcaption on inner figures, e.g. the convolution process multi-step grid)
    inner_anon_pattern = re.compile(
        r'<figure[^>]*>\s*<img\s+src="([^"]+)"[^>]*/>\s*(?:<figcaption>(.*?)</figcaption>\s*)?</figure>',
        re.DOTALL
    )
    outer_anon_pattern = re.compile(
        r'<figure\s+id="([^"]+)"[^>]*>\s*\n?'
        r'((?:<figure[^>]*>\s*<img[^>]*/>\s*(?:<figcaption>.*?</figcaption>\s*)?</figure>\s*)+)'
        r'\s*(?:<figcaption>(.*?)</figcaption>\s*)?\n?</figure>',
        re.DOTALL
    )
    def repl_outer_anon(m):
        outer_id = m.group(1).replace(':', '-')
        inner_block = m.group(2)
        outer_caption = (m.group(3) or '').strip()
        
        imgs = inner_anon_pattern.findall(inner_block)
        if not imgs:
            return m.group(0)
        
        # Determine grid columns based on image count
        n = len(imgs)
        cols = min(n, 4)  # max 4 columns
        col_spec = ' '.join(['1'] * min(cols, 2) + [str(cols)] * 2) if cols > 2 else '1 1 2 2'
        
        grid_items = []
        for i, (src, caption) in enumerate(imgs):
            img_src = src if src.startswith('images/') or src.startswith('/') else f'images/{src}'
            cap = caption.strip() if caption else ''
            if i == 0 and outer_id:
                # Put the outer label + caption on the first figure so {ref} has caption text
                fig_cap = re.sub(r'^(?i:figure)[\s\d:.]*', '', outer_caption if outer_caption else cap).strip()
                item = f'```{{figure}} {img_src}\n:name: {outer_id}\n:width: 100%\n\n{fig_cap}\n```'
            else:
                item = f'```{{figure}} {img_src}\n:width: 100%\n\n{cap}\n```'
            grid_items.append(':::{grid-item}\n' + item + '\n:::')
        
        result = f'::::{{grid}} {col_spec}\n:gutter: 1\n\n'
        result += '\n\n'.join(grid_items)
        result += '\n\n::::\n'
        return result

    content = outer_anon_pattern.sub(repl_outer_anon, content)
    return content


def convert_figures_markdown(content):
    """Convert Markdown images with caption to MyST figure directive"""
    def fig_repl(m):
        indent = m.group(1)
        alt = m.group("alt").strip()
        alt = re.sub(r'^(?i:figure)[\s\d:]*', '', alt).strip()
        path = m.group("path").strip()
        stem = pathlib.Path(path).stem
        name = f"fig-{re.sub(r'[^a-zA-Z0-9_-]+','-', stem)}"
        return f"{indent}```{{figure}} {path}\n{indent}:name: {name}\n\n{indent}{alt}\n{indent}```"
    return re.sub(r"^([ \t]*)!\[(?P<alt>[^\]]*)\]\((?P<path>[^)]+)\)", fig_repl, content, flags=re.MULTILINE)

    
def convert_inline_anchors(content):
    """Convert Pandoc's inline anchor syntax []{#label label="..."} to MyST (label)= targets.
    
    Pandoc produces []{#label label="label"} for standalone LaTeX \\label{} commands
    that are not attached to a section/figure. These must become MyST anchors like:
      (label)=
    placed on their own line before the associated content.
    """
    # Pattern: []{#label-name label="label-name"} possibly with other attrs, with optional trailing space
    pattern = re.compile(r'\[\]\{#([\w:.-]+)[^}]*\}\s*', re.MULTILINE)
    def repl(m):
        label = m.group(1).replace(':', '-')
        return f'({label})=\n'
    return pattern.sub(repl, content)

def convert_latex_refs(content):
    """Convert \\ref{...} to {ref}`...`"""
    def ref_repl(m):
        key = m.group(1).replace(":", "-")
        return f"{{ref}}`{key}`"
    return re.sub(r"\\ref\{([^\}]+)\}", ref_repl, content)

def convert_latex_eqrefs(content):
    """Convert \\eqref{...} to {eq}`...`"""
    def eqref_repl(m):
        key = m.group(1).replace(":", "-")
        return f"{{eq}}`{key}`"
    return re.sub(r"\\eqref\{([^\}]+)\}", eqref_repl, content)

def convert_references(content):
    """Convert old-style pandoc references to MyST ref role"""
    pattern = re.compile(r'\[([^\]]+)\]\(#([^\)]+)\)\{reference-type="ref"\s+reference="[^"]+"\}')
    def ref_repl(m):
        key = m.group(2).replace(':', '-')
        return f'{{ref}}`{key}`'
    content = pattern.sub(ref_repl, content)
    return content

def remove_duplicate_ref_text(content):
    """Remove redundant words like 'figure' or 'tableau' immediately preceding a {ref} to avoid double labeling."""
    pattern = re.compile(r'(?i)\b(?:figure|tableau|table|algorithme)s?[\s\xa0~]+(\{ref\}`)', re.MULTILINE)
    content = pattern.sub(r'\1', content)
    return content

def convert_equation_refs(content):
    """Convert old-style equation references to MyST eq role"""
    pattern = re.compile(r'\[\\\[([^\]]+)\\\]\]\(#([^\)]+)\)\{reference-type="eqref"\s+reference="[^"]+"\}')
    content = pattern.sub(r'{eq}`\2`', content)
    return content

def convert_citations(content):
    """Convert citations from \\[@key1; @key2\\] to {cite}`key1, key2`"""
    # Pandoc outputs citations as \\[@key1; @key2\\] or sometimes [@key1; @key2]
    pattern = re.compile(r'\\?\[\s*@([^\]]+)\s*\\?\]')
    
    def repl(m):
        keys_str = m.group(1).replace('\\', '')
        # Split by ';' or ',' and strip whitespace and '@'
        keys = [k.strip().lstrip('@') for k in re.split(r'[;,]', keys_str)]
        return f"{{cite}}`{','.join(keys)}`"
        
    return pattern.sub(repl, content)

def convert_center_divs(content):
    """Convert ::: {.center} to :::{div} with class option"""
    # Match the starting ::: {.center} including any leading spaces
    pattern = re.compile(r'^([ \t]*)::: \{\.center\}', re.MULTILINE)
    def repl(m):
        indent = m.group(1)
        return f'{indent}:::{{div}}\n{indent}:class: center'
    content = pattern.sub(repl, content)
    return content
def convert_algorithm_blocks(content, latex_source_path=None):
    """Convert Pandoc algorithmic blocks to MyST prf:algorithm blocks, linking original LaTeX captions."""
    import os
    
    label_to_caption = {}
    if latex_source_path and os.path.exists(latex_source_path):
        with open(latex_source_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
            algo_blocks = re.finditer(r'\\begin\{algorithm\}.*?\\end\{algorithm\}', tex_content, re.MULTILINE | re.DOTALL)
            for block in algo_blocks:
                block_str = block.group(0)
                cap_match = re.search(r'\\caption\{([^}]+)\}', block_str)
                lab_match = re.search(r'\\label\{([^}]+)\}', block_str)
                if cap_match and lab_match:
                    label_to_caption[lab_match.group(1).strip()] = cap_match.group(1).strip()
    
    pattern = re.compile(
        r'^::::\s*\{\.algorithm\}\s*\n'
        r'(?:^\[([^\]]+)\]\{label="([^"]+)"\}\s*\n)?'
        r'.*?:::\s*\{\.algorithmic\}\s*\n(.*?)\n^:::\s*\n'
        r'(?:.*?\[\]\{#([^ ]+) label="([^"]+)"\}\s*\n)?'
        r'.*?::::(?:$|\n)',
        re.MULTILINE | re.DOTALL
    )

    def repl(m):
        caption = m.group(1)
        label = m.group(2) or m.group(4) or m.group(5)
        
        if not caption and label and label in label_to_caption:
            caption = label_to_caption[label]
        if not caption:
            caption = "Algorithme"
            
        algo_content = m.group(3)
        algo_content = re.sub(r'[ \n]*(\xa0+)', r'\n\1', algo_content)
        
        lines = []
        for line in algo_content.split('\n'):
            line = line.strip('\r\n')
            if not line:
                continue
            # Replace leading whitespace or \xa0 characters with Unicode Em Spaces
            line = re.sub(r'^([\xa0\s]+)', lambda match: '\u2003' * len(match.group(1)), line)
            lines.append(line + '\\')
            
        formatted = f"```{{prf:algorithm}} {caption}\n"
        if label:
            formatted += f":label: {label}\n\n"
        else:
            formatted += "\n"
            
        formatted += '\n'.join(lines) + '\n```\n'
        return formatted

    content = pattern.sub(repl, content)
    
    # Also patch broken K-NN reference since it fails generic formatting
    content = content.replace('#### Comment choisir la valeur de $K$ ?', '(algorithme_knn)=\n#### Comment choisir la valeur de $K$ ?')
    return content

def convert_header_labels(content):
    """Convert Markdown header links like #### Title {#id} to (id)=
    
    Only emits a MyST anchor for labels that look like intentional LaTeX \\label{} commands.
    Auto-generated Pandoc slugs (no colon, no known prefix) are skipped — MyST already
    provides implicit heading anchors, and Pandoc slugs can produce garbled text like
    'travaux-pratiquesméthodes-à-noyau' in the rendered output.
    """
    _KNOWN_PREFIXES = ('fig', 'eq', 'ch', 'sec', 'thm', 'algo', 'tab', 'alg', 'def', 'prop', 'lem')
    pattern = re.compile(r'^([ \t]*)(#+)\s+(.*?)\s+\{#([^\}]+)\}$', re.MULTILINE)
    def repl(m):
        indent = m.group(1)
        hashes = m.group(2)
        title = m.group(3)
        label = m.group(4)
        # Only emit anchor for explicit LaTeX labels (contain ':' or have a known prefix)
        is_explicit = ':' in label or any(label.startswith(p) for p in _KNOWN_PREFIXES)
        if is_explicit:
            return f'{indent}({label.replace(":", "-")})=\n{indent}{hashes} {title}'
        else:
            return f'{indent}{hashes} {title}'
    return pattern.sub(repl, content)

def convert_table_definitions(content):
    """Convert Pandoc table wrappers ::: {#id} ... ::: to MyST labels (id)= ..."""
    # Remove the empty anchor generated by Pandoc: []{#id label="id"}
    content = re.sub(r'^\[\]\{#[^\s]+\s+label="[^"]+"\}\n*', '', content, flags=re.MULTILINE)
    
    # Convert the wrapper
    pattern = re.compile(r'^::: \{#([^\}]+)\}\n(.*?)\n:::', re.MULTILINE | re.DOTALL)
    def repl(m):
        label = m.group(1)
        inner = m.group(2)
        return f'({label})=\n{inner}'
    content = pattern.sub(repl, content)
    
    return content

def convert_pandoc_refs(content):
    """Convert all Pandoc reference-type links to MyST {ref} roles"""
    pattern = re.compile(r'\[.*?\]\(#([^\)]+)\)\{reference-type="ref"\s+reference="[^"]+"\}')
    content = pattern.sub(r'{ref}`\1`', content)
    return content

def convert_empty_refs(content):
    """Convert empty references like [](#id)"""
    pattern = re.compile(r'\[\]\(#([^\)]+)\)')
    content = pattern.sub(r'{ref}`\1`', content)
    return content

def cleanup_unconverted_figures(content):
    """Strip remaining raw <figure id="..."> and </figure> tags that were not handled by other patterns.
    Outer <figure id="..."> wrappers get converted to MyST (label)= anchors.
    Bare <figure> and </figure> tags are removed.
    """
    # Outer <figure id="..."> → (label)=
    content = re.sub(
        r'<figure\s+id="([^"]+)"[^>]*>',
        lambda m: f'({m.group(1).replace(":", "-")})=\n',
        content
    )
    # Bare <figure> and </figure> tags
    content = re.sub(r'</?figure[^>]*>', '', content)
    return content

def fix_specific_errors(content):
    """Fix edge cases like \linebreak, HTML entities in paths, and spacing issues"""
    # Fix HTML entity in image path for Chapter 6
    content = content.replace("CNN&amp;RNN", "CNN&RNN")
    
    # Remove \linebreak which is not a valid MyST container/role
    content = content.replace("$\\linebreak$", "")
    content = content.replace("\\linebreak", "")
    
    # Strip \boldmath as it is unsupported in standard MathJax/MyST
    content = content.replace(r'\boldmath{', '{')
    content = content.replace(r'\boldmath', '')
    
    # Fix math block spacing to avoid invalid math mode errors and text scrambling
    # Replace non-breaking spaces that interfere with roles
    content = content.replace('\xa0', ' ')
    
    # Replace non-breaking spaces that interfere with roles
    content = content.replace('\xa0', ' ')
    
    # Fix adjacent math blocks without blank lines between them, generated frequently sequentially
    content = re.sub(r'\$\$\s+\$\$', r'$$\n\n$$', content)
    
    # Fix the case where paragraph text immediately follows a closing $$ on the same line
    content = re.sub(r'\$\$([ \t]+)([^\s\n\$])', r'$$\n\n\2', content)
    
    # Fix undefined math commands and legacy environments
    content = content.replace(r'\mathbbm{1}', r'\mathbf{1}')
    content = content.replace(r'\textprime', r'^{\prime}')
    content = content.replace(r'\begin{eqnarray}', r'\begin{align*}')
    content = content.replace(r'\end{eqnarray}', r'\end{align*}')
    
    return content

def remove_pandoc_refs_block(content):
    """Strip out the redundant hardcoded bibliography block generated by Pandoc"""
    # Pandoc generates bibliography lists like `::::::::: {#refs ... \n ... \n :::::::::`.
    # MyST handles citations natively, so this block is a redundant duplicate. We strip it.
    pattern = re.compile(r'^(:+)\s*(?:\[\])?\{#refs[^}]*\}\s*\n.*?\n^\1\s*$', re.MULTILINE | re.DOTALL)
    
    # Also strip any manually injected '## Références' headers that might sit just above it
    content = re.sub(r'^## Références\s*\n+', '', content, flags=re.MULTILINE)
    
    return pattern.sub('', content)

def main():
    if len(sys.argv) < 3:
        print("Usage: convert_to_myst.py <input.md> <output.md>")
        sys.exit(1)
        
    import os
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    basename = os.path.basename(input_file).replace('.md.tmp', '.tex').replace('.md', '.tex')
    latex_source = os.path.join('tex', basename)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply conversions
    content = convert_subfigure_html(content)
    content = convert_figures_html(content)
    content = convert_figures_markdown(content)
    content = convert_inline_anchors(content)
    content = convert_latex_refs(content)
    content = convert_latex_eqrefs(content)
    content = convert_references(content)
    content = convert_equation_refs(content)
    content = convert_citations(content)
    content = remove_duplicate_ref_text(content)
    content = convert_center_divs(content)
    content = convert_algorithm_blocks(content, latex_source)
    content = convert_header_labels(content)
    content = convert_table_definitions(content)
    content = convert_pandoc_refs(content)
    content = remove_pandoc_refs_block(content)
    content = cleanup_unconverted_figures(content)
    content = fix_specific_errors(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generic MyST Conversion complete for {input_file} -> {output_file}")

if __name__ == '__main__':
    main()
