import flet as ft
def main(page: ft.page):
    page.title="My first calculator"
    result =ft.Text(value="0")
    page.add(
        ft.Row(controls=[result]),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC"),
                ft.ElevatedButton(text="+/_"),
                ft.ElevatedButton(text="%"),
                ft.ElevatedButton(text="/")
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="7"),
                ft.ElevatedButton(text="8"),
                ft.ElevatedButton(text="9"),
                ft.ElevatedButton(text="*")
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="4"),
                ft.ElevatedButton(text="5"),
                ft.ElevatedButton(text="6"),
                ft.ElevatedButton(text="-")
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="1"),
                ft.ElevatedButton(text="2"),
                ft.ElevatedButton(text="3"),
                ft.ElevatedButton(text="+")
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="0"),
                ft.ElevatedButton(text="."),
                ft.ElevatedButton(text="+"),
                # ft.ElevatedButton(text="/")
            ]
        ),
        
    )
ft.app(target=main)