import tkinter as tk 

class BlinkerOverlay: 
    def __init__(self,root):  
        # Root is window object 
        self.root = root  
        
        # styling  
        self.root.overrideredirect(True) # get rid of borders 
        self.root.attributes("-topmost",True) # overlay on top of all apps 

        # OVERLAY PART : 
        screenWidth = self.root.winfo_screenwidth() 
        screenHeight = self.root.winfo_screenheight()  
        
        w = 200 
        h = 100   
        x = (screenWidth // 2 ) - (w//2)  
        y = (screenHeight // 2 ) - (h//2)  
        
        self.root.geometry(f"{w}x{h}+{x}+{y}")  
        
        bgcolor = "black" 
        self.root.configure(bg = bgcolor)   
        self.root.wm_attributes("-transparentcolor", bgcolor) 

        self.canvas = tk.Canvas(self.root, width = w, height = h, bg = bgcolor, highlightthickness=0)
        self.canvas.pack() 

        # TIMING PART :  
        # 60 seconds / 5 blinks = 1 prompt every 12 seconds
        self.interval_ms = 12_000 

        # Start hidden
        self.root.withdraw()  

    def schedule_next_prompt(self): 
        # Wait 12 seconds and then trigger the single blink
        self.root.after(self.interval_ms, self.start_blinking_sequence) 

    def start_blinking_sequence(self): 
        self.root.deiconify() # show the transparent overlay 
        self.animateOpenEye() 

    def animateOpenEye(self):  
        self.canvas.delete("all")  
        message = "Time to Blink !!!"   
        txtcolor = "#00FF00"  
        txtStyle = "Helvetica" 
        txtSize = 14  
        txtType = "bold"  

        self.canvas.create_text(100, 15, text = message, fill = txtcolor, font = (txtStyle, txtSize, txtType)) 

        # The oval eye part 
        self.canvas.create_oval(50, 40, 150, 80, fill = "white", tags = "eye")  
        # The pupil eye part 
        self.canvas.create_oval(90, 50, 110, 70, fill = "blue", tags = "eye")  

        # Keep the eye open a bit longer (800ms) so you definitely notice it appearing
        closeAfter_ms = 800  
        self.root.after(closeAfter_ms, self.animateClosedEye)  

    def animateClosedEye(self):  
        self.canvas.delete("eye")  

        # Thick horizontal line to represent closed eye 
        self.canvas.create_line(50, 60, 150, 60, width = 4, fill = "white") 

        # Keep it closed for 400ms, then finish the sequence
        openAfter_ms = 400 
        self.root.after(openAfter_ms, self.finishBlinkCycle)  

    def finishBlinkCycle(self):
        # The single blink is done. Hide the window and wait 12 seconds for the next one.
        self.root.withdraw()
        self.schedule_next_prompt()

# Run only if executed, not if imported as a module
if __name__ == "__main__": 
    root = tk.Tk()  
    app = BlinkerOverlay(root) 
    app.start_blinking_sequence() # Prompts immediately upon running to test it
    root.mainloop()