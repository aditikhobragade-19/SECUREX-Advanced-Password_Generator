import customtkinter as ctk
import secrets
import string
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SecureX(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SECUREX | Digital Security")
        self.geometry("900x780")
        self.minsize(760, 700)
        self.configure(fg_color="#090E1D")

        self.password = ""
        self.password_history = []
        self.visible = False

        self.show_welcome()

    # WELCOME PAGE
    def show_welcome(self):

        self.welcome_frame = ctk.CTkFrame(
            self,
            fg_color="#090E1D",
            corner_radius=0
        )
        self.welcome_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.welcome_frame,
            text="✦",
            font=("Arial", 55, "bold"),
            text_color="#A78BFA"
        ).pack(pady=(75, 5))

        ctk.CTkLabel(
            self.welcome_frame,
            text="SECUREX",
            font=("Arial", 55, "bold"),
            text_color="#A78BFA"
        ).pack(pady=5)

        ctk.CTkLabel(
            self.welcome_frame,
            text="ADVANCED PASSWORD GENERATOR",
            font=("Arial", 14, "bold"),
            text_color="#94A3B8"
        ).pack(pady=5)

        # Welcome Card
        card = ctk.CTkFrame(
            self.welcome_frame,
            fg_color="#151D32",
            corner_radius=25,
            border_width=1,
            border_color="#51418B",
            width=600,
            height=290
        )
        card.pack(padx=30, pady=35)
        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text="🛡️",
            font=("Arial", 65)
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            card,
            text="Welcome to SECUREX",
            font=("Arial", 27, "bold"),
            text_color="#F8FAFC"
        ).pack(pady=8)

        ctk.CTkLabel(
            card,
            text="Your Security, Our Priority.",
            font=("Arial", 16),
            text_color="#A78BFA"
        ).pack(pady=5)

        ctk.CTkLabel(
            card,
            text="Generate strong and secure passwords\n"
                 "to protect your digital world.",
            font=("Arial", 14),
            text_color="#94A3B8",
            justify="center"
        ).pack(pady=12)

        ctk.CTkButton(
            card,
            text="GET STARTED  →",
            command=self.open_generator,
            height=48,
            width=240,
            corner_radius=12,
            font=("Arial", 15, "bold"),
            fg_color="#7C3AED",
            hover_color="#6D28D9"
        ).pack(pady=15)

        ctk.CTkLabel(
            self.welcome_frame,
            text="POWERED BY SMART SECURITY",
            font=("Arial", 11, "bold"),
            text_color="#64748B"
        ).pack(pady=5)

        ctk.CTkLabel(
            self.welcome_frame,
            text="Created by Aditi Khobragade",
            font=("Arial", 12),
            text_color="#94A3B8"
        ).pack(pady=12)

    # OPEN GENERATOR
    def open_generator(self):

        self.welcome_frame.destroy()
        self.build_generator()

    # GENERATOR PAGE
    def build_generator(self):

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(
            self,
            text="← BACK TO HOME",
            command=self.back_home,
            width=150,
            height=32,
            fg_color="#26334D",
            hover_color="#475569"
        ).grid(row=0, column=0, pady=(15, 5))

        ctk.CTkLabel(
            self,
            text="✦ SECUREX",
            font=("Arial", 34, "bold"),
            text_color="#A78BFA"
        ).grid(row=1, column=0, pady=5)

        ctk.CTkLabel(
            self,
            text="ADVANCED PASSWORD GENERATOR",
            font=("Arial", 12, "bold"),
            text_color="#94A3B8"
        ).grid(row=2, column=0, pady=3)

        card = ctk.CTkFrame(
            self,
            fg_color="#151D32",
            corner_radius=22,
            border_width=1,
            border_color="#37305E"
        )
        card.grid(
            row=3, column=0,
            padx=35, pady=15,
            sticky="ew"
        )
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            card,
            text="CREATE YOUR PASSWORD",
            font=("Arial", 18, "bold"),
            text_color="#E2E8F0"
        ).grid(row=0, column=0, pady=(20, 12))

        self.password_var = tk.StringVar()

        self.password_entry = ctk.CTkEntry(
            card,
            textvariable=self.password_var,
            height=50,
            font=("Consolas", 16),
            justify="center",
            fg_color="#090E1D",
            border_color="#8B5CF6",
            placeholder_text="Your password will appear here"
        )
        self.password_entry.grid(
            row=1, column=0,
            padx=25, pady=8, sticky="ew"
        )

        self.show_button = ctk.CTkButton(
            card,
            text="SHOW PASSWORD",
            command=self.toggle_visibility,
            width=160,
            height=32,
            fg_color="#334155",
            hover_color="#475569"
        )
        self.show_button.grid(row=2, column=0, pady=5)

        ctk.CTkButton(
            card,
            text="COPY PASSWORD",
            command=self.copy_password,
            height=36,
            width=190,
            fg_color="#334155",
            hover_color="#475569"
        ).grid(row=3, column=0, pady=6)

        ctk.CTkLabel(
            card,
            text="PASSWORD LENGTH",
            font=("Arial", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=4, column=0, pady=(12, 4))

        self.length_value = ctk.IntVar(value=16)

        self.length_label = ctk.CTkLabel(
            card,
            text="16 Characters",
            font=("Arial", 14, "bold"),
            text_color="#A78BFA"
        )
        self.length_label.grid(row=5, column=0)

        ctk.CTkSlider(
            card,
            from_=4,
            to=64,
            number_of_steps=60,
            variable=self.length_value,
            command=self.update_length,
            progress_color="#8B5CF6",
            button_color="#A78BFA",
            button_hover_color="#C4B5FD",
            width=430
        ).grid(row=6, column=0, pady=8)

        ctk.CTkLabel(
            card,
            text="CUSTOMIZE YOUR PASSWORD",
            font=("Arial", 13, "bold"),
            text_color="#CBD5E1"
        ).grid(row=7, column=0, pady=(12, 8))

        options = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        options.grid(row=8, column=0, pady=4)

        self.upper_var = ctk.BooleanVar(value=True)
        self.lower_var = ctk.BooleanVar(value=True)
        self.number_var = ctk.BooleanVar(value=True)
        self.symbol_var = ctk.BooleanVar(value=True)

        option_list = [
            ("Uppercase A-Z", self.upper_var),
            ("Lowercase a-z", self.lower_var),
            ("Numbers 0-9", self.number_var),
            ("Symbols @#$", self.symbol_var)
        ]

        for i, (label, variable) in enumerate(option_list):
            ctk.CTkCheckBox(
                options,
                text=label,
                variable=variable,
                font=("Arial", 12),
                fg_color="#8B5CF6",
                hover_color="#A78BFA"
            ).grid(
                row=i // 2,
                column=i % 2,
                padx=15, pady=8,
                sticky="w"
            )

        self.strength_label = ctk.CTkLabel(
            card,
            text="STRENGTH: NOT GENERATED",
            font=("Arial", 12, "bold"),
            text_color="#94A3B8"
        )
        self.strength_label.grid(
            row=9, column=0, pady=(15, 5)
        )

        self.strength_bar = ctk.CTkProgressBar(
            card,
            width=350,
            progress_color="#22C55E"
        )
        self.strength_bar.grid(row=10, column=0, pady=5)
        self.strength_bar.set(0)

        ctk.CTkButton(
            card,
            text="✦ GENERATE PASSWORD",
            command=self.generate_password,
            height=46,
            font=("Arial", 15, "bold"),
            fg_color="#7C3AED",
            hover_color="#6D28D9"
        ).grid(
            row=11, column=0,
            padx=30, pady=(18, 7),
            sticky="ew"
        )

        ctk.CTkButton(
            card,
            text="↻ REGENERATE",
            command=self.generate_password,
            height=36,
            fg_color="#26334D",
            hover_color="#475569"
        ).grid(
            row=12, column=0,
            padx=30, pady=(4, 12),
            sticky="ew"
        )

        history_frame = ctk.CTkFrame(
            self,
            fg_color="#151D32",
            corner_radius=15
        )
        history_frame.grid(
            row=4, column=0,
            padx=35, pady=10,
            sticky="ew"
        )
        history_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            history_frame,
            text="RECENT GENERATIONS",
            font=("Arial", 13, "bold"),
            text_color="#A78BFA"
        ).grid(
            row=0, column=0,
            padx=15, pady=10, sticky="w"
        )

        self.history_label = ctk.CTkLabel(
            history_frame,
            text="No passwords generated yet.",
            font=("Arial", 11),
            text_color="#94A3B8",
            justify="left"
        )
        self.history_label.grid(
            row=1, column=0,
            padx=15, pady=5, sticky="w"
        )

        ctk.CTkButton(
            history_frame,
            text="CLEAR HISTORY",
            command=self.clear_history,
            width=120,
            height=30,
            fg_color="#7F1D1D",
            hover_color="#991B1B"
        ).grid(
            row=2, column=0,
            padx=15, pady=10, sticky="e"
        )

        ctk.CTkLabel(
            self,
            text="SECUREX | Created by Aditi Khobragade",
            font=("Arial", 11),
            text_color="#64748B"
        ).grid(row=5, column=0, pady=8)

    def back_home(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.show_welcome()

    def update_length(self, value):
        length = int(float(value))
        self.length_label.configure(
            text=f"{length} Characters"
        )

    def toggle_visibility(self):

        self.visible = not self.visible

        self.password_entry.configure(
            show="" if self.visible else "•"
        )

        self.show_button.configure(
            text="HIDE PASSWORD" if self.visible
            else "SHOW PASSWORD"
        )

    def generate_password(self):

        characters = ""
        required = []

        if self.upper_var.get():
            chars = string.ascii_uppercase
            characters += chars
            required.append(secrets.choice(chars))

        if self.lower_var.get():
            chars = string.ascii_lowercase
            characters += chars
            required.append(secrets.choice(chars))

        if self.number_var.get():
            chars = string.digits
            characters += chars
            required.append(secrets.choice(chars))

        if self.symbol_var.get():
            chars = "!@#$%^&*()-_=+?"
            characters += chars
            required.append(secrets.choice(chars))

        if not characters:
            messagebox.showwarning(
                "SECUREX",
                "Select at least one character type."
            )
            return

        length = int(self.length_value.get())

        if length < len(required):
            messagebox.showwarning(
                "SECUREX",
                "Increase password length."
            )
            return

        remaining = [
            secrets.choice(characters)
            for _ in range(length - len(required))
        ]

        password_list = required + remaining
        secrets.SystemRandom().shuffle(password_list)

        self.password = "".join(password_list)
        self.password_var.set(self.password)

        self.visible = True
        self.password_entry.configure(show="")
        self.show_button.configure(text="HIDE PASSWORD")

        self.update_strength(self.password)

        self.password_history.insert(
            0,
            tk._default_root.tk.call(
                "clock", "format",
                tk._default_root.tk.call("clock", "seconds"),
                "-format", "%H:%M:%S"
            )
        )

        self.password_history = self.password_history[:5]

        self.history_label.configure(
            text="\n".join(
                f"{i + 1}. Password generated at {time}"
                for i, time in enumerate(self.password_history)
            )
        )

    def copy_password(self):

        if not self.password:
            messagebox.showinfo(
                "SECUREX",
                "Generate a password first."
            )
            return

        self.clipboard_clear()
        self.clipboard_append(self.password)

        messagebox.showinfo(
            "SECUREX",
            "Password copied successfully!"
        )

    def clear_history(self):

        self.password_history.clear()

        self.history_label.configure(
            text="No passwords generated yet."
        )

    def update_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            label, color = "WEAK", "#EF4444"
        elif score <= 4:
            label, color = "MEDIUM", "#F59E0B"
        else:
            label, color = "STRONG", "#22C55E"

        self.strength_label.configure(
            text=f"STRENGTH: {label}",
            text_color=color
        )

        self.strength_bar.configure(
            progress_color=color
        )
        self.strength_bar.set(score / 6)


if __name__ == "__main__":
    app = SecureX()
    app.mainloop()