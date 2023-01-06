import flet as ft
def main(page: ft.page):
    def add_clicked(e):
        page.add(ft.checkbox(label=new_task.value))
        new_task.value=""
        page.update()
    
    new_task=ft.TextField(hint_text="Enter Id") 
    page.title="my first app"   
    page.add(new_task,ft.FloatingActionButton(icon=ft.icons.ADD,on_click=add_clicked))
    new_task=ft.TextField(hint_text="Enter Password")
    page.add(new_task,ft.FloatingActionButton(icon=ft.icons.ADD,on_click=add_clicked))
    page.add(ft.ElevatedButton(text="Submit")),
    #ft.app(target=main) #used to open app on desktop
ft.app(target=main, view=ft.WEB_BROWSER) #used to open app on browser