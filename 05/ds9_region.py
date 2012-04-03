
keywords = {"circle":("r",),
            "ellipse":("r_maj", "r_min", "angle"),
            "box":("width", "height", "angle"),
            }

formats = {"circle":"circle({x}, {y}, {r})",
           "ellipse":"ellipse({x}, {y}, {r_maj}, {r_min}, {angle})",
           "box":"box({x}, {y}, {width}, {height}, {angle})",
           }

def ds9_region(shape, x, y, *kl, **kwargs):
    shape_params = ds9_region_get_shape_params(shape, x, y, *kl, **kwargs)
    return formats[shape].format(**shape_params)

def ds9_region_get_shape_params(shape, x, y, *kl, **kwargs):
    shape_params = dict(x=x, y=y)
    shape_keywords = keywords[shape]

    shape_params.update(zip(shape_keywords, kl))

    for k in shape_keywords[len(kl):]:
        shape_params[k] = kwargs[k]

    return shape_params

