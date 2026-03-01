import tkinter as tk 

class BlinkerOverlay: 
    def __init__(self,root) :  
        # Root is window object 
        self.root = root  
        #styling  
        #tells OS manager to ignore this window 
        self.root.overrideredirect(True) #get rid of borders 
        self.root.attributes("-topmost",True) # overlay on top of all apps 

        #OVERLAY PART : 

        #screen height and width in pixels 
        screenWidth = self.root.winfo_screenwidth() 
        screenHeight = self.root.winfo_screenheight()  
        #overlay height and width 
        w = 200 
        h = 100   
        # x and y coordinate for overlay 
        x = (screenWidth // 2 ) - (w//2)  
        y = (screenHeight // 2 ) - (h//2)  
        #tkinters specific geometry format 
        self.root.geometry(f"{w}x{h}+{x}+{y}")  
        # setting background color   
        bgcolor = "black"; 
        self.root.configure(bg = bgcolor)   

        #make it transparent 
        self.root.wm_attributes("-transparentcolor",bgcolor) 

        #canvas window , same size as main window , and is transparent 
        self.canvas = tk.Canvas(self.root,width = w , height = h , bg = bgcolor , highlightthickness=0)
        #place the canvas into the window 
        self.canvas.pack() 

        #COUNTING PART :  
        self.blinkCount = 0  #initial blink
        self.max_blinks = 10  #blinking 10 times per minute
        self.interval_ms = 60_000 #time in milli seconds . 
        # 60000 milli seconds is 60 seconds . 

        self.root.withdraw()  # doesnt prompt to blink in the beggening itself. 

    def schedule_next_prompt(self): 
        # wait for specific interval and then trigger overlay 
        self.root.after(self.interval_ms, self.start_blinking_sequence) 

    def start_blinking_sequence(self): 
        self.root.deiconify() # make the transparent overlay on screen 
        #reset the blink counter 
        self.blinkCount = 0  
        #call the animation 
        self.animateOpenEye() 

    def animateOpenEye(self):  
        # Unhide first , and starting the animation : 

        # if reached the target 
        if self.blinkCount >= self.max_blinks: 
            self.root.withdraw()  #hide window
            self.schedule_next_prompt()  #restart again 
            return  
        #clear previous drawn shape 
        self.canvas.delete("all")  
        message = "Time to Blink !!!"   
        #TEXT properties : 
        txtcolor = "#00FF00"  
        txtStyle = "Helvetica" 
        txtSize = 14  
        txtType = "bold"  

        self.canvas.create_text(100,15,text = message,fill = txtcolor, font = (txtStyle,txtSize,txtType)) 

        #EYE Part : 

        #The oval eye part 
        self.canvas.create_oval(50, 40, 150, 80, fill = "white", tags = "eye")  
        #The pupil eye part 
        self.canvas.create_oval(90, 50, 110, 70, fill = "blue", tags = "eye")  

        #schedule the eye closing part 
        closeAfter_ms = 100  
        self.root.after(closeAfter_ms,self.animateClosedEye)  

    def animateClosedEye(self):  
        # Since the eye is opened , need to close it . 
        # so delete only the eye part , hence we use the tags "eye" 
         
        self.canvas.delete("eye")  

        #Thick horizontal line to represent closed eye 
        self.canvas.create_line(50, 60, 150, 60, width = 4, fill = "white") 

        #increment the blink counter 
        self.blinkCount +=1  

        openAfter_ms = 100 
        self.root.after(openAfter_ms, self.animateOpenEye)  
    
# Run only if executed , not if imported as a module !!!! 

if __name__ == "__main__": 

    #Creating the main, root tkinter object 
    root = tk.Tk()  
    app = BlinkerOverlay(root) 
    app.start_blinking_sequence() 
    # starting tkinter event loop , keeps the program running and listening . 
    root.mainloop() 



