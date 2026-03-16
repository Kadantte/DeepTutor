## Summary

The curve forms a loop resembling the Greek letter $\alpha$ with a self-intersection at the origin $(0,0)$, occurring because distinct parameters $t=-1$ and $t=1$ both yield this point. As $t$ increases, the motion traces the loop counter-clockwise between $x=-1$ and $x=0$, entering from the bottom-right infinity and exiting to the top-right infinity with perpendicular tangents $y=\pm x$. The entire shape is symmetric about the x-axis, ensuring the upper and lower halves of the loop mirror each other perfectly.

---

# Understanding the Parametric Curve $x = t^2 - 1$, $y = t^3 - t$

This curve is a classic example of a **parametric curve with a self-intersection (loop)**. Let me build a complete geometric picture by analyzing the intersection points, direction of motion, and overall shape, incorporating computational verification of key features.

---

## 1. The Self-Intersection: Why Does the Curve Cross Itself?

A self-intersection occurs when **two different parameter values** $t_1 \neq t_2$ produce the **same point** $(x, y)$.

### Finding the Intersection Point

Setting $x(t_1) = x(t_2)$ and $y(t_1) = y(t_2)$:

$$t_1^2 - 1 = t_2^2 - 1 \implies t_1^2 = t_2^2 \implies t_1 = -t_2 \quad (\text{since } t_1 \neq t_2)$$

Substituting into the $y$ equation:

$$t_1^3 - t_1 = (-t_1)^3 - (-t_1) = -t_1^3 + t_1$$

$$2t_1^3 - 2t_1 = 0 \implies 2t_1(t_1^2 - 1) = 0$$

The valid solutions are $t_1 = \pm 1$ (we discard $t_1 = 0$ since it gives $t_2 = 0$, not distinct values).

| Parameter Value | Point $(x, y)$ |
|-----------------|----------------|
| $t = -1$ | $(0, 0)$ |
| $t = 1$ | $(0, 0)$ |

**Conclusion:** The curve passes through the **origin $(0, 0)$ twice** — once at $t = -1$ and again at $t = 1$. This creates the loop [code-1].

![Intersection Point](intersection.png)

---

## 2. Direction of Motion: How Does the Curve Traverse?

To understand the direction of motion, we compute the velocity vector $\vec{v}(t) = \left\langle \frac{dx}{dt}, \frac{dy}{dt} \right\rangle$:

$$\frac{dx}{dt} = 2t$$

$$\frac{dy}{dt} = 3t^2 - 1$$

### Critical Points Where Direction Changes

| Derivative | Zero When | Geometric Meaning |
|------------|-----------|-------------------|
| $\frac{dx}{dt} = 0$ | $t = 0$ | Vertical tangent (leftmost point) |
| $\frac{dy}{dt} = 0$ | $t = \pm\frac{1}{\sqrt{3}} \approx \pm 0.577$ | Horizontal tangent (top/bottom of loop) |

![Derivatives Plot](derivatives_plot.png)

### Motion Direction in Each Interval

| Interval | $\frac{dx}{dt}$ | $\frac{dy}{dt}$ | Motion Direction |
|----------|-----------------|-----------------|------------------|
| $t < -\frac{1}{\sqrt{3}}$ | Negative | Positive | **Left-Up** (Northwest) |
| $-\frac{1}{\sqrt{3}} < t < 0$ | Negative | Negative | **Left-Down** (Southwest) |
| $0 < t < \frac{1}{\sqrt{3}}$ | Positive | Negative | **Right-Down** (Southeast) |
| $t > \frac{1}{\sqrt{3}}$ | Positive | Positive | **Right-Up** (Northeast) |

---

## 3. The Crossing Geometry: Two Different Tangents at the Origin

At the self-intersection point $(0, 0)$, the curve has **two distinct tangent directions**. We calculate the slope using $\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2 - 1}{2t}$:

| Parameter | Velocity Vector $\vec{v}(t)$ | Slope | Tangent Line |
|-----------|------------------------------|-------|--------------|
| $t = -1$ | $\langle -2, 2 \rangle$ | $-1$ | $y = -x$ |
| $t = 1$ | $\langle 2, 2 \rangle$ | $1$ | $y = x$ |

**Key Insight:** The tangents are **perpendicular** (slopes $1$ and $-1$, since $m_1 \cdot m_2 = -1$), confirming this is a true **transversal crossing** at a $90^\circ$ angle, not a cusp or touch point [code-3]. The incoming path (from $t=-1$) follows the line $y = -x$, and the outgoing path (from $t=1$) follows the line $y = x$.

---

## 4. Complete Path Tracing as $t$ Increases

Computational verification confirms the following critical point coordinates [code-3]:

| $t$ Value | Point $(x, y)$ | What Happens |
|-----------|----------------|--------------|
| $t \to -\infty$ | $(\infty, -\infty)$ | Curve comes from bottom-right (4th quadrant) |
| $t = -1$ | $(0, 0)$ | **First crossing** — enters origin moving Left-Up |
| $t = -\frac{1}{\sqrt{3}} \approx -0.577$ | $(-0.666667, 0.384900)$ | Top of loop (horizontal tangent) |
| $t = 0$ | $(-1.000000, 0)$ | **Leftmost point** — vertical tangent, turns downward |
| $t = \frac{1}{\sqrt{3}} \approx 0.577$ | $(-0.666667, -0.384900)$ | Bottom of loop (horizontal tangent) |
| $t = 1$ | $(0, 0)$ | **Second crossing** — exits origin moving Right-Up |
| $t \to +\infty$ | $(\infty, \infty)$ | Curve goes to top-right (1st quadrant) |

### Detailed Interval-by-Interval Traversal

Breaking down the motion into four distinct phases:

1. **Interval $t \in (-\infty, -1)$:** As $t \to -\infty$, $x \to \infty$ and $y \to -\infty$ (Bottom-Right Quadrant IV). The curve approaches the origin from the bottom-right.

2. **Interval $t \in (-1, 0)$:** At $t = -1$, position is $(0,0)$. At $t = 0$, position is $(-1, 0)$ (Vertex). Testing $t = -0.5$: $x = -0.75$, $y = 0.375$ ($y > 0$). The curve moves from the origin into the second quadrant ($x<0, y>0$), forming the **upper half of the loop**.

3. **Interval $t \in (0, 1)$:** At $t = 0$, position is $(-1, 0)$. At $t = 1$, position is $(0, 0)$. Testing $t = 0.5$: $x = -0.75$, $y = -0.375$ ($y < 0$). The curve moves from the vertex into the third quadrant ($x<0, y<0$), forming the **lower half of the loop**, returning to the origin.

4. **Interval $t \in (1, \infty)$:** At $t = 1$, position is $(0,0)$. As $t \to \infty$, $x \to \infty$ and $y \to \infty$ (Top-Right Quadrant I). The curve exits the origin into the first quadrant and extends infinitely to the top-right.

**Loop Direction:** Since the path goes Origin $\to$ Top $\to$ Vertex $\to$ Bottom $\to$ Origin, the loop is traversed **counter-clockwise** as $t$ increases.

---

## 5. Symmetry and Loop Boundaries

### Symmetry Verification (Computationally Confirmed)

$$x(-t) = (-t)^2 - 1 = t^2 - 1 = x(t) \quad (\text{even function})$$

$$y(-t) = (-t)^3 - (-t) = -(t^3 - t) = -y(t) \quad (\text{odd function})$$

Since $x$ is even and $y$ is odd, the point at $-t$ is $(x, -y)$ — the **reflection across the x-axis** of the point at $t$. 

**Conclusion:** The curve is **symmetric with respect to the x-axis**. For every point $(x, y)$ on the curve corresponding to parameter $t$, there is a corresponding point $(x, -y)$ corresponding to parameter $-t$. Computational verification confirms this symmetry [code-3].

### Loop Boundaries (Verified by Computation)

| Boundary | Value | Occurs At |
|----------|-------|-----------|
| Leftmost | $x = -1$ | $t = 0$ |
| Rightmost (crossing) | $x = 0$ | $t = \pm 1$ |
| Topmost | $y = \frac{2}{3\sqrt{3}} \approx 0.385$ | $t = -\frac{1}{\sqrt{3}}$ |
| Bottommost | $y = -\frac{2}{3\sqrt{3}} \approx -0.385$ | $t = \frac{1}{\sqrt{3}}$ |

The loop exists strictly between **$x = -1$** (vertex) and **$x = 0$** (crossing point).

---

## 6. Complete Geometric Picture

![Complete Parametric Curve](parametric_curve.png)

### Visual Summary

```
                    y
                    ↑
                    |        t > 1 (Right-Up to ∞)
                    |       /
                    |      /
        Top of loop •     /  • t = 1 at (0,0)
              (-0.67, 0.38)   /
                    |   /   
                    |  /    
                    | /     
        ────────────•──────────────→ x
              (-1, 0) |    (0,0) crossing
                    | \     
                    |  \    
                    |   \   
        Bottom loop •     \  • t = -1 at (0,0)
              (-0.67, -0.38) \
                    |        \
                    |         \  t < -1 (Left-Up from -∞)
                    ↓
```

### The Complete Story

1. **Shape:** The curve resembles the Greek letter **alpha ($\alpha$)** or a fish shape — a loop on the left with two tails extending to the right.

2. **The Loop:** Exists for $t \in [-1, 1]$, bounded between $x = -1$ and $x = 0$. It is traversed **counter-clockwise** as $t$ increases.

3. **The Crossing:** At $(0, 0)$, the curve intersects itself with two distinct tangent lines ($y = x$ and $y = -x$), forming a $90^\circ$ crossing angle. This occurs at two distinct times: $t = -1$ (entering the loop) and $t = 1$ (exiting the loop).

4. **The Tails:** 
   - **Bottom tail** ($t < -1$): Comes from infinity in the 4th quadrant (bottom-right)
   - **Top tail** ($t > 1$): Goes to infinity in the 1st quadrant (top-right)

5. **Symmetry:** The entire curve is symmetric about the **x-axis**, with the upper loop ($t < 0$) mirroring the lower loop ($t > 0$). This has been computationally verified [code-3].

---

## Key Takeaways

| Question | Answer |
|----------|--------|
| **Does it have a loop?** | Yes — a single loop on the left side ($x \in [-1, 0]$) |
| **Why does (0,0) come from two $t$ values?** | Because $t = -1$ and $t = 1$ both satisfy $x = 0, y = 0$ with different velocities |
| **How does direction change?** | Four distinct motion phases separated by critical points at $t = 0, \pm\frac{1}{\sqrt{3}}$ |
| **What's the overall shape?** | Alpha ($\alpha$) shape: loop on left, two tails extending right, symmetric about x-axis |
| **Is symmetry confirmed?** | Yes — $(x(-t), y(-t)) = (x(t), -y(t))$ confirms x-axis symmetry |
| **Which direction is the loop traversed?** | **Counter-clockwise** as $t$ increases from $-1$ to $1$ |
| **What angle does the crossing make?** | **$90^\circ$** (perpendicular crossing with slopes $1$ and $-1$) |

---

## Summary: The Complete Geometric Picture

Combining all the analysis:

| Feature | Description |
|---------|-------------|
| **Shape** | Alpha-shaped ($\alpha$) curve with a single closed loop on the left and two infinite tails extending to the right |
| **Self-Intersection** | Exactly once at the **origin $(0,0)$**, occurring at $t = -1$ (entering) and $t = 1$ (exiting) |
| **Crossing Angle** | Perpendicular ($90^\circ$) with tangent slopes of $-1$ and $1$ |
| **Loop Boundaries** | Horizontally between $x = -1$ (vertex at $t=0$) and $x = 0$ (crossing point) |
| **Symmetry** | Perfectly symmetric about the **x-axis** |
| **Direction of Motion** | Starts at bottom-right infinity → enters origin → traces upper loop → reaches vertex $(-1,0)$ → traces lower loop → exits origin → proceeds to top-right infinity |
| **Loop Traversal** | **Counter-clockwise** as $t$ increases |

This parametric curve beautifully demonstrates how a single parameter $t$ can trace a path that **crosses itself**, creating a loop while maintaining smooth motion throughout. The computational verification confirms all analytical results, giving you confidence in your sketch [code-1][code-2][code-3].