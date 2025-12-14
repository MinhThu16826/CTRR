import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import copy
from collections import defaultdict

# ==========================================
# PHẦN 1: LOGIC THUẬT TOÁN (CORE)
# ==========================================

class EulerDeliverySolver:
    """
    Class xử lý logic tìm đường đi Euler cho bài toán Giao hàng tối ưu.
    Nhiệm vụ của Thư: Check điều kiện & Tìm lộ trình Hierholzer.
    """
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges_count = 0

    def add_edge(self, u, v):
        """Thêm đường đi 2 chiều giữa các địa điểm"""
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges_count += 1

    def _is_connected(self):
        """Kiểm tra xem khu vực giao hàng có liên thông không"""
        nodes_with_edges = [n for n in self.graph if len(self.graph[n]) > 0]
        if not nodes_with_edges:
            return True

        start_node = nodes_with_edges[0]
        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        # Nếu số node đi được < số node có trong bản đồ -> Không liên thông
        return len(visited) == len(nodes_with_edges)

    def check_euler_status(self):
        """
        Kiểm tra điều kiện Euler.
        Return: (Loại đồ thị, Điểm bắt đầu, Các điểm bậc lẻ)
        """
        if not self._is_connected():
            return "DISCONNECTED", None, []

        # Đếm số bậc (degree) của từng đỉnh
        odd_degree_nodes = [n for n in self.graph if len(self.graph[n]) % 2 != 0]

        if len(odd_degree_nodes) == 0:
            # Chu trình Euler (Circuit): Vào ra cân bằng, quay về chỗ cũ
            start_node = list(self.graph.keys())[0]
            return "CIRCUIT", start_node, []
        elif len(odd_degree_nodes) == 2:
            # Đường đi Euler (Path): Vào 1 nơi, ra 1 nẻo
            # Bắt buộc xuất phát từ 1 trong 2 đỉnh bậc lẻ
            return "PATH", odd_degree_nodes[0], odd_degree_nodes
        else:
            return "NONE", None, odd_degree_nodes

    def get_delivery_route(self):
        """
        Thực hiện thuật toán Hierholzer để tìm lộ trình đi qua tất cả các cạnh
        """
        status, start_node, _ = self.check_euler_status()

        if status == "DISCONNECTED" or status == "NONE":
            return None, status

        # Tạo bản sao đồ thị để xóa cạnh dần khi đi qua
        temp_adj = copy.deepcopy(self.graph)
        
        stack = [start_node]
        route = [] # Lộ trình kết quả

        while stack:
            u = stack[-1]
            
            if temp_adj[u]:
                # Lấy đỉnh kề đầu tiên
                v = temp_adj[u][0]
                
                # Xóa cạnh u-v và v-u khỏi đồ thị tạm
                temp_adj[u].remove(v)
                if u in temp_adj[v]:
                    temp_adj[v].remove(u)
                
                stack.append(v) # Đi tới v
            else:
                # Nếu không còn đường đi từ u, thêm vào lộ trình và lùi lại
                route.append(stack.pop())

        # Hierholzer trả về lộ trình ngược, cần đảo lại
        return route[::-1], status

# ==========================================
# PHẦN 2: TRỰC QUAN HÓA (VISUALIZATION)
# ==========================================

def run_visualization():
    # 1. Khởi tạo dữ liệu mẫu (Hình phong bì thư - Một đồ thị Euler Path kinh điển)
    solver = EulerDeliverySolver()
    
    # Định nghĩa các cạnh (Các con đường)
    edges_data = [
        (1, 2), (1, 3), 
        (2, 3), (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5)
    ]
    
    for u, v in edges_data:
        solver.add_edge(u, v)

    # 2. Tính toán lộ trình
    print("--- ĐANG TÍNH TOÁN LỘ TRÌNH GIAO HÀNG ---")
    route, status = solver.get_delivery_route()

    if route is None:
        print(f"❌ Không tìm thấy lộ trình tối ưu! Trạng thái bản đồ: {status}")
        print("Gợi ý: Cần thêm đường hoặc bỏ bớt đường để số đỉnh bậc lẻ là 0 hoặc 2.")
        return

    print(f"✅ Trạng thái: {status}")
    print(f"📍 Lộ trình chi tiết: {' -> '.join(map(str, route))}")
    print("🚀 Đang mở cửa sổ mô phỏng...")

    # 3. Thiết lập đồ thị NetworkX để vẽ
    G = nx.Graph()
    for u, neighbors in solver.graph.items():
        for v in neighbors:
            G.add_edge(u, v)

    # Chọn layout cố định để node không bị nhảy lung tung
    pos = nx.spring_layout(G, seed=100) 

    # Cấu hình Matplotlib
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.canvas.manager.set_window_title('Mô phỏng Giao Hàng Tối Ưu - Thuật toán Euler')

    def update(frame):
        ax.clear()
        ax.set_title(f"Mô phỏng Shipper (Bước {frame}/{len(route)-1})\n{status}", fontsize=14, color='blue')
        
        # Vẽ nền: Tất cả các node và edge màu xám
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightgray', node_size=600)
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color='lightgray', width=2)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight='bold')

        # Xác định các cạnh đã đi qua (History)
        path_edges = []
        for i in range(frame):
            if i < len(route) - 1:
                path_edges.append((route[i], route[i+1]))
        
        # Vẽ các đường ĐÃ giao hàng xong (Màu Xanh Lá)
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=path_edges, edge_color='#2ecc71', width=4)

        # Vẽ vị trí HIỆN TẠI của Shipper (Màu Cam)
        current_node = route[frame]
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=[current_node], node_color='#e67e22', node_size=800)

        # Vẽ đường ĐANG đi tới bước tiếp theo (Màu Đỏ nét đứt)
        if frame < len(route) - 1:
            next_node = route[frame+1]
            nx.draw_networkx_edges(G, pos, ax=ax, edgelist=[(current_node, next_node)], 
                                   edge_color='#e74c3c', width=3, style='dashed')
            
            # Label hướng dẫn
            ax.text(0.05, 0.95, f"Đang đi: {current_node} -> {next_node}", transform=ax.transAxes, 
                    fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax.axis('off') # Tắt trục tọa độ cho đẹp

    # Tạo Animation
    ani = animation.FuncAnimation(fig, update, frames=len(route), interval=1000, repeat=False)
    
    plt.show()

if __name__ == "__main__":
    run_visualization()
