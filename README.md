# Brainfuck
## Python interpreter to the brainfuck language
A [brainfuck][brainfuck] interpreter

### Usage
```shell
Interpreter usage:
  python3 bf.py <Sourcefile.bf> <Program input>

Translator usage:
  python3 bf.py <input.bf> <output.bf>'''
```

## Requires
- Python 3

## Dialects
Since the program is made for 8 lexical instructions (symbols), saved in a python3 tuple, this interpreter can easily be turned into a brainfuck dialect interpreter. Just change the original tuple for any unicode characters you would like. Some examples and a translator (`translator.py`) are provided:

#### Original
```python
sym = ('>','<','+','-','.',',','[',']')
```

#### Unicat
```python
sym = ('😸','😹','😺','😻','😼','😽','😾','😿')
```

#### Ziim-like
```python
sym = ('→','←','↑','↓','↘','↙','↗','↖')
```

#### Emoji
```python
sym = ('😀','😁','😂','😃','😄','😅','😆','😇')
```

#### Moon
```python
sym = ('🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘')
```

#### Weather
```python
sym = ('🌣','🌤','🌥','🌦','🌧','🌨','🌩','🌪')
```

#### Fruits
```python
sym = ('🍇','🍈','🍉','🍊','🍋','🍌','🍍','🍎')
```

#### Clock
```python
sym = ('🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗')
```

#### Clock
```python
sym = ('👉','👈','👆','👇','👍','👎','👋','👌')

```

You get the idea `Python3` + `Unicode` = 💚

[brainfuck]: https://en.wikipedia.org/wiki/Brainfuck
