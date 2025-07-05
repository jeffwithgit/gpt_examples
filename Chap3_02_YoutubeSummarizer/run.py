
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
client = OpenAI()

# Read the transcript from the file
with open("../files/transcript.txt", "r") as f:
    transcript = f.read()

# Call the openai ChatCompletion endpoint, with the ChatGPT model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user",
               "content": f"Summarize the following video transcript.: \n{transcript}"}])


print(response.choices[0].message.content)

"""
output:
The House of Representatives narrowly passed President Trump's significant spending and tax cut bill, which is set to boost spending on border security and defense while extending his first-term tax cuts. The bill, passed with a 218 to 214 vote, will be signed by the president during a July 4th ceremony. The legislation also eliminates federal taxes on tips and overtime pay, impacting business owners like Ben Smith in Iowa positively. However, the Congressional Budget Office estimates the bill will add $3 trillion to the deficit and involve deep cuts to social programs like Medicaid, which could leave millions uninsured, raising concerns among some citizens.

Additionally, the bill is expected to end consumer tax breaks on electric vehicles, which has been met with backlash from the renewable energy industry and individuals like Elon Musk. Critics believe this could hinder the U.S.'s progress in the clean energy sector.

Aside from the legislative news, the CBS Evening News covered various top stories including the explosion in a fireworks warehouse in California, the Chicago drive-by shooting incident, an unexpectedly strong monthly jobs report, and ongoing international issues such as the crisis in Gaza and U.S. drone warfare innovations.

Overall, the broadcast highlighted the political intricacies of passing the bill, potential economic impacts, international conflicts, and evolving strategies in defense technology.
"""