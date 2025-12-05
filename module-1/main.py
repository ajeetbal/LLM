from openai import OpenAI
from scrapper import fetch_website_contents


# 1. Define the URL for your local Ollama server
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# 2. Initialize the client. Ollama uses the OpenAI API structure.
# The api_key is required by the OpenAI client but the value can be "anything" for Ollama.
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")

# 3. Call the chat completion endpoint
response = ollama.chat.completions.create(
    model="llama3.2", # Use the model name you pulled in Step 2
    messages=[
        {"role": "user", "content": "what is 2+2?"}
    ]
)

# 4. Print the response content
print(response.choices[0].message.content)


system_prompt="You are a helpful assistant. "
user_prompt= """Suggest an email subject for below content - " \
"  Hi Team,I encountered a ModuleNotFoundError: No module named 'scrapper' while running the script. I’m checking the folder structure and module naming to fix the import path. Will update once resolved.
Thanks,
Aman"""

response = ollama.chat.completions.create(
    model="llama3.2", # Use the model name you pulled in Step 2
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)



def messages_for(website):
    return [ {"role": "system", "content": "You are sarcastic assistant and very jolly."},
        {"role": "user", "content": "Summarize this content in Markdown -  " + website}]

def summarize(url):
    website = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model = "llama3.2",
        messages = messages_for(website)
    )
    print (response.choices[0].message.content)


summarize("https://realpython.com/python-web-scraping-practical-introduction")
