---
layout:     post
title:      "Calculus 1 - Unit 1: A quick pre-calculus refresh"
subtitle:   "Lines, Functions, and the Shapes Behind the Data"
description: "Precalculus, minus the stress. Learn slopes, function rules, and graph moves with simple examples you can picture and use."
date:    2025-09-26T12:00:00-04:00
author:     "O.J. Wilcox"
image: "/img/posts/bg-calculus-1-unit-1.png"
tags: [ "Math", "Calculus 1" ]
URL: "/2025/09/26/calculus-1-unit-1-a-quick-pre-calculus-refresh/"
categories: [ Math ]
draft: false
---

## Calculus 1: Unit 1

Precalculus is the toolbox you’ll use all through Calculus I. You’ll see lines, circles, functions, tables/graphs, “average change,” piecewise rules, function mash-ups (composition), and quick ways to shift/stretch graphs. Each bit below tells you: **what it is**, **how to spot it**, and **why it matters** (with examples you’ll actually use).

---

## 1) Lines in the plane (and distance)

**Idea:** A line is the simplest trend. “Steepness” (slope) tells you how fast y goes up when x goes up a little.
**Distance** is just “how far apart are two points.”

* **Everyday:** Road grade signs like “6% grade” are slope.
* **SRE:** During a rollout, graph the error rate over time. If the line is steep, things are getting worse fast → pause or roll back.

**Quick checks**

* Horizontal line: “no change” trend. Vertical line: “undefined slope” (you’d divide by zero—don’t).
* **Distance** on a number line = “how many steps apart” (always positive). On a grid, think “little right triangle” distance between points.

---

## 2) Circles

**Idea:** A circle is “all points the same distance from a center.”

* **Everyday:** A compass drawing a circle around a pushpin.
* **SRE:** “Blast radius” thinking—everything within N hops of a failed service. The **center** is the failure, **radius** is the scope.

**Spot it:** Equations of circles mention a **center** (where it’s located) and a **radius** (how big).

---

## 3) Slope between two points (average change)

**Idea:** Pick any two points on a graph. The slope between them is the **average rate of change** over that span.

* **Everyday:** Town population goes from 3,192 to 5,362 in 10 years → “about 217 people per year.”
* **SRE:** CPU from 40% to 70% in 5 minutes → “about +6% per minute.” This average can hide spikes, but it’s great for a first cut.

**Types to recognize**

* Positive slope (rising), negative (falling), zero (flat), undefined (vertical).

---

## 4) Equations of lines (how to write one fast)

**Idea:** Two popular forms:

* **Slope–intercept:** “y = (slope)·x + (start at y)”

* **Point–slope:** “Start from a known point; move by slope.”

* **Everyday:** Phone plan with base fee + per-GB cost.

* **SRE:** Cloud cost = base + (per-instance × number of instances). Once you know a point and a slope, you can write the whole line.

---

## 5) What is a function?

**Idea:** A **function** is a rule that gives **exactly one** output for each input. (One input → one output.)

* **Everyday:** Put 16 into “square-root,” you always get 4 (not 4 and –4 for our purposes here).
* **SRE:** “Requests → latency” for a fixed system state is a function: at a given request load, there’s a single measured latency value at that moment.

**Not a function:** Same input mapping to multiple outputs (fails the “one input → one output” rule).

---

## 6) Evaluate functions (use the rule)

**Idea:** Function notation just names the rule: **f(x)** means “apply rule f to x.”

* **Everyday:** A(L, W) = area from length & width; P(S) = perimeter from side; D(t) = distance after time t.
* **SRE:** E(t) = error count at minute t. Plug in t = 30 to get the value at minute 30.

---

## 7) The difference quotient (average rate of change, again)

**Idea:** Fancy name, simple job: “How much did the output change when I nudged the input by a little bit?” (It’s the same average-change idea as slope, just written with a tiny step.)

* **Everyday:** Oven temp goes from 325° to 350° in 10 minutes → about +2.5°/min.
* **SRE:** Requests jump when you add a feature flag to 5% of users: difference-quotient thinking tells you “per percentage point of rollout, how much did RPS/latency change?” Useful for controlled rollouts.

*(On the test you’ll simplify expressions; conceptually, remember it’s “change in output over change in input.”)*

---

## 8) Functions from tables and graphs

**Idea:** A function can be a formula, but it can also just be a **table** of values or a **graph**.

* **Everyday:** A spreadsheet of “Year → Revenue.”
* **SRE:** Grafana/Datadog plots are functions: “time → metric value.”

**Two quick skills**

* Build a small table to sketch a graph.
* Use the **vertical line test**: if a vertical line hits the curve twice at the same x, it’s **not** a function.

---

## 9) Reading graphs (carefully)

**Idea:** Graphs tell two kinds of stories:

* **Specific points** (e.g., “at 9 AM the temp was ~68°F”).

* **Shape and trends** (rising, leveling, peaking, sudden drops).

* **Everyday:** Diver off a board—height starts high, drops, hits water, then comes back up.

* **SRE:** Velocity-style plots (burn rate, request rate). Peak shows “fastest point.” Sign change (positive → negative) shows “direction flipped” (e.g., from accumulating to draining).

**Incidents:** Don’t just read the number—read the **shape**: smooth rise vs. sudden cliff means very different root causes.

---

## 10) Piecewise functions (different rules in different zones)

**Idea:** “If x is in this range, use rule A; otherwise use rule B.”

* **Everyday:** Pay is $24/hr up to 40 hours, then $36/hr overtime. Same input (hours), two rules based on the range.
* **SRE:** Autoscaling policies: “If CPU < 60% → do nothing; if ≥ 60% for 5 min → add 1 pod; if ≥ 85% → add 2.” That’s a piecewise policy.

**Graphing tip:** Each **piece** lives on its own **restricted domain**. Use open/closed dots at the boundaries so the graph still passes the vertical line test.

---

## 11) Composition of functions (plug a result into another rule)

**Idea:** Do g first, then feed its result into f. Written as **f(g(x))** (“f of g of x”).

* **Everyday:** Time → radius of a ripple; radius → area. You can go straight from time to area by composing.
* **SRE:** Load → queue length; queue length → latency. Composition gives **load → latency** sensitivity in one step.

**Why care?** Systems are layered. Composition mirrors how outputs become inputs down the stack.

---

## 12) Shifting and stretching graphs (quick mental sketches)

**Idea:** Small edits to a formula cause predictable moves in the graph:

* **+k** outside → move **up**; **–k** outside → move **down**

* **(x – h)** inside → move **right** by h; **(x + h)** inside → move **left** by h

* **Multiply the whole output** → **stretch/compress** vertically; negative sign → **flip** over the x-axis

* **Everyday:** Alarm graph shifted 2 hours right = you woke up later.

* **SRE:** Latency baseline shift after a config change (up/down); compression when caching reduces the amplitude of spikes.

---

## 13) Absolute value functions (distance from zero)

**Idea:** |x| means “how far x is from 0,” always non-negative. The basic graph is a **V** shape.

* **Everyday:** “5 miles east” or “5 miles west” are both distance 5 from home base.
* **SRE:** |error_delta| treats up-spikes and down-spikes as “magnitude of change,” useful for anomaly scores.

**Twist you’ll see:** y = |f(x)| mirrors any parts of y = f(x) that are **below** the x-axis up **above** it (because absolute value can’t be negative).

---

# Tiny “test brain” checklist

* **Line facts:** recognize slope types; write a line fast with a point and a slope.
* **Distance:** think “steps apart” (number line) or “little triangle” (xy-plane).
* **Function vs not:** one input → one output; use the vertical line test.
* **Evaluate:** plug in the input carefully; name functions (A, P, D, f, g) for clarity.
* **Difference quotient:** it’s just average change over a small step.
* **Tables & graphs:** make/interpret a quick table; read points **and** shape.
* **Piecewise:** choose the right rule for the input’s range; graph pieces with correct endpoints.
* **Composition:** outputs feed inputs; f(g(x)) means g first, then f.
* **Shifts/stretches:** move up/down/left/right; stretch/flip; sketch from the base shape.
* **Absolute value:** V-shape; |f(x)| reflects negative parts above the axis.

---

# SRE mini-applications you can steal

* **Error slope guardrail:** “If error trend > X per minute for Y minutes → auto-rollback.”
* **Overtime-like policy:** Piecewise autoscaling thresholds that change response when load crosses cutoffs.
* **Layer sensitivity:** Use composition to explain “how a small load change propagates to latency.”
* **Downtime reading:** Graph shape + endpoints to reconstruct “when it actually got bad” and “when we recovered.”