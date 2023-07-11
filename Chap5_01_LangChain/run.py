from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI, ConversationChain
from langchain import PromptTemplate, LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType



template = """Question: {question}
Let's think step by step.
Answer: """
prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = """ What is the population of the capital of the country where the
Olympic Games were held in 2016? """
llm_chain.run(question)


tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

question = """What is the square root of the population of the capital of the
country where the Olympic Games were held in 2016 ?"""
agent.run(question)



chatbot_llm = OpenAI(model_name='text-ada-001')
chatbot = ConversationChain(llm=chatbot_llm , verbose=True)
chatbot.predict(input='Hello')
