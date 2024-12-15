from megaparse import MegaParse
from langchain_openai import ChatOpenAI
from megaparse.unstructured_convertor import UnstructuredParser

parser = UnstructuredParser()
megaparse = MegaParse(parser)
response = megaparse.load("./data/2412.09605v1.pdf")
# print(response)
megaparse.save("./test.md")