import streamlit as st
import pandas as pd
from graph_manager import GraphManager
from algorithms import bfs, dfs
import time

# Page Configuration
st.set_page_config(
    page_title="Smart Navigation System",
    page_icon="📍",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .highlight-path {
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("📍 AI Smart Navigation System")
st.markdown("""
This application compares **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms for pathfinding in a graph.
BFS guarantees the shortest path in unweighted graphs, while DFS might take a more exploratory route.
""")

# Initialize Graph Manager in Session State
if 'gm' not in st.session_state:
    st.session_state.gm = GraphManager()

# Sidebar for Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Input Method
    input_mode = st.radio("Input Mode", ["Manual (Text)", "Pre-defined Examples"])
    
    if input_mode == "Manual (Text)":
        graph_input = st.text_area(
            "Enter edges (e.g., A-B, B-C, C-D)",
            value="A-B, B-C, A-C, C-D, D-E, B-E",
            help="Use A-B for undirected or A->B for directed."
        )
        is_directed = st.checkbox("Directed Graph", value=False)
    else:
        example = st.selectbox("Choose Example", ["Linear", "Cyclic", "Complex Star", "Disconnected"])
        if example == "Linear":
            graph_input = "A-B, B-C, C-D, D-E"
        elif example == "Cyclic":
            graph_input = "A-B, B-C, C-A, C-D, D-E"
        elif example == "Complex Star":
            graph_input = "A-B, A-C, A-D, B-E, C-E, D-E, E-F"
        else:
            graph_input = "A-B, C-D"
        is_directed = False

    # Process Graph
    st.session_state.gm.parse_input(graph_input, directed=is_directed)
    nodes = st.session_state.gm.get_nodes()
    
    st.divider()
    
    # Navigation Points
    if nodes:
        start_node = st.selectbox("Start Node", nodes, index=0)
        goal_node = st.selectbox("Goal Node", nodes, index=len(nodes)-1 if len(nodes)>1 else 0)
    else:
        st.warning("Please define a graph first.")

# Main Dashboard
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🕸️ Graph Visualization")
    if nodes:
        # Create Graphviz representation
        from graphviz import Digraph, Graph
        
        dot = Digraph() if is_directed else Graph()
        dot.attr(rankdir='LR', size='8,5')
        
        # Add nodes
        for node in nodes:
            color = "#E1F5FE"
            if node == start_node: color = "#C8E6C9"
            if node == goal_node: color = "#FFCDD2"
            dot.node(node, node, style='filled', fillcolor=color)
            
        # Add edges
        adj = st.session_state.gm.get_adjacency_list()
        added_edges = set()
        for u in adj:
            for v in adj[u]:
                edge_key = tuple(sorted((u, v))) if not is_directed else (u, v)
                if edge_key not in added_edges:
                    dot.edge(u, v)
                    added_edges.add(edge_key)
        
        st.graphviz_chart(dot)
    else:
        st.info("Define nodes and edges in the sidebar to visualize.")

with col2:
    st.subheader("🔍 Algorithm Execution")
    run_btn = st.button("Run Comparison", type="primary")
    
    if run_btn and nodes:
        # Run BFS
        bfs_path, bfs_explored, bfs_time = bfs(adj, start_node, goal_node)
        
        # Run DFS
        dfs_path, dfs_explored, dfs_time = dfs(adj, start_node, goal_node)
        
        # Display Results
        st.write("---")
        
        # Metrics Row
        m1, m2, m3 = st.columns(3)
        
        # Comparison Data
        results = {
            "Algorithm": ["BFS (Optimal)", "DFS (Exploratory)"],
            "Path Length": [len(bfs_path) if bfs_path else "N/A", len(dfs_path) if dfs_path else "N/A"],
            "Nodes Explored": [len(bfs_explored), len(dfs_explored)],
            "Time (ms)": [round(bfs_time * 1000, 4), round(dfs_time * 1000, 4)]
        }
        df_results = pd.DataFrame(results)
        
        st.table(df_results)
        
        # Detailed Paths
        st.markdown("#### 🛣️ Paths Found")
        
        with st.expander("Breadth-First Search (BFS) Details", expanded=True):
            if bfs_path:
                st.success(f"Path Found: {' → '.join(bfs_path)}")
                st.info(f"Exploration Order: {', '.join(bfs_explored)}")
            else:
                st.error("No path found using BFS.")
                
        with st.expander("Depth-First Search (DFS) Details", expanded=True):
            if dfs_path:
                st.success(f"Path Found: {' → '.join(dfs_path)}")
                st.info(f"Exploration Order: {', '.join(dfs_explored)}")
            else:
                st.error("No path found using DFS.")

# Footer
st.divider()
st.caption("Built with Python & Streamlit for AI Lab Assignment.")
