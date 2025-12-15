
import tkinter as tk
from tkinter import messagebox
from graph import Graph
from dijkstra import dijkstra

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Shortest Path - Dijkstra")

        self.graph = Graph()

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.info = tk.Label(root, text="")
        self.info.pack()

        self.create_graph()
        self.draw_graph()

        btn = tk.Button(root, text="Run Dijkstra (A → E)", command=self.run)
        btn.pack(pady=10)

    def create_graph(self):
        self.graph.add_node("A", 100, 200)
        self.graph.add_node("B", 200, 100)
        self.graph.add_node("C", 200, 300)
        self.graph.add_node("D", 350, 200)
        self.graph.add_node("E", 500, 200)

        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "C", 2)
        self.graph.add_edge("B", "D", 5)
        self.graph.add_edge("C", "D", 8)
        self.graph.add_edge("D", "E", 2)

    def draw_graph(self, path=None):
        self.canvas.delete("all")

        for u in self.graph.adj:
            x1, y1 = self.graph.pos[u]
            for v, w in self.graph.adj[u]:
                x2, y2 = self.graph.pos[v]
                color = "red" if path and u in path and v in path else "black"
                self.canvas.create_line(x1, y1, x2, y2, fill=color)
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(w))

        for n, (x, y) in self.graph.pos.items():
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=n)

    def run(self):
        cost, path = dijkstra(self.graph, "A", "E")

        if not path:
            messagebox.showerror("Error", "No path found")
            return

        self.draw_graph(path)
        self.info.config(
            text=f"Shortest Path: {' -> '.join(path)} | Cost = {cost}"
        )
