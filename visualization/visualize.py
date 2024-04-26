import sys
import subprocess
import traceback
import re
import matplotlib.pyplot as plt
import networkx as nx

EXEC_CMD = ["../a.out"]

def getSequence(path):
    try:
        with open(path, 'r') as f:
            sequence = f.read()
    except Exception:
        traceback.print_exc()

    return sequence

def getMatches(output):
    intervals = re.findall(r'\{(.*?)\}', output)

    intervals = [tuple(map(int, interval.split(','))) for interval in intervals]

    return intervals

def plotData(sequence, matches):
    fig = plt.figure(figsize=(max(4, len(sequence)/8), max(4, len(sequence)/8)))
    fig.canvas.manager.set_window_title("2D RNA Structure")

    node_colors = {
        "A": "#FF6B6B",
        "C": "#FFD93D",
        "G": "#6BCB77",
        "U": "#4D96FF"
    }

    G = nx.Graph()
    for i, c in enumerate(sequence):
        G.add_node(i, base=c, color=node_colors[c])
    for i in range(0, len(sequence) - 1):
        G.add_edge(i, i+1, color="#00092C", style="-")
    for e in matches:
        G.add_edge(e[0], e[1], color="#FF5F00", style="--")

    nx.draw_kamada_kawai(
        G,
        labels=nx.get_node_attributes(G, "base"),
        style=nx.get_edge_attributes(G, "style").values(),
        node_color=nx.get_node_attributes(G, "color").values(),
        edge_color=nx.get_edge_attributes(G, "color").values(),
        font_color="#151D3B",
        font_weight="bold",
        linewidths=3
    )
    plt.gca().collections[0].set_edgecolor("#00092C")
    plt.gca().collections[0].set_linewidth(1)

    plt.show()

def main():
    subprocess.run(EXEC_CMD + [sys.argv[1]])
    try:
        with open("../out.txt", 'r') as f:
            output = f.read()
    except Exception:
        traceback.print_exc()

    print("Plotting graph...")
    plotData(getSequence(sys.argv[1]), getMatches(output))

if __name__ == "__main__":
    main()