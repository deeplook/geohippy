import os
from os.path import dirname, expanduser, exists
from ipywidgets import Button, HTML, Layout, Textarea, VBox


def save_credentials_ui(path):
    """Make a simple form to save a credentials text file.
    """
    path = expanduser(path)
    if dirname(path):
        os.makedirs(dirname(path), exist_ok=True)
    ht = HTML(
        f'Paste here your credentials to go into '
        '<span style="font-family: monospace">{path}</span>:'
    )
    ta = Textarea(layout=Layout(height="100px", width="500px"))

    def save(button):
        with open(path, "w") as f:
            f.write(ta.value)

    bt = Button(description=f"Save", button_style="info", layout=Layout(width="80px"))
    bt.on_click(save)
    return VBox([ht, ta, bt])
    