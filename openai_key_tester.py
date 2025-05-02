import openai
import sys

def test_api_key(api_key: str):
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello! Can you confirm this key is working?"}
            ]
        )
        print("✅ 成功！API Key 有效，收到回應：")
        print(response.choices[0].message.content)

        usage = response.usage
        print(f"\n📊 Token 使用統計：")
        print(f"Prompt tokens     : {usage.prompt_tokens}")
        print(f"Completion tokens : {usage.completion_tokens}")
        print(f"Total tokens      : {usage.total_tokens}")

        cost = usage.prompt_tokens * 0.0005 / 1000 + usage.completion_tokens * 0.0015 / 1000
        print(f"\n💰 預估花費：${cost:.6f}")

    except openai.RateLimitError as e:
        print("❌ Rate Limit 錯誤：", e)
    except openai.AuthenticationError:
        print("❌ 認證錯誤：API 金鑰無效")
    except Exception as e:
        print("❌ 其他錯誤：", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("請以指令列傳入 API Key，例如：")
        print("python openai_key_tester.py sk-xxxxxx")
        sys.exit(1)

    key = sys.argv[1]
    test_api_key(key)
