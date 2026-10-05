# animations.py


def blend_color(start_color, end_color, progress):
    """
    Creates a color between start_color and end_color.

    progress:
    0.0 = completely start_color
    1.0 = completely end_color
    """

    start_color = start_color.lstrip("#")
    end_color = end_color.lstrip("#")

    start_rgb = tuple(
        int(start_color[i:i + 2], 16)
        for i in (0, 2, 4)
    )

    end_rgb = tuple(
        int(end_color[i:i + 2], 16)
        for i in (0, 2, 4)
    )

    new_rgb = tuple(
        int(
            start_rgb[i]
            + (end_rgb[i] - start_rgb[i]) * progress
        )
        for i in range(3)
    )

    return "#{:02x}{:02x}{:02x}".format(*new_rgb)


def fade_labels(
    app,
    labels,
    start_colors,
    end_colors,
    step=0,
    steps=20,
    speed=40,
    on_complete=None
):

    progress = step / steps

    for label, start_color, end_color in zip(
        labels,
        start_colors,
        end_colors
    ):

        # Make sure the label still exists
        if label.winfo_exists():

            new_color = blend_color(
                start_color,
                end_color,
                progress
            )

            label.configure(
                text_color=new_color
            )

    if step < steps:

        app.after(
            speed,
            lambda: fade_labels(
                app,
                labels,
                start_colors,
                end_colors,
                step + 1,
                steps,
                speed,
                on_complete
            )
        )

    elif on_complete:

        on_complete()