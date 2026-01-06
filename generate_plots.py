
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory if it doesn't exist
OUTPUT_DIR = "assets/visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Generate 8D Feature Vector Visualization (Simulated as Radar Chart)
def generate_radar_chart():
    labels = ['Size', 'Granularity', 'Nucleus/Cytoplasm', 'Mitosis', 'Shape', 'Adhesion', 'Bare Nuclei', 'Chromatin']
    stats_healthy = [1, 2, 1, 1, 2, 8, 1, 1]
    stats_malignant = [8, 7, 8, 7, 7, 2, 8, 9]

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats_healthy += stats_healthy[:1]
    stats_malignant += stats_malignant[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Style: Clinical Medical
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.spines['polar'].set_visible(False)
    
    # Grid lines
    ax.grid(color='#333')
    ax.set_yticklabels([])

    ax.plot(angles, stats_healthy, color='#28a745', linewidth=2, label='Healthy')
    ax.fill(angles, stats_healthy, color='#28a745', alpha=0.25)
    
    ax.plot(angles, stats_malignant, color='#d9534f', linewidth=2, label='Malignant')
    ax.fill(angles, stats_malignant, color='#d9534f', alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='white')

    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), facecolor='#111', edgecolor='#333', labelcolor='white')
    plt.title("8D Feature Vector Overlay", color='white', pad=20)
    
    output_path = os.path.join(OUTPUT_DIR, "feature_vector.png")
    plt.savefig(output_path, facecolor='#0d1117', bbox_inches='tight')
    print(f"Chart saved to {output_path}")

# 2. Generate GATv2 Attention Map (Heatmap)
def generate_heatmap():
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots(figsize=(6, 5))
    
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    
    im = ax.imshow(data, cmap='inferno')
    
    # Customizing axes
    ax.tick_params(colors='white')
    plt.title("GATv2 Attention Weights", color='white')
    
    # Colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.yaxis.set_tick_params(color='white')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')
    
    output_path = os.path.join(OUTPUT_DIR, "attention_heatmap.png")
    plt.savefig(output_path, facecolor='#0d1117', bbox_inches='tight')
    print(f"Heatmap saved to {output_path}")

if __name__ == "__main__":
    print("Generating Visualizations...")
    generate_radar_chart()
    generate_heatmap()
    print("Done.")
