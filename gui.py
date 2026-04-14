import tkinter as tk
from tkinter import messagebox
from database import create_table, add_note, get_all_notes
from nlp_engine import summarize_text, generate_questions

# create database table
create_table()

# functions
def clear_output():
    output_text.delete("1.0", tk.END)

def add_note_ui():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    add_note(text[:20], text)
    messagebox.showinfo("Success", "Note saved successfully!")

def summarize_ui():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    summary = summarize_text(text)

    clear_output()
    output_text.insert(tk.END, summary)

def questions_ui():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    questions = generate_questions(text)

    clear_output()
    for q in questions:
        output_text.insert(tk.END, q + "\n")

def view_notes_ui():
    notes = get_all_notes()

    output_text.delete("1.0", tk.END)

    if not notes:
        output_text.insert(tk.END, "No notes found")
        return

    for i, note in enumerate(notes, 1):
        title = note[0]
        content = note[1]

        output_text.insert(tk.END, f"{i}. Title: {title}\n")
        output_text.insert(tk.END, f"   Content: {content}\n\n")


# UI design
root = tk.Tk()
root.title("AI Smart Study Helper")
root.geometry("750x600")
root.config(bg="#f0f0f0")

# title
tk.Label(root, text="AI Smart Study Helper", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# input box
input_text = tk.Text(root, height=8, width=80, font=("Arial", 12))
input_text.pack(pady=10)

# button frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

tk.Button(btn_frame, text="Add Note", width=15, bg="#4CAF50", fg="white", command=add_note_ui).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Summarize", width=15, bg="#2196F3", fg="white", command=summarize_ui).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Generate Questions", width=20, bg="#FF9800", fg="white", command=questions_ui).grid(row=0, column=2, padx=5, pady=5)
tk.Button(btn_frame, text="View Notes", width=15, bg="#9C27B0", fg="white", command=view_notes_ui).grid(row=0, column=3, padx=5, pady=5)

# output box
output_text = tk.Text(root, height=12, width=80, font=("Arial", 12))
output_text.pack(pady=10)

# run app
root.mainloop()