from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import re


_ = load_dotenv(find_dotenv())

def classify_with_llm(log_msg):
    """
    Generate a variant of the input sentence. For example,
    If input sentence is "User session timed out unexpectedly, user ID: 9250.",
    variant would be "Session timed out for user 9251"
    """
    llm = ChatGroq(model="deepseek-r1-distill-qwen-32b")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Classify the log message into one of these categories: \
                       (1) Workflow Error, (2) Deprecation Warning.\
                       If you can't figure out a category, use 'Unclassified'.\
                       Put the category inside <category> </category> tags."),
            ("human", "{log_message}")
        ]
    )

    chain = prompt | llm

    output = chain.invoke(
        {
            "log_message": log_msg
        }
    )

    match = re.search(r'<category>(.*?)</category>', output.content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category