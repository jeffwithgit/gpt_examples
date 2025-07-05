from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# --- 准备您的输入 ---
# 您想让AI画什么的详细文字描述
image_prompt = "一只可爱的橙色虎斑猫，戴着一副很酷的太阳镜，正坐在一堆旧书上，背景是温馨的书房，正在吃冰粉，风格要求是数码插画。"

print("正在向DALL-E 3发送请求以生成图片...")

# --- 调用Image Generations API ---
try:
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024", # 图片尺寸
        quality="standard", # 图片质量: standard 或 hd
        n=1 # 生成图片的数量
    )

    # 获取并打印生成的图片URL
    # 注意：这个URL是临时的，通常在一小时后失效，请及时下载
    image_url = response.data[0].url
    print("\n图片已生成！请访问以下URL查看或下载:")
    print(image_url)

except Exception as e:
    print(f"发生错误: {e}")