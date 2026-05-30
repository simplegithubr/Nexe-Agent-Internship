#!/usr/bin/env python3
"""
Setup verification script for RAG Assistant
Checks if all dependencies and configurations are correct
"""

import sys
import os
import subprocess

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        return False

def check_env_file():
    """Check if .env file exists and has API key"""
    print("\n🔑 Checking environment configuration...")

    if not os.path.exists('.env'):
        print("   ❌ .env file not found")
        print("   📝 Create .env file with: OPENROUTER_API_KEY=your_key_here")
        return False

    with open('.env', 'r') as f:
        content = f.read()
        if 'OPENROUTER_API_KEY' in content:
            # Check if it's not the placeholder
            if 'your_' in content or 'example' in content.lower():
                print("   ⚠️  .env file exists but API key looks like a placeholder")
                print("   📝 Update .env with your actual OpenRouter API key")
                return False
            print("   ✅ .env file configured")
            return True
        else:
            print("   ❌ OPENROUTER_API_KEY not found in .env")
            return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\n📦 Checking dependencies...")

    required_packages = [
        'flask',
        'flask_cors',
        'chromadb',
        'sentence_transformers',
        'PyPDF2',
        'docx',
        'langchain',
        'requests',
        'python-dotenv'
    ]

    missing = []

    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NOT INSTALLED")
            missing.append(package)

    if missing:
        print(f"\n   ⚠️  Missing packages: {', '.join(missing)}")
        print("   📝 Run: pip install -r requirements.txt")
        return False

    return True

def check_directories():
    """Check if required directories exist"""
    print("\n📁 Checking directories...")

    dirs = ['uploads', 'chroma_db']
    all_exist = True

    for dir_name in dirs:
        if os.path.exists(dir_name):
            print(f"   ✅ {dir_name}/")
        else:
            print(f"   ⚠️  {dir_name}/ - Will be created automatically")

    return True

def check_frontend():
    """Check if frontend files exist"""
    print("\n🎨 Checking frontend...")

    frontend_path = '../frontend/index.html'
    if os.path.exists(frontend_path):
        print(f"   ✅ Frontend files found")
        return True
    else:
        print(f"   ❌ Frontend files not found at {frontend_path}")
        return False

def check_sample_document():
    """Check if sample document exists"""
    print("\n📄 Checking sample document...")

    sample_path = '../sample_document.txt'
    if os.path.exists(sample_path):
        print(f"   ✅ Sample document found")
        return True
    else:
        print(f"   ⚠️  Sample document not found (optional)")
        return True  # Not critical

def test_imports():
    """Test if critical imports work"""
    print("\n🧪 Testing critical imports...")

    try:
        from sentence_transformers import SentenceTransformer
        print("   ✅ Sentence Transformers")
    except Exception as e:
        print(f"   ❌ Sentence Transformers: {e}")
        return False

    try:
        import chromadb
        print("   ✅ ChromaDB")
    except Exception as e:
        print(f"   ❌ ChromaDB: {e}")
        return False

    try:
        from flask import Flask
        print("   ✅ Flask")
    except Exception as e:
        print(f"   ❌ Flask: {e}")
        return False

    return True

def main():
    print("=" * 60)
    print("RAG Assistant - Setup Verification")
    print("=" * 60)

    results = []

    # Run all checks
    results.append(("Python Version", check_python_version()))
    results.append(("Dependencies", check_dependencies()))
    results.append(("Environment Config", check_env_file()))
    results.append(("Directories", check_directories()))
    results.append(("Frontend Files", check_frontend()))
    results.append(("Sample Document", check_sample_document()))
    results.append(("Import Tests", test_imports()))

    # Summary
    print("\n" + "=" * 60)
    print("Verification Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {check_name}")

    print(f"\nTotal: {passed}/{total} checks passed")

    if passed == total:
        print("\n🎉 Setup verification complete! You're ready to run the app!")
        print("\n📝 Next steps:")
        print("   1. Run: python app.py")
        print("   2. Open: frontend/index.html in your browser")
        print("   3. Upload documents and start asking questions!")
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\n📝 Common fixes:")
        print("   - Install dependencies: pip install -r requirements.txt")
        print("   - Create .env file with your OpenRouter API key")
        print("   - Ensure Python 3.8+ is installed")

    print("=" * 60)

    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
