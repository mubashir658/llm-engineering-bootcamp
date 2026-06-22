from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
prompt=ChatPromptTemplate.from_messages(
    [
    ("system","You are a {level} Python tutor.Answer concisely in under 3 lines."),
    ("human","Explain {topic} simply")
    ]
)


chain=prompt|llm

response=chain.invoke({
        "level":"beginner",
        "topic":"embeddings"
})
print(response.content)

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# # define reusable template with variables
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are an expert {role}. Answer concisely in under 3 lines."),
#     ("human", "{question}")
# ])

# # create a chain — pipe prompt into llm
# chain = prompt | llm

# # invoke with different inputs
# response = chain.invoke({
#     "role": "GenAI engineer",
#     "question": "What is a vector database?"
# })
# print(response.content)