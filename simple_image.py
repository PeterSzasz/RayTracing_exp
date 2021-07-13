# displays a simple image

from ray_utility import Ray, Vec3
import pyglet
from math import sqrt

def hit_sphere(center: Vec3, radius: float, r: Ray):
    oc = r.orig - center
    a = 1.0     # if dir is not unit length then: r.dir.dot(r.dir)
    half_b = oc.dot(r.dir)
    c = oc.length_squared() - radius*radius
    discriminant = half_b*half_b - a*c
    if (discriminant < 0):
        return -1.0
    else:
        return (-half_b - sqrt(discriminant)) # /a is unnecessary

def ray_color(r: Ray):
    '''calculate the bluisness in the background, based on the y component'''
    t = hit_sphere(Vec3(0, 0, -1), 0.5, r)
    if (t > 0.0):
        N = r.at(t) - Vec3(0.0, 0.0, -1.0)
        N = N.as_unit_vector()
        return Vec3(N.x+1.0, N.y+1.0, N.z+1.0)*0.5

    unit_direction = r.dir.as_unit_vector()
    t = (unit_direction.y + 1.0) * 0.5
    white_part = Vec3(1.0, 1.0, 1.0) * (1.0-t)
    blue_part = Vec3(0.5, 0.7, 1.0) * t
    return white_part + blue_part   # lerp

if __name__ == "__main__":

    # image
    aspect_ration = 16.0 / 9.0
    image_width = 256
    image_height = int(image_width / aspect_ration)  # w:256 -> h:144
    window = pyglet.window.Window(image_width, 
                                image_height, 
                                style=pyglet.window.Window.WINDOW_STYLE_DIALOG)
    window.set_caption("RayTracing")
    window.set_location(1200, 500)
    @window.event
    def on_draw():

        # camera
        viewport_height = 2.0   # projection plane or 'lense' height and width
        viewport_width = aspect_ration * viewport_height
        focal_length = 1.0      # eye distance from lense
        origin = Vec3() # null vector
        horizontal = Vec3(viewport_width, 0.0, 0.0)
        vertical = Vec3(0.0, viewport_height, 0.0)
        lower_left_corner = origin - horizontal/2.0 - vertical/2.0 - Vec3(0.0, 0.0, focal_length)
        #print(lower_left_corner)

        # render
        window.clear()
        #ai = pyglet.image.AbstractImage(maxx, maxy)
        #ai.blit_into()
        #pyglet.gl.glDrawPixels()   #might use this instead
        for y in range(0, image_height):
            for x in range(0, image_width):
                u = float(x)/(image_width-1)
                v = float(y)/(image_height-1)
                direction = lower_left_corner + horizontal*u + vertical*v - origin
                r = Ray(origin, direction)
                c = ray_color(r)
                pyglet.graphics.draw(1,
                                    pyglet.gl.GL_POINTS,
                                    ('v2i', (x, y)),
                                    ('c3B', (int(c.x*255), int(c.y*255), int(c.z*255)))
                                    )

    pyglet.app.run()
    