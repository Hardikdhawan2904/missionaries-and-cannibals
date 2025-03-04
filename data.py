def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    
    # Ensure numbers are non-negative
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    
    # Ensure missionaries are never outnumbered by cannibals on either side
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False

    return True

def get_next_states(state):
    m_left, c_left, boat, m_right, c_right = state
    
    # Possible moves depending on the boat's position
    if boat == "left":
        moves = [
            (m_left - 2, c_left, "right", m_right + 2, c_right),  # Move 2 missionaries
            (m_left - 1, c_left - 1, "right", m_right + 1, c_right + 1),  # Move 1 missionary & 1 cannibal
            (m_left, c_left - 2, "right", m_right, c_right + 2),  # Move 2 cannibals
            (m_left - 1, c_left, "right", m_right + 1, c_right),  # Move 1 missionary
            (m_left, c_left - 1, "right", m_right, c_right + 1)   # Move 1 cannibal
        ]
    else:
        moves = [
            (m_left + 2, c_left, "left", m_right - 2, c_right),  # Move 2 missionaries back
            (m_left + 1, c_left + 1, "left", m_right - 1, c_right - 1),  # Move 1 missionary & 1 cannibal back
            (m_left, c_left + 2, "left", m_right, c_right - 2),  # Move 2 cannibals back
            (m_left + 1, c_left, "left", m_right - 1, c_right),  # Move 1 missionary back
            (m_left, c_left + 1, "left", m_right, c_right - 1)   # Move 1 cannibal back
        ]
    
    # Filter out invalid states
    return [move for move in moves if is_valid(move)]

def bfs(start, goal):
    queue = [(start, [])]  # Queue stores (state, path)
    visited = set()  # To track visited states
    
    while queue:
        state, path = queue.pop(0)
        
        if state == goal:
            return path + [state]  # Return full solution path
        
        if state not in visited:
            visited.add(state)
            next_states = get_next_states(state)
            
            for next_state in next_states:
                queue.append((next_state, path + [state]))  # Add new states to queue

    return []  # Return empty if no solution found

# Initial and goal states
start_state = (3, 3, "left", 0, 0)
goal_state = (0, 0, "right", 3, 3)

# Solve the problem using BFS
path = bfs(start_state, goal_state)

# Print solution path
print("Solution path:")
for step in path:
    print(step)