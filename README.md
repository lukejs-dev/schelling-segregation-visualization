## Project Documentation was created with assistance from ai tools

# Schelling's Segregation Model Visualization

An interactive visualization of Schelling's Segregation Model using Streamlit. This project demonstrates how small individual preferences for similar neighbors can lead to large-scale segregation patterns.

## About the Model

Schelling's model shows that a small preference for similar neighbors can lead to complete segregation, even if total segregation is not desired by any individual. In this implementation:
- Each cell represents a house/agent
- Colors represent different groups (blue and red)
- White spaces represent empty houses
- Agents move if they are "unhappy" with their neighborhood composition

## Installation

1. Clone this repository
```bash
git clone https://github.com/YourUsername/SchellingsSegregationVisualization.git
cd SchellingsSegregationVisualization
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

### Parameters

Adjust the simulation parameters using the sidebar:
- **Population Size**: Total number of agents in the simulation
- **Empty Houses Ratio**: Proportion of empty houses
- **Similarity Threshold**: Minimum ratio of similar neighbors for an agent to be "happy"
- **Number of Iterations**: How many times to run the simulation

## Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib
