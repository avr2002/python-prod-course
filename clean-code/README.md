## **What is Clean Code?**

Clean code is crucial for maintaining and scaling software projects. It should be:

- Easy to maintain and change
- Understandable by others
- Secure
- Correct aka “it works”
- Relevant to the project needs, e.g. no irrelevant features that bloat the codebase

**Most importantly: Clean code is code that is easy to change!**


## Notes

Here's an overview of the refactorings made to the RPG script, accompanied by specific before-and-after code examples for a more concrete understanding:

### 1. Descriptive Variable Names

**Old Script**:

```python
ph = 10  # player health
dh = 10  # dragon health
dd = 0   # dragon defense
```

**Refactored Script**:

```python
PLAYER_MAX_HEALTH = 10
DRAGON_MAX_HEALTH = 10
DRAGON_DEFENSE = 0
```

**Explanation**: Variable names in the refactored script are more descriptive and use upper camel case to indicate they are constants. This makes the code's purpose clearer and helps other developers understand what these variables represent without needing comments.

### 2. Extract logic into modular, “pure” (stateless) functions

**Old Script**:

```python
while True:
    # Inline game loop handling all aspects of gameplay
    if pm == "a":
        dh -= 1
    # More game logic...
```

**Refactored Script**:

```python
def play_game(player_health: int, dragon_health: int, dragon_defense: int) -> None:
    while True:
        player_move = get_player_move()
        if player_move == "a":
            dragon_health = handle_player_attack(dragon_health)
        # Further refactored game logic...
```

**Explanation**: The `play_game` function encapsulates the main game logic, abstracting the details into helper functions and improving the modularity of the code.


### 3. Helper Functions

**Old Script**:

```python
# Damage calculation and turn logic intermixed with game loop
if pm == "a":
    dh -= 1  # player attacks dragon
elif pm == "h":
    ph += random.randint(0, 2)  # player heals
```

**Refactored Script**:

```python
def handle_player_attack(dragon_health: int) -> int:
    print("You hit the dragon!")
    return dragon_health - 1

def handle_player_heal(player_health: int) -> int:
    heal_amount = random.randint(0, 5)
    return min(player_health + heal_amount, PLAYER_MAX_HEALTH)
```

**Explanation**: Combat and healing logic are extracted into separate functions (`handle_player_attack`, `handle_player_heal`), isolating these tasks and making the main loop cleaner and more focused.


### 4. Eliminate global variables (or other state)

**Old Script**:

```python
# Global variables accessible throughout the entire script
ph = 10
dh = 10
dd = 0
```

**Refactored Script**:

```python
# Global variables removed; state passed explicitly to functions
def play_game(player_health: int, dragon_health: int, dragon_defense: int):
    # Game logic using local variables and parameters
```

**Explanation**: By minimizing the use of global variables, the refactored script reduces the risk of side effects from unintended modifications, thereby enhancing code reliability and testability.


### 5. Order functions from most abstract (high level) to least abstract (low level)

**Old Script**:

```python
# All game logic mixed in a single loop
while True:
    process_game_round()
    # More logic...
```

**Refactored Script**:

```python
def play_game():
    initialize_game()
    while not game_over():
        process_game_round()
```

**Explanation**: The refactored script is organized to present the most abstract functions (like `play_game`) first, guiding the reader through the game's high-level flow before diving into detailed logic, improving understandability.


### 6. Named Function Arguments

**Old Script**:

```python
draw_health_bars(ph, dh)
```

**Refactored Script**:

```python
draw_health_bars(player_health=ph, dragon_health=dh)
```

**Explanation**: Using named keyword arguments makes it clear what each argument represents, reducing the need to check the function signature frequently.



### 7. Consistent Abstraction Levels

**Bad:**

A function `end_round` mixes direct UI manipulation with game logic, cluttering the high-level operations with low-level details:

```python
# example where level of implementation details is inconsistent within a function

def end_round(players, game_state):
    # low-level implementation details
    for player in players:
        player.score += calculate_score(player.actions)
        if player.score >= 100:
            display_winner(player)
            break
    # calls to functions with implementation abstracted away
    save_game_state(game_state)
    update_leaderboard_display(players)
    refresh_ui_elements()

```

Refactored:

```python
# high-level function
def end_round(players, game_state):
    update_scores(players)
    check_for_winner(players)
    save_game_state(game_state)
    update_ui(players)

# lower-level functions with implementation details
def update_scores(players):
    for player in players:
        player.score += calculate_score(player.actions)

def check_for_winner(players):
    for player in players:
        if player.score >= 100:
            announce_winner(player)
            break

def update_ui(players):
    update_leaderboard_display(players)
    refresh_ui_elements()

def announce_winner(player):
    display_winner(player)  # Handles all UI for displaying a winner

```

**Explanation**: This refactor organizes the function into distinct roles: `update_scores` and `check_for_winner` focus on game logic, while `update_ui` and `announce_winner` manage UI updates. Each function now operates at a similar level of abstraction, enhancing readability and maintainability by clearly separating game logic from UI concerns.

The operations within a function or block are kept at a consistent level of abstraction, aiding in maintaining a clean separation between high-level game management logic and lower-level implementation details. This approach simplifies understanding and maintaining the code.


## Assignments

- Read the article about Clean Code. Look for new concepts to apply to your own code.
- Read through the original and refactored versions of the text-based RPG to absorb the techniques that we used to do the refactoring.

## Resources / Links

### [TestDriven.io](http://TestDriven.io) article about Clean Code

- [Clean Code Article](https://testdriven.io/blog/clean-code-python/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python PEP 8](https://peps.python.org/pep-0008/)

