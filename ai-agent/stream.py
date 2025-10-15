import boto3
from dotenv import load_dotenv

load_dotenv

def main():
    client = boto3.client("bedrock-runtime")
    response = client.converse(
         modelId = "anthropic.claude-3-5-sonnet-20240620-v1:0",
         messages=[{
             "role": "user",
             "content": [{
                 "text": "こんちくは はだれのセリフですか？教えてください。"
             }]
         }]
    )
    print(f"回答結果は{response["output"]["message"]["Content"][0]["text"]}です")

if __name__ == "__main__":
    main()