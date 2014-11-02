import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

# video = 3D numpy array (frames, height, width)
fig = plot.figure()

a = np.random.random((video.shape[1], video.shape[2]))
img = plot.imshow(a, cmap = "gray")

def init():
    img.set_data(np.random.random((video.shape[1], video.shape[2])))
    return [img]

def animate(i):
    img.set_array(video[i])
    return [img]

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(video), interval = 50, blit = True)
anim.save("animation.mp4")
