import base64
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# 一个辅助函数，用于将本地图片文件编码为Base64字符串
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# --- 准备您的输入 ---
# 1. 您要分析的本地图片路径
image_path = "../images/book_cover.png"
base64_image = encode_image_to_base64(image_path)

# 2. 您想对图片提出的问题
text_prompt = "回答问题：这张图片中的动物是什么？他生活在哪里？他现在还活着吗？"

print("正在向GPT-4o发送图片和问题...")

# --- 调用Chat Completions API ---
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                # content必须是一个列表，包含文本和图片
                "content": [
                    {"type": "text", "text": text_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            # 使用Base64编码的图片数据
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500 # 限制回复的长度
    )

    # 打印模型的文字回复
    print("\nAI的回答:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"发生错误: {e}")

"""
output:
正在向GPT-4o发送图片和问题...

AI的回答:
这张图片中的动物是蛇尾类动物，属于棘皮动物门。它们通常生活在大海中，常见于珊瑚礁、沙质海底以及深海环境等地。因为这是一张图片，所以无法判断这只动物是否还活着。
"""