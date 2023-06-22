from fpdf import FPDF

class PDF(FPDF):
    def name(self):
        return input("Name: ")

    def shirt(self):
        self.add_page()
        self.set_font("helvetica", "B", 55)
        self.cell(0, 10, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self.image("shirtificate.png", w=pdf.epw)
        self.set_font("helvetica", "I", 25)
        self.set_text_color(255,255,255)
        self.text(x=49, y= 135, txt = self.name() + " took CS50")
        self.output("shirtificate.pdf")


pdf = PDF()
pdf.shirt()


