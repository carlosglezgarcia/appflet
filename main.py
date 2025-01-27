import flet as ft


def main(page: ft.Page):
    def change_tel(e):
        if check_mail.value:
            check_tel.value = False
        botones_check.update()

    def change_mail(e):
        if check_tel.value:
            check_mail.value = False
        botones_check.update()

    def agregar(e):
        dato_tel = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(nombre.value)),
                ft.DataCell(ft.Text(idioma.value)),
                ft.DataCell(ft.Text(telef.value)),
                ft.DataCell(
                    ft.IconButton(
                        "delete",
                        icon_color="red",
                        on_click=lambda e: eliminar(dato_tel),
                    )
                ),
            ]
        )

        dato_mail = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(nombre.value)),
                ft.DataCell(ft.Text(idioma.value)),
                ft.DataCell(ft.Text(correo.value)),
                ft.DataCell(
                    ft.IconButton(
                        "delete",
                        icon_color="red",
                        on_click=lambda e: eliminar(dato_mail),
                    )
                ),
            ]
        )
        if check_tel.value and (nombre.value and idioma.value and telef.value):
            datos.rows.append(dato_tel)

        elif check_mail.value and (nombre.value and idioma.value and correo.value):
            datos.rows.append(dato_mail)

        page.snack_bar = ft.SnackBar(
            content=ft.Text("DATO INGRESADO CORRECTAMENTE", size=30), bgcolor="green"
        )
        page.snack_bar.open = True
        page.update()

    def borrar(_):
        nombre.value = ""
        contra.value = ""
        idioma.value = ""
        correo.value = ""
        telef.value = ""
        check_tel.value = True
        check_mail.value = False
        text_area.value = ""
        formulario.update()

    def eliminar(dato):
        datos.rows.remove(dato)
        page.snack_bar = ft.SnackBar(
            ft.Text("SE ELIMINO EL DATO", size=30), bgcolor="red"
        )
        page.snack_bar.open = True
        page.update()

    page.title = "Mi aplicación con flet"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE_600)
    # page.padding = ft.Padding(0, 40, 0, 0)
    # Título
    titulo = ft.Text(
        "NUEVO USUARIO", size=30, width=400, text_align=ft.TextAlign.CENTER
    )

    # INPUTS
    # Input Nombre
    nombre = ft.TextField(label="Nombre", expand=True)
    # Input Contraseña
    contra = ft.TextField(
        label="Password",
        expand=True,
        password=True,
        can_reveal_password=True,
    )
    # Dropdown Idioma
    idioma = ft.Dropdown(
        label="Idioma",
        expand=True,
        options=[
            ft.dropdown.Option("Español"),
            ft.dropdown.Option("Inglés"),
            ft.dropdown.Option("Francés"),
        ],
    )
    # Input Correo
    correo = ft.TextField(
        label="Correo electrónico",
        expand=True,
        autofill_hints=ft.AutofillHint.EMAIL,
    )
    # Input Teléfono
    telef = ft.TextField(
        label="Teléfono",
        expand=True,
        autofill_hints=ft.AutofillHint.TELEPHONE_NUMBER,
    )
    # Checkbox de correo o telefono
    comun = ft.Text(value="Comunicación", width=120, text_align=ft.TextAlign.CENTER)

    check_tel = ft.CupertinoCheckbox(
        label="Teléfono", value=True, on_change=change_mail
    )
    check_mail = ft.CupertinoCheckbox(label="Correo electrónico", on_change=change_tel)
    botones_check = ft.Row([check_tel, check_mail])
    text_area = ft.TextField(
        label="Observaciones",
        multiline=True,
        min_lines=5,
        max_lines=5,
    )

    BtnAgregar = ft.ElevatedButton(
        text="Agregar", width=100, bgcolor="blue", color="white", on_click=agregar
    )

    BtnBorrar = ft.ElevatedButton(
        text="Borrar", width=100, bgcolor="red", color="white", on_click=borrar
    )

    datos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Idioma")),
            ft.DataColumn(ft.Text("Correo")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[],
    )
    formulario = ft.Column(
        width=400,
        controls=[
            titulo,
            nombre,
            contra,
            idioma,
            correo,
            telef,
            comun,
            botones_check,
            text_area,
            ft.Row(
                controls=[BtnAgregar, BtnBorrar],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ],
    )
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    content=formulario,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.top_left,
                    bgcolor=ft.Colors.BLACK38,
                    width=450,
                    border_radius=10,
                ),
                ft.Container(
                    content=datos,
                    margin=10,
                    alignment=ft.alignment.top_center,
                    bgcolor=ft.Colors.BLACK38,
                ),
            ],
        )
    )


ft.app(target=main)
