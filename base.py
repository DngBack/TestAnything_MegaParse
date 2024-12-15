from megaparse import MegaParse
from langchain_openai import ChatOpenAI
# Using wrong import in repo 
# from megaparse.parser.unstructured_parser import UnstructuredParser  
from megaparse.unstructured_convertor import UnstructuredParser

from dotenv import load_dotenv
import os 

load_dotenv()

llama_parse_api_key = os.getenv('LLAMA_PARSE_API_KEY')


parser = UnstructuredParser()
megaparse = MegaParse(file_path="./data/2412.09605v1.pdf", llama_parse_api_key=llama_parse_api_key)
response = megaparse.load(llama_parse_api_key=llama_parse_api_key)
print(response)
megaparse.save_md("./test.md")