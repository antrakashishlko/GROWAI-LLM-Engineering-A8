# ============================================================
# 1. IMPORTS AND MODEL SETUP
# ============================================================

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

# Create the local Ollama model
model = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://localhost:11434"
)

print("Ollama model connected successfully!")

# ============================================================
# 2. SIMPLE KNOWLEDGE BASE
# ============================================================

knowledge_base = {
    "artificial intelligence": (
        "Artificial Intelligence (AI) is the field of computer science "
        "that focuses on creating systems capable of performing tasks "
        "that normally require human intelligence, such as learning, "
        "reasoning, perception and decision-making."
    ),

    "machine learning": (
        "Machine Learning is a branch of AI in which computers learn "
        "patterns from data and use those patterns to make predictions "
        "or decisions without being explicitly programmed for every task."
    ),

    "deep learning": (
        "Deep Learning is a type of machine learning that uses "
        "multi-layer neural networks to learn complex patterns from "
        "large amounts of data."
    ),

    "natural language processing": (
        "Natural Language Processing or NLP is a field of AI that "
        "allows computers to process, understand and generate human language."
    )
}

# ============================================================
# 3. RESEARCH TOOL
# ============================================================

@tool
def research_lookup(topic: str) -> str:
    """Retrieve information about a topic from the local knowledge base."""

    topic_lower = topic.lower()

    for key, information in knowledge_base.items():

        if key in topic_lower or topic_lower in key:
            return information

    return (
        f"No information about '{topic}' was found "
        "in the local knowledge base."
    )

# Test the research tool
print("\nResearch Tool Test:")
print(
    research_lookup.invoke(
        {"topic": "artificial intelligence"}
    )
)

# ============================================================
# 4. RESEARCH AGENT
# ============================================================

research_agent = create_agent(
    model=model,
    tools=[research_lookup],
    system_prompt=(
        "You are a Research Agent. "
        "Your job is to retrieve accurate information from the "
        "provided local knowledge base. "
        "Always use the research_lookup tool when you need factual "
        "information. Give concise, factual answers based only on "
        "the available knowledge."
    )
)

print("\nResearch Agent created successfully!")

# ============================================================
# 5. ANALYSIS / COMPARISON TOOL
# ============================================================

@tool
def compare_information(text1: str, text2: str) -> str:
    """Compare two text snippets and return a structured comparison."""

    return f"""
Comparison:

First topic:
{text1}

Second topic:
{text2}

Similarities:
- Both topics are related to artificial intelligence and computer science.
- Both involve computational methods for solving problems.

Differences:
- The first topic focuses on its specific concepts and characteristics.
- The second topic focuses on a different set of concepts and characteristics.

Summary:
The two topics are related, but they have different purposes,
methods and characteristics.
"""

# Test the comparison tool
print("\nAnalysis Tool Test:")

print(
    compare_information.invoke({
        "text1": "Machine Learning learns patterns from data.",
        "text2": "Deep Learning uses multi-layer neural networks."
    })
)

# ============================================================
# 6. ANALYSIS AGENT
# ============================================================

analysis_agent = create_agent(
    model=model,
    tools=[compare_information],
    system_prompt=(
        "You are an Analysis Agent. "
        "Your job is to compare and analyse information. "
        "When you need to compare two pieces of information, "
        "use the compare_information tool. "
        "Present the result clearly with similarities, differences "
        "and a concise summary."
    )
)

print("\nAnalysis Agent created successfully!")

# ============================================================
# 7. WRAP RESEARCH AGENT AS A TOOL
# ============================================================

@tool
def research_agent_tool(question: str) -> str:
    """Use the Research Agent to retrieve information from the knowledge base."""

    response = research_agent.invoke({
        "messages": [
            ("user", question)
        ]
    })

    return response["messages"][-1].content

# ============================================================
# 8. WRAP ANALYSIS AGENT AS A TOOL
# ============================================================

@tool
def analysis_agent_tool(question: str) -> str:
    """Use the Analysis Agent to analyse or compare information."""

    response = analysis_agent.invoke({
        "messages": [
            ("user", question)
        ]
    })

    return response["messages"][-1].content

# ============================================================
# 9. SUPERVISOR AGENT
# ============================================================

supervisor_tools = [
    research_agent_tool,
    analysis_agent_tool
]

supervisor = create_agent(
    model=model,
    tools=supervisor_tools,
    system_prompt=(
        "You are the Supervisor Agent coordinating two specialist agents.\n\n"

        "Research Agent: Use this agent to retrieve factual information "
        "from the local knowledge base.\n\n"

        "Analysis Agent: Use this agent for comparison, analysis, "
        "similarities, differences and summaries.\n\n"

        "Routing rules:\n"
        "1. For factual questions, use the Research Agent.\n"
        "2. For comparison or analysis questions, use the Analysis Agent.\n"
        "3. If a question requires researching two topics and then comparing "
        "them, first use the Research Agent to obtain the information and "
        "then use the Analysis Agent to compare the information.\n"
        "4. Combine the specialist results into one clear final answer."
    )
)

print("\nSupervisor Agent created successfully!")

# ============================================================
# 10. SUPERVISOR TEST - RESEARCH QUESTION
# ============================================================

question = "What is artificial intelligence?"

response = supervisor.invoke({
    "messages": [
        ("user", question)
    ]
})

print("\n" + "=" * 60)
print("SUPERVISOR TEST")
print("=" * 60)

print("\nQuestion:")
print(question)

print("\nFinal Answer:")
print(response["messages"][-1].content)

# ============================================================
# 11. SUPERVISOR TEST - ANALYSIS QUESTION
# ============================================================

analysis_question = (
    "Compare Machine Learning and Deep Learning. "
    "Explain their similarities and differences."
)

analysis_response = supervisor.invoke({
    "messages": [
        ("user", analysis_question)
    ]
})

print("\n" + "=" * 60)
print("ANALYSIS ROUTING TEST")
print("=" * 60)

print("\nQuestion:")
print(analysis_question)

print("\nFinal Answer:")
print(analysis_response["messages"][-1].content)

# ============================================================
# 12. COLLABORATION TEST
# ============================================================

collaboration_question = (
    "Research Machine Learning and Deep Learning from the knowledge base, "
    "then compare the two and explain their similarities and differences."
)

collaboration_response = supervisor.invoke({
    "messages": [
        ("user", collaboration_question)
    ]
})

print("\n" + "=" * 60)
print("COLLABORATION TEST")
print("=" * 60)

print("\nQuestion:")
print(collaboration_question)

print("\nFinal Answer:")
print(collaboration_response["messages"][-1].content)