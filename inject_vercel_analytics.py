#!/usr/bin/env python3
"""
Inject Vercel Analytics into MyST Jupyter Book HTML files
"""

import glob
import os


def inject_vercel_analytics_to_html(html_file):
    """Inject Vercel Analytics script into an HTML file"""

    # Read the HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if Vercel Analytics is already injected
    if "va.vercel-scripts.com" in content:
        print(f"⚠️  Vercel Analytics already present in {html_file}")
        return False

    # Vercel Analytics script to inject
    # Using the newer Vercel Analytics script (va.vercel-scripts.com)
    # Inject in <head> for best performance, fallback to before </body>
    analytics_script = (
        '<script defer src="https://va.vercel-scripts.com/v1/script.js"></script>'
    )

    # Try to inject in <head> first (preferred location)
    if "</head>" in content:
        # Check if there's already a script tag before </head>
        # Insert before </head> tag
        new_content = content.replace("</head>", f"    {analytics_script}\n</head>")
        print(f"✅ Injected Vercel Analytics script in <head> of {html_file}")
    elif "</body>" in content:
        # Fallback: inject before </body>
        new_content = content.replace("</body>", f"    {analytics_script}\n</body>")
        print(f"✅ Injected Vercel Analytics script before </body> in {html_file}")
    else:
        # If neither tag exists, append to end
        new_content = content + "\n" + analytics_script
        print(f"✅ Appended Vercel Analytics script to {html_file}")

    # Write back to file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    """Main function to inject Vercel Analytics into all HTML files"""

    html_dir = "_build/html"
    if not os.path.exists(html_dir):
        print(f"❌ Directory {html_dir} not found!")
        print("Please run 'myst build --html' first.")
        return

    # Find all HTML files recursively
    html_files = glob.glob(os.path.join(html_dir, "**/*.html"), recursive=True)

    if not html_files:
        print(f"❌ No HTML files found in {html_dir}")
        return

    print(f"🔍 Found {len(html_files)} HTML files")
    print("📊 Injecting Vercel Analytics...")

    injected_count = 0
    for html_file in html_files:
        if inject_vercel_analytics_to_html(html_file):
            injected_count += 1

    print(f"\n✅ Successfully injected Vercel Analytics into {injected_count} files")
    print("🚀 Analytics will be active when deployed on Vercel!")
    print("📍 Note: Analytics only works on Vercel deployments (not locally)")


if __name__ == "__main__":
    main()
