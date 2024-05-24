import tkinter
import customtkinter
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pyautogui as pya
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Watermark Creator")
        self.geometry("580x180")
        self.angle = 0
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["0", "45", "90", "120", "180","270"], command=self.angle_of_pic, width = 70)
        self.add_path = customtkinter.CTkButton(self, text="Open file", command=self.set_file)
        self.txt = customtkinter.CTkLabel(self,text= "Angle")
        self.fade = customtkinter.CTkSlider(self, from_=0, to=255, command=self.wt_fade, width= 255)
        self.path = customtkinter.CTkEntry(self, placeholder_text="Path to your file (exmple D:\\screenshots\\example.png)", width=370)
        self.button = customtkinter.CTkButton(self, text="Add watermark", command=self.pic_send, fg_color = "green", hover_color="darkgreen")
        self.text = customtkinter.CTkEntry(self, placeholder_text="Text of your watermark", width=370)
        self.switch = customtkinter.CTkSwitch(self, text="Black / White",onvalue="white", offvalue="black")
        self.info = customtkinter.CTkSwitch(self, text="Show only / Save only", onvalue="save", offvalue="show")
        self.amount_txt = customtkinter.CTkLabel(self, text="Fade of the watermark:"+" "*15+"of 255")
        self.amount_entry = customtkinter.CTkEntry(self, width=35, height=20)
        self.amount_entry.insert(0, int(self.fade.get())//1)
        self.amount_entry.grid(row=2, column=0, padx=(0,15),pady=0)
        self.path.grid(row=0, column=0, padx=10, pady=0)
        self.text.grid(row=1, column=0, padx=10, pady=10)
        self.switch.grid(row=2, column=1, padx=0, pady=0)
        self.info.grid(row=1, column=1, padx=0, pady=0)
        self.button.grid(row=3, column=1, padx=30, pady=10)
        self.add_path.grid(row=0, column=1, padx=30, pady=5)
        self.fade.grid(row=3,column=0,padx=(0,100),pady=0)
        self.optionmenu.grid(row=3, column=0, padx=(300,0), pady=0)
        self.txt.grid(row=2, column=0, padx=(300,0), pady=0)
        self.amount_txt.grid(row=2, column=0, padx=(0, 107), pady=0)

        self.bind("<Return>", self.set_fd)

    def set_fd(self,pas):
        amount = int(self.fade.get())
        if int(self.amount_entry.get()) != amount:
            amount = int(self.amount_entry.get())
            self.fade.set(amount)
    def wt_fade(self,val):
        fade = int(self.fade.get())
        self.amount_entry.delete(0, [2**10])
        self.amount_entry.insert(0, fade)
    def angle_of_pic(self,angle):
        self.angle = self.optionmenu.get()
    def set_file(self):
        self.path_to = tkinter.filedialog.askopenfilename()
        self.path.delete(0, 1)
        self.path.insert(0,self.path_to)

    def pic_send(self):
        path = self.path.get()
        text = self.text.get()
        info = self.info.get()
        color = self.switch.get()
        size = round(len(text))
        fade = int(self.fade.get())//1
        angle = int(self.angle)
        size *= 57
        img = Image.new(mode="RGBA", size=(1920, 1080))
        font = ImageFont.truetype("arial.ttf", 100)
        I = ImageDraw.Draw(img)

        rg = 0
        dn = 0
        if color == "white":
            r, g, b = 255, 255, 255

        else:
            r, g, b = 0, 0, 0

        for l in range(50):
            for i in range(40):
                I.text((rg, dn), text, font=font, fill=(r, g, b, fade))
                rg += size
            rg = 0
            dn += 135

        img = img.rotate(angle)

        try:
            img1 = Image.open(path).convert("RGBA")

        except:
            pya.alert("There is an error here\nplease check if your path is correct")

        else:
            if img.size != img1.size:
                img = img.resize(img1.size)

            img_remade = Image.alpha_composite(img1, img)

            if info == "save":
                img_remade.save(f"by_ske8ter.png")

            elif info == "show":
                img_remade.show()


app = App()
app.mainloop()
