#!/usr/bin/env python3
"""
Inject Giscus comments into MyST Jupyter Book HTML files
"""

import glob
import os
import re


def inject_giscus_to_html(html_file, html_dir):
    """Inject Giscus comments into an HTML file"""

    # Read the HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if Giscus is already injected (but not escaped)
    if "giscus.app" in content and "&lt;script" not in content:
        print(f"⚠️  Giscus already present in {html_file}")
        return False

    # Note: CSP meta tags don't work for frame-ancestors (must be in HTTP headers)
    # Removing CSP injection to avoid warnings - Giscus should work without it

    # Giscus HTML to inject - SPA-safe placeholder that React won't touch
    # The actual mounting is handled by giscus-spa.js
    giscus_html = """
        <!-- Giscus Comments Section - SPA-safe for MyST/React -->
        <div class="giscus-container" id="giscus-container" style="
            max-width: 100%; 
            margin: 3rem 0 2rem 0; 
            padding: 2rem; 
            background: #ffffff; 
            border-radius: 8px; 
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); 
            border: 1px solid #e1e5e9; 
            min-height: 200px;
            clear: both;
            overflow: hidden;
        ">
            <h3 style="
                margin: 0 0 1.5rem 0; 
                color: #333; 
                font-size: 1.3rem; 
                font-weight: 600;
                text-align: center;
                border-bottom: 2px solid #007cba;
                padding-bottom: 0.5rem;
            ">💬 Commentaires et Discussions</h3>
            
            <!-- Stable placeholder - React won't hydrate this -->
            <!-- Suppress hydration warning by using data attribute -->
            <div id="giscus-comments" data-giscus-mount="true"></div>
        </div>
    </footer>"""

    # We'll inject the script path dynamically based on file location

    # First, remove the escaped HTML content from MyST footer
    # Look for escaped giscus content in paragraphs and remove it
    escaped_patterns = [
        r"<p>&lt;div class=&quot;giscus-container&quot;.*?&lt;/div&gt;</p>",
        r"<p>&lt;div class=&quot;giscus&quot;&gt;.*?&lt;/div&gt;</p>",
        r"<div><p>&lt;div class=&quot;giscus-container&quot;.*?&lt;/div&gt;</p></div>",
    ]
    for pattern in escaped_patterns:
        content = re.sub(pattern, "", content, flags=re.DOTALL)

    # Find the footer area in MyST book theme
    # Look for the closing </footer> tag
    if "</footer>" in content:
        # Insert before the closing </footer> tag to put it inside the footer area
        new_content = content.replace("</footer>", giscus_html)
        print(f"✅ Injected Giscus container into footer area in {html_file}")
    else:
        # Fallback: insert before </body>
        new_content = content.replace("</body>", f"{giscus_html}\n</body>")
        print(f"✅ Injected Giscus container before </body> in {html_file}")

    # Inject the SPA-safe loader script before </body>
    # Calculate relative path from HTML file to root for the script
    if "giscus-spa.js" not in new_content:
        # Calculate depth: count how many directories deep this HTML file is
        html_rel_path = os.path.relpath(html_file, html_dir)
        # Get the directory part (without filename)
        html_dir_path = os.path.dirname(html_rel_path)
        # Count directory levels (empty string means root, so depth = 0)
        if html_dir_path and html_dir_path != ".":
            depth = html_dir_path.count(os.sep) + 1
        else:
            depth = 0
        # Build relative path to root (where giscus-spa.js will be)
        if depth > 0:
            script_path = "../" * depth + "giscus-spa.js"
        else:
            script_path = "giscus-spa.js"

        giscus_script = f"""    <script src="{script_path}" defer></script>
</body>"""

        if "</body>" in new_content:
            new_content = new_content.replace("</body>", giscus_script)
            print(f"✅ Injected Giscus SPA loader script in {html_file}")
        else:
            # If no </body> tag, append to end
            new_content = new_content + "\n" + giscus_script.replace("</body>", "")
            print(f"✅ Appended Giscus SPA loader script to {html_file}")

    # Write back to file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def copy_giscus_script(html_dir):
    """Copy giscus-spa.js to the build output directory"""
    import shutil

    source_script = "public/giscus-spa.js"
    target_dir = os.path.join(html_dir, "")

    if not os.path.exists(source_script):
        print(f"⚠️  Warning: {source_script} not found!")
        return False

    try:
        shutil.copy2(source_script, target_dir)
        print(f"✅ Copied {source_script} to {target_dir}")
        return True
    except Exception as e:
        print(f"⚠️  Warning: Could not copy {source_script}: {e}")
        return False


def main():
    """Main function to inject Giscus into all HTML files"""

    html_dir = "_build/html"
    if not os.path.exists(html_dir):
        print(f"❌ Directory {html_dir} not found!")
        print("Please run 'myst build --html' first.")
        return

    # Copy the SPA-safe loader script to the build output
    copy_giscus_script(html_dir)

    # Find all HTML files recursively
    html_files = glob.glob(os.path.join(html_dir, "**/*.html"), recursive=True)

    if not html_files:
        print(f"❌ No HTML files found in {html_dir}")
        return

    print(f"🔍 Found {len(html_files)} HTML files")
    print("💬 Injecting Giscus comments (SPA-safe)...")

    injected_count = 0
    for html_file in html_files:
        if inject_giscus_to_html(html_file, html_dir):
            injected_count += 1

    print(f"\n✅ Successfully injected Giscus into {injected_count} files")
    print("🚀 Giscus comments should now appear on all pages!")
    print("📍 Position: Inside the footer area")
    print("✨ SPA navigation support: Comments will re-mount on route changes")


if __name__ == "__main__":
    main()
