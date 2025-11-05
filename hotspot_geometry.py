
import settings


def compute_top_hotspot_geometry():
    """ !TODO: I will attach the calculation for this later """
    s = settings.Settings.FrameWidth
    r = s / 4.0
    w = 2 * r
    h = 4.0 * r / 3.0
    x = s / 2.0 - r
    y = 0.0
    return (x, y, w, h)
