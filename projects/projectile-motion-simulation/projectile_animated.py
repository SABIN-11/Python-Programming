"""
2D Projectile Motion Simulation (no air resistance) - with animation

Controls:
  - Sliders: initial velocity, launch angle, gravity (changing any of them
    restarts the animation), and playback speed
  - Play/Pause and Replay buttons
  - Move the mouse directly onto the trajectory to read position and velocity
  - Reset button restores default values
"""

import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

plt.rcParams["toolbar"] = "None"   # hides the toolbar / white status bar at the bottom

# ---------------------------------------------------------------- defaults
V0_DEFAULT = 30.0       # m/s
ANGLE_DEFAULT = 45.0    # degrees
G_DEFAULT = 9.81        # m/s^2
SPEED_DEFAULT = 1.0     # playback speed (1.0 = real time)
N_POINTS = 500          # number of points along the trajectory
HIT_RADIUS_PX = 12      # how close (in screen pixels) the mouse must be to the path
FRAME_MS = 16           # timer interval (~60 frames per second)

# ---------------------------------------------------------------- colours (dark theme)
BG = "#1e2128"          # window background
PANEL = "#262b34"       # plot background
FG = "#e8eaed"          # text
GRID = "#3b4150"        # grid lines, borders
ACCENT = "#4cc2ff"      # trajectory
GROUND = "#c08a5a"
APEX = "#6fdc8c"
LAND = "#ffb454"
CURSOR = "#ff5f6d"
BALL = "#ffd166"


# ---------------------------------------------------------------- physics
def compute_trajectory(v0, angle_deg, g):
    """Return trajectory arrays and summary quantities."""
    theta = np.radians(angle_deg)
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)

    flight_time = 2 * v0 * np.sin(theta) / g
    max_height = (v0 * np.sin(theta)) ** 2 / (2 * g)
    range_ = v0 ** 2 * np.sin(2 * theta) / g

    t = np.linspace(0, flight_time, N_POINTS)
    x = vx0 * t
    y = vy0 * t - 0.5 * g * t ** 2

    return {
        "t": t, "x": x, "y": y,
        "vx0": vx0, "vy0": vy0, "g": g, "v0": v0,
        "T": flight_time, "H": max_height, "R": range_,
    }


# ---------------------------------------------------------------- blitting helper
class BlitManager:
    """
    Makes animation smooth. The static parts of the figure (axes, grid, labels,
    sliders...) are drawn once and stored as an image. Each animation frame then
    only restores that image and redraws the few moving artists on top of it.
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.artists = []
        self.background = None
        self.stale = True            # True while a full redraw is pending
        canvas.mpl_connect("draw_event", self.on_draw)

    def add(self, artist):
        artist.set_animated(True)
        self.artists.append(artist)

    def on_draw(self, event):
        if event is not None and event.canvas is not self.canvas:
            return
        self.background = self.canvas.copy_from_bbox(self.canvas.figure.bbox)
        self.stale = False
        self.draw_animated()

    def draw_animated(self):
        for artist in self.artists:
            self.canvas.figure.draw_artist(artist)

    def update(self):
        if self.stale or self.background is None:
            return
        self.canvas.restore_region(self.background)
        self.draw_animated()
        self.canvas.blit(self.canvas.figure.bbox)


# ---------------------------------------------------------------- figure
fig = plt.figure(figsize=(12, 7), facecolor=BG)
fig.canvas.manager.set_window_title("Projectile Motion Simulation")

ax = fig.add_axes([0.07, 0.32, 0.58, 0.62], facecolor=PANEL)
ax.set_xlabel("Horizontal distance x (m)", color=FG)
ax.set_ylabel("Height y (m)", color=FG)
ax.set_title("Projectile Trajectory (no air resistance)", color=FG)
ax.tick_params(colors=FG)
for spine in ax.spines.values():
    spine.set_color(GRID)
ax.grid(True, color=GRID, alpha=0.6)

state = compute_trajectory(V0_DEFAULT, ANGLE_DEFAULT, G_DEFAULT)

# Faint full path (also used for the mouse hover readout)
(path_line,) = ax.plot(state["x"], state["y"], color=ACCENT, lw=1.5, ls="--",
                       alpha=0.35, clip_on=False)
ax.axhline(0, color=GROUND, lw=3)  # ground
(launch_dot,) = ax.plot([0], [0], "o", color=FG, ms=7, clip_on=False, label="Launch (0, 0)")
(apex_dot,) = ax.plot([], [], "o", color=APEX, ms=7, clip_on=False, label="Max height")
(land_dot,) = ax.plot([], [], "s", color=LAND, ms=7, clip_on=False, label="Landing")
ax.legend(loc="upper right", facecolor=BG, edgecolor=GRID, labelcolor=FG)

# Moving artists (drawn every frame through the BlitManager)
(trail_line,) = ax.plot([], [], color=ACCENT, lw=3, clip_on=False)
(ball_dot,) = ax.plot([], [], "o", color=BALL, ms=13, zorder=6, clip_on=False)
ball_arrow = ax.annotate(
    "", xy=(0, 0), xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color=BALL, lw=2),
)
time_label = ax.text(
    0.02, 0.96, "", transform=ax.transAxes, color=FG, fontsize=11,
    family="monospace", va="top",
)
(cursor_dot,) = ax.plot([], [], "o", color=CURSOR, ms=11, zorder=5, clip_on=False)
velocity_arrow = ax.annotate(
    "", xy=(0, 0), xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color=CURSOR, lw=2),
)
velocity_arrow.set_visible(False)

# Text panels on the right
results_text = fig.text(
    0.69, 0.90, "", fontsize=11, family="monospace", va="top", color=FG,
    bbox=dict(boxstyle="round", facecolor="#243447", edgecolor="#3f5f80"),
)
cursor_text = fig.text(
    0.69, 0.60, "", fontsize=11, family="monospace", va="top", color=FG,
    bbox=dict(boxstyle="round", facecolor="#40262b", edgecolor="#80474f"),
)

CURSOR_HINT = (
    "Cursor readout\n"
    "--------------\n"
    "Touch the trajectory\n"
    "with the mouse to\n"
    "inspect that point."
)

blit = BlitManager(fig.canvas)
for artist in (trail_line, ball_dot, ball_arrow, time_label,
               cursor_dot, velocity_arrow, cursor_text):
    blit.add(artist)


# ---------------------------------------------------------------- sliders and buttons
def make_slider(rect, label, vmin, vmax, vinit, fmt=None):
    slider_ax = fig.add_axes(rect, facecolor=GRID)
    kwargs = {"valfmt": fmt} if fmt else {}
    s = Slider(slider_ax, label, vmin, vmax, valinit=vinit, color=ACCENT, **kwargs)
    if hasattr(s, "track"):
        s.track.set_facecolor(GRID)   # dark track behind the coloured fill
    s.label.set_color(FG)
    s.valtext.set_color(FG)
    return s


def make_button(rect, label):
    button_ax = fig.add_axes(rect)
    b = Button(button_ax, label, color="#333a47", hovercolor="#465064")
    b.label.set_color(FG)
    return b


s_v0 = make_slider([0.12, 0.20, 0.50, 0.03], "Velocity (m/s)", 1, 100, V0_DEFAULT)
s_angle = make_slider([0.12, 0.14, 0.50, 0.03], "Angle (deg)", 1, 89, ANGLE_DEFAULT)
s_g = make_slider([0.12, 0.08, 0.50, 0.03], "Gravity (m/s²)", 1, 25, G_DEFAULT)
s_speed = make_slider([0.12, 0.02, 0.50, 0.03], "Speed", 0.1, 10, SPEED_DEFAULT, fmt="%.1fx")

btn_play = make_button([0.68, 0.17, 0.12, 0.05], "Pause")
btn_replay = make_button([0.82, 0.17, 0.12, 0.05], "Replay")
btn_reset = make_button([0.68, 0.09, 0.12, 0.05], "Reset")


# ---------------------------------------------------------------- view
def set_view():
    """Origin (0, 0) sits in the bottom-left corner; x and y use the same scale."""
    w = 1.12 * state["R"]
    h = 1.30 * state["H"]
    box = ax.get_window_extent()
    aspect = box.height / box.width       # screen height / screen width of the plot area
    if w * aspect >= h:
        h = w * aspect                    # plot is wide: stretch the y-range
    else:
        w = h / aspect                    # plot is tall: stretch the x-range
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)


def request_full_redraw():
    """Use after changing anything that is not an animated artist."""
    blit.stale = True
    fig.canvas.draw_idle()


# ---------------------------------------------------------------- animation
sim_time = 0.0          # simulated time since launch (seconds)
playing = True
last_wall = None        # wall-clock time of the previous frame


def draw_ball(t):
    """Place the ball, its trail and its velocity arrow at simulated time t."""
    t = min(max(t, 0.0), state["T"])
    vx = state["vx0"]
    vy = state["vy0"] - state["g"] * t
    bx = vx * t
    by = max(state["vy0"] * t - 0.5 * state["g"] * t ** 2, 0.0)

    n = int(np.searchsorted(state["t"], t, side="right"))
    trail_line.set_data(np.append(state["x"][:n], bx), np.append(state["y"][:n], by))
    ball_dot.set_data([bx], [by])

    scale = 0.18 * state["R"] / state["v0"]
    ball_arrow.xy = (bx + vx * scale, by + vy * scale)
    ball_arrow.set_position((bx, by))
    ball_arrow.set_visible(True)

    time_label.set_text(f"t = {t:5.2f} s   speed = {np.hypot(vx, vy):6.2f} m/s")


def restart():
    global sim_time, playing
    sim_time = 0.0
    playing = True
    btn_play.label.set_text("Pause")
    draw_ball(0.0)


def tick():
    """Called by the timer ~60 times per second. Time-based, so speed stays correct."""
    global sim_time, playing, last_wall
    now = time.perf_counter()
    dt = 0.0 if last_wall is None else min(now - last_wall, 0.1)
    last_wall = now

    if not playing or blit.stale or blit.background is None:
        return

    sim_time += dt * s_speed.val
    finished = sim_time >= state["T"]
    if finished:
        sim_time = state["T"]
        playing = False

    draw_ball(sim_time)
    blit.update()

    if finished:
        btn_play.label.set_text("Play")
        request_full_redraw()


def on_play_pause(_):
    global playing
    if not playing and sim_time >= state["T"]:
        restart()                       # animation had finished: start over
    else:
        playing = not playing
        btn_play.label.set_text("Pause" if playing else "Play")
    request_full_redraw()


def on_replay(_):
    restart()
    request_full_redraw()


# ---------------------------------------------------------------- updates
cursor_active = False


def refresh_cursor_artists():
    # While playing, the timer redraws every frame anyway
    if not playing:
        blit.update()


def hide_cursor():
    global cursor_active
    if cursor_active:
        cursor_active = False
        cursor_dot.set_data([], [])
        velocity_arrow.set_visible(False)
        cursor_text.set_text(CURSOR_HINT)
        refresh_cursor_artists()


def update_plot(_=None):
    global state, cursor_active
    state = compute_trajectory(s_v0.val, s_angle.val, s_g.val)

    path_line.set_data(state["x"], state["y"])
    apex_dot.set_data([state["R"] / 2], [state["H"]])
    land_dot.set_data([state["R"]], [0])
    set_view()

    results_text.set_text(
        "Results\n"
        "-------\n"
        f"Time of flight : {state['T']:8.2f} s\n"
        f"Max height     : {state['H']:8.2f} m\n"
        f"Range          : {state['R']:8.2f} m\n"
        "\n"
        f"vx (constant)  : {state['vx0']:8.2f} m/s\n"
        f"vy initial     : {state['vy0']:8.2f} m/s"
    )

    cursor_active = False
    cursor_dot.set_data([], [])
    velocity_arrow.set_visible(False)
    cursor_text.set_text(CURSOR_HINT)

    restart()                           # new parameters -> animate from the start
    request_full_redraw()


def on_mouse_move(event):
    if event.inaxes is not ax or event.x is None:
        hide_cursor()
        return

    # Distance (in screen pixels) from the mouse to every point of the path
    pts = ax.transData.transform(np.column_stack([state["x"], state["y"]]))
    dist = np.hypot(pts[:, 0] - event.x, pts[:, 1] - event.y)
    idx = int(np.argmin(dist))
    if dist[idx] > HIT_RADIUS_PX:
        hide_cursor()                   # mouse is not touching the trajectory
        return

    global cursor_active
    cursor_active = True

    t = state["t"][idx]
    px, py = state["x"][idx], state["y"][idx]
    vx = state["vx0"]
    vy = state["vy0"] - state["g"] * t
    speed = np.hypot(vx, vy)
    direction = np.degrees(np.arctan2(vy, vx))

    cursor_dot.set_data([px], [py])

    # Arrow showing velocity direction; length scales with speed
    scale = 0.18 * state["R"] / state["v0"]
    velocity_arrow.xy = (px + vx * scale, py + vy * scale)
    velocity_arrow.set_position((px, py))
    velocity_arrow.set_visible(True)

    cursor_text.set_text(
        "Cursor readout\n"
        "--------------\n"
        f"time  t : {t:7.2f} s\n"
        f"x       : {px:7.2f} m\n"
        f"y       : {py:7.2f} m\n"
        f"vx      : {vx:7.2f} m/s\n"
        f"vy      : {vy:7.2f} m/s\n"
        f"speed   : {speed:7.2f} m/s\n"
        f"heading : {direction:7.1f} deg"
    )
    refresh_cursor_artists()


def on_resize(_):
    set_view()
    request_full_redraw()


def on_reset(_):
    s_speed.reset()
    s_v0.reset()
    s_angle.reset()
    s_g.reset()


s_v0.on_changed(update_plot)
s_angle.on_changed(update_plot)
s_g.on_changed(update_plot)
btn_play.on_clicked(on_play_pause)
btn_replay.on_clicked(on_replay)
btn_reset.on_clicked(on_reset)
fig.canvas.mpl_connect("motion_notify_event", on_mouse_move)
fig.canvas.mpl_connect("resize_event", on_resize)

timer = fig.canvas.new_timer(interval=FRAME_MS)
timer.add_callback(tick)
fig.canvas.mpl_connect("close_event", lambda event: timer.stop())

update_plot()
timer.start()
plt.show()