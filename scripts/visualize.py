import os
import subprocess
import traceback
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pathlib import Path

CMD = ["./a.out"]


def getRNASequence():
    try:
        with open("../in.txt", "r") as f:
            sequence = f.read()
    except Exception:
        traceback.print_exc()

    return sequence


def getRNAPairs(output):
    intervals = re.findall(r"\{(.*?)\}", output)
    intervals = [tuple(map(int, interval.split(","))) for interval in intervals]

    return intervals


def plotData(sequence, matches):
    fig, ax = plt.subplots(
        figsize=(max(8, len(sequence) / 4), max(8, len(sequence) / 4))
    )
    fig.canvas.manager.set_window_title("2D RNA Structure")

    node_colors = {"A": "#ADD8E6", "C": "#00FF00", "G": "#FF474C", "U": "#FFFF00"}
    node_names = {"A": "Adenine", "C": "Cytosine", "G": "Guanine", "U": "Uracil"}

    G = nx.Graph()
    for i, c in enumerate(sequence):
        G.add_node(i, position=i, base=c, color=node_colors[c], name=node_names[c])
    for i in range(0, len(sequence) - 1):
        G.add_edge(i, i + 1, color="#000000", style="-", type="1D Structure Edge")
    for e in matches:
        G.add_edge(
            e[0],
            e[1],
            color="#808080",
            style="--",
            type="2D Structure Edge",
            pairing=f"{sequence[e[0]]} - {sequence[e[1]]}",
        )

    pos = nx.kamada_kawai_layout(G)
    labels = nx.draw_networkx_labels(
        G,
        pos=pos,
        ax=ax,
        labels=nx.get_node_attributes(G, "base"),
        font_weight="bold",
        font_color="#000000",
    )
    nodes = nx.draw_networkx_nodes(
        G,
        pos=pos,
        ax=ax,
        label=nx.get_node_attributes(G, "base"),
        node_color=nx.get_node_attributes(G, "color").values(),
        linewidths=3,
    )
    edges = nx.draw_networkx_edges(
        G,
        pos=pos,
        ax=ax,
        style=nx.get_edge_attributes(G, "style").values(),
        edge_color=nx.get_edge_attributes(G, "color").values(),
    )

    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(20, 20),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->"),
    )
    annot.set_visible(False)

    def update_annot_node(ind):
        node = ind["ind"][0]

        xy = pos[node]
        annot.xy = xy

        node_attr = {"node": node}
        node_attr.update(G.nodes[node])

        required_attributes = ["position", "name"]
        text = "\n".join(
            f"{k}: {v}" for k, v in node_attr.items() if k in required_attributes
        )

        annot.set_text(text)

    def update_annot_edge(ind):
        edge = list(G.edges)[ind["ind"][0]]

        xy = (pos[edge[0]] + pos[edge[1]]) / 2
        annot.xy = xy

        edge_attr = {"edge": edge}
        edge_attr.update(G.edges[edge])

        required_attributes = ["type", "pairing"]
        text = "\n".join(
            f"{k}: {v}" for k, v in edge_attr.items() if k in required_attributes
        )

        annot.set_text(text)

    def hover(event):
        vis = annot.get_visible()

        if event.inaxes == ax:
            cont_node, ind_node = nodes.contains(event)
            cont_edge, ind_edge = edges.contains(event)
            if cont_node:
                update_annot_node(ind_node)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            elif cont_edge:
                update_annot_edge(ind_edge)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    adenine_point = Line2D(
        [0],
        [0],
        label="Adenine",
        marker="s",
        markersize=10,
        markeredgecolor="#000000",
        markerfacecolor="#ADD8E6",
        linestyle="",
    )
    cytosine_point = Line2D(
        [0],
        [0],
        label="Cytosine",
        marker="s",
        markersize=10,
        markeredgecolor="#000000",
        markerfacecolor="#00FF00",
        linestyle="",
    )
    guanine_point = Line2D(
        [0],
        [0],
        label="Guanine",
        marker="s",
        markersize=10,
        markeredgecolor="#000000",
        markerfacecolor="#FF474C",
        linestyle="",
    )
    uracil_point = Line2D(
        [0],
        [0],
        label="Uracil",
        marker="s",
        markersize=10,
        markeredgecolor="#000000",
        markerfacecolor="#FFFF00",
        linestyle="",
    )
    one_d_line = Line2D(
        [0], [0], label="1D Structure Edge", color="#000000", linestyle="-"
    )
    two_d_line = Line2D(
        [0], [0], label="2D Structure Edge", color="#808080", linestyle="--"
    )

    plt.gca().collections[0].set_edgecolor("#000000")
    plt.gca().collections[0].set_linewidth(1)
    plt.gca().legend(
        handles=[
            adenine_point,
            cytosine_point,
            guanine_point,
            uracil_point,
            one_d_line,
            two_d_line,
        ],
        loc="lower right",
    )

    plt.show()


def main():
    wd = os.getcwd()
    subprocess.run(CMD, cwd=Path(wd).parents[0])

    try:
        with open("../out.txt", "r") as f:
            output = f.read()
    except Exception:
        traceback.print_exc()

    print("Plotting the 2D structure...")
    plotData(getRNASequence(), getRNAPairs(output))


if __name__ == "__main__":
    main()
