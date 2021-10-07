import os
from os.path import dirname, expanduser, exists
from ipywidgets import Button, HBox, HTML, Layout, Textarea, VBox


def save_credentials_ui(path):
    """Make a simple form to save a credentials text file.
    """
    path = expanduser(path)
    if dirname(path):
        os.makedirs(dirname(path), exist_ok=True)
    ht = HTML(
        f'Paste here your credentials to go into '
        f'<span style="font-family: monospace">{path}</span>:'
    )
    ta = Textarea(layout=Layout(height="100px", width="500px"))

    def save(button):
        with open(path, "w") as f:
            f.write(ta.value)

    def close(button):
        ui.close()

    save_bt = Button(description=f"Save", icon="save", button_style="info", layout=Layout(width="80px"))
    close_bt = Button(description="Close", icon="close", button_style="info", layout=Layout(width="80px"))
    save_bt.on_click(save)
    close_bt.on_click(close)
    ui = VBox([ht, ta, HBox([save_bt, close_bt])])
    return ui
