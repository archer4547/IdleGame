import flet as ft
import time, random


def main(page: ft.Page):
    page.title = 'Factories of Factories'
    page.window_maximized = True
    page.theme_mode = 'light'
    page.window_min_width = 912
    page.window_min_height = 488.5
    page.window_max_width = 1550.4
    page.window_max_height = 830.4
    page.padding = 0
    
    
    
    def on_resize(e):
        side_container.width = page.width/6
        side_container.height = page.height
        
        for sidebarButton in side_container.content.controls:
            button = sidebarButton.button.controls[0]
            button.width = page.width/7
            button.height = page.height/17
            button.update()
        
        factories_container.width = 5*page.width/6
        factories_container.height = page.height
        
        trees_container.width = 5*page.width/6
        trees_container.height = page.height
        
        upgrades_container.width = 5*page.width/6
        upgrades_container.height = page.height
        
        page.update()
        
    page.on_resize = on_resize
    
    
    def on_route_change(route):
        page.views.clear()
        if page.route == '/':
            page.views.append(
                ft.View(
                    '/',
                    controls=[
                        ft.Row(controls=[side_container, factories_container], spacing=0)
                    ],
                    padding=0
                )
            )
        elif page.route == '/trees':
            page.views.append(
                ft.View(
                    '/',
                    controls=[
                        ft.Row(controls=[side_container, trees_container], spacing=0)
                    ],
                    padding=0
                )
            )
        elif page.route == '/upgrades':
            page.views.append(
                ft.View(
                    '/',
                    controls=[
                        ft.Row(controls=[side_container, upgrades_container], spacing=0)
                    ],
                    padding=0
                )
            )
        elif page.route == '/how_to_play':
            page.views.append(
                ft.View(
                    '/',
                    controls=[
                        ft.Row(
                            controls=[how_to_play_view],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    vertical_alignment= 'center',
                    padding=0
                )
            )
        page.clean()
        page.add(page.views[-1])
    
    page.on_route_change = on_route_change
    
    def go_to_factories(e):
        page.go('/')
    def go_to_trees(e):
        page.go('/trees')
    def go_to_upgrades(e):
        page.go('/upgrades')
    def go_to_how_to_play(e):
        page.go('/how_to_play')
    
    class SidebarButton(ft.UserControl):
        def __init__(self, text, onClick):
            super().__init__()
            self.text = text
            self.onClick = onClick
            self.button = ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text=self.text,
                        width=page.width/7,
                        height=page.height/17,
                        on_click=self.onClick
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            
        def build(self):
            return self.button
    
    side_container = ft.Container(
        content=ft.Column(
            controls=[
                SidebarButton('Factories', go_to_factories),
                SidebarButton('Trees', go_to_trees),
                SidebarButton('Upgrades', go_to_upgrades),
                SidebarButton('How to play', go_to_how_to_play),
            ]
        ),
        width=page.width/6,
        height=page.height,
        bgcolor=ft.colors.TEAL_100
    )
    
    factories_container = ft.Container(
        content=ft.ListView(
            controls=[
                
            ]
        ),
        width=5*page.width/6,
        height=page.height,
        bgcolor=ft.colors.TEAL_200
    )
    for i in range(50):
        factories_container.content.controls.append(ft.Text(f'row {i}'))
    
    trees_container = ft.Container(
        content=ft.ListView(
            controls=[
                
            ]
        ),
        width=5*page.width/6,
        height=page.height,
        bgcolor=ft.colors.TEAL_200
    )
    for i in range(50):
        trees_container.content.controls.append(ft.Text(f'row {i+50}'))
    
    upgrades_container = ft.Container(
        content=ft.ListView(
            controls=[
                
            ]
        ),
        width=5*page.width/6,
        height=page.height,
        bgcolor=ft.colors.TEAL_200
    )
    for i in range(50):
        upgrades_container.content.controls.append(ft.Text(f'row {i+100}'))
    
    how_to_play_view = ft.Container(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(),
                            ft.Text('How to play', size=40),
                            ft.IconButton(icon=ft.icons.CLOSE, icon_size=40, on_click=go_to_factories)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Container(
                        ft.Text(
                            'hi'
                        ),
                        margin=15
                    )
                ]
            )
        ),
        width=8*page.width/10,
        height=8*page.height/10,
        bgcolor=ft.colors.GREY,
        border_radius=10
    )
    
       
    page.go('/')
    
    # while True:
    #     time.sleep(0.3)
    #     print(page.window_width, page.window_height)
        
    # 1550.4 | 830.4
    # 924 | 375.2


ft.app(main)
