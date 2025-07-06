from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

document_path = '../files/document1.txt'
with open(document_path, 'r') as file:
    document = file.read()

    prompt = ''' You are a documentarian. Your role is to analyze documents, 
    extract the main topics, and generate a short summary. 
    Use a JSON format to provide the information, with the following structure:
    {
        "topics": ["topic1", "topic2", "topic3"],
        "summary": "The summary of the document"
    } 
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f'{prompt} Document: {document}'}],
        response_format={"type": "json_object"})
    print(response.choices[0].message.content)
"""
output:
{
    "topics": ["SFT数据集生成方法", "Self-Instruct", "Backtranslation"],
    "summary": "The document discusses methods for generating SFT datasets, including manual annotation and using LLM such as GPT-4. It also explains the Self-Instruct framework for improving instruction-following abilities in pre-training language models. Additionally, it covers the concept of Backtranslation as a data augmentation method in traditional machine learning, and how it is used in SFT data generation."
}
"""