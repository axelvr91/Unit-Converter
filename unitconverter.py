import customtkinter as ctk

# Configuración global del tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Base por defecto

class UnitConverterFuturistic(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("NEON CONVERTER v1.0")
        self.geometry("500x550")
        self.configure(fg_color="#0D0E15")  # Fondo oscuro futurista
        self.resizable(False, False)

        # Título Principal (Rosa Neón)
        self.title_label = ctk.CTkLabel(
            self, 
            text="SYSTEM UNIT CONVERTER", 
            font=ctk.CTkFont(family="Courier New", size=24, weight="bold"),
            text_color="#FF007F"
        )
        self.title_label.pack(pady=20)

        # Entrada de Valor (Azul Eléctrico)
        self.value_label = ctk.CTkLabel(
            self, text="ENTER VALUE TO CONVERT:", 
            font=ctk.CTkFont(family="Courier New", size=12),
            text_color="#00E5FF"
        )
        self.value_label.pack(pady=5)
        
        self.entry_value = ctk.CTkEntry(
            self, 
            placeholder_text="0.00",
            width=200,
            font=ctk.CTkFont(family="Courier New", size=16),
            border_color="#00E5FF",
            fg_color="#1A1C28",
            text_color="#FFFFFF"
        )
        self.entry_value.pack(pady=10)

        # Contenedor de Pestañas (Modos de conversión)
        self.tabview = ctk.CTkTabview(
            self, 
            width=400, 
            height=180,
            fg_color="#1A1C28",
            segmented_button_selected_color="#FF007F",
            segmented_button_selected_hover_color="#00E5FF",
            segmented_button_unselected_color="#0D0E15"
        )
        self.tabview.pack(pady=15)
        
        self.tab_length = self.tabview.add("LENGTH")
        self.tab_weight = self.tabview.add("WEIGHT")

        self.setup_length_tab()
        self.setup_weight_tab()

        # Botón de Acción (Azul Eléctrico)
        self.btn_convert = ctk.CTkButton(
            self, 
            text="EXECUTE CONVERSION", 
            command=self.process_conversion,
            font=ctk.CTkFont(family="Courier New", size=14, weight="bold"),
            fg_color="#00E5FF",
            text_color="#000000",
            hover_color="#00FF66"
        )
        self.btn_convert.pack(pady=20)

        # Pantalla de Resultados (Verde / Amarillo Neón)
        self.result_frame = ctk.CTkFrame(self, width=400, height=80, fg_color="#0D0E15", border_color="#00FF66", border_width=1)
        self.result_frame.pack(pady=10)
        self.result_frame.pack_propagate(False)

        self.result_label = ctk.CTkLabel(
            self.result_frame, 
            text="AWAITING SYSTEM INPUT...", 
            font=ctk.CTkFont(family="Courier New", size=14),
            text_color="#ECEB4B" # Amarillo para estado de espera
        )
        self.result_label.pack(expand=True)

    def setup_length_tab(self):
        self.length_option = ctk.StringVar(value="m_to_ft")
        
        rb1 = ctk.CTkRadioButton(
            self.tab_length, text="Meters to Feet", variable=self.length_option, value="m_to_ft",
            text_color="#FFFFFF", border_color="#FF007F", hover_color="#00FF66"
        )
        rb1.pack(pady=15, anchor="w", padx=40)
        
        rb2 = ctk.CTkRadioButton(
            self.tab_length, text="Feet to Meters", variable=self.length_option, value="ft_to_m",
            text_color="#FFFFFF", border_color="#FF007F", hover_color="#00FF66"
        )
        rb2.pack(pady=15, anchor="w", padx=40)

    def setup_weight_tab(self):
        self.weight_option = ctk.StringVar(value="kg_to_lb")
        
        rb1 = ctk.CTkRadioButton(
            self.tab_weight, text="Kilograms to Pounds", variable=self.weight_option, value="kg_to_lb",
            text_color="#FFFFFF", border_color="#FF007F", hover_color="#00FF66"
        )
        rb1.pack(pady=15, anchor="w", padx=40)
        
        rb2 = ctk.CTkRadioButton(
            self.tab_weight, text="Pounds to Kilograms", variable=self.weight_option, value="lb_to_kg",
            text_color="#FFFFFF", border_color="#FF007F", hover_color="#00FF66"
        )
        rb2.pack(pady=15, anchor="w", padx=40)

    def process_conversion(self):
        # Validación de entrada
        try:
            value = float(self.entry_value.get())
        except ValueError:
            self.result_label.configure(text="ERROR: INVALID NUMERIC VALUE", text_color="#FF007F")
            return

        current_tab = self.tabview.get()
        
        if current_tab == "LENGTH":
            mode = self.length_option.get()
            if mode == "m_to_ft":
                res = value * 3.28084
                self.result_label.configure(text=f"{value} m = {res:.4f} ft", text_color="#00FF66")
            else:
                res = value / 3.28084
                self.result_label.configure(text=f"{value} ft = {res:.4f} m", text_color="#00FF66")
                
        elif current_tab == "WEIGHT":
            mode = self.weight_option.get()
            if mode == "kg_to_lb":
                res = value * 2.20462
                self.result_label.configure(text=f"{value} kg = {res:.4f} lbs", text_color="#00FF66")
            else:
                res = value / 2.20462
                self.result_label.configure(text=f"{value} lbs = {res:.4f} kg", text_color="#00FF66")

if __name__ == "__main__":
    app = UnitConverterFuturistic()
    app.mainloop()