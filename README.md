# Graph-Based Social Network Analysis for Influencer Detection

## Overview

This project implements a graph-based social network analysis system for identifying influential users and understanding community structures within a social network.

The system represents users as nodes and interactions between users as directed edges. Graph analytics techniques are applied to measure user influence, connectivity, and the role of users in connecting different parts of the network.

## Objectives

- Represent social network interactions as a graph.
- Identify influential users using PageRank.
- Measure user connectivity using Degree Centrality.
- Identify bridge users using Betweenness Centrality.
- Detect communities within the social network.
- Demonstrate the application of graph analytics to social network analysis.

## Dataset

The project uses a social network edge-list dataset stored in `data.txt`.

Each line represents a directed interaction between two users:

    source_user target_user

The source user represents the initiating node and the target user represents the connected node.

## Methodology

The analysis follows these stages:

    Social Network Data
            ↓
    Data Preprocessing
            ↓
    Graph Construction
            ↓
    PageRank Analysis
            ↓
    Degree Centrality Analysis
            ↓
    Community Detection
            ↓
    Betweenness Centrality Analysis
            ↓
    Result Analysis

## Algorithms Used

### 1. PageRank

PageRank is used to estimate the relative importance or influence of users in the directed social network.

### 2. Degree Centrality

Degree centrality measures how well-connected each user is within the network.

### 3. Community Detection

The project uses the greedy modularity-based community detection algorithm to identify groups of closely connected users.

### 4. Betweenness Centrality

Betweenness centrality identifies users that act as bridges between different parts of the network.

## Technology Stack

- Python
- NetworkX
- Hadoop HDFS environment for dataset/storage setup
- Git / GitHub

## Results

The implemented analysis produced the following results:

| Analysis | Top User | Score |
|---|---|---:|
| PageRank | F | 0.060 |
| Degree Centrality | F | 0.840 |
| Betweenness Centrality | F | 0.099 |

The community detection analysis identified four communities in the analyzed network.

### Top Influencer

User `F` obtained the highest PageRank score of `0.060`.

### Most Connected User

User `F` obtained the highest degree centrality score of `0.840`.

### Top Connector

User `F` obtained the highest betweenness centrality score of `0.099`.

## Visualization

The generated social network graph is available in:

`outputs/social_network_graph.png`

![Social Network Graph](outputs/social_network_graph.png)

## Project Structure

    graph-based-social-network-analysis/
    │
    ├── data.txt
    ├── project.py
    ├── requirements.txt
    ├── .gitignore
    │
    ├── outputs/
    │   └── social_network_graph.png
    │
    ├── screenshots/
    │
    └── report/

## How to Run

### 1. Clone the repository

    git clone https://github.com/shashank-bhat10/Graph-Based-Social-Network-Analysis.git
    cd Graph-Based-Social-Network-Analysis

### 2. Install the required package

    pip install -r requirements.txt

### 3. Run the analysis

    python3 project.py

The program calculates PageRank, Degree Centrality, community structures, and Betweenness Centrality and displays the results in the terminal.

## Future Improvements

- Process larger social network datasets.
- Integrate distributed processing using Apache Spark.
- Incorporate real-time social network data.
- Apply advanced graph analytics and Graph Neural Networks.
- Develop interactive result visualizations.

## Authors

**Shashank Bhat**  
B.Tech. Data Science & Engineering  
Manipal Institute of Technology, MAHE

**Sohan Sanil**  
B.Tech. Data Science & Engineering  
Manipal Institute of Technology, MAHE
