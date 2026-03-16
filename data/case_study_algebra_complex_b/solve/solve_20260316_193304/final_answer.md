## Summary

To sketch this y-axis symmetric nodal cubic, plot the self-intersection at $(0, 2)$ occurring at $t = \pm\sqrt{3}$ and the extrema at $(\pm 2, 0)$ with vertical tangents and $(0, -1)$ with a horizontal tangent. The curve is confined to $y \geq -1$, forming a loop between $y=-1$ and $y=2$ that is traced clockwise as $t$ increases. Beyond the loop, two symmetric tails extend upward to infinity from the intersection point.

---

# Understanding the Parametric Curve $x = t^3 - 3t$, $y = t^2 - 1$

This curve is a **nodal cubic** (specifically a Tschirnhausen Cubic) with distinctive symmetry, a self-intersection point, and clear motion patterns. Below is a comprehensive guide to help you sketch it confidently, with all claims verified through symbolic computation and code execution [code-1].

---

## 1. Symmetry Properties

The curve exhibits **symmetry about the y-axis**. This is determined by analyzing how the coordinate functions behave under the transformation $t \to -t$:

$$x(-t) = (-t)^3 - 3(-t) = -t^3 + 3t = -(t^3 - 3t) = -x(t)$$

$$y(-t) = (-t)^2 - 1 = t^2 - 1 = y(t)$$

**Interpretation:** Since $x(t)$ is an **odd function** and $y(t)$ is an **even function**, for every point $(x, y)$ at parameter $t$, there is a corresponding point $(-x, y)$ at parameter $-t$. 

**Practical Benefit:** You only need to sketch the curve for $t \geq 0$ and reflect it across the y-axis to complete the picture.

---

## 2. Critical Points and Tangents

To understand where the motion slows, stops, or changes direction, we analyze the derivatives:

$$\frac{dx}{dt} = 3t^2 - 3 = 3(t-1)(t+1)$$

$$\frac{dy}{dt} = 2t$$

### 2.1 Vertical Tangents (Horizontal Motion Stops)

When $\frac{dx}{dt} = 0$, the curve stops moving horizontally. Code execution confirms these occur at $t = \pm 1$ [code-1]:

| $t$ | Point $(x, y)$ | Significance |
|-----|----------------|--------------|
| $t = -1$ | $(2, 0)$ | **Rightmost point** of the loop, x-intercept |
| $t = 1$ | $(-2, 0)$ | **Leftmost point** of the loop, x-intercept |

At these points, the tangent line is **vertical**. The curve reverses its horizontal direction here.

### 2.2 Horizontal Tangents (Vertical Motion Stops)

When $\frac{dy}{dt} = 0$, the curve stops moving vertically. Code execution confirms this occurs at $t = 0$ [code-1]:

| $t$ | Point $(x, y)$ | Significance |
|-----|----------------|--------------|
| $t = 0$ | $(0, -1)$ | **Bottommost point** of the curve, y-intercept |

At this point, the tangent line is **horizontal**. The curve reverses its vertical direction here.

### 2.3 Speed Analysis

The speed of motion along the curve is:

$$v = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = \sqrt{(3t^2-3)^2 + (2t)^2}$$

The motion **slows significantly** near $t = 0, \pm 1$ where derivatives vanish, but **never stops completely** (since $dx/dt$ and $dy/dt$ are never zero simultaneously).

---

## 3. Self-Intersection (The Loop)

The curve crosses itself at exactly **one point**. This has been **verified through symbolic computation and code execution** [code-1].

### 3.1 Finding the Intersection

From $y(t_1) = y(t_2)$:
$$t_1^2 - 1 = t_2^2 - 1 \implies t_1^2 = t_2^2 \implies t_1 = \pm t_2$$

For distinct parameters, we need $t_1 = -t_2$. Substituting into $x(t_1) = x(t_2)$:

$$t_1^3 - 3t_1 = (-t_1)^3 - 3(-t_1)$$
$$t_1^3 - 3t_1 = -t_1^3 + 3t_1$$
$$2t_1^3 - 6t_1 = 0 \implies 2t_1(t_1^2 - 3) = 0$$

Solutions: $t_1 = 0$ (not distinct) or $t_1 = \pm\sqrt{3}$.

### 3.2 Intersection Point (Code-Verified)

At $t = \pm\sqrt{3}$:
$$x = (\sqrt{3})^3 - 3(\sqrt{3}) = 3\sqrt{3} - 3\sqrt{3} = 0$$
$$y = (\sqrt{3})^2 - 1 = 3 - 1 = 2$$

**The curve self-intersects at $(0, 2)$**. Code execution confirms that $t = \sqrt{3}$ and $t = -\sqrt{3}$ both yield exactly $(0, 2)$, and **no other distinct parameter pairs produce the same point** [code-1].

---

## 4. Implicit Cartesian Equation (Code-Verified)

Eliminating the parameter $t$ gives the Cartesian form. This has been **verified using sympy** [code-1]:

From $y = t^2 - 1$, we get $t^2 = y + 1$.

From $x = t(t^2 - 3) = t(y + 1 - 3) = t(y - 2)$, squaring gives:

$$x^2 = t^2(y - 2)^2 = (y + 1)(y - 2)^2$$

**Standard Form (Code-Verified):**
$$x^2 - y^3 + 3y^2 - 4 = 0$$

Or equivalently:
$$x^2 = (y + 1)(y - 2)^2 = y^3 - 3y^2 + 4$$

**Constraint:** Since $x^2 \geq 0$ and $(y-2)^2 \geq 0$, we must have $y + 1 \geq 0$, meaning **$y \geq -1$**. This confirms $(0, -1)$ is the absolute minimum.

**Curve Type:** This is a **Tschirnhausen Cubic** (also called a Nodal Cubic) with a characteristic loop structure [code-1].

---

## 5. Motion Direction (Tracing as $t$ Increases)

Imagine a particle moving along the curve as $t$ goes from $-\infty$ to $+\infty$. Code execution verifies the direction in each region [code-1]:

| Parameter Range | $dx/dt$ | $dy/dt$ | Motion Direction | Key Events |
|-----------------|---------|---------|------------------|------------|
| $t < -\sqrt{3}$ | Right | Down | Down and Right | Left tail approaching from top-left infinity |
| $t = -\sqrt{3}$ | Right | Down | Through $(0, 2)$ | **First crossing** of self-intersection |
| $-\sqrt{3} < t < -1$ | Right | Down | Down and Right | Right side of loop |
| $t = -1$ | 0 | Down | At $(2, 0)$ | **Rightmost point** (vertical tangent) |
| $-1 < t < 0$ | Left | Down | Left and Down | Bottom-right quadrant of loop |
| $t = 0$ | Left | 0 | At $(0, -1)$ | **Bottommost point** (horizontal tangent) |
| $0 < t < 1$ | Left | Up | Left and Up | Bottom-left quadrant of loop |
| $t = 1$ | 0 | Up | At $(-2, 0)$ | **Leftmost point** (vertical tangent) |
| $1 < t < \sqrt{3}$ | Right | Up | Right and Up | Left side of loop returning to intersection |
| $t = \sqrt{3}$ | Right | Up | Through $(0, 2)$ | **Second crossing** of self-intersection |
| $t > \sqrt{3}$ | Right | Up | Up and Right | Right tail extending to top-right infinity |

**Loop Direction:** The loop is traced **clockwise** as $t$ increases (from $(0,2) \to (2,0) \to (0,-1) \to (-2,0) \to (0,2)$).

---

## 6. Key Points Summary Table

The following table consolidates all critical points verified through code execution [code-1]:

| Parameter $t$ | Point $(x, y)$ | Tangent Type | Geometric Significance |
|:-------------:|:--------------:|:------------:|:----------------------:|
| $-\infty$ | $(-\infty, \infty)$ | Slanted | Start: Top-left infinity |
| $-\sqrt{3} \approx -1.73$ | $(0, 2)$ | Slanted | **Self-intersection**, y-intercept (first pass) |
| $-1$ | $(2, 0)$ | **Vertical** | **Rightmost point**, x-intercept |
| $0$ | $(0, -1)$ | **Horizontal** | **Bottommost point**, y-intercept |
| $1$ | $(-2, 0)$ | **Vertical** | **Leftmost point**, x-intercept |
| $\sqrt{3} \approx 1.73$ | $(0, 2)$ | Slanted | **Self-intersection**, y-intercept (second pass) |
| $+\infty$ | $(+\infty, \infty)$ | Slanted | End: Top-right infinity |

---

## 7. Step-by-Step Sketching Instructions

### Step 1: Set Up the Axes
- Draw the x and y axes.
- Mark the **y-axis as the line of symmetry**.

### Step 2: Plot the Five Key Points
Mark these points clearly:
- $(0, 2)$ — Self-intersection (crossing point, y-intercept)
- $(2, 0)$ — Rightmost extent (x-intercept)
- $(0, -1)$ — Bottom vertex (y-intercept)
- $(-2, 0)$ — Leftmost extent (x-intercept)

### Step 3: Draw the Loop
Connect the points in this order for the loop portion:
$$(0, 2) \to (2, 0) \to (0, -1) \to (-2, 0) \to (0, 2)$$

**Important details:**
- Make the curve **vertical** at $(\pm 2, 0)$ (tangents are vertical lines)
- Make the curve **horizontal/flat** at $(0, -1)$ (tangent is horizontal)
- Ensure smooth transitions at all points

### Step 4: Draw the Tails
- **Left tail:** From $(0, 2)$, extend a curve going **up and left** toward $(-\infty, \infty)$
- **Right tail:** From $(0, 2)$, extend a curve going **up and right** toward $(+\infty, \infty)$

### Step 5: Add Direction Arrows
Indicate the motion as $t$ increases:
- Left tail: Arrow pointing **down-right** toward the intersection
- Loop: **Clockwise** arrows (right side down, bottom left, left side up)
- Right tail: Arrow pointing **up-right** away from the intersection

### Step 6: Verify Symmetry
Check that the left half is a mirror image of the right half across the y-axis.

---

## 8. Visual Reference

![Parametric Curve Plot](parametric_curve.png)

*The curve shows the characteristic loop with self-intersection at $(0, 2)$, verified through code execution [code-1]. The loop is bounded between $y = -1$ and $y = 2$, with two tails extending upward. Key points are marked with their parameter values. This is a Tschirnhausen Cubic (Nodal Cubic).*

---

## 9. Common Confusions Clarified

| Question | Answer |
|----------|--------|
| **Can different $t$ values give the same height?** | Yes! Any $t$ and $-t$ give the same $y$ (since $y$ is even). For example, $t = \pm 1$ both give $y = 0$. |
| **Can different $t$ values give the same point?** | Yes, but **only at $(0, 2)$** where $t = \pm\sqrt{3}$. Code verification confirms no other distinct pairs exist [code-1]. |
| **Where does motion slow down?** | Near $t = 0, \pm 1$ where derivatives approach zero. The particle moves slowest at these critical points. |
| **Does the curve ever stop?** | No. $dx/dt$ and $dy/dt$ are never zero simultaneously, so the particle is always moving. |
| **What bounds the curve vertically?** | The curve exists only for $y \geq -1$ (from the Cartesian equation). The loop is bounded between $y = -1$ and $y = 2$. |
| **Which direction does the loop trace?** | **Clockwise** as $t$ increases (from top intersection, right side down, bottom, left side up, back to intersection). |
| **Where are the axis intercepts?** | **x-intercepts:** $(\pm 2, 0)$ at $t = \pm 1$. **y-intercepts:** $(0, -1)$ at $t = 0$ and $(0, 2)$ at $t = \pm\sqrt{3}$ [code-1]. |

---

## 10. Quick Sketching Checklist

Before finalizing your sketch, verify:

- [ ] Y-axis symmetry is preserved
- [ ] Self-intersection at $(0, 2)$ is marked
- [ ] Loop extends from $x = -2$ to $x = 2$ horizontally
- [ ] Bottom vertex at $(0, -1)$ has a horizontal tangent
- [ ] Side points at $(\pm 2, 0)$ have vertical tangents
- [ ] Two tails extend upward from $(0, 2)$ to infinity
- [ ] Direction arrows show clockwise loop motion
- [ ] Curve exists only for $y \geq -1$
- [ ] All five key points are plotted: $(0, 2)$, $(2, 0)$, $(0, -1)$, $(-2, 0)$, $(0, 2)$

---

## Conclusion

This parametric curve forms a **single loop with a self-intersection** at $(0, 2)$, symmetric about the y-axis. The motion traces the left tail downward, loops **clockwise** through the bottom vertex $(0, -1)$, and exits up the right tail. All key features have been **verified through symbolic computation and code execution** [code-1]:

- Self-intersection at $t = \pm\sqrt{3}$ produces exactly $(0, 2)$
- No other distinct parameter pairs yield the same point
- Critical points at $t = 0, \pm 1$ give horizontal and vertical tangents respectively
- Cartesian equation $x^2 = (y + 1)(y - 2)^2$ confirms $y \geq -1$
- Axis intercepts: x-intercepts at $(\pm 2, 0)$, y-intercepts at $(0, -1)$ and $(0, 2)$
- Curve type: **Tschirnhausen Cubic (Nodal Cubic)**

By plotting the **five key points** from the table above and respecting the vertical/horizontal tangents, you can sketch this curve confidently every time. The visual reference above shows the complete curve with all critical points marked [code-1].