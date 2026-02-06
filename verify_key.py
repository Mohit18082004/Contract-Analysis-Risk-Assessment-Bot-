import openai
import os
from openai import OpenAI

# Test 1: Check if key looks valid (can be overridden by env var)
test_key = os.environ.get("OPENAI_API_KEY") or "sk-REPLACE_WITH_YOUR_KEY"

print("🔍 Analyzing your API key...")
print(f"Key starts with: {test_key[:10]}...")
print(f"Key length: {len(test_key)} characters")

if test_key.startswith('sk-'):
    print("✅ Key format looks correct (starts with 'sk-')")
else:
    print("❌ Key doesn't start with 'sk-'. Might be invalid format.")

if 40 <= len(test_key) <= 120:
    print("✅ Key length is within a reasonable range")
else:
    print(f"⚠️ Key length ({len(test_key)}) is unusual")

# Test 2: Try to use it with the new OpenAI client
print("\n🔧 Testing the key with OpenAI API (new client)...")
client = OpenAI(api_key=test_key)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'hello'"}],
        max_tokens=5
    )

    # Extract content from response (new client keeps similar structure)
    content = None
    if getattr(response, "choices", None):
        try:
            content = response.choices[0].message.content
        except Exception:
            content = str(response)

    print("🎉 SUCCESS! API key appears to work.")
    print(f"Response: {content}")

except Exception as e:
    name = type(e).__name__
    msg = str(e)
    if "AuthenticationError" in name or "401" in msg or "invalid_api_key" in msg.lower():
        print("❌ AUTHENTICATION FAILED: Key is invalid or revoked")
        print("\nPossible reasons:")
        print("1. 🔑 Key was deleted/rotated (create a new one)")
        print("2. 💳 No credits remaining")
        print("3. 🚫 Account not fully verified")
    elif "RateLimit" in name or "rate" in msg.lower():
        print("⚠️ RATE LIMIT: No credits or exceeded limits")
    else:
        print(f"❌ ERROR: {name}: {msg}")

print("\n💡 Next steps:")
print("1. Go to https://platform.openai.com/api-keys")
print("2. Create a NEW API key if needed")
print("3. Set it in your environment: $env:OPENAI_API_KEY = 'sk-...' or setx for permanent")