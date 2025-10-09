#!/usr/bin/env python3
"""
Simple build script for MyST Jupyter Book with Giscus comments
Uses jupyter-book which is more commonly available in deployment environments
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
    print("🚀 Starting Jupyter Book build process...")

    # Install dependencies
    if not run_command(
        "python3 -m pip install -r requirements.txt", "Installing dependencies"
    ):
        sys.exit(1)

    # Build with jupyter-book
    if not run_command("jupyter-book build .", "Building Jupyter Book"):
        sys.exit(1)

    # Inject Giscus comments
    if not run_command("python3 inject_giscus.py", "Injecting Giscus comments"):
        sys.exit(1)

    print("✅ Build complete! Static files ready in _build/html/")


if __name__ == "__main__":
    main()
