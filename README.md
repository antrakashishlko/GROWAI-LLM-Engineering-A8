# GROWAI LLM Engineering – Assignment 8

## Multi-Agent Research Assistant & MCP Server

This project demonstrates a multi-agent system with specialized Research and Analysis Agents coordinated by a Supervisor Agent, along with an MCP server and client using FastMCP.

## Purpose

The purpose of this assignment is to understand how multiple specialized AI agents can work together under a Supervisor Agent and how MCP can provide a standardized way to expose and call tools.

## Features

- Builds a multi-agent system using LangChain
- Uses a Supervisor Agent for task routing
- Implements a specialized Research Agent
- Implements a specialized Analysis Agent
- Uses custom tools with the `@tool` decorator
- Uses a local Qwen3 0.6B model through Ollama
- Implements a local knowledge base for research
- Supports research and comparison workflows
- Demonstrates collaboration between specialized agents
- Builds an MCP server using FastMCP
- Provides Weather and News tools through the MCP server
- Uses an MCP client to call the exposed tools
- Includes live execution and output demonstration

## Requirements

- Python 3.x
- Ollama
- Qwen3 0.6B
- LangChain
- LangChain Core
- LangChain Ollama
- FastMCP

Install the required Python dependencies using:
```text
pip install -r requirements.txt
```

Make sure Ollama is installed and the Qwen3 0.6B model is available locally:
```text
ollama pull qwen3:0.6b
```

## Setup / Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies using `requirements.txt`.
4. Make sure Ollama is installed and running.
5. Make sure the `qwen3:0.6b` model is available locally.

## How to Run

### 1. Run the Multi-Agent System

Execute:
```text
python agents.py
```

The program initializes the local LLM, creates the Research and Analysis Agents, wraps them as tools and creates the Supervisor Agent.

It then demonstrates:

- Research-based routing
- Analysis-based routing
- Collaboration between agents

### 2. Run the MCP Server

Start the MCP server using:
```text
python mcp_server.py
```

The server exposes two tools:

- `get_weather`
- `get_news`

Keep the MCP server running while executing the client.

### 3. Run the MCP Client

In another terminal, execute:
```text
python mcp_client.py
```

The client connects to the MCP server and calls both available tools.

## Multi-Agent Architecture

The system contains three main agents:

### Research Agent

The Research Agent retrieves factual information from the local knowledge base using the `research_lookup` tool.

### Analysis Agent

The Analysis Agent compares and analyzes two pieces of information using the `compare_information` tool.

### Supervisor Agent

The Supervisor Agent coordinates the specialist agents and decides which agent should handle a user's request.

The routing workflow is:

#### User Question → Supervisor → Research / Analysis Agent → Final Answer

For questions requiring both research and comparison, the system demonstrates agent collaboration.

## MCP Server

The FastMCP server exposes two custom tools:

### Weather Tool

`get_weather(city)` returns mock weather information for supported cities.

### News Tool

`get_news(topic)` returns mock news information for supported topics.

### MCP Client

The MCP client connects to the FastMCP server and demonstrates calling both tools.

The communication flow is:

#### MCP Client → MCP Server → Tool Execution → Result → Client

## Test Cases

The multi-agent system includes tests for:

1. A factual research question.
2. A comparison and analysis question.
3. A collaboration question requiring research followed by comparison.

The MCP client also tests:

4. Weather information retrieval.
5. News information retrieval.

## Real-World Relevance

Multi-agent architectures are useful when complex tasks can be divided among specialized AI systems. A Supervisor Agent can route tasks to appropriate specialists, similar to how different teams handle different responsibilities in a real organization.

MCP provides a standardized approach for connecting AI applications with external tools and services. These concepts can be applied to research assistants, customer-support systems, data-analysis applications, productivity tools and other AI automation systems.

## Edge Case / Failure Point

A possible failure point is when the requested topic is not available in the local knowledge base. In this case, the Research Tool returns a clear message indicating that no information was found.

Similarly, the Weather and News tools return an appropriate message when information for an unsupported city or topic is requested.

## Project Files

- `agents.py` – Main multi-agent implementation containing the Research Agent, Analysis Agent, Supervisor Agent, custom tools and test cases.
- `mcp_server.py` – FastMCP server containing the Weather and News tools.
- `mcp_client.py` – MCP client that connects to the server and calls the available tools.
- `requirements.txt` – Required Python dependencies.
- `.gitignore` – Files and folders excluded from Git tracking.

## Assignment

GROWAI LLM Engineering & Generative AI – Assignment 8

