#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMR Cable Generator Tools
Converted from Figma design to Python tkinter
"""

import tkinter as tk
from tkinter import ttk
import math

# Windows taskbar icon support
try:
    from ctypes import windll
    myappid = 'emr.cablegenerator.tools.1.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass


class ModernButton(tk.Canvas):
    """Custom button widget with modern styling"""
    def __init__(self, parent, text, command, bg_color, hover_color, **kwargs):
        super().__init__(parent, highlightthickness=0, **kwargs)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.command = command
        self.text = text
        
        self.configure(bg=bg_color, height=35)
        self.text_id = self.create_text(
            0, 0, text=text, fill='white', 
            font=('Segoe UI', 9, 'bold'), anchor='center'
        )
        
        self.bind('<Button-1>', lambda e: command())
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<Configure>', self._on_configure)
    
    def _on_configure(self, event):
        self.coords(self.text_id, event.width // 2, event.height // 2)
    
    def _on_enter(self, event):
        self.configure(bg=self.hover_color)
    
    def _on_leave(self, event):
        self.configure(bg=self.bg_color)


class CableGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EMR Cable Generator Tools")
        self.root.geometry("1000x750")
        self.root.resizable(False, False)
        
        # Set window icon
        try:
            self.root.iconbitmap('app.ico')
        except:
            pass
        
        # Center window on screen
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1000
        window_height = 750
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Figma Color Palette
        self.colors = {
            'bg_main': '#2d3e50',
            'bg_section': '#3a4f63',
            'bg_input': '#4a5f73',
            'border': '#5a6f83',
            'title_bar': '#0066cc',
            'title_bar_hover': '#0052a3',
            'output_bg': '#1a2f1a',
            'output_border': '#2d4a2d',
            'output_text': '#4ade80',
            'text_primary': '#ffffff',
            'text_secondary': '#d1d5db',
            'text_label': '#9ca3af',
            'button_blue': '#0066cc',
            'button_blue_hover': '#0052a3',
            'button_gray': '#4a5f73',
            'button_gray_hover': '#5a6f83',
            'button_green': '#28a745',
            'button_green_hover': '#218838',
            'gradient_start': '#3a4f63',
            'gradient_end': '#2d3e50',
        }
        
        self.root.configure(bg=self.colors['bg_main'])
        
        # Main container
        main_container = tk.Frame(root, bg=self.colors['bg_main'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Header (no title bar)
        header = tk.Frame(main_container, bg=self.colors['gradient_start'], height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title_label = tk.Label(header, text="EMR Cable Generator Tools",
                              bg=self.colors['gradient_start'], fg=self.colors['text_primary'],
                              font=('Segoe UI', 18, 'bold'))
        title_label.pack(expand=True)
        
        # Tab Navigation
        tab_frame = tk.Frame(main_container, bg=self.colors['bg_main'])
        tab_frame.pack(fill=tk.X, padx=16, pady=(16, 0))
        
        # Center container for tabs
        tab_center = tk.Frame(tab_frame, bg=self.colors['bg_main'])
        tab_center.pack(expand=True)
        
        self.active_tab = 'cable'
        self.tab_buttons = {}
        
        tabs = [
            ('cable', 'Cable Generator'),
            ('ci', 'Cluster Description Generator'),
            ('feeder', 'Feeder Description Generator')
        ]
        
        for tab_id, tab_name in tabs:
            btn = tk.Label(tab_center, text=tab_name, 
                          font=('Segoe UI', 9),
                          padx=24, pady=8, cursor='hand2')
            btn.pack(side=tk.LEFT, padx=(0, 8))
            btn.bind('<Button-1>', lambda e, t=tab_id: self.switch_tab(t))
            self.tab_buttons[tab_id] = btn
        
        # Content area
        self.content_frame = tk.Frame(main_container, bg=self.colors['bg_main'])
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=16)
        
        # Create all tab panels
        self.panels = {}
        self.panels['cable'] = self.create_cable_panel()
        self.panels['ci'] = self.create_ci_panel()
        self.panels['feeder'] = self.create_feeder_panel()
        
        # Show initial tab
        self.switch_tab('cable')
    
    def create_title_bar(self, parent):
        """Create custom title bar"""
        title_bar = tk.Frame(parent, bg=self.colors['title_bar'], height=32)
        title_bar.pack(fill=tk.X)
        title_bar.pack_propagate(False)
        
        # Icon and title
        left_frame = tk.Frame(title_bar, bg=self.colors['title_bar'])
        left_frame.pack(side=tk.LEFT, padx=12, pady=6)
        
        icon_box = tk.Frame(left_frame, bg='#4d7fbf', width=16, height=16)
        icon_box.pack(side=tk.LEFT, padx=(0, 8))
        
        tk.Label(left_frame, text="EMR Cable Generator Tools",
                bg=self.colors['title_bar'], fg='white',
                font=('Segoe UI', 9)).pack(side=tk.LEFT)
        
        # Window controls (minimize, maximize, close)
        controls = tk.Frame(title_bar, bg=self.colors['title_bar'])
        controls.pack(side=tk.RIGHT, padx=4, pady=4)
        
        for symbol in ['−', '□', '×']:
            btn = tk.Label(controls, text=symbol, bg=self.colors['title_bar'],
                          fg='white', width=3, height=1, font=('Segoe UI', 10))
            btn.pack(side=tk.LEFT, padx=1)
            if symbol == '×':
                btn.bind('<Button-1>', lambda e: self.root.quit())
                btn.bind('<Enter>', lambda e: e.widget.configure(bg='#dc3545'))
                btn.bind('<Leave>', lambda e: e.widget.configure(bg=self.colors['title_bar']))
            else:
                btn.bind('<Enter>', lambda e: e.widget.configure(bg=self.colors['title_bar_hover']))
                btn.bind('<Leave>', lambda e: e.widget.configure(bg=self.colors['title_bar']))
    
    def switch_tab(self, tab_id):
        """Switch between tabs"""
        self.active_tab = tab_id
        
        # Update tab button styles
        for tid, btn in self.tab_buttons.items():
            if tid == tab_id:
                btn.configure(bg=self.colors['button_blue'], fg='white')
            else:
                btn.configure(bg=self.colors['bg_section'], fg=self.colors['text_secondary'])
        
        # Show/hide panels
        for pid, panel in self.panels.items():
            if pid == tab_id:
                panel.pack(fill=tk.BOTH, expand=True)
            else:
                panel.pack_forget()
    
    def create_input_section(self, parent, title="Input Parameters"):
        """Create styled input section"""
        section = tk.Frame(parent, bg=self.colors['bg_section'], 
                          highlightbackground=self.colors['border'],
                          highlightthickness=1)
        section.pack(fill=tk.BOTH, expand=True, padx=(0, 12))
        
        # Header
        header = tk.Label(section, text=title, bg=self.colors['bg_section'],
                         fg=self.colors['text_primary'], font=('Segoe UI', 9),
                         anchor='w')
        header.pack(fill=tk.X, padx=16, pady=(12, 8))
        
        separator = tk.Frame(section, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, padx=16, pady=(0, 12))
        
        # Input container
        input_container = tk.Frame(section, bg=self.colors['bg_section'])
        input_container.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 32))
        
        return input_container
    
    def create_output_section(self, parent):
        """Create styled output section"""
        section = tk.Frame(parent, bg=self.colors['bg_section'],
                          highlightbackground=self.colors['border'],
                          highlightthickness=1)
        section.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = tk.Label(section, text="Result Output", bg=self.colors['bg_section'],
                         fg=self.colors['text_primary'], font=('Segoe UI', 9),
                         anchor='w')
        header.pack(fill=tk.X, padx=16, pady=(12, 8))
        
        separator = tk.Frame(section, bg=self.colors['border'], height=1)
        separator.pack(fill=tk.X, padx=16, pady=(0, 12))
        
        # Output text
        output_text = tk.Text(section, bg=self.colors['output_bg'],
                             fg=self.colors['output_text'],
                             font=('Consolas', 9),
                             highlightbackground=self.colors['output_border'],
                             highlightthickness=1,
                             relief=tk.FLAT,
                             padx=16, pady=16,
                             wrap=tk.WORD,
                             state='disabled')
        output_text.pack(fill=tk.BOTH, expand=True, padx=16, pady=(0, 60))
        
        return output_text
    
    def create_input_field(self, parent, label_text, row):
        """Create styled input field"""
        label = tk.Label(parent, text=label_text, bg=self.colors['bg_section'],
                        fg=self.colors['text_primary'], font=('Segoe UI', 9),
                        anchor='w')
        label.grid(row=row, column=0, sticky='w', pady=(0, 12))
        
        entry = tk.Entry(parent, bg=self.colors['bg_input'],
                        fg=self.colors['text_primary'],
                        font=('Segoe UI', 9),
                        relief=tk.FLAT,
                        highlightbackground=self.colors['border'],
                        highlightthickness=1,
                        insertbackground=self.colors['text_primary'])
        entry.grid(row=row+1, column=0, sticky='ew', pady=(0, 12), ipady=6)
        
        return entry
    
    def create_cable_panel(self):
        """Cable Generator Panel"""
        panel = tk.Frame(self.content_frame, bg=self.colors['bg_main'])
        
        # Two column layout
        left_col = tk.Frame(panel, bg=self.colors['bg_main'])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        right_col = tk.Frame(panel, bg=self.colors['bg_main'])
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12, 0))
        
        # Input section
        input_container = self.create_input_section(left_col)
        input_container.grid_columnconfigure(0, weight=1)
        
        # Cable Category
        category_label = tk.Label(input_container, text="Cable Category:",
                                 bg=self.colors['bg_section'],
                                 fg=self.colors['text_label'],
                                 font=('Segoe UI', 9), anchor='w')
        category_label.grid(row=0, column=0, sticky='w', pady=(0, 8))
        
        category_frame = tk.Frame(input_container, bg=self.colors['bg_section'])
        category_frame.grid(row=1, column=0, sticky='ew', pady=(0, 12))
        
        self.cable_category = tk.StringVar(value='cluster')
        self.category_buttons = {}
        
        for value, text in [('cluster', 'Cluster Cable'), ('feeder', 'Feeder Cable')]:
            btn = tk.Label(category_frame, text=text,
                          font=('Segoe UI', 9),
                          cursor='hand2',
                          padx=16, pady=8)
            btn.pack(side=tk.LEFT, padx=(0, 8), fill=tk.X, expand=True)
            btn.bind('<Button-1>', lambda e, v=value: self.select_cable_category(v))
            self.category_buttons[value] = btn
        
        # Dynamic input fields
        self.cable_inputs_frame = tk.Frame(input_container, bg=self.colors['bg_section'])
        self.cable_inputs_frame.grid(row=2, column=0, sticky='ew')
        self.cable_inputs_frame.grid_columnconfigure(0, weight=1)
        
        self.cable_entries = {}
        
        # Initialize with cluster category
        self.select_cable_category('cluster')
        
        # Buttons
        btn_frame = tk.Frame(left_col, bg=self.colors['bg_main'])
        btn_frame.pack(fill=tk.X, pady=(24, 0))
        
        ModernButton(btn_frame, "GENERATE", self.generate_cable,
                    self.colors['button_blue'], self.colors['button_blue_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        
        ModernButton(btn_frame, "RESET", self.reset_cable,
                    self.colors['button_gray'], self.colors['button_gray_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=6)
        
        ModernButton(btn_frame, "COPY", lambda: self.copy_result(self.cable_output),
                    self.colors['button_green'], self.colors['button_green_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))
        
        # Output section
        self.cable_output = self.create_output_section(right_col)
        
        return panel
    
    def select_cable_category(self, category):
        """Select cable category and update button colors"""
        self.cable_category.set(category)
        
        # Update button colors
        for cat, btn in self.category_buttons.items():
            if cat == category:
                btn.configure(bg=self.colors['button_green'], fg='white')
            else:
                btn.configure(bg=self.colors['bg_input'], fg=self.colors['text_secondary'])
        
        self.update_cable_fields()
    
    def update_cable_fields(self):
        """Update cable input fields based on category"""
        for widget in self.cable_inputs_frame.winfo_children():
            widget.destroy()
        
        self.cable_entries.clear()
        category = self.cable_category.get()
        
        row = 0
        
        if category == 'feeder':
            self.cable_entries['olt'] = self.create_input_field(
                self.cable_inputs_frame, "OLT Code:", row)
            row += 2
        
        self.cable_entries['fdt'] = self.create_input_field(
            self.cable_inputs_frame, "FDT Code:", row)
        row += 2
        
        if category == 'cluster':
            self.cable_entries['line'] = self.create_input_field(
                self.cable_inputs_frame, "Line Code:", row)
            row += 2
        
        # Feeder Type dropdown (only for feeder)
        if category == 'feeder':
            label = tk.Label(self.cable_inputs_frame, text="Feeder Type:",
                            bg=self.colors['bg_section'],
                            fg=self.colors['text_label'],
                            font=('Segoe UI', 9), anchor='w')
            label.grid(row=row, column=0, sticky='w', pady=(0, 12))
            
            feeder_types = ['SUBFEEDER', 'HUBFEEDER', 'MAINFEEDER']
            self.feeder_type_var = tk.StringVar(value=feeder_types[0])
            
            combo_feeder = ttk.Combobox(self.cable_inputs_frame, textvariable=self.feeder_type_var,
                                values=feeder_types, state='readonly', font=('Segoe UI', 9))
            combo_feeder.grid(row=row+1, column=0, sticky='ew', pady=(0, 12), ipady=4)
            row += 2
        
        # Cable Type dropdown
        label = tk.Label(self.cable_inputs_frame, text="Cable Type:",
                        bg=self.colors['bg_section'],
                        fg=self.colors['text_label'],
                        font=('Segoe UI', 9), anchor='w')
        label.grid(row=row, column=0, sticky='w', pady=(0, 12))
        
        cable_types = ['24C/2T', '36C/3T', '48C/4T'] if category == 'cluster' else \
                     ['24C/2T', '48C/4T', '96C/8T', '144C/12T', '288C/24T']
        
        self.cable_type_var = tk.StringVar(value=cable_types[0])
        
        combo = ttk.Combobox(self.cable_inputs_frame, textvariable=self.cable_type_var,
                            values=cable_types, state='readonly', font=('Segoe UI', 9))
        combo.grid(row=row+1, column=0, sticky='ew', pady=(0, 12), ipady=4)
        row += 2
        
        self.cable_entries['length'] = self.create_input_field(
            self.cable_inputs_frame, "Length by OTDR (m):", row)
    
    def generate_cable(self):
        """Generate cable name"""
        category = self.cable_category.get()
        
        try:
            if category == 'cluster':
                fdt = self.cable_entries['fdt'].get().strip()
                line = self.cable_entries['line'].get().strip()
                ctype = self.cable_type_var.get()
                length = self.cable_entries['length'].get().strip()
                
                result = f"{fdt} - CABLE LINE {line} (FO {ctype}) - AE - {length} M"
            else:
                olt = self.cable_entries['olt'].get().strip()
                fdt = self.cable_entries['fdt'].get().strip()
                feeder_type = self.feeder_type_var.get()
                ctype = self.cable_type_var.get()
                length = self.cable_entries['length'].get().strip()
                
                result = f"{olt} - {fdt} ({feeder_type} CABLE FO {ctype}) - AE - {length} M"
            
            self.set_output(self.cable_output, result.upper())
        except Exception as e:
            self.set_output(self.cable_output, f"Error: {str(e)}")
    
    def reset_cable(self):
        """Reset cable inputs"""
        for entry in self.cable_entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)
        self.set_output(self.cable_output, "")
    
    def create_ci_panel(self):
        """CI Description Generator Panel"""
        panel = tk.Frame(self.content_frame, bg=self.colors['bg_main'])
        
        # Two column layout
        left_col = tk.Frame(panel, bg=self.colors['bg_main'])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        right_col = tk.Frame(panel, bg=self.colors['bg_main'])
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12, 0))
        
        # Input section
        input_container = self.create_input_section(left_col)
        input_container.grid_columnconfigure(0, weight=1)
        
        self.ci_entries = {}
        row = 0
        
        for key, label in [('route', 'Route (m):'), ('fdt', 'Slack FDT (unit):'),
                          ('fat', 'Slack FAT (unit):'), ('otdr', 'By OTDR (m):')]:
            self.ci_entries[key] = self.create_input_field(input_container, label, row)
            row += 2
        
        # Buttons
        btn_frame = tk.Frame(left_col, bg=self.colors['bg_main'])
        btn_frame.pack(fill=tk.X, pady=(24, 0))
        
        ModernButton(btn_frame, "GENERATE", self.generate_ci,
                    self.colors['button_blue'], self.colors['button_blue_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        
        ModernButton(btn_frame, "RESET", self.reset_ci,
                    self.colors['button_gray'], self.colors['button_gray_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=6)
        
        ModernButton(btn_frame, "COPY", lambda: self.copy_result(self.ci_output),
                    self.colors['button_green'], self.colors['button_green_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))
        
        # Output section
        self.ci_output = self.create_output_section(right_col)
        
        return panel
    
    def generate_ci(self):
        """Generate CI description"""
        try:
            route = float(self.ci_entries['route'].get() or 0)
            fdt = float(self.ci_entries['fdt'].get() or 0)
            fat = float(self.ci_entries['fat'].get() or 0)
            otdr = self.ci_entries['otdr'].get() or '0'
            
            total_slack = fdt + fat
            route_plus_slack = route + (total_slack * 20)
            total_length = math.ceil(route_plus_slack * 1.05)
            
            result = f"""Total Route : {route} m
Total Slack : {total_slack} unit ({fdt} slack FDT & {fat} slack FAT) @20 m
Toleransi : 5%
Total Length Cable : {route} + {total_slack * 20} = {route_plus_slack} m + ({route_plus_slack} m x 5%) = {total_length} m
By OTDR : {otdr} m"""
            
            self.set_output(self.ci_output, result.upper())
        except Exception as e:
            self.set_output(self.ci_output, f"Error: {str(e)}")
    
    def reset_ci(self):
        """Reset CI inputs"""
        for entry in self.ci_entries.values():
            entry.delete(0, tk.END)
        self.set_output(self.ci_output, "")
    
    def create_feeder_panel(self):
        """Feeder Description Generator Panel"""
        panel = tk.Frame(self.content_frame, bg=self.colors['bg_main'])
        
        # Two column layout
        left_col = tk.Frame(panel, bg=self.colors['bg_main'])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        right_col = tk.Frame(panel, bg=self.colors['bg_main'])
        right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12, 0))
        
        # Input section
        input_container = self.create_input_section(left_col)
        input_container.grid_columnconfigure(0, weight=1)
        
        self.feeder_entries = {}
        row = 0
        
        for key, label in [('route', 'Route (m):'), ('slack', 'Slack (unit):'),
                          ('otdr', 'By OTDR (m):')]:
            self.feeder_entries[key] = self.create_input_field(input_container, label, row)
            row += 2
        
        # Buttons
        btn_frame = tk.Frame(left_col, bg=self.colors['bg_main'])
        btn_frame.pack(fill=tk.X, pady=(24, 0))
        
        ModernButton(btn_frame, "GENERATE", self.generate_feeder,
                    self.colors['button_blue'], self.colors['button_blue_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        
        ModernButton(btn_frame, "RESET", self.reset_feeder,
                    self.colors['button_gray'], self.colors['button_gray_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=6)
        
        ModernButton(btn_frame, "COPY", lambda: self.copy_result(self.feeder_output),
                    self.colors['button_green'], self.colors['button_green_hover'],
                    width=150).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))
        
        # Output section
        self.feeder_output = self.create_output_section(right_col)
        
        return panel
    
    def generate_feeder(self):
        """Generate feeder description"""
        try:
            route = float(self.feeder_entries['route'].get() or 0)
            slack = float(self.feeder_entries['slack'].get() or 0)
            otdr = self.feeder_entries['otdr'].get() or '0'
            
            route_plus_slack = route + (slack * 20)
            total_length = math.ceil(route_plus_slack * 1.05)
            
            result = f"""Total Route : {route} m
Total Slack : {slack} unit @20 m
Toleransi : 5%
Total Length Cable : {route} + {slack * 20} = {route_plus_slack} m + ({route_plus_slack} m x 5%) = {total_length} m
By OTDR : {otdr} m"""
            
            self.set_output(self.feeder_output, result.upper())
        except Exception as e:
            self.set_output(self.feeder_output, f"Error: {str(e)}")
    
    def reset_feeder(self):
        """Reset feeder inputs"""
        for entry in self.feeder_entries.values():
            entry.delete(0, tk.END)
        self.set_output(self.feeder_output, "")
    
    def set_output(self, text_widget, content):
        """Set text in output widget"""
        text_widget.config(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(1.0, content if content else "Result will be displayed here...")
        text_widget.config(state='disabled')
    
    def copy_result(self, text_widget):
        """Copy result to clipboard"""
        content = text_widget.get(1.0, tk.END).strip()
        if content and content != "Result will be displayed here...":
            self.root.clipboard_clear()
            self.root.clipboard_append(content)


def main():
    root = tk.Tk()
    app = CableGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
