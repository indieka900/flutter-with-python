import flet
import time
from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
    page.title = "Counter App"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    txt_field = TextField(value='0', width=100, text_align='right')

    def descending(e):
        while(ascending):
            time.sleep(1)
            txt_field.value = int(txt_field.value)-1
            page.update()

    def ascending(e):
        while(True):
            time.sleep(0.5)
            txt_field.value = int(txt_field.value)+1
            page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=descending),
                txt_field,
                IconButton(icons.ADD, on_click=ascending),
            ]
        )
    )

flet.app(target=main)