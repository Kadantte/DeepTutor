## Summary

The intersection forms Viviani's Curve, a single closed loop resembling a figure-8 that resides entirely on the right hemisphere ($x \ge 0$) of the sphere. The curve anchors at the North and South poles $(0,0,\pm 2)$ and self-intersects at the equator point $(2,0,0)$, maintaining symmetry across both the $xy$ and $xz$ planes. To sketch it, trace a path from $(2,0,0)$ that wraps around the cylinder's circular footprint $(x-1)^2 + y^2 = 1$ while oscillating vertically between $z=\pm 2$.

---

# Geometric Understanding of the Cylinder-Sphere Intersection

The intersection of the cylinder $(x-1)^2 + y^2 = 1$ and the sphere $x^2 + y^2 + z^2 = 4$ forms a famous space curve known as **Viviani's Curve**. To sketch this confidently, you need to understand how the two surfaces sit relative to each other, where the curve anchors in space, and how it traverses between these points.

## 1. The Big Picture: "A Figure-8 on the Right Hemisphere"

Before diving into details, establish this core mental model [code-1]:

*   **The Shape**: The curve is a **figure-8 (lemniscate)** wrapped around the **right hemisphere** of the sphere ($x \ge 0$).
*   **The Pinch**: The loops cross each other at the very front tip of the sphere, point **$(2,0,0)$**.
*   **The Lobes**: One loop goes up to the **North Pole $(0,0,2)$**, the other goes down to the **South Pole $(0,0,-2)$**.
*   **The Containment**: The curve never leaves the surface of the cylinder, which means it never goes past $x=0$ (the $z$-axis) and never goes past $x=2$. It is entirely contained in the "right" half of the sphere.

**Visual Analogy**: The curve looks like a **tennis ball seam** that has been squashed so that one crossing point is pinned to the equator at $(2,0,0)$, and the two loops wrap over the top and under the bottom of the sphere, passing through the poles [code-1].

## 2. Spatial Relationship of the Surfaces

Before tracing the curve, visualize the two surfaces and their positioning:

*   **The Sphere**: Centered at the origin $(0,0,0)$ with radius $R=2$. It bounds the entire curve within $-2 \le x, y, z \le 2$.
*   **The Cylinder**: A vertical tube of radius $r=1$ with its central axis along the line $x=1, y=0$ (parallel to the $z$-axis). It extends infinitely in the $z$-direction.
*   **Containment Relationship**: The cylinder is **not** centered on the sphere's axis. Instead, it is offset to the right (positive $x$).
    *   The cylinder's horizontal cross-section is the circle $(x-1)^2 + y^2 = 1$ in the $xy$-plane.
    *   This circle passes through the origin $(0,0)$ and touches the sphere's equatorial boundary at exactly one point: $(2,0)$.
    *   The cylinder lies entirely within the sphere's width ($x \in [0, 2]$). Consequently, the cylinder passes vertically through the sphere without punching out the sides. The sphere "caps" the cylinder at the top and bottom.

**Key Insight**: The entire curve resides in the region $x \ge 0$, biased towards the positive $x$-axis due to the cylinder's offset. This is derived from the cylinder equation: $x^2 + y^2 = 2x$ implies $x(2-x) = y^2 \ge 0$, so $0 \le x \le 2$ [code-1].

## 3. Key Anchor Points and Self-Intersection

The curve is a single continuous closed loop with a self-intersection point. You can anchor your sketch using the critical coordinates that define the extrema of the curve [code-1]:

| Point Type | Coordinates | Geometric Significance |
| :--- | :--- | :--- |
| **The Pinch (Self-Intersection)** | $(2, 0, 0)$ | Located on the positive $x$-axis. The curve crosses itself here where the cylinder is tangent to the sphere. Tangent vectors are $(0, 1, 1)$ and $(0, 1, -1)$ — distinct directions confirming true self-intersection. |
| **The Poles (Back of Sphere)** | $(0, 0, 2)$ and $(0, 0, -2)$ | North and South poles of the sphere. The cylinder passes through the origin, so the curve cuts through these poles. These are the leftmost points (min $x$) on the $z$-axis. |
| **The Shoulders (Widest Points)** | $(1, \pm 1, \pm \sqrt{2})$ | Located at $x=1$ (center of cylinder). Maximum $y$-width with $z = \pm \sqrt{2} \approx \pm 1.41$. These four points form a rectangle the curve passes through. |

**Visualization Tip**: The curve does not cross the $z=0$ plane anywhere except at $(2,0,0)$. It pinches to a single point at the equator and reaches its maximum vertical height at the poles.

## 4. Coordinate Extrema

Understanding the bounds of each coordinate helps constrain your mental model [code-1]:

| Coordinate | Minimum | Maximum | Location |
| :--- | :--- | :--- | :--- |
| **$x$** | $0$ | $2$ | $x=0$ at the back (poles), $x=2$ at the front (pinch) |
| **$y$** | $-1$ | $1$ | $y=\pm 1$ at $x=1$ (cylinder sides) |
| **$z$** | $-2$ | $2$ | $z=\pm 2$ at $x=0$ (sphere poles) |

## 5. Symmetry Properties

The curve inherits specific symmetries from the surfaces, which simplifies sketching. You only need to visualize one quarter of the curve; the rest follows by reflection [code-1]:

1.  **Reflection across the $xy$-plane ($z \to -z$)**:
    *   The cylinder equation contains no $z$ term, and the sphere has $z^2$.
    *   **Geometric Meaning**: The upper half ($z>0$) is a mirror image of the lower half ($z<0$).

2.  **Reflection across the $xz$-plane ($y \to -y$)**:
    *   Both equations contain $y^2$ terms, which are unchanged under $y \to -y$.
    *   **Geometric Meaning**: The "front" ($y>0$) is a mirror image of the "back" ($y<0$).

3.  **Rotational Symmetry ($180^\circ$) about the $x$-axis**:
    *   This is the composition of the two reflections above: $(x, y, z) \to (x, -y, -z)$.
    *   **Geometric Meaning**: If you rotate the curve 180 degrees around the $x$-axis, it maps onto itself.

4.  **No Symmetry across the $yz$-plane ($x \to -x$)**:
    *   The cylinder equation becomes $x^2 + y^2 = -2x$ under $x \to -x$, which describes a different cylinder centered at $x=-1$.
    *   **Geometric Meaning**: The curve is **not** symmetric left-to-right across the origin. It exists entirely in $x \ge 0$.

**Combined Effect**: You only need to determine the shape of the curve in the first octant ($x>0, y>0, z>0$), then reflect across the coordinate planes to complete the 3D shape.

## 6. Parametric Traversal and Path Structure

To imagine "walking" along the curve, use the natural parameterization of the cylinder. Let $t$ be the angle in the $xy$-plane centered at $(1,0)$ [code-1]:

$$
\begin{aligned}
x(t) &= 1 + \cos(t) \\
y(t) &= \sin(t) \\
z(t) &= 2\sin(t/2)
\end{aligned}
$$

**Derivation**: Substituting the cylinder parameterization into the sphere equation:
$$
\begin{aligned}
(1 + \cos(t))^2 + \sin^2(t) + z^2 &= 4 \\
1 + 2\cos(t) + \cos^2(t) + \sin^2(t) + z^2 &= 4 \\
2 + 2\cos(t) + z^2 &= 4 \\
z^2 &= 2(1 - \cos(t)) = 4\sin^2(t/2)
\end{aligned}
$$

Therefore $z = \pm 2\sin(t/2)$ [code-1].

**Important Note**: The full single closed loop (Viviani's curve) requires $t \in [0, 4\pi]$ with $z = 2\sin(t/2)$. The range $t \in [0, 2\pi]$ covers the projection once, resulting in two symmetric branches meeting at $z=0$ [code-1].

| Parameter $t$ | Point $(x, y, z)$ | Position Description |
| :--- | :--- | :--- |
| $t = 0$ | $(2, 0, 0)$ | **Start**: The pinch point on the equator |
| $t = \pi/2$ | $(1, 1, \sqrt{2})$ | **Shoulder**: Maximum $y$-width, rising |
| $t = \pi$ | $(0, 0, 2)$ | **Peak**: North Pole of the sphere |
| $t = 3\pi/2$ | $(1, -1, \sqrt{2})$ | **Shoulder**: Maximum $y$-width, descending |
| $t = 2\pi$ | $(2, 0, 0)$ | **Return**: Back to the pinch point |

### Mental Movie: Traversal Path

Start your finger at the crossing point **$(2,0,0)$** (Front Center) [code-1]:

*   **Upper Loop**: Move up and to the right ($y>0$). You climb the sphere's surface, moving "back" towards the origin ($x$ decreases). You reach the widest point at $x=1, y=1$, then curve inward to reach the **North Pole $(0,0,2)$**. From the North Pole, continue down the "other side" ($y<0$), mirroring your path, to return to **$(2,0,0)$**.
*   **Lower Loop**: From **$(2,0,0)$**, move down and to the right. Mirror the upper loop's motion to reach the **South Pole $(0,0,-2)$** and return.

The curve is a **single continuous closed loop** that does not split into multiple components. It wraps once around the cylinder while staying on the sphere surface [code-1].

## 7. 2D Projections: The Shadow Views

If you struggle with 3D depth, sketch the 2D "shadows" first to build confidence [code-1]:

| View | Projection | Shape Description |
| :--- | :--- | :--- |
| **Top View ($xy$-plane)** | $(x-1)^2 + y^2 = 1$ | A perfect **circle**. The curve lies directly on the cylinder wall. |
| **Front View ($xz$-plane)** | $z^2 = 4 - 2x$ | A **parabola** opening to the left. Vertex at $(2,0)$, passes through $(0, \pm 2)$. The curve traces this arc twice (once for $y>0$, once for $y<0$). |
| **Side View ($yz$-plane)** | $(1 - z^2/2)^2 + y^2 = 1$ | A classic **figure-8 (lemniscate)** crossing at the origin $(y=0, z=0)$. Top loop touches $z=2$, bottom touches $z=-2$. |

**Critical Insight**: The curve forms a **self-intersecting figure-8** when viewed from certain angles (particularly the $yz$-plane projection), but in 3D space it is a **single closed loop** that wraps around the cylinder once while oscillating vertically on the sphere [code-1].

These projections help verify your 3D sketch: the top view should look circular, the front view parabolic, and the side view should show the characteristic figure-8 crossing.

## 8. Step-by-Step Sketching Guide

To draw the 3D situation confidently, follow these steps [code-1]:

### Phase 1: Establish the Framework

1.  **Draw the Sphere**: Lightly sketch a circle for the equator and an ellipse for a latitude line to establish 3D perspective. Mark the North Pole $(0,0,2)$, South Pole $(0,0,-2)$, and the "rightmost" point $(2,0,0)$.
2.  **Mark the Anchors**: 
    *   Dot at **$(2,0,0)$** (Rightmost edge of sphere) — this is the crossing point.
    *   Dot at **$(0,0,2)$** (Top pole).
    *   Dot at **$(0,0,-2)$** (Bottom pole).
3.  **Draw the Cylinder (Ghosted)**: Lightly sketch the cylinder $(x-1)^2 + y^2 = 1$. It should look like a tube passing through the sphere, tangent to the $z$-axis.

### Phase 2: Draw the Curve

4.  **Sketch the Upper Loop ($z \ge 0$)**:
    *   Start at the pinch $(2,0,0)$.
    *   Curve upward and backward, passing through the "shoulder" at approximately $(1, 1, 1.4)$.
    *   **Crucial Detail**: Make sure it bulges **out** towards the viewer (positive $y$) before curving back to the $z$-axis. It should look like it wraps around the "side" of the sphere.
    *   Continue curving to touch the North Pole $(0,0,2)$.
    *   Mirror this path for $y < 0$ (behind the $xz$-plane) to complete the upper loop.

5.  **Sketch the Lower Loop ($z \le 0$)**:
    *   Mirror the upper loop across the $xy$-plane (equator).
    *   It should meet the upper loop at $(2,0,0)$ and pass through the South Pole $(0,0,-2)$.

6.  **Refine the Crossing**: At $(2,0,0)$, make it clear that one branch comes from above and one from below, crossing at an angle (like an 'X' viewed from the side). The tangent vectors $(0, 1, 1)$ and $(0, 1, -1)$ confirm distinct crossing directions.

### Phase 3: Add Depth Cues

7.  **Line Weight**: Use a thicker line for the parts of the curve where $y>0$ (front-right) and a thinner or dashed line for $y<0$ (back-right) if your viewpoint is from the first octant ($x,y,z > 0$).
8.  **Shading**: If shading the sphere, keep the curve in the lit area ($x>0$). Remember the curve never goes to the "back" of the sphere ($x<0$).
9.  **The "Window" Concept**: Viviani's Curve defines the edge of a "window" cut into the sphere. The area inside the curve (towards the $x$-axis) is the part of the sphere removed by the cylinder. Visualizing this "cutout" helps place the curve correctly.

### Common Visualization Mistakes to Avoid

| Mistake | Correction |
| :--- | :--- |
| Thinking curve passes through origin | It passes near origin ($x=0$) but at $z=\pm 2$, not $z=0$ |
| Drawing two separate loops | It's **ONE** continuous closed loop |
| Making it symmetric about $z$-axis | It's offset; symmetry is about $xz$-plane only |
| Forgetting the cylinder offset | Cylinder center is at $(1,0)$, **NOT** $(0,0)$ |
| Drawing curve in $x<0$ region | The curve is entirely contained in $x \ge 0$ (right hemisphere) |

## 9. Visual Reference

The following plot shows the intersection curve generated from the parametric equations. Note how the curve passes through the poles and pinches at the equator [code-1].

![Intersection Curve](intersection_curve.png)

**Key features to notice in the plot**:
*   The curve forms a **figure-8 shape** when viewed from certain angles.
*   It passes through both poles $(0,0,\pm 2)$ at the back of the sphere.
*   The curve meets at the rightmost point $(2,0,0)$ where it self-intersects.
*   The curve is entirely contained within $x \ge 0$.
*   The blue branch represents $z > 0$ and the red branch represents $z < 0$ [code-1].

## 10. Mental Model Summary

**For Confident Sketching** [code-1]:

1.  Remember it is a **single closed loop** with a self-intersection at $(2,0,0)$.
2.  Anchor on the **three key points**: $(2,0,0)$, $(0,0,2)$, and $(0,0,-2)$.
3.  Use the **symmetries**: Draw one quarter, then reflect across $y=0$ and $z=0$.
4.  Respect the **cylinder's footprint**: The top view must be a circle centered at $(1,0)$.
5.  Keep it in **$x \ge 0$**: The curve never crosses to the negative $x$ side of the sphere.
6.  **Depth cues**: Thicker lines for $y>0$, thinner/dashed for $y<0$; emphasize the "X" crossing at $(2,0,0)$.

**Alternative Analogy**: Visualize a ribbon wrapped around a vertical pipe (the cylinder) that's been pushed against the inside of a ball (the sphere). The ribbon touches the ball's top and bottom while circling the pipe once, creating an elegant asymmetric loop that's wider on one side than the other [code-1].

## 11. Quick Reference Table

| Property | Value |
| :--- | :--- |
| **Shape** | Single closed loop (appears as figure-8 in projection) |
| **Anchor points** | $(2,0,0)$ front, $(0,0,2)$ north pole, $(0,0,-2)$ south pole |
| **Self-intersection** | At $(2,0,0)$ with tangent vectors $(0,1,1)$ and $(0,1,-1)$ |
| **Symmetry** | Mirror symmetry across $xy$-plane and $xz$-plane |
| **Extent** | $x \in [0,2]$, $y \in [-1,1]$, $z \in [-2,2]$ |
| **Hemisphere** | Entirely contained in right hemisphere ($x \ge 0$) |
| **Traversal** | One complete circuit around cylinder while oscillating vertically on sphere |
| **Parametric form** | $x = 1 + \cos(t)$, $y = \sin(t)$, $z = 2\sin(t/2)$ for $t \in [0, 4\pi]$ |
| **Top projection** | Circle $(x-1)^2 + y^2 = 1$ |
| **Front projection** | Parabola $z^2 = 4 - 2x$ |
| **Side projection** | Figure-8 (lemniscate) |

By combining the anchor points, symmetries, parametric behavior, 2D projections, and depth cues, you can confidently reconstruct this 3D shape from memory and sketch Viviani's Curve with accuracy.