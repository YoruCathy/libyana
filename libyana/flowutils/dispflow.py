import math

from matplotlib.colors import hsv_to_rgb
import numpy as np


def radial_flow(flow):
    flow_x = flow[:, :, 0]
    flow_y = flow[:, :, 1]
    flow_mag = np.sqrt(flow_x ** 2 + flow_y ** 2)
    flow_ang = np.arctan2(flow_y, flow_x)
    return flow_ang, flow_mag


def normalize_flow(flow_ang, flow_mag):
    min_ang = -math.pi
    max_ang = math.pi
    flow_ang = (flow_ang - min_ang) / (max_ang - min_ang)
    flow_mag = (flow_mag - flow_mag.min()) / (flow_mag.max() - flow_mag.min())
    return flow_ang, flow_mag


def disp_flow(flow):
    flow_ang, flow_mag = radial_flow(flow)
    flow_ang, flow_mag = normalize_flow(flow_ang, flow_mag)
    hsv = np.stack((flow_ang, flow_mag, np.ones_like(flow_ang)), 2)
    rgb = hsv_to_rgb(hsv)  # In range [0, 1]
    return rgb
