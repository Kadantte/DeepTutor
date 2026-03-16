## Summary

The intersection comprises **two separate horizontal ellipses** located at the planes $z = \pm 2\sqrt{2}$, rather than a single connected space curve. The cylinder passes through the ellipsoid's interior like a vertical tunnel, touching the surface only at these upper and lower rings where the cross-sections exactly match. A correct sketch must emphasize the vertical gap between these disjoint curves and their symmetry across the $xy$-plane, avoiding any connecting lines between the two levels.

---

# Building a Spatial Picture: Ellipsoid–Cylinder Intersection

## 1. Standard Forms and Dimensions

First, let's establish the exact geometry of both surfaces.

### Ellipsoid
The equation $36x^2 + 16y^2 + 9z^2 = 144$ converts to standard form:

$$\frac{x^2}{4} + \frac{y^2}{9} + \frac{z^2}{16} = 1$$

| Axis | Semi-axis Length | Full Extent |
|------|------------------|-------------|
| $x$  | $a = 2$          | $[-2, 2]$   |
| $y$  | $b = 3$          | $[-3, 3]$   |
| $z$  | $c = 4$          | $[-4, 4]$   |

This is a **bounded, closed surface** centered at the origin, elongated along the $z$-axis with proportions $x : y : z = 2 : 3 : 4$.

### Elliptic Cylinder
The equation $9x^2 + 4y^2 = 18$ converts to standard form:

$$\frac{x^2}{2} + \frac{y^2}{9/2} = 1$$

| Axis | Semi-axis Length | Full Extent |
|------|------------------|-------------|
| $x$  | $A = \sqrt{2} \approx 1.414$ | $[-\sqrt{2}, \sqrt{2}]$ |
| $y$  | $B = \frac{3\sqrt{2}}{2} \approx 2.121$ | $[-\frac{3\sqrt{2}}{2}, \frac{3\sqrt{2}}{2}]$ |
| $z$  | $\infty$         | $(-\infty, \infty)$ |

This is an **unbounded surface** extending infinitely in the $z$-direction with a fixed elliptical cross-section in the $xy$-plane. The cylinder equation has **no $z$-dependence**, which is crucial for understanding the intersection topology. Note that each intersection ellipse has the same axis ratio as the cylinder: $x : y = 2 : 3$.

---

## 2. Spatial Relationship at the Equator ($z = 0$)

At the "waist" of the ellipsoid ($z = 0$), we can directly compare the two cross-sections:

| Surface | $x$-semi-axis | $y$-semi-axis |
|---------|---------------|---------------|
| Ellipsoid equator | $2$ | $3$ |
| Cylinder cross-section | $\sqrt{2} \approx 1.414$ | $\frac{3\sqrt{2}}{2} \approx 2.121$ |

**Key Observation:** The cylinder is **strictly narrower** than the ellipsoid in both directions:
- $\sqrt{2} < 2$ (x-direction)
- $\frac{3\sqrt{2}}{2} < 3$ (y-direction)

**Geometric Implication:** At $z = 0$, the entire cylinder lies **inside** the ellipsoid's interior volume. The surfaces do not touch at the equator.

![Cross-section verification at z ≈ 2.83](cross_section_verification.png)

---

## 3. Where the Intersection Occurs

To find where the surfaces meet, substitute the cylinder constraint into the ellipsoid equation.

**Key Algebraic Insight:** Notice that $36x^2 + 16y^2 = 4(9x^2 + 4y^2)$. Since the cylinder gives us $9x^2 + 4y^2 = 18$:

$$\begin{aligned}
36x^2 + 16y^2 + 9z^2 &= 144 \\
4(9x^2 + 4y^2) + 9z^2 &= 144 \\
4(18) + 9z^2 &= 144 \\
72 + 9z^2 &= 144 \\
9z^2 &= 72 \\
z^2 &= 8 \\
z &= \pm 2\sqrt{2} \approx \pm 2.828
\end{aligned}$$

**Critical Result:** The intersection occurs at **two constant $z$-planes**: $z = +2\sqrt{2}$ and $z = -2\sqrt{2}$.

### Verification at Intersection Planes

At $z = \pm 2\sqrt{2}$, the ellipsoid's cross-section shrinks. The effective semi-axes become:

$$\begin{aligned}
\text{Scale factor} &= \sqrt{1 - \frac{z^2}{c^2}} = \sqrt{1 - \frac{8}{16}} = \sqrt{0.5} \approx 0.7071 \\
a_{\text{eff}} &= 2 \times 0.7071 = 1.4142 = \sqrt{2} = A_{\text{cyl}} \\
b_{\text{eff}} &= 3 \times 0.7071 = 2.1213 = \frac{3\sqrt{2}}{2} = B_{\text{cyl}}
\end{aligned}$$

**Perfect Match:** At exactly $z = \pm 2\sqrt{2}$, the ellipsoid's cross-section **coincides exactly** with the cylinder's cross-section. This is where the surfaces intersect.

**Verification:** The ellipsoid extends from $z = -4$ to $z = +4$, so $z = \pm 2\sqrt{2} \approx \pm 2.828$ lies within bounds. ✓

**Vertical Positioning:** The curves sit at $2.828/4 \approx 70.7\%$ of the ellipsoid's half-height—meaning they're in the **upper and lower thirds** of the ellipsoid, not at the equator.

---

## 4. Topology: Two Separate Closed Curves

### Why Two Curves (Not One)?

| Property | Implication |
|----------|-------------|
| Cylinder is infinite in $z$ | Extends beyond ellipsoid's $z$-bounds $[-4, 4]$ |
| Cylinder is inside ellipsoid at $z = 0$ | Must exit the ellipsoid to reach $z = \pm\infty$ |
| Ellipsoid is closed and convex | Cylinder pierces through top and bottom |
| Intersection at constant $z$-planes | Creates horizontal closed loops |
| No points exist for $-2\sqrt{2} < z < +2\sqrt{2}$ | No connecting path between curves |

**Topological Conclusion:** The intersection consists of **two separate closed curves** (ellipses), not one connected space curve.

### Why Not One Connected Curve?

A connected curve would require a continuous path from $z = -2\sqrt{2}$ to $z = +2\sqrt{2}$. However:
- No points exist on both surfaces for $-2\sqrt{2} < z < +2\sqrt{2}$
- The cylinder "exits" the ellipsoid at $z = -2\sqrt{2}$ and "re-enters" at $z = +2\sqrt{2}$ (or vice versa)
- These two ellipses are at different $z$-heights with **no connecting path**
- The vertical gap between curves is $2 \times 2\sqrt{2} \approx 5.656$ units

### Curve Characteristics

| Property | Value |
|----------|-------|
| Number of curves | 2 |
| Shape | Ellipses (horizontal) |
| Locations | $z = +2\sqrt{2}$ and $z = -2\sqrt{2}$ |
| Symmetry | Symmetric with respect to the $xy$-plane |
| Connectivity | Disconnected from each other |
| Each curve is | Closed and continuous |

### Distinguishing Two Curves from One Connected Curve

| Feature | Two Separate Curves (Actual) | Single Connected Curve (Incorrect) |
|---------|-----------------------------|-----------------------------------|
| **Vertical gap** | Clear gap of $4\sqrt{2}$ units | No gap—curves connect |
| **Topology** | Two disjoint closed loops | One continuous loop |
| **$z$-range** | Only at $z = \pm 2\sqrt{2}$ | Spans continuous $z$-range |
| **Cylinder relationship** | Cylinder inside ellipsoid for $|z| < 2\sqrt{2}$ | Cylinder intersects surface continuously |
| **Visual cue** | Two distinct horizontal rings | One twisted or vertical curve |

**Key implication for sketching:** **Emphasize the vertical gap**—this is the most important feature to convey. Do not draw any connecting lines between the two ellipses.

---

## 5. Symmetry Properties

Both surfaces possess reflection symmetries across all three coordinate planes, and the intersection inherits all of these. This is because both surface equations contain **only even powers** of $x$, $y$, and $z$.

### Equation-Based Symmetry Analysis

| Surface | $x$-term | $y$-term | $z$-term | Symmetry Implication |
|---------|----------|----------|----------|---------------------|
| Ellipsoid | $x^2$ | $y^2$ | $z^2$ | Symmetric about all three coordinate planes |
| Cylinder | $x^2$ | $y^2$ | (none) | Symmetric about $xz$ and $yz$ planes; invariant along $z$ |

**Inference:** If $(x, y, z)$ satisfies both equations, then:
- $(-x, y, z)$ also satisfies both → **$yz$-plane symmetry**
- $(x, -y, z)$ also satisfies both → **$xz$-plane symmetry**
- $(x, y, -z)$ also satisfies both → **$xy$-plane symmetry**

### Three Levels of Symmetry

| Symmetry Type | Description | Visual Meaning |
|---------------|-------------|----------------|
| **Inter-Curve** ($xy$-plane, $z \to -z$) | Upper ellipse at $z = +2\sqrt{2}$ maps to lower ellipse at $z = -2\sqrt{2}$ | Mirror image across $z = 0$ |
| **Intra-Curve** ($xz$-plane, $y \to -y$) | Each ellipse symmetric front-to-back | Left half ↔ right half |
| **Intra-Curve** ($yz$-plane, $x \to -x$) | Each ellipse symmetric left-to-right | Front half ↔ back half |

### Relationship to Each Coordinate Plane

| Coordinate Plane | Relationship to Intersection Curves |
|-----------------|-------------------------------------|
| **$xy$-plane ($z = 0$)** | Curves are **parallel** to this plane; $xy$-plane bisects the space between the two curves symmetrically (mirror plane) |
| **$xz$-plane ($y = 0$)** | Curves are **symmetric** about this plane; each ellipse crosses at $x = \pm\sqrt{2}$, $z = \pm 2\sqrt{2}$ (4 points total) |
| **$yz$-plane ($x = 0$)** | Curves are **symmetric** about this plane; each ellipse crosses at $y = \pm\frac{3\sqrt{2}}{2}$, $z = \pm 2\sqrt{2}$ (4 points total) |

**Key Geometric Facts:**
- Both curves are **perpendicular to the $z$-axis** (they lie in horizontal planes)
- Both curves are **centered on the $z$-axis** (their centers are at $(0, 0, \pm 2\sqrt{2})$)
- The $z$-axis passes through the "holes" of both elliptical loops
- 180° rotation about the $z$-axis maps each curve onto itself

### Symmetry Diagram

```
                    z
                    ↑
                    │     Upper ellipse (z = +2√2)
                    │    ╭─────────────╮
                    │   ╱               ╲
                    │  │      (0,0,+z)   │
                    │   ╲               ╱
                    │    ╰─────────────╯
                    │
        ────────────┼─────────────────────── xy-plane (z = 0, mirror plane)
                    │
                    │    ╭─────────────╮
                    │   ╱               ╲
                    │  │      (0,0,-z)   │
                    │   ╲               ╱
                    │    ╰─────────────╯
                    │     Lower ellipse (z = -2√2)
                    │
                    └──────────────────────────→ y
                   ╱
                  ╱
                 x
```

**Key implication for sketching:** Ensure perfect symmetry in your drawing—any asymmetry suggests an error. The origin $(0,0,0)$ should be at the geometric center of the entire figure.

---

## 6. Extreme Points on the Intersection Curves

For precise sketching, know the exact coordinates of key points on each ellipse:

| Point Type | Coordinates | Count | Numerical Values |
|------------|-------------|-------|------------------|
| Max/Min $X$ | $(\pm\sqrt{2}, 0, +2\sqrt{2})$ and $(\pm\sqrt{2}, 0, -2\sqrt{2})$ | 4 points | $x \approx \pm 1.414$ |
| Max/Min $Y$ | $(0, \pm\frac{3\sqrt{2}}{2}, +2\sqrt{2})$ and $(0, \pm\frac{3\sqrt{2}}{2}, -2\sqrt{2})$ | 4 points | $y \approx \pm 2.121$ |
| $Z$-planes | $z = +2\sqrt{2}$ (upper), $z = -2\sqrt{2}$ (lower) | 2 planes | $z \approx \pm 2.828$ |

**Total:** 8 extreme points define the bounding box of both ellipses.

**Key observation:** All intersection points lie within ellipsoid bounds ($|x|<2$, $|y|<3$, $|z|<4$), confirming the cylinder passes completely through.

**Ellipse proportions:** Each intersection ellipse has semi-axes $\sqrt{2} : \frac{3\sqrt{2}}{2} = 2 : 3$, meaning they are **wider in the $y$-direction than the $x$-direction**.

**Key implication for sketching:** Mark these 8 points explicitly to establish scale and position. Use them to verify symmetry in your drawing.

---

## 7. Complete 3D Visualization

![3D visualization of ellipsoid and cylinder intersection](ellipsoid_cylinder_intersection.png)

The visualization above shows:
- **Cyan surface:** The ellipsoid (bounded, closed)
- **Orange surface:** The elliptic cylinder (unbounded, passes through)
- **Red curves:** The two intersection ellipses at $z = \pm 2\sqrt{2}$

### Visual Techniques for Showing Curves Lie on the Ellipsoid Surface

| Technique | Purpose |
|-----------|---------|
| **Transparent wireframe ellipsoid** | Shows full ellipsoid context ($z$ from $-4$ to $+4$) while keeping curves visible |
| **Bold, contrasting intersection curves** | Makes the two ellipses stand out against the surface |
| **Faint cylinder wireframe** | Optionally show cylinder passing through to indicate intersection is cylinder-constrained |
| **Curves follow ellipsoid curvature** | Ensure curves appear to lie on the surface at those $z$-levels |

**Key geometric relationship:** At $z = \pm 2\sqrt{2}$, the ellipsoid cross-section simplifies to:

$$\frac{x^2}{4 \cdot (1 - 8/16)} + \frac{y^2}{9 \cdot (1 - 8/16)} = 1 \quad \Rightarrow \quad \frac{x^2}{2} + \frac{y^2}{9/2} = 1$$

This is exactly the cylinder equation, confirming the curves lie on both surfaces simultaneously.

---

## 8. Visibility from Common Viewing Angles

When sketching or visualizing, understand what portions are visible from different perspectives:

| View Direction | What's Visible | What's Hidden | Sketching Guidance |
|----------------|----------------|---------------|-------------------|
| **Top-down** (along $-z$) | Both ellipses project to same shape | Depth information lost | Use different line styles (solid/dashed) or colors to distinguish upper vs. lower |
| **Side** (along $x$-axis) | Two horizontal line segments at different heights | Cannot see $x$-extent of ellipses | Shows vertical separation clearly |
| **Side** (along $y$-axis) | Two horizontal line segments at different heights | Cannot see $y$-extent of ellipses | Same as above |
| **Oblique/Isometric** | Both ellipses visible as separate curves | Some portions hidden by ellipsoid surface | **Recommended view** - shows 3D relationship best |
| **Front** (along $+z$) | Upper ellipse fully visible; lower may be hidden | Lower ellipse partially obscured by ellipsoid | Use dashed lines for hidden portions |
| **First Octant** (looking from $x>0, y>0, z>0$) | Front-right portion of upper ellipse; front-right portion of lower ellipse | Back-left portions of both ellipses; lower ellipse partially obscured | Good for showing depth |

**Key implication for sketching:**
- Front portions of both ellipses should be **solid lines**
- Back portions should be **dashed** (hidden by ellipsoid surface)
- Lower ellipse may be partially obscured by upper ellipsoid surface depending on viewpoint

---

## 9. What a Correct Sketch Should Emphasize

When sketching this intersection by hand, emphasize these features:

### Essential Elements

| Feature | Specification | Visual Cue |
|---------|---------------|------------|
| **Ellipsoid** | $a=2$, $b=3$, $c=4$ | Draw as elongated sphere, tallest in $z$; use transparent wireframe or light dashed lines |
| **Cylinder** | $A=\sqrt{2}$, $B=3\sqrt{2}/2$ | Show cylinder walls lightly to indicate intersection is cylinder-constrained |
| **Upper curve** | $z = +2\sqrt{2} \approx 2.83$ | Draw as horizontal ellipse, solid line (visible) |
| **Lower curve** | $z = -2\sqrt{2} \approx -2.83$ | Draw as horizontal ellipse, dashed where hidden |
| **Entry/Exit** | Cylinder penetrates top & bottom | Show cylinder continuing beyond ellipsoid |
| **Symmetry** | Mirror across $xy$-plane | Make upper/lower curves identical in shape |
| **Z-axis positioning** | Mark $z = \pm 2\sqrt{2}$ planes | Use horizontal reference lines with labels |

### Critical Visual Elements

1. **Two distinct horizontal rings** — not one continuous spiral or figure-8
2. **Cylinder extends beyond ellipsoid** — show portions above $z=+4$ and below $z=-4$
3. **Ellipsoid is transparent/wireframe** — so intersection curves are visible
4. **Perspective cue** — tilt view slightly so both $z$-levels are distinguishable
5. **Label $z$-values** — annotate $z = \pm 2\sqrt{2}$ on the sketch
6. **Front/back distinction** — use solid lines for front portions, dashed lines for back portions of each ellipse
7. **Vertical gap** — show clear separation between curves (distance ≈ 5.656 units)

### Emphasizing Two Separate Curves (Not One Connected Curve)

| Feature | How to Emphasize |
|---------|------------------|
| **Vertical separation** | Show clear gap between $z=+2\sqrt{2}$ and $z=-2\sqrt{2}$ |
| **No connecting lines** | Do NOT draw any vertical lines connecting the two ellipses |
| **Different shading** | Use slightly different line weights or colors for upper vs. lower curve |
| **Plane indicators** | Draw faint horizontal planes at each $z$-level to show they're in different slices |
| **Labeling** | Explicitly label "$z = +2\sqrt{2}$" and "$z = -2\sqrt{2}$" on the sketch |

### Common Mistakes to Avoid

| Mistake | Correction |
|---------|------------|
| Drawing one connected curve wrapping around | Draw two separate horizontal loops |
| Placing intersection at $z = 0$ | Place at $z = \pm 2\sqrt{2} \approx \pm 2.83$ |
| Making curves touch at the sides | Curves are horizontal ellipses at constant $z$ |
| Showing cylinder outside ellipsoid at equator | Cylinder is inside at $z = 0$, exits at $z = \pm 2\sqrt{2}$ |
| Making curves tilt or spiral | They are perfectly horizontal |
| Showing cylinder ending at ellipsoid surface | It passes through completely |
| Curves appearing to merge or connect | They are topologically disconnected |

### Relative Proportions for Accurate Sketch

**Ellipsoid proportions (semi-axes ratio):**
- $x : y : z = 2 : 3 : 4$
- The ellipsoid is tallest in $z$-direction, intermediate in $y$, shortest in $x$

**Intersection ellipse proportions (semi-axes ratio):**
- $x : y = \sqrt{2} : \frac{3\sqrt{2}}{2} = 2 : 3$ (same as cylinder)
- Each ellipse is wider in $y$ than in $x$

**Vertical positioning:**
- $z = \pm 2\sqrt{2} \approx \pm 2.828$
- This is $2.828/4 \approx 70.7\%$ of the ellipsoid's half-height
- The curves sit in the upper and lower thirds of the ellipsoid, not at the equator

**Scale relationship:**
- Cylinder fits inside ellipsoid at $z=0$ ($A=1.414 < a=2$; $B=2.121 < b=3$)
- Intersection ellipses are smaller than ellipsoid's equatorial cross-section

---

## 10. Complete Sketch Checklist

Use this checklist to verify your 3D sketch is accurate:

| # | Feature | How to Show |
|---|---------|-------------|
| 1 | **Two horizontal ellipses** | Draw parallel ellipses at $z \approx \pm 2.83$ |
| 2 | **Vertical separation** | Leave clear gap; no connections between curves |
| 3 | **Ellipse dimensions** | $y$-axis ≈ 1.5× wider than $x$-axis for each ellipse |
| 4 | **8 extreme points** | Mark $(\pm\sqrt{2}, 0, \pm 2\sqrt{2})$ and $(0, \pm 3\sqrt{2}/2, \pm 2\sqrt{2})$ |
| 5 | **Ellipsoid context** | Light wireframe showing full ellipsoid ($z$ from $-4$ to $+4$) |
| 6 | **Visibility** | Solid lines for front, dashed for back portions |
| 7 | **Symmetry** | Ensure mirror symmetry across all coordinate planes |
| 8 | **Viewpoint** | Use oblique/isometric view to show 3D relationship |

---

## 11. Spatial Picture Synthesis

### Mental Model

```
                    z = +4 (ellipsoid top)
                         |
                    z = +2√2 ← UPPER ELLIPSE (intersection)
                         |
                    z =  0   (ellipsoid equator, NO intersection)
                         |
                    z = -2√2 ← LOWER ELLIPSE (intersection)
                         |
                    z = -4 (ellipsoid bottom)
```

### The Cylinder's Path

1. Comes from $z = +\infty$ (outside ellipsoid)
2. **Enters** ellipsoid at $z = +2\sqrt{2}$ (first intersection curve)
3. Passes through ellipsoid interior (no surface contact)
4. **Exits** ellipsoid at $z = -2\sqrt{2}$ (second intersection curve)
5. Continues to $z = -\infty$ (outside ellipsoid)

### Helpful Analogy

> Imagine a vertical pipe passing through a football. The pipe touches the football's surface at exactly two horizontal rings — one near the top, one near the bottom. Between these rings, the pipe is inside the football. Outside these rings, the pipe is outside the football.

---

## 12. Summary: Building Your Mental Picture

Think of it this way:

1. **Start with the ellipsoid:** A closed, football-shaped surface centered at the origin, stretching from $z = -4$ to $z = +4$.

2. **Insert the cylinder:** A vertical elliptical tube that is narrower than the ellipsoid's waist. At $z = 0$, it floats entirely inside without touching the surface.

3. **Follow the cylinder upward:** As $z$ increases, the ellipsoid's cross-section shrinks. At $z = 2\sqrt{2} \approx 2.83$, the ellipsoid's cross-section has shrunk enough to match the cylinder exactly—this is where they intersect.

4. **Continue upward:** Beyond $z = 2\sqrt{2}$, the cylinder exits the ellipsoid and continues to $z = +\infty$ outside the ellipsoid.

5. **Repeat downward:** The same happens symmetrically at $z = -2\sqrt{2}$.

6. **Result:** Two separate horizontal elliptical rings where the cylinder punches through the ellipsoid's top and bottom caps.

---

## 13. Quick Reference: Answers to Your Questions

| Question | Answer |
|----------|--------|
| **One curve or two?** | **Two separate closed curves** (disconnected) |
| **Curve shape?** | **Horizontal ellipses** at $z = \pm 2\sqrt{2}$ |
| **How they sit on ellipsoid?** | One ring near top, one ring near bottom; symmetric about $xy$-plane |
| **Relation to coordinate planes?** | Parallel to $xy$-plane; do not cross $z=0$; symmetric across all three planes |
| **Sketch emphasis?** | Two distinct horizontal rings, cylinder passing through, ellipsoid wireframe, label $z$-values |

### Reliable Spatial Picture

> The intersection consists of **two disjoint horizontal elliptical rings** on the ellipsoid surface, located at heights $z = +2\sqrt{2}$ and $z = -2\sqrt{2}$. The elliptic cylinder passes completely through the ellipsoid like a vertical tunnel, touching the surface only at these two rings. Between the rings, the cylinder lies inside the ellipsoid; outside the rings, it lies outside. The configuration is symmetric with respect to all three coordinate planes and the origin. Each ellipse is wider in the $y$-direction (semi-axis ≈ 2.121) than in the $x$-direction (semi-axis ≈ 1.414), and both curves sit at approximately 70.7% of the ellipsoid's half-height from the center.

### Final Key Takeaways

**The intersection consists of TWO separate horizontal elliptical curves at $z = \pm 2\sqrt{2}$, not one connected curve.** A correct 3D sketch must emphasize:

1. **Two distinct parallel ellipses** with clear vertical separation (≈5.66 units)
2. **Each ellipse matches the cylinder's cross-section** ($x$ semi-axis $\sqrt{2}$, $y$ semi-axis $3\sqrt{2}/2$)
3. **Both curves lie on the ellipsoid surface** at approximately 71% of maximum height
4. **Complete symmetry** about all three coordinate planes
5. **No connection between the curves**—the cylinder passes through the ellipsoid's interior between them

The most common mistake would be drawing a single connected curve; the key visual cue to prevent this is emphasizing the empty space between $z = +2\sqrt{2}$ and $z = -2\sqrt{2}$ where the cylinder is inside the ellipsoid but not intersecting its surface.

This mental model should help you reliably visualize and sketch the intersection geometry.