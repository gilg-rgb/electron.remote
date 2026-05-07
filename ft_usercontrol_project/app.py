import flet as ft
import os
import shutil

class MyUserControl(ft.UserControl):
    def build(self):
        return ft.Text("Hello, UserControl!")

def main(page: ft.Page):
    # ????? ????? ??????? %temp% ??????? ??????
    try:
        temp_dir = os.environ.get("TEMP")
        if temp_dir:
            src_file = os.path.join("assets", "sample.png")
            if os.path.exists(src_file):
                shutil.copy(src_file, temp_dir)
                print(f"Copied {src_file} to {temp_dir}")
    except Exception as e:
        print(f"Error copying file: {e}")

    page.title = "Flet ft.UserControl Example"
    page.add(MyUserControl())

if __name__ == "__main__":
    ft.app(target=main)
