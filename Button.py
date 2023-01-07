import flet as ft
def main(page: ft.page):
    first_name=ft.TextField(label="Enter First Name",autofocus=True)
    last_name=ft.TextField(label="EnterLast Name")
    email_add=ft.TextField(label="Enter email")
    greeting=ft.Column()
    def btn_click(e):
        greeting.controls.append(ft.Text(f"Your Name is : {first_name.value} {last_name.value}"))
        greeting.controls.append(ft.Text(f"Email is : {email_add.value}"))
        first_name.value=""
        last_name.value=""
        email_add.value=""
        page.update()
        first_name.focus()
    page.add(
        first_name,last_name,email_add,
        ft.ElevatedButton("click to check",on_click=btn_click),
        greeting,
    )
ft.app(target=main,view=ft.WEB_BROWSER)

