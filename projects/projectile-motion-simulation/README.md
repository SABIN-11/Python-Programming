# Projectile Motion Simulation

An interactive 2D simulation of projectile motion built with Python, NumPy, and Matplotlib. I created this project to explore the equations of projectile motion visually and presented it at a science exhibition.

## Features

- **Animated trajectory:** Watch the projectile move along its parabolic path, with a trail and velocity arrow.
- **Interactive parameters:** Adjust the initial speed, launch angle, gravitational acceleration, and playback speed with sliders.
- **Live physics readouts:** View the time of flight, maximum height, horizontal range, and initial velocity components.
- **Inspect any point:** Move the cursor onto the trajectory to inspect the projectile's approximate time, position, velocity components, speed, and direction.
- **Playback controls:** Pause, resume, replay, or reset the simulation.
- **Automatic plot scaling:** The plot adjusts to the selected launch parameters.

## Preview

Run the program locally to see the animation and interactive controls. A screenshot or short GIF can be added here later.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Installation and setup

1. Clone or download this repository.
2. Open a terminal in this project folder.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the simulation:

   ```bash
   python projectile_animated.py
   ```

A desktop Matplotlib window is required for the sliders, buttons, and animation.

## Physics model

The simulation assumes ideal projectile motion: air resistance is ignored, gravitational acceleration is constant, and the projectile lands at the same height from which it was launched.

For initial speed \(v_0\), launch angle (θ), gravitational acceleration \(g\), and time \(t\), the initial velocity components are

\[
v_{x0}=v_0\cos\θ, \qquad v_{y0}=v_0\sin\θ.
\]

The position is calculated from

\[
x(t)=v_0\cos\θ\,t
\]

\[
y(t)=v_0\sin\θ\,t-\frac{1}{2}gt^2.
\]

For the same launch and landing height, the program also calculates the time of flight, maximum height, and horizontal range:

\[
T=\frac{2v_0\sin\θ}{g}, \qquad
H=\frac{v_0^2\sin^2\θ}{2g}, \qquad
R=\frac{v_0^2\sin(2\θ)}{g}.
\]

These equations let the simulation update the trajectory and numerical readouts whenever a parameter changes.

## Project structure

```text
projectile-motion-simulation/
├── projectile_animated.py
├── requirements.txt
└── README.md
```

## Limitations

- Air resistance and wind are not modelled.
- The launch and landing heights are assumed to be equal.
- The simulation is intended for learning and visualization, not precision engineering.

## Possible extensions

- Add air resistance and compare the resulting path with ideal projectile motion.
- Plot how the horizontal range changes with launch angle.
- Compare trajectories for different initial speeds and gravitational fields.

## Technologies

Python · NumPy · Matplotlib
