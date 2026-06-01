### Logits

```
"The cat sat on the ___"
         ↓
mat:   8.2   ← high
floor: 7.9   ← high
roof:  6.1   ← medium
banana: -3.4 ← low
the:   -8.1  ← very low
```

These are LOGITS (raw scores)

### Softmax

Softmax converts them to probabilities

```
mat:    34%
floor:  28%
roof:   12%
banana:  0.1%
the:     0.001%
```

These are PROBABILITIES

### Outlines

Outlines intercepts logits right here:

```
Model outputs logits
        ↓
Outlines sets logits of invalid tokens to -infinity
        ↓
Softmax → those tokens get probability 0%
        ↓
Model literally cannot sample them
```
