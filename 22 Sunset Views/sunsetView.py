def sunsetViews(buildings, direction):
    [startIdx, step] = [0, 1] if direction == "WEST" else [len(buildings) - 1, -1]

    stack = []
    idx = startIdx
    maxHeight = float('-inf')

    while idx >= 0 and idx < len(buildings):
        if buildings[idx] > maxHeight:
            stack.append(idx)
            maxHeight = buildings[idx]
        idx += step
    
    return stack[::-1] if direction == "EAST" else stack
    