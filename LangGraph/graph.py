# Build a first workflow or graph using LangGraph

# State

# First, define the state of the graph

#  The state schema serves as the input schema for all Nodes and Edges in the graph

#  Let's use the TypeDict class from python's typing module for our schema, which provides the type jints for the keys



from typing_extensions import TypedDict

class State(TypedDict):
    graph_info: str

# Node-1
def start_play(state: State):
    print("Start play Node has been called")
    return {"graph_info":state["graph_info"] + "I'm palnning to play"}

# Node-2
def cricket(state:State):
    print("criket")
    return {"graph_info":state["graph_info"] + "cricket"}

# Node-3
def badminton(state: State):
    print("badminton")
    return {"graph_info": state["graph_info"] + "badminton"}

import random
from typing import Literal

def random_play(state:State) -> Literal['cricket', 'badminton']:
    if random.random >0.5:
        return 'badminton'
    else:
        return 'cricket'
    

from IPython.display import Image,display # Pip3 install IPython
from langgraph.graph import StateGraph, START, END

#----------------------Build Graph-------------------#
graph = StateGraph(State)


# Add all the Nodes
graph.add_node("start_play", start_play)
graph.add_node("cricket", cricket)
graph.add_node("badminton", badminton)


## Schedule the flow of the graph
graph.add_edge(START, "start_play")
graph.add_conditional_edges("start_play", random_play)
graph.add_edge("cricket", END)
graph.add_edge("badminton", END)




import os

## Run the grpah, we need to compile the graph
graph_builder = graph.compile()

# 1. Get the binary PNG data
png_data = graph_builder.get_graph().draw_mermaid_png()

# 2. Define the output file path
output_filename = "langgraph_visualization.png"

# 3. Write the binary data to the file
with open(output_filename, "wb") as f:
    f.write(png_data)

print(f"Graph saved successfully to: {os.path.abspath(output_filename)}")

# VS Code will automatically detect the new PNG file in your file explorer.

## View the graph
# display(Image(graph_builder.get_graph().draw_mermaid_png()))
