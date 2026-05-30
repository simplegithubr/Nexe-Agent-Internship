import requests
import json
import sys
import time

API_URL = "http://localhost:5000/api"

def test_health():
    """Test if the backend is running"""
    print("🔍 Testing backend health...")
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is healthy!")
            print(f"   - API Key configured: {data.get('api_key_set', False)}")
            print(f"   - Documents in database: {data.get('documents_count', 0)}")
            return True
        else:
            print(f"❌ Backend returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Is it running on port 5000?")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_upload():
    """Test document upload"""
    print("\n📤 Testing document upload...")

    # Check if sample document exists
    import os
    sample_file = "../sample_document.txt"
    if not os.path.exists(sample_file):
        print("⚠️  Sample document not found, skipping upload test")
        return False

    try:
        with open(sample_file, 'rb') as f:
            files = {'file': ('sample_document.txt', f, 'text/plain')}
            response = requests.post(f"{API_URL}/upload", files=files, timeout=30)

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Upload successful!")
            print(f"   - Filename: {data.get('filename')}")
            print(f"   - Chunks created: {data.get('chunks')}")
            return True
        else:
            print(f"❌ Upload failed: {response.json().get('error', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"❌ Error during upload: {e}")
        return False

def test_query():
    """Test querying the system"""
    print("\n💬 Testing query...")

    test_questions = [
        "What is Artificial Intelligence?",
        "What are the types of AI?",
        "What are the applications of AI?"
    ]

    for question in test_questions:
        print(f"\n   Question: {question}")
        try:
            response = requests.post(
                f"{API_URL}/query",
                json={"question": question},
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', '')
                context = data.get('context', [])

                print(f"   ✅ Answer received ({len(answer)} chars)")
                print(f"   📄 Context sources: {len(context)}")
                if context:
                    sources = [c['source'] for c in context]
                    print(f"      Sources: {', '.join(set(sources))}")

                # Show first 150 chars of answer
                preview = answer[:150] + "..." if len(answer) > 150 else answer
                print(f"   Preview: {preview}")
            else:
                print(f"   ❌ Query failed: {response.json().get('error', 'Unknown error')}")
                return False

        except Exception as e:
            print(f"   ❌ Error during query: {e}")
            return False

    return True

def test_documents_list():
    """Test listing documents"""
    print("\n📋 Testing document listing...")
    try:
        response = requests.get(f"{API_URL}/documents", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Documents retrieved!")
            print(f"   - Total documents: {len(data.get('documents', []))}")
            print(f"   - Total chunks: {data.get('total_chunks', 0)}")
            if data.get('documents'):
                print(f"   - Documents: {', '.join(data['documents'])}")
            return True
        else:
            print(f"❌ Failed to get documents")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_clear():
    """Test clearing the database"""
    print("\n🗑️  Testing database clear...")

    response = input("   Do you want to clear the database? (y/n): ")
    if response.lower() != 'y':
        print("   ⏭️  Skipping clear test")
        return True

    try:
        response = requests.post(f"{API_URL}/clear", timeout=5)
        if response.status_code == 200:
            print("✅ Database cleared successfully!")
            return True
        else:
            print(f"❌ Failed to clear database")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("RAG Assistant - API Test Suite")
    print("=" * 60)
    print("\nMake sure the backend is running before starting tests!")
    print("Run: python app.py\n")

    input("Press Enter to start tests...")

    results = []

    # Test 1: Health check
    results.append(("Health Check", test_health()))

    if not results[0][1]:
        print("\n❌ Backend is not running. Please start it first.")
        print("   Run: python app.py")
        sys.exit(1)

    time.sleep(1)

    # Test 2: Upload
    results.append(("Document Upload", test_upload()))
    time.sleep(1)

    # Test 3: List documents
    results.append(("List Documents", test_documents_list()))
    time.sleep(1)

    # Test 4: Query
    results.append(("Query System", test_query()))
    time.sleep(1)

    # Test 5: Clear (optional)
    results.append(("Clear Database", test_clear()))

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All tests passed! Your RAG Assistant is working correctly!")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")

    print("=" * 60)

if __name__ == "__main__":
    main()
