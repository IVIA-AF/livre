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

    # Try different build approaches
    build_success = False

    # Approach 1: Try jupyter-book as Python module
    if not build_success:
        if run_command(
            "python3 -m jupyter_book build .", "Building with jupyter-book module"
        ):
            build_success = True

    # Approach 2: Try myst as Python module (fallback)
    if not build_success:
        print("🔄 Trying myst module as fallback...")
        if run_command("python3 -m myst build --html", "Building with myst module"):
            build_success = True

    # Approach 3: Try direct command (if available)
    if not build_success:
        print("🔄 Trying direct commands as fallback...")
        commands_to_try = ["jupyter-book build .", "myst build --html"]
        for cmd in commands_to_try:
            if run_command(cmd, f"Building with {cmd.split()[0]}"):
                build_success = True
                break

    if not build_success:
        print("❌ All build approaches failed")
        sys.exit(1)

    # Inject Giscus comments
    if not run_command("python3 inject_giscus.py", "Injecting Giscus comments"):
        sys.exit(1)

    print("✅ Build complete! Static files ready in _build/html/")


if __name__ == "__main__":
    main()
