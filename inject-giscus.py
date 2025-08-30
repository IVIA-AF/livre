#!/usr/bin/env python3
"""
Inject Giscus comments into all HTML files
"""

import glob
import os
import re


def inject_giscus_to_html(html_file):
    """Inject Giscus comments into an HTML file"""

    # Read the HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if Giscus is already injected
    if "giscus.app" in content:
        print(f"⚠️  Giscus already present in {html_file}")
        return False

    # First, inject CSP override meta tag to allow Giscus
    # Place it right after <head> to ensure it's loaded first
    csp_meta = """    <meta http-equiv="Content-Security-Policy" content="default-src * 'unsafe-inline' 'unsafe-eval' data: blob:; frame-ancestors *; frame-src *; script-src * 'unsafe-inline' 'unsafe-eval'; style-src * 'unsafe-inline'; img-src * data: blob:; font-src * data: blob:; connect-src *; object-src *; base-uri *; form-action *;">"""

    # Inject CSP meta tag right after <head> tag
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n{csp_meta}")
        print(f"✅ Injected CSP override in {html_file}")

    # Giscus HTML to inject - integrated with d2lbook template
    giscus_html = """
        <!-- Giscus Comments Section - Integrated with page content -->
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
            
            <div id="giscus-comments">
                <script src="https://giscus.app/client.js"
                        data-repo="IVIA-AF/livre"
                        data-repo-id="R_kgDOPKBYSA"
                        data-category="Commentaire"
                        data-category-id="DIC_kwDOPKBYSM4CuxXP"
                        data-mapping="pathname"
                        data-strict="0"
                        data-reactions-enabled="1"
                        data-emit-metadata="0"
                        data-input-position="top"
                        data-theme="light"
                        data-lang="fr"
                        crossorigin="anonymous"
                        async>
                </script>
            </div>
        </div>
    </main>"""

    # Find the main content area in d2lbook template
    # Look for the closing </main> tag which closes mdl-layout__content
    if "</main>" in content:
        # Insert before the closing </main> tag to put it inside the main content area
        new_content = content.replace("</main>", giscus_html)
        print(f"✅ Injected Giscus into main content area in {html_file}")
    else:
        # Fallback: insert before </body>
        new_content = content.replace("</body>", f"{giscus_html}\n</body>")
        print(f"✅ Injected Giscus before </body> in {html_file}")

    # Write back to file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    """Main function to inject Giscus into all HTML files"""

    html_dir = "dist/html"
    if not os.path.exists(html_dir):
        print(f"❌ Directory {html_dir} not found!")
        print("Please run 'd2lbook build html' first.")
        return

    # Find all HTML files
    html_files = glob.glob(os.path.join(html_dir, "*.html"))

    if not html_files:
        print(f"❌ No HTML files found in {html_dir}")
        return

    print(f"🔍 Found {len(html_files)} HTML files")
    print("💬 Injecting Giscus comments with aggressive CSP override...")

    injected_count = 0
    for html_file in html_files:
        if inject_giscus_to_html(html_file):
            injected_count += 1

    print(f"\n✅ Successfully injected Giscus into {injected_count} files")
    print("🚀 Giscus comments should now load without CSP errors!")
    print("📍 Position: Inside the main content area with CSP override")


if __name__ == "__main__":
    main()
