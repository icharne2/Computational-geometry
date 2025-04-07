import numpy as np
import tkinter as tk
from tkinter import simpledialog, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def normalize(v):
    return v / np.linalg.norm(v)

def ray_sphere_intersection(ray_origin, ray_direction, sphere_center, sphere_radius):
    b = 2 * np.dot(ray_direction, ray_origin - sphere_center)
    c = np.dot(ray_origin - sphere_center, ray_origin - sphere_center) - sphere_radius**2
    delta = b**2 - 4 * c
    if delta > 0:
        sqrt_delta = np.sqrt(delta)
        t1 = (-b - sqrt_delta) / 2
        t2 = (-b + sqrt_delta) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None

def render_scene(sphere_center):
    width, height = 640, 480
    camera = np.array([2, 0, 0])
    sphere_radius = 1
    light_position = np.array([5, 5, -10])
    image = np.zeros((height, width, 3))

    for y in range(height):
        for x in range(width):
            screen_x = (x - width / 2) / width * 2
            screen_y = -(y - height / 2) / height * 2
            ray_direction = normalize(np.array([screen_x, screen_y, 1]))

            t = ray_sphere_intersection(camera, ray_direction, sphere_center, sphere_radius)
            if t is not None:
                intersection = camera + t * ray_direction
                normal = normalize(intersection - sphere_center)
                light_dir = normalize(light_position - intersection)
                diffuse = max(np.dot(normal, light_dir), 0)

                image[y, x] = np.clip(diffuse * np.array([1.0, 0.5, 0.25]), 0, 1)
            else:
                image[y, x] = np.array([0, 0, 0])

    return image, camera

def update_image():
    global sphere_center, canvas, fig, ax
    image, camera = render_scene(sphere_center)
    ax.clear()
    ax.imshow(image, extent=(-3, 7, -5, 5))
    ax.set_xlim(-3, 7)
    ax.set_ylim(-5, 5)
    ax.set_aspect('auto')
    ax.set_xticks(np.linspace(-3, 7, 11))
    ax.set_yticks(np.linspace(-5, 5, 11))
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    sphere_text = f'Sphere: {sphere_center[:2]}'
    ax.text(0.95, 0.05, sphere_text, color='white', fontsize=12, transform=ax.transAxes, ha='right', va='bottom', backgroundcolor='black')
    canvas.draw()

def set_sphere_position():
    global temp_sphere_center
    x = simpledialog.askfloat("Input", "Enter sphere X position:", initialvalue=sphere_center[0])
    y = simpledialog.askfloat("Input", "Enter sphere Y position:", initialvalue=sphere_center[1])
    if x is not None and y is not None:
        temp_sphere_center = np.array([x, y, sphere_center[2]])

def apply_changes():
    global sphere_center, temp_sphere_center
    if temp_sphere_center is not None:
        sphere_center = temp_sphere_center
        update_image()

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        fig.savefig(file_path)

# Initial sphere center position
sphere_center = np.array([0, 0, 5])
temp_sphere_center = None

# Create main window
root = tk.Tk()
root.title("Ray Tracing UI")

# Create a figure for matplotlib
fig = Figure(figsize=(6.4, 4.8), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack()

set_position_button = tk.Button(button_frame, text="Set Sphere Position", command=set_sphere_position)
set_position_button.pack(side=tk.LEFT)

apply_button = tk.Button(button_frame, text="Apply Changes", command=apply_changes)
apply_button.pack(side=tk.LEFT)

save_button = tk.Button(button_frame, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT)

# Initial rendering
update_image()

# Run the Tkinter event loop
root.mainloop()
