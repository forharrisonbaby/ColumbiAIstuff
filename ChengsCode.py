import pygame
from collections import deque
import sys
import time

# Configuration
CELL_SIZE = 80
FPS = 3
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
TEXT_COLOR = (20, 20, 20)

N = int(input("Enter N: "))

def isSafe(state, row, col):
    for r in range(row):
        c = state[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def drawBoard(screen, state, step, start_time, is_solution=False, solution_num=None):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 36)
    start_time += 1
    # Draw chessboard
    for i in range(N):
        for j in range(N):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw queens
    for i, col in enumerate(state):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = i * CELL_SIZE + CELL_SIZE // 2
        queen_color = GREEN if is_solution else RED
        pygame.draw.circle(screen, queen_color, (x, y), CELL_SIZE // 3)

    # Display step or solution number
    if is_solution:
        caption = f"Solution #{solution_num} Time: {round(time.time()-start_time, 2)}"
    else:
        caption = f"N-Queens DFS - Step {step} Time: {round(time.time()-start_time, 2)}"
    pygame.display.set_caption(caption)

    # Optional: show text on screen
    label = font.render(caption, True, TEXT_COLOR)
    screen.blit(label, (10, CELL_SIZE * N - 40))

    pygame.display.flip()

def bfsNQueensPygame():
    pygame.init()
    screen = pygame.display.set_mode((CELL_SIZE * N, CELL_SIZE * N))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    queue = deque()
    queue.append([])
    step = 0
    solution_count = 0

    global start_time 
    start_time = time.time()
    while queue:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        state = queue.popleft()
        row = len(state)

        # Check if complete solution
        if row == N:
            solution_count += 1
            drawBoard(screen, state, step, start_time, is_solution=True, solution_num=solution_count)
            continue

        drawBoard(screen, state, step, start_time)
        step += 1

        for col in range(N):
            if isSafe(state, row, col):
                queue.append(state + [col])

    # Show final message before quitting
    pygame.display.set_caption(f"Done! {solution_count} solutions found.")
    while True:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def dfsNQueensPygame():
    pygame.init()
    screen = pygame.display.set_mode((CELL_SIZE * N, CELL_SIZE * N))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    stack = []  # DFS uses a stack
    stack.append([])  # start with empty state
    step = 0
    solution_count = 0

    global start_time 
    start_time = time.time()
    while stack:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        state = stack.pop()  # DFS: use pop from end
        row = len(state)

        if row == N:
            solution_count += 1
            drawBoard(screen, state, step, start_time, is_solution=True, solution_num=solution_count)
            continue

        drawBoard(screen, state, step, start_time)
        step += 1

        # Generate children in reverse to maintain left-to-right DFS order
        for col in reversed(range(N)):
            if isSafe(state, row, col):
                stack.append(state + [col])  # push onto stack

    # Show final message before quitting
    pygame.display.set_caption(f"Done! {solution_count} solutions found.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Run
dfsNQueensPygame()
