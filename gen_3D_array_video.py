import numpy
import matplotlib.pyplot
import matplotlib.animation

# video = 3D numpy array (frames, height, width)
fig, axes = matplotlib.pyplot.subplots()

# Amazingly, we can not start with the first frame of our video.
# Even if we copy the first frame. It also appears to need to be random.
a = numpy.random.random((video.shape[1], video.shape[2]))
# Does not work with matshow.
img = axes.imshow(a, interpolation="none", cmap = "gray")

def init():
    img.set_data(numpy.random.random((video.shape[1], video.shape[2])))
    return [img]

def animate(i):
    img.set_array(video[i])
    return [img]

anim = matplotlib.animation.FuncAnimation(fig,
                                          animate,
                                          init_func = init,
                                          frames = len(video),
                                          interval = 50)
anim.save("animation.mp4")
