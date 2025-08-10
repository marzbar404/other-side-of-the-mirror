init python:
    game_title = "Other Side of the Mirror"
    game_version = "v1.0"
    game_description = "Other Side of the Mirror is a (genre) game about a teenager's experience with gender dysphoria and how it effects her daily life."

screen main_menu():
    tag menu
    add "main_menu_bg.jpg"
    add Solid("#0008")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        text game_title size 70 color "#FFFFFF" outlines [(2, "#000", 0, 0)]

    vbox:
        spacing 15
        xalign 0.5
        yalign 0.5

        textbutton "Start Game" action Start()
        textbutton "Load Game" action ShowMenu("load")
        textbutton "Preferences" action ShowMenu("preferences")
        textbutton "About" action ShowMenu("about")
        textbutton "Quit" action Quit(confirm=True)

screen load():
    tag menu
    add "main_menu_bg.jpg"
    add Solid("#0008")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        text "Load Game" size 50 color "#FFFFFF" outlines [(2, "#000", 0, 0)]

    frame:
        background None
        xalign 0.5
        yalign 0.25
        has vbox spacing 10

        grid 3 2 spacing 10:
            for i in range(1, 7):
                button:
                    action FileAction(i)
                    has fixed
                    text FileTime(i, empty=_("Empty Slot")) size 20
                    text FileSaveName(i) size 15

    frame:
        background None
        xalign 0.5
        yalign 0.9
        textbutton "Back" action Return()

screen preferences():
    tag menu
    add "main_menu_bg.jpg"
    add Solid("#0008")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        text "Preferences" size 50 color "#FFFFFF" outlines [(2, "#000", 0, 0)]

    vbox:
        spacing 15
        xalign 0.5
        yalign 0.3

        text "Text Speed" size 25
        bar value Preference("text speed")

        text "Music Volume" size 25
        bar value Preference("music volume")

        text "Sound Volume" size 25
        bar value Preference("sound volume")

    frame:
        background None
        xalign 0.5
        yalign 0.9
        textbutton "Back" action Return()

screen about():
    tag menu
    add "main_menu_bg.jpg"
    add Solid("#0008")

    frame:
        background None
        xalign 0.5
        yalign 0.1
        text "About" size 50 color "#FFFFFF" outlines [(2, "#000", 0, 0)]

    vbox:
        spacing 15
        xalign 0.5
        yalign 0.3

        text game_title size 40 color "#FFFFFF"
        text "Version: [game_version]" size 20 color "#CCCCCC"
        text game_description size 25 color "#FFFFFF" xmaximum 800

        text "Made with love by Marzlib Studios" size 23 color "#FFFFFF" yoffset 20

    frame:
        background None
        xalign 0.5
        yalign 0.9
        textbutton "Back" action Return()
