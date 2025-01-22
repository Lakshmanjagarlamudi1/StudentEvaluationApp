import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk 
import os
 
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Data Filter Application")
        self.geometry("600x400")
 
        self.uploaded_folder_path = None
 
        self.create_main_menu()
 
    def create_main_menu(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()
 
        # Main Menu UI
        tk.Label(self, text="Welcome to the Student Data Filter Application", font=("Arial", 16)).pack(pady=10)
 
        # Add an image (
        try:
            image = Image.open(r"image.png")  # Replace with your image file
            image = image.resize((300, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            tk.Label(self, image=photo).pack(pady=10)
            self.image = photo  # Keep a reference to prevent garbage collection
        except FileNotFoundError:
            tk.Label(self, text="[Image Missing]", font=("Arial", 10), fg="red").pack()
 
        tk.Button(self, text="Upload Folder of PDFs", command=self.upload_folder, width=25).pack(pady=10)
 
    def upload_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.uploaded_folder_path = folder_path
            pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
            if pdf_files:
                messagebox.showinfo("Folder Upload", f"Folder uploaded successfully: {len(pdf_files)} PDF(s) found.")
                self.choose_service()
            else:
                messagebox.showwarning("No PDFs Found", "The selected folder does not contain any PDF files.")
 
    def choose_service(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()
 
        # Service Selection UI
        tk.Label(self, text="Choose a Service", font=("Arial", 16)).pack(pady=10)
 
        tk.Button(self, text="Eligible Students", command=self.service_eligible_students, width=25).pack(pady=5)
        tk.Button(self, text="Student Program Evaluation", command=self.service_program_evaluation, width=25).pack(pady=5)
 
    def service_eligible_students(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()
 
        # Eligible Students UI
        tk.Label(self, text="Find Eligible Students", font=("Arial", 16)).pack(pady=10)
 
        tk.Label(self, text="Target Course:").pack()
        course_entry = tk.Entry(self, width=30)
        course_entry.pack(pady=5)
 
        tk.Label(self, text="Pre-requirements (comma-separated):").pack()
        prereq_entry = tk.Entry(self, width=30)
        prereq_entry.pack(pady=5)
 
        def submit_eligible_students():
            course = course_entry.get().strip()
            prereqs = prereq_entry.get().strip()
            if course and prereqs:
                prereq_list = [p.strip() for p in prereqs.split(",")]
                # Here you would call your logic code to process the data
                ################################################################################
                ################################################################################
                messagebox.showinfo("Success", f"Eligibility check complete for {course} with prereqs {prereq_list}")
                self.create_main_menu()
            else:
                messagebox.showerror("Input Error", "Please fill in all fields.")
 
        tk.Button(self, text="Submit", command=submit_eligible_students, width=15).pack(pady=10)
        tk.Button(self, text="Back", command=self.choose_service, width=15).pack()
 
    def service_program_evaluation(self):
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.destroy()
 
        # Program Evaluation UI
        tk.Label(self, text="Student Program Evaluation", font=("Arial", 16)).pack(pady=10)
 
        tk.Label(self, text="Enter Student ID:").pack()
        student_id_entry = tk.Entry(self, width=30)
        student_id_entry.pack(pady=5)
 
        def submit_program_evaluation():
            student_id = student_id_entry.get().strip()
            if student_id:
                # Here you would call your logic code to process the data
                # For example, generate an Excel file
                messagebox.showinfo("Success", f"Program evaluation complete for Student ID {student_id}. Excel file generated.")
                self.create_main_menu()
            else:
                messagebox.showerror("Input Error", "Please enter a Student ID.")
 
        tk.Button(self, text="Submit", command=submit_program_evaluation, width=15).pack(pady=10)
        tk.Button(self, text="Back", command=self.choose_service, width=15).pack()
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()