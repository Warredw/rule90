
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

class Rule90:
    def __init__(self, number_of_cells, number_of_iterations):
        self.number_of_cells = number_of_cells
        self.number_of_iterations = number_of_iterations
        
        # Initialize the grid
        self.lifetime = np.zeros((number_of_iterations, number_of_cells), dtype=int)
        self.lifetime[0, number_of_cells // 2] = 1  # Set the middle cell to 1
        
    def update(self):
        for t in range(1, self.number_of_iterations):
            for i in range(1, self.number_of_cells - 1):
                left = self.lifetime[t-1, i-1]
                right = self.lifetime[t-1, i+1]
                self.lifetime[t, i] = left ^ right  # XOR operation
    
    def run(self):
        self.update()
        return self.lifetime

st.title("Rule 90 Cellular Automaton Visualization")

# User input for dynamic adjustments
num_cells = st.slider("Number of Cells", min_value=10, max_value=200, value=100, step=10)
num_iterations = st.slider("Number of Iterations", min_value=10, max_value=200, value=50, step=10)

if st.button("Generate Rule 90 Simulation"):
    model = Rule90(num_cells, num_iterations)
    lifetime = model.run()

    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(lifetime, cmap="binary", aspect="auto")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("Cells")
    ax.set_ylabel("Iterations")
    ax.set_title("Rule 90 Evolution")
    
    st.pyplot(fig)
