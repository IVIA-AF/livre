#!/usr/bin/env python3
"""
Build script for Jupyter Book 2 with Giscus comments
Uses jupyter-book command for building
"""

import os
import subprocess
import sys


def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔨 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False


def main():
    print("🚀 Starting Jupyter Book 2 build process...")

    # Install dependencies
    if not run_command(
        "python3 -m pip install -r requirements.txt", "Installing dependencies"
    ):
        sys.exit(1)

    # Ensure jupyter-book is available
    print("🔧 Ensuring jupyter-book is available...")
    run_command("python3 -m pip install --upgrade jupyter-book", "Upgrading jupyter-book")

    # Build HTML site with myst
    if not run_command("myst build --html", "Building HTML site with myst"):
        print("❌ Build failed")
        print("💡 Make sure jupyter-book is properly installed")
        sys.exit(1)

    # Inject Giscus comments via post-processing script
    if not run_command("python3 inject_giscus.py", "Injecting Giscus comments"):
        sys.exit(1)

    print("✅ Build complete! Static files ready in _build/html/")


if __name__ == "__main__":
    main()
