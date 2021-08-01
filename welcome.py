from tkinter import *
from PIL import Image, ImageTk
import webbrowser

root1 = Tk()
root1.title('Ging HomeScreen')

root1.geometry('414x705')
root1.resizable(False, False)



def topFeature():
    top = Toplevel()
    top.title('Ging Top Feature Screen')
    top.geometry('415x705')
    top.resizable(False, False)

    global imageb
    global backImage
    imageb = ImageTk.PhotoImage(Image.open('ui/brianakingInfo.png'))
    backImage = ImageTk.PhotoImage(Image.open('ui/gingPopupback.png'))

    backButton = Button(top, image=backImage, command=top.destroy, borderwidth=0)
    brianaScreen = Label(top, image=imageb, borderwidth=0, compound=TOP)

    backButton.grid(row=0, column=0)
    brianaScreen.grid(row=1, column=0)

    # just set up for extra time, we can change command function as well to have optional variable so we can pass
    # this informaiton along, the id would just be which of the list of influencers, etc. was shown.

def newsFeature():
    news = Toplevel()
    news.title('Ging Top Feature Screen')
    news.geometry('415x705')
    news.resizable(False, False)
    global backImage
    global imageStory

    imageStory = ImageTk.PhotoImage(Image.open('ui/storiesScreen.png'))
    backImage = ImageTk.PhotoImage(Image.open('ui/gingPopupback.png'))

    backButton = Button(news, image=backImage, command=news.destroy, borderwidth=0)
    storiesScreen = Label(news, image=imageStory, borderwidth=0, compound=TOP)

    backButton.grid(row=0, column=0)
    storiesScreen.grid(row=1, column=0)

def openweb(url):
    webbrowser.open(url, new=1)

def WelcomeScreen():
    global welcome_image
    welcome_image = ImageTk.PhotoImage(Image.open('ui/Welcome_ScreenReal.png'))
    welcome = Button(root1, image=welcome_image, command=Home_Page, borderwidth=0, pady=30)
    welcome.grid(row=0, column=0)


# when button is pressed, there is an input where you will but the type of feature it is so it passes into the
# correct if statement


def Home_Page():
    home = Toplevel()
    home.title('Ging Welcome Screen')

    home.geometry('414x705')
    home.resizable(False, False)

    global my_img
    global my_img1
    global my_img2
    global my_img3
    global my_img4
    global my_img5
    global my_img6

    my_img = ImageTk.PhotoImage(Image.open("ui/gsbIcon.png"))
    my_img1 = ImageTk.PhotoImage(Image.open("ui/featureOneB.png"))
    my_img2 = ImageTk.PhotoImage(Image.open("ui/gingTitle.jpg"))
    my_img3 = ImageTk.PhotoImage(Image.open("ui/suit2.png"))
    my_img4 = ImageTk.PhotoImage(Image.open("ui/2021FemStories.png"))
    my_img5 = ImageTk.PhotoImage(Image.open("ui/home_bar-2.png"))
    my_img6 = ImageTk.PhotoImage(Image.open("ui/rectFiller.png"))

    # defines all the widgets on the screen
    icon = Label(home, image=my_img2)
    feature1_image = Button(home, image=my_img1, command=topFeature, borderwidth=0, pady=80)

    feature2_image = Button(home, image=my_img4, command=newsFeature, borderwidth=0, pady=30)
    feature3_image = Button(home, image=my_img3, command= lambda: openweb("https://www.missguidedus.com/dusky-pink-co-ord-tailored-longline-blazer-10222663?istCompanyId=6f000e44-d468-46b6-b05b-e9e08130e2eb&istFeedId=bb042319-c37d-44d3-b420-74f752055777&istItemId=iapwwqxax&istBid=xztt&gclid=Cj0KCQjw6ZOIBhDdARIsAMf8YyFCVYM2T0FCGieEIcWDMWf9KvCIThNVvjLvDcLPucqaDUbsEjhCxGEaAp7MEALw_wcB&gclsrc=aw.ds"), borderwidth=0, pady=60)
    home_bar = Button(home, image=my_img5, borderwidth=0, pady=30)
    rectangle = Label(home, image=my_img6, padx=30)

    # puts everything on the grid
    icon.grid(row=1, column=1, columnspan=2)
    feature1_image.grid(row=2, column=1, columnspan=2)
    feature2_image.grid(row=3, column=1)
    feature3_image.grid(row=4, column=1)
    home_bar.grid(row=5, column=1, columnspan=2)
    rectangle.grid(row=3, column=2, rowspan=2)


WelcomeScreen()
mainloop()
