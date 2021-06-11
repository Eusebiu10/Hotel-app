import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st

from Controllers.Functions import Functions
from Menus.GasteMenu import GasteMenu
from Menus.ZimmerMenu import ZimmerMenu


class Controller:
    # controller which handles the functionalities of the GUI and creates the requested submenus(Guest/Room/General)
    # initialise our repositories which hold the list of objects(guests, rooms)
    gasteMenu = GasteMenu()
    zimmerMenu = ZimmerMenu()
    # initialise the functions class which contains functions to be used by the GUI buttons
    functions = Functions()
    functions.set_gasteMenu( gasteMenu )
    functions.set_zimmerMenu( zimmerMenu )

    def openNewWindowGuest(self):

        # initialise window
        newWindow = tk.Toplevel()
        newWindow.title( "Guests Menu" )
        newWindow.geometry( "600x700" )

        # set background
        filename = tk.PhotoImage( file="Resources\\background.png" )
        background_label = tk.Label( newWindow, image=filename )
        background_label.place( x=0, y=0, relwidth=1, relheight=1 )

        # hover functions
        def show_button_hover(e):
            status_label.config( text='Show all guests' )
        def insert_button_hover(e):
            status_label.config( text='Insert new guest' )
        def update_button_hover(e):
            status_label.config( text='Update guest firstname' )
        def delete_button_hover(e):
            status_label.config( text='Delete guest by id' )
        def return_button_hover(e):
            status_label.config( text='Return to Main Menu' )
        def button_leave(e):
            status_label.config( text='' )

        # status label
        status_label = tk.Label( newWindow, text='', bd=1, relief=tk.SUNKEN, anchor=tk.E, bg='#edb879' )
        status_label.pack( fill=tk.X, side=tk.BOTTOM )

        # scrollable text container for our results
        text = st.ScrolledText( newWindow, width=56, height=7, font=("Times New Roman", 15) )
        text.place( relx=0.5, rely=0.14, anchor=tk.CENTER )
        text.configure( state='disabled' )

        # button for showing all guests
        showGuests_button = tk.Button( newWindow, text="Show Guests", width=55, bg='#edb879',
                                       command=lambda: self.show_elements( newWindow, 0 ),
                                       font=('Helvetica', 10, 'bold') )
        showGuests_button.place( relx=0.5, rely=0.3, anchor=tk.CENTER )

        # input forms for insert first and last name of new guest
        entry1 = tk.Entry( newWindow, width=25, borderwidth=3 )
        entry2 = tk.Entry( newWindow, width=25, borderwidth=3 )
        labelVor = tk.Label( newWindow, text='Vorname:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelVor.place( relx=0.4, rely=0.34, anchor=tk.E )
        entry1.place( relx=0.5, rely=0.38, anchor=tk.E )
        labelNach = tk.Label( newWindow, text='Nachname:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelNach.place( relx=0.6, rely=0.34, anchor=tk.W )
        entry2.place( relx=0.5, rely=0.38, anchor=tk.W )

        # button which inserts the new guest
        insertGuest_button = tk.Button( newWindow, text="Insert Guest", width=55, bg='#edb879',
                                        command=lambda: self.insert_guest( entry1, entry2 ),
                                        font=('Helvetica', 10, 'bold') )
        insertGuest_button.place( relx=0.5, rely=0.44, anchor=tk.CENTER )

        # input forms for guest to be updated
        entry3 = tk.Entry( newWindow, width=25, borderwidth=3 )
        entry4 = tk.Entry( newWindow, width=25, borderwidth=3 )
        labelIdUp = tk.Label( newWindow, text='Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdUp.place( relx=0.4, rely=0.5, anchor=tk.E )
        entry3.place( relx=0.5, rely=0.54, anchor=tk.E )
        labelVorUp = tk.Label( newWindow, text='Vorname:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelVorUp.place( relx=0.6, rely=0.5, anchor=tk.W )
        entry4.place( relx=0.5, rely=0.54, anchor=tk.W )

        # button which updates the guest based on input
        updateGuest_button = tk.Button( newWindow, text="Update Guest Name", width=55, bg='#edb879',
                                        command=lambda: self.uppdate_vorname( entry3, entry4 ),
                                        font=('Helvetica', 10, 'bold') )
        updateGuest_button.place( relx=0.5, rely=0.6, anchor=tk.CENTER )

        # input form for guest to be deleted
        entry5 = tk.Entry( newWindow, width=25, borderwidth=3 )
        labelIdUp = tk.Label( newWindow, text='Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdUp.place( relx=0.5, rely=0.66, anchor=tk.CENTER )
        entry5.place( relx=0.5, rely=0.7, anchor=tk.CENTER )

        # button for delete guest based on input
        deleteGuest_button = tk.Button( newWindow, text="Delete Guest", width=55, bg='#edb879',
                                        command=lambda: self.delete_gast( entry5 ), font=('Helvetica', 10, 'bold') )
        deleteGuest_button.place( relx=0.5, rely=0.76, anchor=tk.CENTER )

        # button for closing window
        return_button = tk.Button( newWindow, text="Return", width=55, bg='#e38f19',
                                   command=newWindow.destroy, font=('Helvetica', 10, 'bold') )
        return_button.place( relx=0.5, rely=0.9, anchor=tk.CENTER )

        # bind hover function events to the buttons
        showGuests_button.bind( "<Enter>", show_button_hover )
        insertGuest_button.bind( "<Enter>", insert_button_hover )
        updateGuest_button.bind( "<Enter>", update_button_hover )
        deleteGuest_button.bind( "<Enter>", delete_button_hover )
        return_button.bind( "<Enter>", return_button_hover )
        showGuests_button.bind( "<Leave>", button_leave )
        insertGuest_button.bind( "<Leave>", button_leave )
        updateGuest_button.bind( "<Leave>", button_leave )
        deleteGuest_button.bind( "<Leave>", button_leave )
        return_button.bind( "<Leave>", button_leave )

        # set modularity for windows
        newWindow.grab_set()
        newWindow.mainloop()

    def openNewWindowRoom(self):

        # initialise new window
        newWindow = tk.Toplevel()
        newWindow.title( "Rooms Menu" )
        newWindow.geometry( "600x700" )

        # set background
        filename = tk.PhotoImage( file="Resources\\background.png" )
        background_label = tk.Label( newWindow, image=filename )
        background_label.place( x=0, y=0, relwidth=1, relheight=1 )

        # set button hover functions
        def show_button_hover(e):
            status_label.config( text='Show all rooms' )
        def insert_button_hover(e):
            status_label.config( text='Insert new room' )
        def update_button_hover(e):
            status_label.config( text='Update room price' )
        def delete_button_hover(e):
            status_label.config( text='Delete room by id' )
        def return_button_hover(e):
            status_label.config( text='Return to Main Menu' )
        def button_leave(e):
            status_label.config( text='' )

        # create status label
        status_label = tk.Label( newWindow, text='', bd=1, relief=tk.SUNKEN, anchor=tk.E, bg='#edb879' )
        status_label.pack( fill=tk.X, side=tk.BOTTOM )

        # create scrollable text container
        text = st.ScrolledText( newWindow, width=56, height=7, font=("Times New Roman", 15) )
        text.place( relx=0.5, rely=0.14, anchor=tk.CENTER )
        text.configure( state='disabled' )

        # create button for displaying rooms
        showRooms_button = tk.Button( newWindow, text="Show Rooms", width=55, bg='#edb879',
                                      command=lambda: self.show_elements( newWindow, 1 ),
                                      font=('Helvetica', 10, 'bold') )
        showRooms_button.place( relx=0.5, rely=0.3, anchor=tk.CENTER )

        #create label and input forms for entering new Room attributes
        labelNummer = tk.Label( newWindow, text='Nummer:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelNummer.place( relx=0.34, rely=0.34, anchor=tk.E )
        labelAnzahl = tk.Label( newWindow, text='Anzahl:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelAnzahl.place( relx=0.43, rely=0.42, anchor=tk.E )
        labelPrice = tk.Label( newWindow, text='Price:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelPrice.place( relx=0.5, rely=0.34, anchor=tk.CENTER )
        labelFarbe = tk.Label( newWindow, text='Farbe:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelFarbe.place( relx=0.57, rely=0.42, anchor=tk.W )
        labelMeer = tk.Label( newWindow, text='Meer:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelMeer.place( relx=0.68, rely=0.34, anchor=tk.W )
        entryNummer = tk.Entry( newWindow, width=20, borderwidth=3 )
        entryAnzahl = tk.Entry( newWindow, width=20, borderwidth=3 )
        entryPrice = tk.Entry( newWindow, width=20, borderwidth=3 )
        entryFarbe = tk.Entry( newWindow, width=20, borderwidth=3 )
        entryMeer = tk.Entry( newWindow, width=20, borderwidth=3 )
        entryNummer.place( relx=0.4, rely=0.38, anchor=tk.E )
        entryAnzahl.place( relx=0.5, rely=0.46, anchor=tk.E )
        entryPrice.place( relx=0.5, rely=0.38, anchor=tk.CENTER )
        entryFarbe.place( relx=0.5, rely=0.46, anchor=tk.W )
        entryMeer.place( relx=0.6, rely=0.38, anchor=tk.W )

        # insert new room button using values from the above inputs
        insertRoom_button = tk.Button( newWindow, text="Insert Room", width=55, bg='#edb879',
                                       command=lambda: self.insert_room( entryNummer, entryAnzahl, entryPrice,
                                                                         entryFarbe, entryMeer ),
                                       font=('Helvetica', 10, 'bold') )
        insertRoom_button.place( relx=0.5, rely=0.52, anchor=tk.CENTER )

        # create labels and input forms for fields required for updating room price
        labelIdUp = tk.Label( newWindow, text='Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdUp.place( relx=0.4, rely=0.56, anchor=tk.E )
        labelPriceUp = tk.Label( newWindow, text='Price:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelPriceUp.place( relx=0.6, rely=0.56, anchor=tk.W )
        entryIdUp = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryPriceUp = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryIdUp.place( relx=0.5, rely=0.6, anchor=tk.E )
        entryPriceUp.place( relx=0.5, rely=0.6, anchor=tk.W )

        # update room price button
        updateRoomPrice_button = tk.Button( newWindow, text="Update Room Price", width=55, bg='#edb879',
                                            command=lambda: self.update_price( entryIdUp, entryPriceUp ),
                                            font=('Helvetica', 10, 'bold') )
        updateRoomPrice_button.place( relx=0.5, rely=0.66, anchor=tk.CENTER )

        # create labels and input forms for the fields required for deleting room
        labelIdDel = tk.Label( newWindow, text='Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdDel.place( relx=0.5, rely=0.7, anchor=tk.CENTER )
        entryIdDel = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryIdDel.place( relx=0.5, rely=0.74, anchor=tk.CENTER )

        # delete room button
        deleteRoom_button = tk.Button( newWindow, text="Delete Room", width=55, bg='#edb879',
                                       command=lambda: self.delete_room( entryIdDel ), font=('Helvetica', 10, 'bold') )
        deleteRoom_button.place( relx=0.5, rely=0.8, anchor=tk.CENTER )

        # return button
        return_button = tk.Button( newWindow, text="Return", width=55, bg='#e38f19',
                                   command=newWindow.destroy, font=('Helvetica', 10, 'bold') )
        return_button.place( relx=0.5, rely=0.9, anchor=tk.CENTER )

        # bind hover event functions for buttons
        showRooms_button.bind( "<Enter>", show_button_hover )
        insertRoom_button.bind( "<Enter>", insert_button_hover )
        updateRoomPrice_button.bind( "<Enter>", update_button_hover )
        deleteRoom_button.bind( "<Enter>", delete_button_hover )
        return_button.bind( "<Enter>", return_button_hover )
        showRooms_button.bind( "<Leave>", button_leave )
        insertRoom_button.bind( "<Leave>", button_leave )
        updateRoomPrice_button.bind( "<Leave>", button_leave )
        deleteRoom_button.bind( "<Leave>", button_leave )
        return_button.bind( "<Leave>", button_leave )

        # set window modularity
        newWindow.grab_set()
        newWindow.mainloop()

    def openNewWindowGeneral(self):

        # create new window
        newWindow = tk.Toplevel()
        newWindow.title( "General Menu" )
        newWindow.geometry( "600x700" )

        # set background image
        filename = tk.PhotoImage( file="Resources\\background.png" )
        background_label = tk.Label( newWindow, image=filename )
        background_label.place( x=0, y=0, relwidth=1, relheight=1 )

        # define button hover event functions
        def show_active_guests_hover(e):
            status_label.config( text='Show all current guests' )
        def show_filtered_rooms_hover(e):
            status_label.config( text='Show filtered rooms by price and sea view' )
        def show_free_rooms_hover(e):
            status_label.config( text='Show all todays free rooms' )
        def book_room_hover(e):
            status_label.config( text='Book room' )
        def return_button_hover(e):
            status_label.config( text='Return to Main Menu' )
        def button_leave(e):
            status_label.config( text='' )

        # define status label
        status_label = tk.Label( newWindow, text='', bd=1, relief=tk.SUNKEN, anchor=tk.E, bg='#edb879' )
        status_label.pack( fill=tk.X, side=tk.BOTTOM )

        # create scrollable text container
        text = st.ScrolledText( newWindow, width=56, height=7, font=("Times New Roman", 15) )
        text.place(relx=0.5, rely=0.14, anchor=tk.CENTER )
        text.configure( state='disabled' )

        # button for showing all active guests
        showActiveGuests_button = tk.Button( newWindow, text="Show Active Guests", width=55, bg='#edb879',
                                             command=lambda: self.show_elements( newWindow, 2 ),
                                             font=('Helvetica', 10, 'bold') )
        showActiveGuests_button.place( relx=0.5, rely=0.3, anchor=tk.CENTER )

        # define labels and input forms for fields required for filltering rooms
        labelPrice = tk.Label( newWindow, text='Price:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelPrice.place( relx=0.4, rely=0.34, anchor=tk.E )
        labelMeer = tk.Label( newWindow, text='Meer:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelMeer.place( relx=0.6, rely=0.34, anchor=tk.W )
        entryPrice = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryMeer = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryPrice.place( relx=0.5, rely=0.38, anchor=tk.E )
        entryMeer.place( relx=0.5, rely=0.38, anchor=tk.W )

        # button for displaying rooms filtered by using the above inputs
        showFilteredRooms_button = tk.Button( newWindow, text="Show Filtered Rooms", width=55, bg='#edb879',
                                              command=lambda: self.filltert_rooms( newWindow, entryPrice,
                                                                                   entryMeer ),
                                              font=('Helvetica', 10, 'bold') )
        showFilteredRooms_button.place( relx=0.5, rely=0.43, anchor=tk.CENTER )

        # button for displaying today's free rooms
        showTodayFreeRooms_button = tk.Button( newWindow, text="Show Today's Free Rooms", width=55,
                                               bg='#edb879', command=lambda: self.show_elements( newWindow, 3 ),
                                               font=('Helvetica', 10, 'bold') )
        showTodayFreeRooms_button.place( relx=0.5, rely=0.49, anchor=tk.CENTER )

        # labels and input forms required for booking a room
        labelIdGast = tk.Label( newWindow, text='Guest Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdGast.place( relx=0.4, rely=0.53, anchor=tk.E )
        labelIdRoom = tk.Label( newWindow, text='Room Id:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelIdRoom.place( relx=0.6, rely=0.53, anchor=tk.W )
        labelAnzahl = tk.Label( newWindow, text='Anzahl:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelAnzahl.place( relx=0.4, rely=0.62, anchor=tk.E )
        labelDate = tk.Label( newWindow, text='Date:', bg='#fee5ad', font=('Helvetica', 10, 'bold') )
        labelDate.place( relx=0.6, rely=0.62, anchor=tk.W )
        entryIdGast = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryIdRoom = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryAnzahl = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryDate = tk.Entry( newWindow, width=25, borderwidth=3 )
        entryIdGast.place( relx=0.5, rely=0.57, anchor=tk.E )
        entryIdRoom.place( relx=0.5, rely=0.57, anchor=tk.W )
        entryAnzahl.place( relx=0.5, rely=0.66, anchor=tk.E )
        entryDate.place( relx=0.5, rely=0.66, anchor=tk.W )

        # button for booking room
        bookRoom_button = tk.Button( newWindow, text="Book Room", width=55, bg='#edb879',
                                     command=lambda: self.book_room( entryIdGast, entryIdRoom, entryAnzahl, entryDate ),
                                     font=('Helvetica', 10, 'bold') )
        bookRoom_button.place( relx=0.5, rely=0.72, anchor=tk.CENTER )

        # button for returning to main window
        return_button = tk.Button( newWindow, text="Return", width=55, bg='#e38f19', command=newWindow.destroy )
        return_button.place( relx=0.5, rely=0.9, anchor=tk.CENTER )

        # bind hover event functions to the buttons
        showActiveGuests_button.bind( "<Enter>", show_active_guests_hover )
        showFilteredRooms_button.bind( "<Enter>", show_filtered_rooms_hover )
        showTodayFreeRooms_button.bind( "<Enter>", show_free_rooms_hover )
        bookRoom_button.bind( "<Enter>", book_room_hover )
        return_button.bind( "<Enter>", return_button_hover )
        showActiveGuests_button.bind( "<Leave>", button_leave )
        showFilteredRooms_button.bind( "<Leave>", button_leave )
        showTodayFreeRooms_button.bind( "<Leave>", button_leave )
        bookRoom_button.bind( "<Leave>", button_leave )
        return_button.bind( "<Leave>", button_leave )

        # set window modularity
        newWindow.grab_set()
        newWindow.mainloop()

    def browse_file(self):

        # function which opens a file manager browse form and lets us select 2 .txt files from everywhere
        self.gasteMenu = GasteMenu()
        self.zimmerMenu = ZimmerMenu()
        guestsList = filedialog.askopenfilename( filetypes=(("Template files", "*.txt"), ("All files", "*")) )
        roomsList = filedialog.askopenfilename( filetypes=(("Template files", "*.txt"), ("All files", "*")) )

        # each line from the selected files, will have the values separated by comma, introduced into our
        # guests and rooms repositories defined above
        with open( guestsList ) as q:
            for line in q:
                # line strip takes text from txt by line
                # split uses comma to separate data from the line
                # values that were 'splitted', are inserted into our repositories
                self.gasteMenu.einfugen_Gast( line.strip().split( ',' )[0], line.strip().split( ',' )[1] )
        with open( roomsList ) as r:
            for line in r:
                self.zimmerMenu.einfugen_zimmer( line.strip().split( ',' )[0], line.strip().split( ',' )[1],
                                                 line.strip().split( ',' )[2], line.strip().split( ',' )[3],
                                                 line.strip().split( ',' )[4] )

    def show_elements(self, window, type):

        # this functions inserts text into our scrollable text container
        text = st.ScrolledText( window, width=56, height=7, font=("Times New Roman", 15) )
        text.place( relx=0.5, rely=0.14, anchor=tk.CENTER )

        # for type parameter beeing 0, it will show all guests
        if type == 0:
            i = 0
            # iterate through guest repository
            for g in self.gasteMenu.get_GastList():
                recipient = ''
                recipient = recipient + "Id: " + str(
                    i ) + "  Vorname: " + g.get_vorname() + "  Nachname: " + g.get_nachname()
                text.insert( tk.INSERT, recipient + "\n" )
                i = i + 1

        # for 1 we display all rooms
        if type == 1:
            # iterate through room repository
            for r in self.zimmerMenu.get_zimmerList():
                recipient = ''
                recipient = recipient + "Nummer: " + str( r.get_nummer() ) + "  Anzahl: " + str(
                    r.get_anzahl() ) + "  Preis: " + str(
                    r.get_preis() ) + "  Farbe: " + r.get_farbe() + "  Meerblick: " \
                            + str( r.get_meerblick() )
                text.insert( tk.INSERT, recipient + "\n" )

        # for 2 we display all current guests, using function from Functions class
        if type == 2:
            self.functions.set_gasteMenu( self.gasteMenu )
            self.functions.set_zimmerMenu( self.zimmerMenu )
            for g in self.functions.aktuelle_gaste():
                recipient = ''
                recipient = recipient + "Vorname: " + g.get_vorname() + "  Nachname: " + g.get_nachname()
                text.insert( tk.INSERT, recipient + "\n" )

        # for 3 we display all today's free rooms, using function from Functions class
        if type == 3:
            self.functions.set_zimmerMenu( self.zimmerMenu )
            self.functions.set_gasteMenu( self.gasteMenu )
            for r in self.functions.frei_zimmer_heute():
                recipient = ''
                recipient = recipient + "Nummer: " + str( r.get_nummer() ) + "  Anzahl: " + str(
                    r.get_anzahl() ) + "  Preis: " + str(
                    r.get_preis() ) + "  Farbe: " + r.get_farbe() + "  Meerblick: " \
                            + str( r.get_meerblick() )
                text.insert( tk.INSERT, recipient + "\n" )

    # functions for inserting new guest
    def insert_guest(self, entry1, entry2):
        self.gasteMenu.einfugen_Gast( entry1.get(), entry2.get() )

    # functions for updating vorname
    def uppdate_vorname(self, entry3, entry4):
        self.gasteMenu.aktualisieren_vorname( int( entry3.get() ), entry4.get() )

    # function for deleting guest
    def delete_gast(self, entry5):
        self.gasteMenu.loschen_gast( int( entry5.get() ) )

    # function for inserting new room
    def insert_room(self, entryNummer, entryAnzahl, entryPrice, entryFarbe, entryMeer):
        self.zimmerMenu.einfugen_zimmer( int( entryNummer.get() ), int( entryAnzahl.get() ), float( entryPrice.get() ),
                                         entryFarbe.get(), bool( entryMeer.get() ) )

    # function for updating price
    def update_price(self, entryId, entryPrice):
        self.zimmerMenu.aktualisieren_preis( int( entryId.get() ), float( entryPrice.get() ) )

    # function for deleting room
    def delete_room(self, entryId):
        self.zimmerMenu.loschen_zimmer( int( entryId.get() ) )

    # function for filtering rooms, using function from Functions class
    def filltert_rooms(self, window, entryPrice, entryMeer):
        self.functions.set_zimmerMenu( self.zimmerMenu )
        self.functions.set_gasteMenu( self.gasteMenu )
        text = st.ScrolledText( window, width=56, height=7, font=("Times New Roman", 15) )
        text.place( relx=0.5, rely=0.14, anchor=tk.CENTER )
        for r in self.functions.filltert_zimmer( float( entryPrice.get() ), str( entryMeer.get() ) ):
            recipient = ''
            recipient = recipient + "Nummer: " + str( r.get_nummer() ) + "  Anzahl: " + str(
                r.get_anzahl() ) + "  Preis: " + str( r.get_preis() ) + "  Farbe: " + r.get_farbe() + "  Meerblick: " \
                        + str( r.get_meerblick() )
            text.insert( tk.INSERT, recipient + "\n" )

    # function for booking room, using function from Gast class
    def book_room(self, entryGastId, entryRoomId, entryRoomAnzahl, entryDate):
        self.gasteMenu.get_GastList()[int( entryGastId.get() )].mache_reservierung( int( entryRoomId.get() ),
                                                                                    int( entryRoomAnzahl.get() ),
                                                                                    str( entryDate.get() ),
                                                                                    self.zimmerMenu.get_zimmerList(),
                                                                                    self.gasteMenu.get_GastList() )
        self.functions.set_zimmerMenu( self.zimmerMenu )
        self.functions.set_gasteMenu( self.gasteMenu )
