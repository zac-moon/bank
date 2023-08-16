import easygui

#simple tet with button "OK"
easygui.msgbox('Hello there')

#button choice box, you can choose button labels
choice = easygui.buttonbox('Choose a number :',choices=['1','2','3'])
easygui.msgbox(f'You choose {choice}')

#choicbox with differnet long form options
choice = easygui.choicebox("What's your choice Number?", choices=['1','2','3'])
easygui.msgbox(f'You choose {choice}')

#SINGLE TEXT INPUT
choice = easygui.enterbox('ENTER SOMETHING')
easygui.msgbox(f"You entered {choice}")