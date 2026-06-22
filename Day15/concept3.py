from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a {level} Python tutor."),

    ("human" ,"Explain {topic} simply")
])

chain=prompt|llm|parser




topics=["RAG","embedding"]
for topic in topics:
    result = chain.invoke({
    "level": "beginner",
    "topic":topic})
    print(f"\n{topic.upper()}:")
    print(type(result))   # should be <class 'str'>
    print(result)


