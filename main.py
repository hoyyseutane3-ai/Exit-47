import tkinter as tk
import random

class Exit47MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("EXIT 47")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="#050505") 

        # --- GAME STATE & SETTINGS ---
        self.unlocked_chapters = 1 
        self.mark_state = "Normal"
        self.leo_friendship = 0
        self.romance_bond = 0
        
        self.settings = {
            "text_speed": 150,    
            "timer_difficulty": 1.0, 
            "text_size": 15
        }

        # Global Menu Fonts
        self.font_tiny = ("sans-serif", 10, "bold")
        self.font_small = ("sans-serif", 12, "italic") # For your name
        self.font_title = ("Impact", 60, "bold") 
        self.font_subtitle = ("sans-serif", 14, "bold")
        self.font_button = ("sans-serif", 18, "bold")

        self.menu_frame = tk.Frame(self.root, bg="#050505")
        self.menu_frame.pack(expand=True, fill=tk.BOTH)

        self.timer_running = False
        self.build_main_menu()

    def build_main_menu(self):
        self.timer_running = False
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        tk.Label(self.menu_frame, text="FROM THE WRITER OF LIFE EATER", font=self.font_tiny, bg="#050505", fg="#777777", pady=20).pack()
        
        title_frame = tk.Frame(self.menu_frame, bg="#050505")
        title_frame.pack(pady=(20, 0))
        shadow = tk.Label(title_frame, text="EXIT 47", font=self.font_title, bg="#050505", fg="#1a1a1a")
        shadow.place(x=3, y=3)
        tk.Label(title_frame, text="EXIT 47", font=self.font_title, bg="#050505", fg="#ffffff").pack()

        # YOUR CREATOR NAME
        tk.Label(self.menu_frame, text="By hoyy", font=self.font_small, bg="#050505", fg="#aaaaaa").pack(pady=(5, 10))

        tk.Label(self.menu_frame, text="ROMANCE THRILLER 2026", font=self.font_subtitle, bg="#050505", fg="#ffffff").pack(pady=(0, 40))

        self.create_hover_button("NEW GAME", self.start_chapter_1)
        self.create_hover_button("CHAPTER SELECT", self.build_chapter_select) 
        self.create_hover_button("SETTINGS", self.build_settings_menu) 
        self.create_hover_button("EXIT", self.root.quit)

    def create_hover_button(self, text, command):
        btn = tk.Label(self.menu_frame, text=text, font=self.font_button, bg="#050505", fg="#555555", cursor="hand2")
        btn.pack(pady=10)
        btn.bind("<Button-1>", lambda e: command())

    def build_settings_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        tk.Label(self.menu_frame, text="SETTINGS", font=self.font_subtitle, bg="#050505", fg="#ffffff", pady=20).pack()
        
        back_btn = tk.Label(self.menu_frame, text="<<< BACK TO MENU >>>", font=self.font_button, bg="#8b0000", fg="#ffffff", padx=20, pady=15)
        back_btn.pack(pady=10)
        back_btn.bind("<Button-1>", lambda e: self.build_main_menu())
        
        tk.Label(self.menu_frame, text="TEXT TYPE SPEED", font=self.font_tiny, bg="#050505", fg="#777777", pady=10).pack()
        sf = tk.Frame(self.menu_frame, bg="#050505")
        sf.pack()
        tk.Button(sf, text="VERY SLOW", command=lambda: self.update_setting("text_speed", 250)).pack(side=tk.LEFT, padx=5)
        tk.Button(sf, text="STEADY", command=lambda: self.update_setting("text_speed", 150)).pack(side=tk.LEFT, padx=5)
        tk.Button(sf, text="FAST", command=lambda: self.update_setting("text_speed", 50)).pack(side=tk.LEFT, padx=5)

    def update_setting(self, key, value):
        self.settings[key] = value
        l = tk.Label(self.menu_frame, text="SPEED UPDATED", bg="white", fg="black")
        l.pack()
        self.root.after(500, l.destroy)

    def build_chapter_select(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        tk.Label(self.menu_frame, text="CHAPTER SELECT", font=self.font_subtitle, bg="#050505", fg="#ffffff", pady=20).pack()
        back_btn = tk.Label(self.menu_frame, text="<<< BACK TO MENU >>>", font=self.font_button, bg="#8b0000", fg="#ffffff", padx=20, pady=15)
        back_btn.pack(pady=10)
        back_btn.bind("<Button-1>", lambda e: self.build_main_menu())
        self.create_hover_button("CHAPTER 1", self.start_chapter_1)

    def setup_game_screen(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        self.root.update()

        header = tk.Frame(self.menu_frame, bg="#080808", height=60)
        header.pack(fill=tk.X, side=tk.TOP)
        tk.Frame(header, bg="#ff0000", height=2).pack(fill=tk.X, side=tk.BOTTOM) 
        tk.Label(header, text="EXIT 47", font=("Impact", 18), bg="#080808", fg="#ffffff").pack(side=tk.LEFT, padx=25, pady=15)
        
        back_btn = tk.Label(header, text="MENU", font=("sans-serif", 12, "bold"), bg="#080808", fg="#555555")
        back_btn.pack(side=tk.RIGHT, padx=25, pady=15)
        back_btn.bind("<Button-1>", lambda e: self.build_main_menu())

        self.bottom_controls = tk.Frame(self.menu_frame, bg="#050505", padx=20, pady=10)
        self.bottom_controls.pack(fill=tk.X, side=tk.BOTTOM)

        self.timer_canvas = tk.Canvas(self.bottom_controls, height=15, bg="#2b2b2b", bd=0, highlightthickness=0)
        self.timer_bar = self.timer_canvas.create_rectangle(0, 0, 0, 15, fill="#ff0000", width=0)

        self.btn_a = tk.Button(self.bottom_controls, font=("sans-serif", 14, "bold"), bg="#1a1a1a", fg="#ffffff", relief=tk.FLAT, pady=15)
        self.btn_b = tk.Button(self.bottom_controls, font=("sans-serif", 14, "bold"), bg="#1a1a1a", fg="#ffffff", relief=tk.FLAT, pady=15)
        self.btn_continue = tk.Label(self.bottom_controls, text=">> TAP TO CONTINUE <<", font=("sans-serif", 14, "bold"), bg="#050505", fg="#444444", pady=20)

        self.border_frame = tk.Frame(self.menu_frame, bg="#1a1a1a", padx=2, pady=2)
        self.border_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.text_container = tk.Frame(self.border_frame, bg="#0a0a0a")
        self.text_container.pack(fill=tk.BOTH, expand=True)

        self.story_text = tk.Text(
            self.text_container, bg="#0a0a0a", fg="#ffffff", font=("sans-serif", self.settings["text_size"]), 
            wrap=tk.WORD, bd=0, highlightthickness=0, state=tk.DISABLED, spacing2=8, padx=20, pady=20
        )
        self.story_text.pack(fill=tk.BOTH, expand=True)
        self.story_text.tag_configure("system", foreground="#ff0000", font=("monospace", 14, "bold"))

        self.text_queue = []
        self.timer_running = False
        self.flash_state = True

    # --- ENGINE TOOLS ---
    def queue_text(self, text, text_type="story"):
        self.text_queue.append((text, text_type))

    def play_scene(self, a=None, b=None, ca=None, cb=None, d=0, df=None):
        dur = d * self.settings["timer_difficulty"]
        self.pending = {"a": a, "b": b, "ca": ca, "cb": cb, "d": dur, "df": df}
        self.process_queue()

    def process_queue(self):
        if not hasattr(self, 'story_text'): return
        if not self.text_queue:
            self.show_controls()
            return
        t, ty = self.text_queue.pop(0)
        self.type_char(t, ty, 0)

    def type_char(self, text, text_type, i):
        if not hasattr(self, 'story_text'): return
        if i < len(text):
            try:
                self.story_text.config(state=tk.NORMAL)
                self.story_text.insert(tk.END, text[i], text_type)
                self.story_text.config(state=tk.DISABLED)
                self.story_text.see(tk.END)
                
                base_speed = self.settings["text_speed"]
                jitter = random.randint(int(base_speed * 0.7), int(base_speed * 1.3))
                self.root.after(jitter, self.type_char, text, text_type, i + 1)
            except: pass
        else:
            try:
                self.story_text.config(state=tk.NORMAL)
                self.story_text.insert(tk.END, "\n\n")
                self.story_text.config(state=tk.DISABLED)
                self.root.after(1000, self.process_queue) 
            except: pass

    def show_controls(self):
        p = self.pending
        if p["a"]:
            self.timer_canvas.pack(fill=tk.X, pady=5)
            self.btn_a.config(text=p["a"], command=lambda: self.make_choice(p["ca"]))
            self.btn_b.config(text=p["b"], command=lambda: self.make_choice(p["cb"]))
            self.btn_a.pack(fill=tk.X, pady=5)
            self.btn_b.pack(fill=tk.X, pady=5)
            self.start_timer(p["d"], p["df"])
        else:
            self.btn_continue.pack(fill=tk.X, side=tk.BOTTOM)
            self.btn_continue.bind("<Button-1>", lambda e: self.make_choice(p["df"]))
            self.flash_continue()

    def flash_continue(self):
        if not hasattr(self, 'btn_continue') or not self.btn_continue.winfo_viewable(): return
        color = "#ffffff" if self.flash_state else "#444444"
        self.btn_continue.config(fg=color)
        self.flash_state = not self.flash_state
        self.root.after(600, self.flash_continue)

    def start_timer(self, duration, callback):
        self.total_time = duration
        self.time_left = duration
        self.timer_callback = callback
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if not self.timer_running: return
        if self.time_left <= 0:
            self.make_choice(self.timer_callback)
            return
        try:
            w = self.timer_canvas.winfo_width()
            nw = (self.time_left / self.total_time) * w
            self.timer_canvas.coords(self.timer_bar, 0, 0, nw, 15)
            self.time_left -= 0.05
            self.root.after(50, self.update_timer)
        except: self.timer_running = False

    def make_choice(self, cmd):
        self.timer_running = False
        try:
            self.btn_a.pack_forget()
            self.btn_b.pack_forget()
            self.btn_continue.pack_forget()
            self.timer_canvas.pack_forget()
            self.story_text.config(state=tk.NORMAL)
            self.story_text.delete("1.0", tk.END)
            self.story_text.config(state=tk.DISABLED)
            cmd()
        except: pass

    # =====================================================================
    # 🚨 CHAPTER 1 STORY BRANCHES 🚨
    # =====================================================================

    def start_chapter_1(self):
        self.setup_game_screen()
        self.root.after(1000, self.c1_s1)

    def c1_s1(self):
        self.queue_text("I wake up at 6:45 AM with my heart hammering against my ribs. I'm fifteen minutes late for work. My brain is foggy from whatever happened last night, and my bare feet hit the cold floor.")
        self.play_scene(
            a="Rush out of bed", 
            b="Pause for moment", 
            ca=self.c1_s1_rush, 
            cb=self.c1_s1_pause, 
            d=7, 
            df=self.c1_s1_freeze
        )

    def c1_s1_rush(self):
        self.mark_state = "High Confusion"
        self.queue_text("I shove the blankets off, ignore the alarm, and rush straight downstairs as fast as I can.")
        self.play_scene(df=self.c1_s2)

    def c1_s1_pause(self):
        self.mark_state = "Calm/Mild Confusion"
        self.queue_text("I sit on the bed for a few moments, reach over to switch off the alarm, and walk downstairs slowly.")
        self.play_scene(df=self.c1_s2)

    def c1_s1_freeze(self):
        self.mark_state = "Disassociated"
        self.queue_text("I just sit there on the edge of the bed staring at the wall until Anna calls out to me.")
        self.play_scene(df=self.c1_s2)

    def c1_s2(self):
        self.queue_text("I hop downstairs. The first thing I see is Anna, my lady from heaven, in the kitchen preparing breakfast. She looks up at me while the pan is sizzling with eggs.")
        self.queue_text("'Good morning!' she says, her eyes widening.")
        self.queue_text("'Morning... uhm, why didn't you wake me up?' I ask.")
        self.queue_text("She looks back at the sizzling pan. 'I didn't wanna disturb your peaceful sleep, plus I wanted you to wake up on your own without me nagging you every morning,' she responds.")
        self.queue_text("We've been married for 4 months, but it feels like forever ago.")
        self.queue_text("'Go upstairs and prepare yourself while I keep on making food, We've got a long day ahead of us,' she adds.")
        self.queue_text("Marrying Anna was a dream, and it still is. I look back on our wedding pictures every night before I sleep, from the day she said I do, wedding bells and a white dress. A surreal day that lingers in my memory. Her smile, her eyes, her hair. She looked like a princess pulled out of a Disney movie.")
        self.play_scene(df=self.c1_s3)

    def c1_s3(self):
        self.queue_text("After breakfast, we went to work. A year ago, before we got married, she had an idea of her own company that helped people move stuff. I helped her create it, then a few months later, 'SOUTH MOVERS' was created. We had two friends who joined into the company; Leo and Sarah. Leo was the truck driver, Sarah handled most of our finances, Anna was the manager, CEO—she basically handles everything, and I help load the items on and off. We deliver the deliveries together to ensure a good review. Our workshop is small but it gets the job done.")
        self.queue_text("When we get to the workshop, Leo is already loading the items onto the back of the truck.")
        self.queue_text("'Mark, can you get a move on and help me with this?' Leo says.")
        self.queue_text("We step up and start lifting the heavy wardrobe into the truck.")
        self.queue_text("'Well, you guys are late, care to explain what happened?' Leo adds as he huffs with his hands on his hips.")
        self.queue_text("'Well, you better ask Mr. sleepy head over here, he just chose to over sleep on an important day,' Anna responds while gazing at me.")
        self.queue_text("'Well lucky for you guys the hard part is already done, we're moving out in few minutes,' Sarah says.")
        self.queue_text("Sarah is the type of person to wake up two hours earlier in the morning for a delivery that's supposed to be done in the afternoon. She's basically a crackhead at doing work fast.")
        self.queue_text("'How long is the drive?' Anna asks.")
        self.queue_text("'Six hours, give or take. But we might cut it to four if we take Leo's short route that he keeps on talking about,' Sarah responds.")
        self.queue_text("'What? It's either we go six hours or take away two which will save us the journey, you pick,' Leo says as he leans his hands on the desk near him.")
        self.queue_text("'Fine, we'll take your scenic route, but only if you are driving,' Anna responds while spinning the keys around her fingers.")
        self.queue_text("'Fine by me,' Leo responds.")
        self.play_scene(df=self.c1_s4)

    def c1_s4(self):
        self.queue_text("Our customer is moving to a different city far away from New Mexico, so this delivery is gonna be a long one. We drive off, the road is long. We find a gas station on the way and steam off for a few minutes then drive off again. Sarah is on her phone while Anna looks out the window with the sun beaming on her face, and her hair blowing in the wind. She looks magical.")
        self.queue_text("'Hey, how long are you gonna keep drooling over your wife man, you look like you just met her,' Leo whispers to me.")
        self.play_scene(
            a="whisper back", 
            b="joke about it", 
            ca=self.c1_s4_sincere, 
            cb=self.c1_s4_deflect, 
            d=8, 
            df=self.c1_s4_silent
        )

    def c1_s4_sincere(self):
        self.leo_friendship += 1
        self.romance_bond += 1
        self.queue_text("I whisper back, 'I just can't get over the fact that I'm married to her, I never imagined me being a married man.'")
        self.queue_text("Leo smiles. 'Well get used to it man because you guys are gonna live out till 80,' he whispers.")
        self.play_scene(df=self.chapter_end)

    def c1_s4_deflect(self):
        self.queue_text("I chuckle and whisper back, 'Just making sure she doesn't fire us for being late this morning. Keep your eyes on the road.'")
        self.queue_text("Leo smirks and shakes his head, focusing back on the highway.")
        self.play_scene(df=self.chapter_end)

    def c1_s4_silent(self):
        self.romance_bond += 1
        self.queue_text("I just smile softly and don't say anything, keeping my gaze on Anna.")
        self.queue_text("Leo rolls his eyes playfully and mutters, 'Hopeless,' before turning up the radio.")
        self.play_scene(df=self.chapter_end)

    def chapter_end(self):
        self.unlocked_chapters = 2
        self.queue_text("END OF CHAPTER 1", "system")
        self.play_scene(df=self.build_main_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = Exit47MainMenu(root)
    root.mainloop()
