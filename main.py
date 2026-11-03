import tkinter as tk
import psycopg2


# DATABASE CONNECTION

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="Cruz_4110"
)

cursor = conn.cursor()


# CREATE DATABASE TABLE FINAL GRADES

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_final_grades (
        name VARCHAR(100) PRIMARY KEY,
        gen001 NUMERIC(5,2),
        gen002 NUMERIC(5,2),
        gen006 NUMERIC(5,2),
        mat152 NUMERIC(5,2),
        nstp NUMERIC(5,2),
        ped030 NUMERIC(5,2),
        ite260 NUMERIC(5,2),
        ite366 NUMERIC(5,2)
    )
""")

conn.commit()


# WINDOW 1

window = tk.Tk()
window.geometry("700x750")
window.title("ITE 260 PROJECT")
window.config(background="#e3ddcc")


# ENTRY NAME

entry_name = tk.Entry(
    window,
    font=("Consolas", 15)
)

entry_name.insert(0, "Enter your name")
entry_name.place(x=215, y=250)


# NAME ERROR

name_error = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="red",
    bg="#e3ddcc"
)

name_error.place(x=245, y=350)


# CLEARING "ENTER YOUR NAME" TEXT

def clear_placeholder(event):

    if entry_name.get() == "Enter your name":
        entry_name.delete(0, tk.END)

    name_error.config(text="")


def restore_placeholder(event):

    if entry_name.get() == "":
        entry_name.insert(0, "Enter your name")


entry_name.bind("<FocusIn>", clear_placeholder)
entry_name.bind("<FocusOut>", restore_placeholder)


# LABEL 1 STUDENT CALCU

label1 = tk.Label(
    window,
    text="Student Grade Calculator for BSIT1-11",
    font=("Verdana", 20),
    fg="#8ce0ff",
    bg="#26353b",
    relief=tk.SUNKEN,
    bd=5,
    pady=20,
    padx=50
)

label1.place(x=20, y=20)


# LABEL 2 ENTER YOUR NAME

label2 = tk.Label(
    window,
    text="Enter your name:",
    font=("Arial", 20, "bold"),
    fg="#000000",
    bg="#e3ddcc"
)

label2.place(x=210, y=200)


# LABEL 3 CALCULATE FINAL GRADE

label3 = tk.Label(
    window,
    text="Calculate your final grade!",
    font=("Arial", 10),
    fg="#8FC217",
    bg="#26353b"
)

label3.place(x=250, y=75)


# WINDOW 2

def create_window():

    student_name = entry_name.get().strip()

    # IF NO NAME ENTERED IN ENTRY BOX

    if student_name == "Enter your name" or student_name == "":
        name_error.config(text="Please enter your name.")
        return

    name_error.config(text="")

    # NEW WINDOW FRAME

    new_window = tk.Toplevel(window)
    new_window.geometry("700x750")
    new_window.title("Student Grades")
    new_window.config(background="#e3ddcc")

    window.withdraw()

    # LABEL 4 WELCOME

    label4 = tk.Label(
        new_window,
        text=f"WELCOME, {student_name}!",
        font=("Consolas", 18),
        bg="#e3ddcc"
    )

    label4.place(x=50, y=20)


    # TABLE

    tk.Label(
        new_window,
        text="Subject",
        bg="#e3ddcc"
    ).place(x=72, y=70)

    tk.Label(
        new_window,
        text="P1",
        bg="#e3ddcc"
    ).place(x=270, y=70)

    tk.Label(
        new_window,
        text="P2",
        bg="#e3ddcc"
    ).place(x=350, y=70)

    tk.Label(
        new_window,
        text="P3",
        bg="#e3ddcc"
    ).place(x=430, y=70)

    tk.Label(
        new_window,
        text="FINAL GRADE",
        bg="#e3ddcc"
    ).place(x=500, y=70)

    tk.Label(
        new_window,
        text="STATUS",
        bg="#e3ddcc"
    ).place(x=625, y=70)


    # GEN001

    tk.Label(new_window, text="GEN001", bg="#e3ddcc").place(x=70, y=120)

    gen001_p1 = tk.Entry(new_window, width=8)
    gen001_p1.place(x=260, y=120)

    gen001_p2 = tk.Entry(new_window, width=8)
    gen001_p2.place(x=340, y=120)

    gen001_p3 = tk.Entry(new_window, width=8)
    gen001_p3.place(x=420, y=120)

    gen001_result = tk.Label(new_window, text="-", bg="white", width=10)
    gen001_result.place(x=500, y=120)

    gen001_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    gen001_status.place(x=625, y=120)


    # GEN002

    tk.Label(new_window, text="GEN002", bg="#e3ddcc").place(x=70, y=160)

    gen002_p1 = tk.Entry(new_window, width=8)
    gen002_p1.place(x=260, y=160)

    gen002_p2 = tk.Entry(new_window, width=8)
    gen002_p2.place(x=340, y=160)

    gen002_p3 = tk.Entry(new_window, width=8)
    gen002_p3.place(x=420, y=160)

    gen002_result = tk.Label(new_window, text="-", bg="white", width=10)
    gen002_result.place(x=500, y=160)

    gen002_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    gen002_status.place(x=625, y=160)


    # GEN006

    tk.Label(new_window, text="GEN006", bg="#e3ddcc").place(x=70, y=200)

    gen006_p1 = tk.Entry(new_window, width=8)
    gen006_p1.place(x=260, y=200)

    gen006_p2 = tk.Entry(new_window, width=8)
    gen006_p2.place(x=340, y=200)

    gen006_p3 = tk.Entry(new_window, width=8)
    gen006_p3.place(x=420, y=200)

    gen006_result = tk.Label(new_window, text="-", bg="white", width=10)
    gen006_result.place(x=500, y=200)

    gen006_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    gen006_status.place(x=625, y=200)


    # MAT152

    tk.Label(new_window, text="MAT152", bg="#e3ddcc").place(x=70, y=240)

    mat152_p1 = tk.Entry(new_window, width=8)
    mat152_p1.place(x=260, y=240)

    mat152_p2 = tk.Entry(new_window, width=8)
    mat152_p2.place(x=340, y=240)

    mat152_p3 = tk.Entry(new_window, width=8)
    mat152_p3.place(x=420, y=240)

    mat152_result = tk.Label(new_window, text="-", bg="white", width=10)
    mat152_result.place(x=500, y=240)

    mat152_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    mat152_status.place(x=625, y=240)


    # NSTP

    tk.Label(new_window, text="NSTP", bg="#e3ddcc").place(x=70, y=280)

    nstp_p1 = tk.Entry(new_window, width=8)
    nstp_p1.place(x=260, y=280)

    nstp_p2 = tk.Entry(new_window, width=8)
    nstp_p2.place(x=340, y=280)

    nstp_p3 = tk.Entry(new_window, width=8)
    nstp_p3.place(x=420, y=280)

    nstp_result = tk.Label(new_window, text="-", bg="white", width=10)
    nstp_result.place(x=500, y=280)

    nstp_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    nstp_status.place(x=625, y=280)


    # PED030

    tk.Label(new_window, text="PED030", bg="#e3ddcc").place(x=70, y=320)

    ped030_p1 = tk.Entry(new_window, width=8)
    ped030_p1.place(x=260, y=320)

    ped030_p2 = tk.Entry(new_window, width=8)
    ped030_p2.place(x=340, y=320)

    ped030_p3 = tk.Entry(new_window, width=8)
    ped030_p3.place(x=420, y=320)

    ped030_result = tk.Label(new_window, text="-", bg="white", width=10)
    ped030_result.place(x=500, y=320)

    ped030_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    ped030_status.place(x=625, y=320)


    # ITE260

    tk.Label(new_window, text="ITE260", bg="#e3ddcc").place(x=70, y=360)

    ite260_p1 = tk.Entry(new_window, width=8)
    ite260_p1.place(x=260, y=360)

    ite260_p2 = tk.Entry(new_window, width=8)
    ite260_p2.place(x=340, y=360)

    ite260_p3 = tk.Entry(new_window, width=8)
    ite260_p3.place(x=420, y=360)

    ite260_result = tk.Label(new_window, text="-", bg="white", width=10)
    ite260_result.place(x=500, y=360)

    ite260_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    ite260_status.place(x=625, y=360)


    # ITE366

    tk.Label(new_window, text="ITE366", bg="#e3ddcc").place(x=70, y=400)

    ite366_p1 = tk.Entry(new_window, width=8)
    ite366_p1.place(x=260, y=400)

    ite366_p2 = tk.Entry(new_window, width=8)
    ite366_p2.place(x=340, y=400)

    ite366_p3 = tk.Entry(new_window, width=8)
    ite366_p3.place(x=420, y=400)

    ite366_result = tk.Label(new_window, text="-", bg="white", width=10)
    ite366_result.place(x=500, y=400)

    ite366_status = tk.Label(new_window, text="-", bg="#e3ddcc")
    ite366_status.place(x=625, y=400)


    # CALCULATE GRADES

    def calculate():

        try:

            # CHECK IF ALL GRADES ARE BETWEEN 0 AND 100

            all_grades = [
                gen001_p1.get(),
                gen001_p2.get(),
                gen001_p3.get(),

                gen002_p1.get(),
                gen002_p2.get(),
                gen002_p3.get(),

                gen006_p1.get(),
                gen006_p2.get(),
                gen006_p3.get(),

                mat152_p1.get(),
                mat152_p2.get(),
                mat152_p3.get(),

                nstp_p1.get(),
                nstp_p2.get(),
                nstp_p3.get(),

                ped030_p1.get(),
                ped030_p2.get(),
                ped030_p3.get(),

                ite260_p1.get(),
                ite260_p2.get(),
                ite260_p3.get(),

                ite366_p1.get(),
                ite366_p2.get(),
                ite366_p3.get()
            ]

            for grade in all_grades:

                grade = float(grade)

                if grade < 0 or grade > 100:

                    grade_error.config(
                        text="Enter your grade between 0 and 100.",
                        fg="red"
                    )

                    return

            grade_error.config(text="")


            # GEN001 GRADE COMPUTATION

            gen001 = (
                0.33 * float(gen001_p1.get()) +
                0.33 * float(gen001_p2.get()) +
                0.34 * float(gen001_p3.get())
            )

            # GEN002 GRADE COMPUTATION

            gen002 = (
                0.33 * float(gen002_p1.get()) +
                0.33 * float(gen002_p2.get()) +
                0.34 * float(gen002_p3.get())
            )

            # GEN006 GRADE COMPUTATION

            gen006 = (
                0.33 * float(gen006_p1.get()) +
                0.33 * float(gen006_p2.get()) +
                0.34 * float(gen006_p3.get())
            )

            # MAT152 GRADE COMPUTATION

            mat152 = (
                0.33 * float(mat152_p1.get()) +
                0.33 * float(mat152_p2.get()) +
                0.34 * float(mat152_p3.get())
            )

            # NSTP GRADE COMPUTATION

            nstp = (
                0.33 * float(nstp_p1.get()) +
                0.33 * float(nstp_p2.get()) +
                0.34 * float(nstp_p3.get())
            )

            # PED030 GRADE COMPUTATION

            ped030 = (
                0.33 * float(ped030_p1.get()) +
                0.33 * float(ped030_p2.get()) +
                0.34 * float(ped030_p3.get())
            )


            # MAJOR GRADES COMPUTATION
            # P3 IS THE FINAL GRADE

            ite260 = float(ite260_p3.get())
            ite366 = float(ite366_p3.get())


            # DISPLAY FINAL GRADES

            gen001_result.config(text=f"{gen001:.2f}")
            gen002_result.config(text=f"{gen002:.2f}")
            gen006_result.config(text=f"{gen006:.2f}")
            mat152_result.config(text=f"{mat152:.2f}")
            nstp_result.config(text=f"{nstp:.2f}")
            ped030_result.config(text=f"{ped030:.2f}")

            ite260_result.config(text=f"{ite260:.2f}")
            ite366_result.config(text=f"{ite366:.2f}")


            # SUBJECT STATUS

            if gen001 >= 50:
                gen001_status.config(text="PASS")
            else:
                gen001_status.config(text="FAIL")

            if gen002 >= 50:
                gen002_status.config(text="PASS")
            else:
                gen002_status.config(text="FAIL")

            if gen006 >= 50:
                gen006_status.config(text="PASS")
            else:
                gen006_status.config(text="FAIL")

            if mat152 >= 50:
                mat152_status.config(text="PASS")
            else:
                mat152_status.config(text="FAIL")

            if nstp >= 50:
                nstp_status.config(text="PASS")
            else:
                nstp_status.config(text="FAIL")

            if ped030 >= 50:
                ped030_status.config(text="PASS")
            else:
                ped030_status.config(text="FAIL")


            # MAJOR STATUS

            if ite260 >= 80:
                ite260_status.config(text="PASS")
            else:
                ite260_status.config(text="FAIL")

            if ite366 >= 80:
                ite366_status.config(text="PASS")
            else:
                ite366_status.config(text="FAIL")


            # SAVE FINAL GRADES TO DATABASE

            cursor.execute("""
                INSERT INTO student_final_grades (
                    name,
                    gen001, gen002, gen006,
                    mat152, nstp, ped030,
                    ite260, ite366
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (name)
                DO UPDATE SET
                    gen001 = EXCLUDED.gen001,
                    gen002 = EXCLUDED.gen002,
                    gen006 = EXCLUDED.gen006,
                    mat152 = EXCLUDED.mat152,
                    nstp = EXCLUDED.nstp,
                    ped030 = EXCLUDED.ped030,
                    ite260 = EXCLUDED.ite260,
                    ite366 = EXCLUDED.ite366
            """, (
                student_name,
                round(gen001, 2),
                round(gen002, 2),
                round(gen006, 2),
                round(mat152, 2),
                round(nstp, 2),
                round(ped030, 2),
                round(ite260, 2),
                round(ite366, 2)
            ))

            conn.commit()


            # HIGHEST AND LOWEST

            grades = [
                gen001,
                gen002,
                gen006,
                mat152,
                nstp,
                ped030,
                ite260,
                ite366
            ]

            highest = max(grades)
            lowest = min(grades)

            highest_label.config(
                text=f"Highest Grade: {highest:.2f}"
            )

            lowest_label.config(
                text=f"Lowest Grade: {lowest:.2f}"
            )


        # IF NOT ALL GRADES ARE ENTERED

        except ValueError:

            grade_error.config(
                text="Please enter all grades.",
                fg="red"
            )


    # CALCULATE BUTTON

    calculate_button = tk.Button(
        new_window,
        text="CALCULATE",
        command=calculate
    )

    calculate_button.place(x=310, y=450)


    # CONNECTED TO EXCEPT VALUEERROR

    grade_error = tk.Label(
        new_window,
        text="",
        bg="#e3ddcc",
        fg="red"
    )

    grade_error.place(x=220, y=500)


    # HIGHEST GRADE

    highest_label = tk.Label(
        new_window,
        text="Highest Grade: -",
        bg="#e3ddcc"
    )

    highest_label.place(x=200, y=540)


    # LOWEST GRADE

    lowest_label = tk.Label(
        new_window,
        text="Lowest Grade: -",
        bg="#e3ddcc"
    )

    lowest_label.place(x=420, y=540)


    # BACK

    def go_back():

        new_window.destroy()
        window.deiconify()


    back_button = tk.Button(
        new_window,
        text="BACK",
        command=go_back
    )

    back_button.place(x=20, y=680)


# CLOSE PROGRAM

def close_program():

    cursor.close()
    conn.close()
    window.destroy()


# ENTER BUTTON

enter_button1 = tk.Button(
    window,
    text="Enter",
    command=create_window,
    font=("Arial", 15),
    fg="#f0fbff",
    bg="#2f72de",
    relief=tk.RAISED,
    bd=5
)

enter_button1.place(x=245, y=300)


# QUIT BUTTON

quit_button = tk.Button(
    window,
    text="Quit",
    font=("Arial", 15),
    command=close_program,
    fg="#f0fbff",
    bg="#454c57",
    relief=tk.RAISED,
    bd=5
)

quit_button.place(x=350, y=300)


# CLOSE DATABASE WHEN WINDOW IS CLOSED

window.protocol("WM_DELETE_WINDOW", close_program)


window.mainloop()