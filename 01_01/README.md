# DSA Implementation: Practical Application of Pair Sum Logic

Welcome to my DSA learning space! This repository demonstrates how the foundational **Pair Sum (Two Sum)** algorithmic pattern scales from a simple interview problem to a core logic driver in production systems like **Google Maps** and **Atlassian Jira**.

---

## 🚀 Real-World Applications

### 1. Google Maps (Transit Routing Optimization)
When computing multi-modal transit routes, the routing engine matches incoming and outgoing transit legs to fit a precise layover constraint ($Arrival\_Offset + Departure\_Offset = Target\_Layover$). Since timetables are sequential, it utilizes the efficient **Two-Pointer approach** to scan connections in $O(n)$ time.

### 2. Atlassian Jira (Sprint Capacity Planning)
Jira Automation pairs unassigned backlog tasks to perfectly exhaust a developer's remaining sprint hours ($Task\_A + Task\_B = Remaining\_Capacity$). It utilizes a **Hash Map lookup** to achieve instant matches without nested iterations.

---

## 🛠️ Algorithms & Implementations

Here are the optimized implementations demonstrating the core trade-offs between **Time Complexity** and **Space Complexity**.

### Approach 1: Hash Map Solution (Optimized for Speed)
* **Time Complexity:** $O(n)$ — Single pass lookup.
* **Space Complexity:** $O(n)$ — Stores elements in memory.

```python
# Python Implementation using a Hash Map
def pair_sum_hash_map(nums, target):
    seen = {} # value -> index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []