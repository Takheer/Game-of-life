# Game-of-life
Implementation of the Conway's Game of Life

To start the game, you can create a predefined field and specify the coordinates of living cells:
```
field.create_living_cells([
    (7, 2),
    (8, 2),
    (9, 2),
    (8, 4)
])
```

The method `field.generate_next_state()` is used to produce the next state of the game.
You can create your own visualization for this or just use a builtin method `field.display_cli()`

### Sample usage
```
field = Field(16, 8)
field.create_living_cells([
    (7, 2),
    (8, 2),
    (9, 2),
    (8, 4)
])
field.display_cli()
time.sleep(1)
    
while True:
    field.generate_next_state()
    field.display_cli()
    time.sleep(1)
```
