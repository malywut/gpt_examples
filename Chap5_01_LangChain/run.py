from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import load_tools, create_react_agent, AgentExecutor



template = """Question: {question}
Let's think step by step.
Answer: """
prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = """ What is the population of the capital of the country where the
Olympic Games were held in 2016? """
llm_chain.invoke(question)


tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = create_react_agent(
    tools=tools,
    llm=llm,
    prompt = hub.pull("hwchase17/react"),

)

question = """What is the square root of the population of the capital of the
country where the Olympic Games were held in 2016 ?"""
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": question})



chatbot_llm = OpenAI(model_name='gpt-3.5-turbo-instruct')
chatbot = ConversationChain(llm=chatbot_llm , verbose=True)
chatbot.predict(input='Hello')
chatbot.predict(input='Can I ask you a question? Are you an AI?')