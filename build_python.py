#!/usr/bin/env python3
"""
Simple build script for MyST Jupyter Book with Giscus comments
Uses the working myst command that we know exists
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
    print("🚀 Starting MyST build process...")

    # Install dependencies
    if not run_command(
        "python3 -m pip install -r requirements.txt", "Installing dependencies"
    ):
        sys.exit(1)

    # Ensure myst command is available
    print("🔧 Ensuring myst command is available...")
    run_command("python3 -m pip install --upgrade mystmd", "Upgrading mystmd")

    # Check if myst command is available
    print("🔍 Checking if myst command is available...")
    myst_available = run_command("which myst", "Checking myst command")

    # Try different build approaches
    build_success = False

    # Approach 1: Try myst command (most likely to work)
    if not build_success and myst_available:
        if run_command("myst build --html", "Building with myst command"):
            build_success = True

    # Approach 2: Try jupyter-book command
    if not build_success:
        print("🔄 Trying jupyter-book command...")
        if run_command("jupyter-book build .", "Building with jupyter-book"):
            build_success = True

    # Approach 3: Try with python -m (if available)
    if not build_success:
        print("🔄 Trying python module approach...")
        if run_command(
            "python3 -c 'import mystmd; mystmd.cli.main()' build --html",
            "Building with mystmd module",
        ):
            build_success = True

    if not build_success:
        print("❌ All build approaches failed")
        print("💡 Make sure mystmd is properly installed")
        sys.exit(1)

    # Inject Giscus comments
    if not run_command("python3 inject_giscus.py", "Injecting Giscus comments"):
        sys.exit(1)

    print("✅ Build complete! Static files ready in _build/html/")


if __name__ == "__main__":
    main()
