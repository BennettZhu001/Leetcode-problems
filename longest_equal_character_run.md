# Longest Run of Equal Characters

## Problem

Given a string `s`, return the length of its longest contiguous run of the same character.

For this exercise, assume `0 <= len(s) <= 100_000`. Return `0` for an empty string.

Examples:

| Input | Output | Explanation |
|---|---:|---|
| `"abbcccaa"` | 3 | The longest run is `"ccc"`. |
| `"aaaa"` | 4 | The whole string is one run. |
| `"ababa"` | 1 | Adjacent characters always differ. |
| `""` | 0 | There are no characters. |

A run must be contiguous: the four occurrences of `a` in `"aabaa"` do not form a run of length four.

## 1. The common approach: a linear scan

Scan from left to right, keeping two lengths:

- `current`: the length of the run ending at the current position.
- `best`: the longest run encountered so far.

When the next character matches the previous one, extend `current`. Otherwise, start a new run of length one. After either change, update `best`.

For a nonempty string, both lengths start at one. Handle the empty string separately.

### Why it works

After processing position `i`, `current` describes exactly the run ending at `i`. Every run has an ending position, so tracking the largest `current` value finds the answer.

This resembles your maximum-subarray DP: one state describes the best answer ending at a particular position, and another describes the best answer anywhere in the processed portion.

**Complexity:** O(n) time and O(1) extra space.

**Exercise:** Trace `current` and `best` for `"abbcccaa"`, then implement the scan yourself.

## 2. Your idea: return enough information to merge two halves

Split the string into adjacent left and right segments. The longest run is either entirely in the left half, entirely in the right half, or crosses the split.

Returning only each half's longest run is insufficient. Consider:

```text
"aabb" + "bbcc"
```

Each half has a longest run of two, but the combined string has a run of four. To discover that crossing run, the parent needs information about the boundaries.

### Design a segment summary

For each nonempty segment, return these six fields:

| Field | Meaning | Why the parent needs it |
|---|---|---|
| `best` | Longest run anywhere in the segment | Handles answers contained in one half |
| `prefix` | Length of the equal-character run at the start | Can join a left segment's suffix |
| `suffix` | Length of the equal-character run at the end | Can join a right segment's prefix |
| `length` | Number of characters in the segment | Detects whether a boundary run covers the whole segment |
| `first` | First character | Checks whether boundary characters match |
| `last` | Last character | Checks whether boundary characters match |

This is a constant-sized summary. The six-field representation is convenient, but not uniquely necessary: with access to the original string and segment boundaries, some fields could be derived instead.

### Derive the merge

Let `L` and `R` be summaries of adjacent, nonempty segments. Their boundary runs can join precisely when:

```text
L.last == R.first
```

If they match, the longest crossing run has length `L.suffix + R.prefix`. Otherwise, no equal-character run crosses the split.

Therefore:

```text
crossing = L.suffix + R.prefix if the boundary characters match, else 0
best = max(L.best, R.best, crossing)
```

But finding `best` is not enough: the parent must return a complete summary that its own parent can use.

The combined prefix normally equals `L.prefix`. It extends into the right segment only when both conditions hold:

1. The entire left segment is one run: `L.prefix == L.length`.
2. The boundary characters match.

In that case, the combined prefix is `L.length + R.prefix`.

Similarly, the combined suffix normally equals `R.suffix`. If the entire right segment is one run and the boundary characters match, it becomes `R.length + L.suffix`.

The remaining fields are straightforward:

```text
length = L.length + R.length
first = L.first
last = R.last
```

### Worked merge

For `"aabb"` and `"bbcc"`:

| Field | Left: `"aabb"` | Right: `"bbcc"` | Combined: `"aabbbbcc"` |
|---|---:|---:|---:|
| `best` | 2 | 2 | 4 |
| `prefix` | 2 | 2 | 2 |
| `suffix` | 2 | 2 | 2 |
| `length` | 4 | 4 | 8 |
| `first` | `a` | `b` | `a` |
| `last` | `b` | `c` | `c` |

The boundary characters match, so the suffix and prefix join into four `b`s. Neither half is entirely one run, so the combined prefix and suffix do not extend across the split.

### Base case and recursive structure

A one-character segment has `best = prefix = suffix = length = 1`, with `first` and `last` equal to that character.

Handle the empty string before recursion. For a longer string, recursively summarize both halves, then merge their summaries. Return the final summary's `best` field as the problem's answer.

Use index boundaries into the original string to avoid copying substrings.

### Why it works

Assume both child summaries are correct. Every run in their combined segment either stays within a child or crosses the boundary. The `best` calculation considers all three possibilities.

A prefix can cross the boundary only if it covers the whole left child; a suffix can cross only if it covers the whole right child. The character comparison then determines whether extension is valid. Thus the merge produces all six fields correctly. Together with the one-character base case, this establishes correctness recursively.

**Complexity:** Each merge takes O(1) time. With balanced splitting and index boundaries, there are O(n) calls and O(log n) recursion depth, giving O(n) time and O(log n) extra stack space. Constant-sized information per call does not mean constant space for the whole recursion.

## 3. When does your approach become useful?

For one answer on a fixed string, the linear scan is simpler and uses less extra space. Both approaches take optimal O(n) time in the worst case.

Now change the problem: after each single-character replacement, report the new longest run.

Running the scan after every replacement costs O(n) per update. Instead, store your summaries in a segment tree: leaves represent individual characters, and each internal node stores the merged summary of its children.

A replacement changes one leaf. Only that leaf's ancestors need their summaries recomputed, so an update takes O(log n) time. The whole-string answer is available from the root's `best` field in O(1) time. Building the tree takes O(n) time and storing it takes O(n) space.

This is where the extra summary information pays off: it makes recomputing the answer after a local change efficient.

## 4. Practice before coding

1. Merge `"aaa"` and `"aabb"` by hand. Which boundary run extends, and why?
2. Merge `"baa"` and `"aaa"`. How does this differ from the previous case?
3. Explain why matching boundary characters alone does not imply that the combined prefix extends into the right half.
4. Implement the summary merge as its own function, then use it inside a recursive solution.
5. Compare your recursive answer with your linear scan on empty strings, single characters, all-equal strings, alternating strings, and runs that cross the split.

The general design question behind your idea is: **What must each smaller problem report so that its parent can compute both the answer and an equally useful summary?**
