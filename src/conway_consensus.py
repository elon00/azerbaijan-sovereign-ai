"""
Conway Automaton (B3/S23) Consensus Engine
Maintains decentralized liveness consensus and peer-node health across sovereign nodes.
"""
class ConwayConsensusGrid:
    def __init__(self, width: int = 8, height: int = 8):
        self.width = width
        self.height = height
        # Seed with a standard stable blinker / glider
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.grid[1][2] = 1
        self.grid[2][3] = 1
        self.grid[3][1] = 1
        self.grid[3][2] = 1
        self.grid[3][3] = 1

    def count_neighbors(self, r: int, c: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr = (r + dr) % self.height
                nc = (c + dc) % self.width
                count += self.grid[nr][nc]
        return count

    def step(self) -> int:
        """Executes one B3/S23 generation step. Returns live cell count."""
        next_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        live_count = 0
        for r in range(self.height):
            for c in range(self.width):
                neighbors = self.count_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if neighbors in (2, 3):
                        next_grid[r][c] = 1
                        live_count += 1
                else:
                    if neighbors == 3:
                        next_grid[r][c] = 1
                        live_count += 1
        self.grid = next_grid
        return live_count
