# Game-of-life
Implementation of the Conway's Game of Life

To start the game, you can create a predefined field and specify the coordinates of living cells:
```python
field = Field([
    (7, 2),
    (8, 2),
    (9, 2),
    (8, 4)
])
```
Or randomize it:
```python
field = Field().randomize(5, deviation=3)
```

The method `field.generate_next_state()` is used to produce the next state of the game.
You can create your own visualization for this or just use a builtin method `field.display_cli()`
If you want to use your own visualization, you can get the current state directly from the `generate_next_state()` or use `get_state()` method

### Sample usage
```python
field = Field([
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
