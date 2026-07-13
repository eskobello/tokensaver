from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

class AiPromptEnchancer():
    def __init__(self, model, sys_prompt):
        load_dotenv()
        self.llm = ChatOpenAI(model=model)
        self.sys_prompt = sys_prompt
        
    def run(self, question):
        messages = [
            SystemMessage(content=self.sys_prompt),
            HumanMessage(content=question)
        ]
        response = self.llm.invoke(messages)
        self.tokens_count(response=response)
        return response.content

    def tokens_count(self, response):
        usage = response.response_metadata.get("token_usage", {})
        print(f"\n--- Tokeny ---")
        print(f"Wejście:  {usage.get('prompt_tokens', '?')}")
        print(f"Wyjście:  {usage.get('completion_tokens', '?')}")
        print(f"Łącznie:  {usage.get('total_tokens', '?')}")