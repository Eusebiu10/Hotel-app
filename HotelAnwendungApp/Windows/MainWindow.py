from Controllers.Controller import *


class MainWindow:

    # initialise main window
    def __init__(self, root):
        # define hover functions which change the text of the status label, based on event
        def guest_button_hover(e):
            status_label.config( text='Go to Guest Menu' )

        def room_button_hover(e):
            status_label.config( text='Go to Room Menu' )

        def general_button_hover(e):
            status_label.config( text='Go to General Menu' )

        def import_button_hover(e):
            status_label.config( text='Import desired files for Guests and Rooms' )

        def exit_button_hover(e):
            status_label.config( text='Exit Application' )

        def button_leave(e):
            status_label.config( text='' )

        # initialise window
        self.root = root
        root.title( "Hotel Anwendung" )
        root.geometry( "600x700" )

        # initialise controller
        controller = Controller()

        # set background image using png photo from resources folder
        filename = tk.PhotoImage( file="Resources\\background.png" )
        background_label = tk.Label( root, image=filename )
        background_label.place( x=0, y=0, relwidth=1, relheight=1 )

        # create status label as tooltip
        status_label = tk.Label( root, text='', bd=1, relief=tk.SUNKEN, anchor=tk.E, bg='#edb879' )

        status_label.pack( fill=tk.X, side=tk.BOTTOM )

        # create buttons which use functions from controller
        guest_button = tk.Button( root, text="Guest Menu", width=55, bg='#edb879',
                                  command=controller.openNewWindowGuest, font=('Helvetica', 10, 'bold') )
        guest_button.place( relx=0.5, rely=0.3, anchor=tk.CENTER )
        room_button = tk.Button( root, text="Rooms Menu", width=55, bg='#edb879', command=controller.openNewWindowRoom,
                                 font=('Helvetica', 10, 'bold') )
        room_button.place( relx=0.5, rely=0.4, anchor=tk.CENTER )
        general_button = tk.Button( root, text="General Menu", width=55, bg='#edb879',
                                    command=controller.openNewWindowGeneral, font=('Helvetica', 10, 'bold') )
        general_button.place( relx=0.5, rely=0.5, anchor=tk.CENTER )
        import_button = tk.Button( root, text="Import Data", width=55, bg='#edb879',
                                   command=controller.browse_file, font=('Helvetica', 10, 'bold') )
        import_button.place( relx=0.5, rely=0.6, anchor=tk.CENTER )

        # exit button that closes current window
        exit_button = tk.Button( root, text="Exit", width=55, bg='#e38f19', command=self.root.destroy,
                                 font=('Helvetica', 10, 'bold') )
        exit_button.place(
            relx=0.5, rely=0.9, anchor=tk.CENTER )

        # bind hover effect functions to the buttons
        guest_button.bind( "<Enter>", guest_button_hover )
        room_button.bind( "<Enter>", room_button_hover )
        general_button.bind( "<Enter>", general_button_hover )
        import_button.bind( "<Enter>", import_button_hover )
        exit_button.bind( "<Enter>", exit_button_hover )
        guest_button.bind( "<Leave>", button_leave )
        room_button.bind( "<Leave>", button_leave )
        general_button.bind( "<Leave>", button_leave )
        import_button.bind( "<Leave>", button_leave )
        exit_button.bind( "<Leave>", button_leave )
        self.root.mainloop()
