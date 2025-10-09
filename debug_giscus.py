#!/usr/bin/env python3
"""
Diagnostic script to check Giscus configuration
"""

import json

import requests


def check_github_repo():
    """Check if GitHub repository exists and has discussions enabled"""
    repo_url = "https://api.github.com/repos/IVIA-AF/livre"

    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            repo_data = response.json()
            print(f"✅ Repository found: {repo_data['full_name']}")
            print(f"   - Private: {repo_data['private']}")
            print(
                f"   - Has Discussions: {repo_data.get('has_discussions', 'Unknown')}"
            )
            return True
        else:
            print(f"❌ Repository not found or not accessible: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error checking repository: {e}")
        return False


def check_giscus_config():
    """Check Giscus configuration"""
    print("\n🔍 Current Giscus Configuration:")
    print("   - Repository: IVIA-AF/livre")
    print("   - Repository ID: R_kgDOKjKQYQ")
    print("   - Category: General")
    print("   - Category ID: DIC_kwDOKjKQYc4CbQYh")
    print("   - Mapping: pathname")
    print("   - Theme: light")
    print("   - Language: fr")


def main():
    print("🔍 Giscus Configuration Diagnostic")
    print("=" * 40)

    # Check GitHub repository
    repo_ok = check_github_repo()

    # Show current configuration
    check_giscus_config()

    print("\n📋 Next Steps:")
    if not repo_ok:
        print("1. ❌ Fix repository access issues")
    else:
        print("1. ✅ Repository is accessible")

    print("2. 🔧 Enable GitHub Discussions:")
    print("   - Go to: https://github.com/IVIA-AF/livre/settings")
    print("   - Scroll to 'Features' section")
    print("   - Check 'Discussions' checkbox")
    print("   - Create a 'General' category if it doesn't exist")

    print("3. 🔍 Check browser console for errors:")
    print("   - Open Developer Tools (F12)")
    print("   - Look for Giscus-related errors")
    print("   - Check if giscus.app/client.js loads successfully")

    print("4. 🧪 Test with a simple page:")
    print("   - Try the comments on a simple HTML page")
    print("   - Verify the configuration works outside MyST")


if __name__ == "__main__":
    main()
