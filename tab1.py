from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import json
import os
language = ""
project_name = ""
com_vaf = 0

class Frames(object):
    def __init__(self):
        self.saved_data = None
        self.lang = StringVar()
        self.done = None
        self.fp = 0
        self.mycheck1 = StringVar()
        self.text_entry = IntVar()
        self.current_language = None
        self.filename = None
        self.starting_row_count = 1
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0
        self.var4 = 0
        self.var5 = 0
        self.var6 = 0
        self.var7 = 0
        self.var8 = 0
        self.var9 = 0
        self.var10 = 0
        self.var11 = 0
        self.var12 = 0
        self.var13 = 0
        self.ECF1 = 0
        self.ECF2 = 0
        self.ECF3 = 0
        self.ECF4 = 0
        self.ECF5 = 0
        self.ECF6 = 0
        self.ECF7 = 0
        self.ECF8 = 0
        self.d1 = {}
        self.a2 = {}
        self.UUCW_dict = {}
        self.UAW_dict = {}
        self.TCF_dict = {}
        self.ECF_dict = {}
        self.starting_row_count = 2
        self.proj_name = tk.StringVar()
        global tab3
        self.save = False
        self.current_row = 2

    def valueAdjustment(self):
        global Frames
        self.newwin = Toplevel(root)
        self.newwin.title('New Window')
        self.newwin.geometry("600x600")
        self.newwin.resizable(0, 0)


        assign = tk.Label(self.newwin,
                          text="Assign a value from 0 to 5 for each of the following Value Adjustment Factors:")
        recovery = tk.Label(self.newwin, text="Does the system require reliable backup and recovery processes?")
        reader = tk.Label(self.newwin,text = "Are specialized data communications required to transfer information to or from the application?")
        assign1 = tk.Label(self.newwin,text ="Are there distributed processing functions?")
        reader1 = tk.Label(self.newwin, text="Is performance critical?")
        recovery1 = tk.Label(self.newwin,text="Will the system run in an existing,heavily utilized operational environment?")
        assign2 = tk.Label(self.newwin, text = "Does the system require online data entry?")
        reader2 = tk.Label(self.newwin,
                           text="Does the online data entry require the input transaction to be built over multiple screens ot operations?")
        recovery2 =tk.Label(self.newwin, text="Are the internal logical files updated online?")
        assign3 = tk.Label(self.newwin, text="Is the internal processing comples?")
        reader3 = tk.Label(self.newwin, text="Is the code designed to be reuseable?")
        recovery3 = tk.Label(self.newwin, text="Are the conversions and installation included in the design?")
        assign4 = tk.Label(self.newwin,
                           text="Is the system designed ot multiple instructions in different organizations?")
        reader4 = tk.Label(self.newwin, text="Does the systeme require reliable backup and recovery processes?")
        recovery4 = tk.Label(self.newwin, text="Does the systeme require reliable backup and recovery processes?")
        doneButton = tk.Button(self.newwin, text=f"Done.", command=self.compute_vaf_done)
        cancel = tk.Button(self.newwin, text=f"Cancel.", command=self.close_window)

        self.m = tk.IntVar()
        self.o = tk.IntVar()
        self.p = tk.IntVar()
        self.q = tk.IntVar()
        self.r = tk.IntVar()
        self.s = tk.IntVar()
        self.t = tk.IntVar()
        self.u = tk.IntVar()
        self.v = tk.IntVar()
        self.a1 = tk.IntVar()
        self.x = tk.IntVar()
        self.y = tk.IntVar()
        self.z = tk.IntVar()
        self.a = tk.IntVar()

        self.m.set(0)
        self.o.set(0)
        self.p.set(0)
        self.q.set(0)
        self.r.set(0)
        self.s.set(0)
        self.t.set(0)
        self.u.set(0)
        self.v.set(0)
        self.a1.set(0)
        self.x.set(0)
        self.y.set(0)
        self.z.set(0)
        self.a.set(0)

        self.comboExample2 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.m)
        self.comboExample3 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.o)
        self.comboExample4 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.p)
        self.comboExample5 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.q)
        self.comboExample6 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.r)
        self.comboExample7 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.s)
        self.comboExample8 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.t)
        self.comboExample9 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.u)
        self.comboExample10 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.v)
        self.comboExample11 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.a1)
        self.comboExample12 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.x)
        self.comboExample13 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.y)
        self.comboExample14 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.z)
        self.comboExample15 = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.a)

        assign.place(x=0,y=20)
        recovery.place(x=0,y=50)
        reader.place(x=0,y=80)
        assign1.place(x=0, y=110)
        reader1.place(x=0, y=140)
        recovery1.place(x=0, y=170)
        assign2.place(x=0, y=200)
        reader2.place(x=0, y=230)
        recovery2.place(x=0, y=260)
        assign3.place(x=0, y=290)
        reader3.place(x=0, y=320)
        recovery3.place(x=0, y=350)
        assign4.place(x=0, y=380)
        reader4.place(x=0, y=410)
        recovery4.place(x=0, y=440)
        doneButton.place(x=0, y=470)
        cancel.place(x=0, y=500)

        self.comboExample2.place(x=500, y=50)
        self.comboExample3.place(x=500, y=80)
        self.comboExample4.place(x=500, y=110)
        self.comboExample5.place(x=500, y=140)
        self.comboExample6.place(x=500, y=170)
        self.comboExample7.place(x=500, y=200)
        self.comboExample8.place(x=500, y=230)
        self.comboExample9.place(x=500, y=260)
        self.comboExample10.place(x=500, y=290)
        self.comboExample11.place(x=500, y=320)
        self.comboExample12.place(x=500, y=350)
        self.comboExample13.place(x=500, y=380)
        self.comboExample14.place(x=500, y=410)
        self.comboExample15.place(x=500, y=440)

        if self.saved_data and self.saved_data["value_adjustment_window"]:
            print(self.saved_data["value_adjustment_window"])
            self.comboExample2.current(int(self.saved_data["value_adjustment_window"]["m"]))
            self.comboExample3.current(int(self.saved_data["value_adjustment_window"]["o"]))
            self.comboExample4.current(int(self.saved_data["value_adjustment_window"]["p"]))
            self.comboExample5.current(int(self.saved_data["value_adjustment_window"]["q"]))
            self.comboExample6.current(int(self.saved_data["value_adjustment_window"]["r"]))
            self.comboExample7.current(int(self.saved_data["value_adjustment_window"]["s"]))
            self.comboExample8.current(int(self.saved_data["value_adjustment_window"]["t"]))
            self.comboExample9.current(int(self.saved_data["value_adjustment_window"]["u"]))
            self.comboExample10.current(int(self.saved_data["value_adjustment_window"]["v"]))
            self.comboExample11.current(int(self.saved_data["value_adjustment_window"]["a1"]))
            self.comboExample12.current(int(self.saved_data["value_adjustment_window"]["x"]))
            self.comboExample13.current(int(self.saved_data["value_adjustment_window"]["y"]))
            self.comboExample14.current(int(self.saved_data["value_adjustment_window"]["z"]))
            self.comboExample15.current(int(self.saved_data["value_adjustment_window"]["a"]))



        else:
            self.comboExample2.current(0)
            self.comboExample3.current(0)
            self.comboExample4.current(0)
            self.comboExample5.current(0)
            self.comboExample6.current(0)
            self.comboExample7.current(0)
            self.comboExample8.current(0)
            self.comboExample9.current(0)
            self.comboExample10.current(0)
            self.comboExample11.current(0)
            self.comboExample12.current(0)
            self.comboExample13.current(0)
            self.comboExample14.current(0)
            self.comboExample15.current(0)
        print("==========")

        if not self.a2:
            self.a2 = {'m': self.comboExample2.get(),'o':self.comboExample3.get(),'p':self.comboExample4.get(),'q':self.comboExample5.get(),'r':self.comboExample6.get(),
                       's':self.comboExample7.get(),'t':self.comboExample8.get(),'u':self.comboExample9.get(),'v':self.comboExample10.get(),'a1':self.comboExample11.get(),'x':self.comboExample12.get(),
                       'y':self.comboExample13.get(),'z':self.comboExample14.get(),'a':self.comboExample15.get()}
            #print(self.a2)
        else:
            print("called this")

            self.comboExample2.current(int(self.a2['m'])),self.comboExample3.current(int(self.a2['o'])), \
            self.comboExample4.current(int(self.a2['p'])), self.comboExample5.current(int(self.a2['q'])), \
            self.comboExample6.current(int(self.a2['r'])), self.comboExample7.current(int(self.a2['s'])), \
            self.comboExample8.current(int(self.a2['t'])), self.comboExample9.set(int(self.a2['u'])), \
            self.comboExample10.current(int(self.a2['v'])), self.comboExample11.current(int(self.a2['a1'])), \
            self.comboExample12.current(int(self.a2['x'])), self.comboExample13.current(int(self.a2['y'])), \
            self.comboExample14.current(int(self.a2['z'])), self.comboExample15.current(int(self.a2['a']))

    def compute_vaf_done(self):
        global com_vaf
        self.compute_vaf()
        self.a2['m'] = self.comboExample2.get()
        self.a2['o'] = self.comboExample3.get()
        self.a2['p'] = self.comboExample4.get()
        self.a2['q'] = self.comboExample5.get()
        self.a2['r'] = self.comboExample6.get()
        self.a2['s'] = self.comboExample7.get()
        self.a2['t'] = self.comboExample8.get()
        self.a2['u'] = self.comboExample9.get()
        self.a2['v'] = self.comboExample10.get()
        self.a2['a1'] = self.comboExample11.get()
        self.a2['x'] = self.comboExample12.get()
        self.a2['y'] = self.comboExample13.get()
        self.a2['z'] = self.comboExample14.get()
        self.a2['a'] = self.comboExample15.get()
        self.newwin.destroy()
        end = len(self.value_adjustment.get())
        self.value_adjustment.delete(0, end)
        self.value_adjustment.insert(0, com_vaf)


        print(self.a2)

    def compute_vaf(self):
        global com_vaf

        com_vaf = self.m.get() + self.o.get() + self.p.get() + self.q.get() + self.r.get() + self.s.get() + self.t.get() + self.u.get() + self.v.get() + self.a1.get() + self.x.get() + self.y.get() + self.z.get() + self.a.get()

    def TCF(self):
        self.newwin = Toplevel(root)
        self.newwin.title('New Window')
        self.newwin.geometry("800x800")
        self.newwin.resizable(0, 0)

        assign = tk.Label(self.newwin,
                          text="Assign a value from 0 to 5 for each of the following Value Adjustment Factors:")
        DS = tk.Label(self.newwin, text=" T1      Distributed System ")
        Per = tk.Label(self.newwin, text="T2        Performance ")
        Enu = tk.Label(self.newwin, text="T3        End User Efficiency")
        CIP = tk.Label(self.newwin, text="T4        Complex internal processing")
        Reu = tk.Label(self.newwin, text="T5       Reusability")
        ETI = tk.Label(self.newwin, text="T6      Easy to install")
        ETU = tk.Label(self.newwin, text="T7     Easy to Use")
        Port = tk.Label(self.newwin, text="T8       Portable")
        ETC = tk.Label(self.newwin, text="T9        Easy to change")
        Conc = tk.Label(self.newwin, text="T10       Concurrent")
        SSF = tk.Label(self.newwin, text="T11     Special Security Features")
        PDATED = tk.Label(self.newwin,
                          text="T12        Provide direct acess to external data")
        Spl = tk.Label(self.newwin, text="T13       Special users training faclities are required")
        self.var1 = IntVar()
        m1 = tk.Label(self.newwin, textvariable=self.var1)
        self.var1.set(2)
        self.var2 = IntVar()
        m2 = tk.Label(self.newwin, textvariable=self.var2)
        self.var2.set(1)
        self.var3 = IntVar()
        m3 = tk.Label(self.newwin, textvariable=self.var3)
        self.var3.set(1)
        self.var4 = IntVar()
        m4 = tk.Label(self.newwin, textvariable=self.var4)
        self.var4.set(1)
        self.var5 = IntVar()
        m5 = tk.Label(self.newwin, textvariable=self.var5)
        self.var5.set(1)
        self.var6 = DoubleVar()
        m6 = tk.Label(self.newwin, textvariable=self.var6)
        self.var6.set(0.5)
        self.var7 = DoubleVar()
        m7 = tk.Label(self.newwin, textvariable=self.var7)
        self.var7.set(0.5)
        self.var8 = IntVar()
        m8 = tk.Label(self.newwin, textvariable=self.var8)
        self.var8.set(2)
        self.var9 = IntVar()
        m9 = tk.Label(self.newwin, textvariable=self.var9)
        self.var9.set(1)
        self.var10 = IntVar()
        m10 = tk.Label(self.newwin, textvariable=self.var10)
        self.var10.set(1)
        self.var11 = IntVar()
        m11 = tk.Label(self.newwin, textvariable=self.var11)
        self.var11.set(1)
        self.var12 = IntVar()
        m12 = tk.Label(self.newwin, textvariable=self.var12)
        self.var12.set(1)
        self.var13 = IntVar()
        m13 = tk.Label(self.newwin, textvariable=self.var13)
        self.var13.set(1)

        TotalFactors = tk.Button(self.newwin, text="Total Factors", command=self.entry)
        doneButton = tk.Button(self.newwin, text=f"Done", command=self.TCF_done)
        cancel = tk.Button(self.newwin, text=f"Cancel.", command=self.close_window)

        m1.place(x=300, y=50)
        m2.place(x=300, y=80)
        m3.place(x=300, y=110)
        m4.place(x=300, y=140)
        m5.place(x=300, y=170)
        m6.place(x=300, y=200)
        m7.place(x=300, y=230)
        m8.place(x=300, y=260)
        m9.place(x=300, y=290)
        m10.place(x=300, y=320)
        m11.place(x=300, y=350)
        m12.place(x=300, y=380)
        m13.place(x=300, y=410)

        self.mds = tk.IntVar()
        self.oper = tk.IntVar()
        self.penu = tk.IntVar()
        self.qcip = tk.IntVar()
        self.rreu = tk.IntVar()
        self.seti = tk.IntVar()
        self.tetu = tk.IntVar()
        self.uport = tk.IntVar()
        self.vetc = tk.IntVar()
        self.wconc = tk.IntVar()
        self.xssf = tk.IntVar()
        self.ypdated = tk.IntVar()
        self.zspl = tk.IntVar()

        self.mds.set(0)
        self.oper.set(0)
        self.penu.set(0)
        self.qcip.set(0)
        self.rreu.set(0)
        self.seti.set(0)
        self.tetu.set(0)
        self.uport.set(0)
        self.vetc.set(0)
        self.wconc.set(0)
        self.xssf.set(0)
        self.ypdated.set(0)
        self.zspl.set(0)

        self.comboExample2ds = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.mds)
        self.comboExample3per = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.oper)
        self.comboExample4enu = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.penu)
        self.comboExample5cip = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.qcip)
        self.comboExample6reu = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.rreu)
        self.comboExample7eti = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.seti)
        self.comboExample8etu = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.tetu)
        self.comboExample9port = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.uport)
        self.comboExample10etc = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.vetc)
        self.comboExample11conc = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.wconc)
        self.comboExample12ssf = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.xssf)
        self.comboExample13pdated = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]),textvariable=self.ypdated)
        self.comboExample14spl = ttk.Combobox(self.newwin, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.zspl)

        assign.place(x=0, y=20)
        DS.place(x=0, y=50)
        Per.place(x=0, y=80)
        Enu.place(x=0, y=110)
        CIP.place(x=0, y=140)
        Reu.place(x=0, y=170)
        ETI.place(x=0, y=200)
        ETU.place(x=0, y=230)
        Port.place(x=0, y=260)
        ETC.place(x=0, y=290)
        Conc.place(x=0, y=320)
        SSF.place(x=0, y=350)
        PDATED.place(x=0, y=380)
        Spl.place(x=0, y=410)

        TotalFactors.place(x=0, y=470)
        doneButton.place(x=0, y=500)
        cancel.place(x=0, y=530)

        self.comboExample2ds.place(x=500, y=50)
        self.comboExample3per.place(x=500, y=80)
        self.comboExample4enu.place(x=500, y=110)
        self.comboExample5cip.place(x=500, y=140)
        self.comboExample6reu.place(x=500, y=170)
        self.comboExample7eti.place(x=500, y=200)
        self.comboExample8etu.place(x=500, y=230)
        self.comboExample9port.place(x=500, y=260)
        self.comboExample10etc.place(x=500, y=290)
        self.comboExample11conc.place(x=500, y=320)
        self.comboExample12ssf.place(x=500, y=350)
        self.comboExample13pdated.place(x=500, y=380)
        self.comboExample14spl.place(x=500, y=410)

        self.comboExample2ds.current(0)
        self.comboExample3per.current(0)
        self.comboExample4enu.current(0)
        self.comboExample5cip.current(0)
        self.comboExample6reu.current(0)
        self.comboExample7eti.current(0)
        self.comboExample8etu.current(0)
        self.comboExample9port.current(0)
        self.comboExample10etc.current(0)
        self.comboExample11conc.current(0)
        self.comboExample12ssf.current(0)
        self.comboExample13pdated.current(0)
        self.comboExample14spl.current(0)

        if self.saved_data and self.saved_data["TCF_dict"]:
            self.comboExample2ds.current(int(self.saved_data['TCF_dict']['TCF2']))
            self.comboExample3per.current(int(self.saved_data['TCF_dict']['TCF3']))
            self.comboExample4enu.current(int(self.saved_data['TCF_dict']['TCF4']))
            self.comboExample5cip.current(int(self.saved_data['TCF_dict']['TCF5']))
            self.comboExample6reu.current(int(self.saved_data['TCF_dict']['TCF6']))
            self.comboExample7eti.current(int(self.saved_data['TCF_dict']['TCF7']))
            self.comboExample8etu.current(int(self.saved_data['TCF_dict']['TCF8']))
            self.comboExample9port.current(int(self.saved_data['TCF_dict']['TCF9']))
            self.comboExample10etc.current(int(self.saved_data['TCF_dict']['TCF10']))
            self.comboExample11conc.current(int(self.saved_data['TCF_dict']['TCF11']))
            self.comboExample12ssf.current(int(self.saved_data['TCF_dict']['TCF12']))
            self.comboExample13pdated.current(int(self.saved_data['TCF_dict']['TCF13']))
            self.comboExample14spl.current(int(self.saved_data['TCF_dict']['TCF14']))

        T1 = IntVar()
        if self.saved_data:
            T1.set(self.saved_data['TCF_dict']['T1'])
        T2 = IntVar()
        if self.saved_data:
            T2.set(self.saved_data['TCF_dict']['T2'])
        T3 = IntVar()
        if self.saved_data:
            T3.set(self.saved_data['TCF_dict']['T3'])
        T4 = IntVar()
        if self.saved_data:
            T4.set(self.saved_data['TCF_dict']['T4'])
        T5 = IntVar()
        if self.saved_data:
            T5.set(self.saved_data['TCF_dict']['T5'])
        T6 = IntVar()
        if self.saved_data:
            T6.set(self.saved_data['TCF_dict']['T6'])
        T7 = IntVar()
        if self.saved_data:
            T7.set(self.saved_data['TCF_dict']['T7'])
        T8 = IntVar()
        if self.saved_data:
            T8.set(self.saved_data['TCF_dict']['T8'])
        T9 = IntVar()
        if self.saved_data:
            T9.set(self.saved_data['TCF_dict']['T9'])
        T10 = IntVar()
        if self.saved_data:
            T10.set(self.saved_data['TCF_dict']['T10'])
        T11 = IntVar()
        if self.saved_data:
            T11.set(self.saved_data['TCF_dict']['T11'])
        T12 = IntVar()
        if self.saved_data:
            T12.set(self.saved_data['TCF_dict']['T12'])
        T13 = IntVar()
        if self.saved_data:
            T13.set(self.saved_data['TCF_dict']['T13'])
        T14= IntVar()
        if self.saved_data:
            T14.set(self.saved_data['TCF_dict']['T14'])
        self.T1 = Entry(self.newwin, width=7,textvariable = T1)
        self.T2 = Entry(self.newwin, width=7,textvariable =T2)
        self.T3 = Entry(self.newwin, width=7,textvariable = T3)
        self.T4 = Entry(self.newwin, width=7,textvariable = T4)
        self.T5 = Entry(self.newwin, width=7,textvariable =T5)
        self.T6 = Entry(self.newwin, width=7,textvariable =T6)
        self.T7 = Entry(self.newwin, width=7,textvariable =T7)
        self.T8 = Entry(self.newwin, width=7,textvariable= T8)
        self.T9 = Entry(self.newwin, width=7,textvariable=T9)
        self.T10 = Entry(self.newwin, width=7,textvariable=T10)
        self.T11 = Entry(self.newwin, width=7,textvariable=T11)
        self.T12 = Entry(self.newwin, width=7,textvariable=T12)
        self.T13 = Entry(self.newwin, width=7,textvariable=T13)
        self.T14 = Entry(self.newwin, width=7,textvariable=T14)

        self.T1.place(x=600, y=50)
        self.T2.place(x=600, y=80)
        self.T3.place(x=600, y=110)
        self.T4.place(x=600, y=140)
        self.T5.place(x=600, y=170)
        self.T6.place(x=600, y=200)
        self.T7.place(x=600, y=230)
        self.T8.place(x=600, y=260)
        self.T9.place(x=600, y=290)
        self.T10.place(x=600, y=310)
        self.T11.place(x=600, y=350)
        self.T12.place(x=600, y=380)
        self.T13.place(x=600, y=410)
        self.T14.place(x=600, y=470)

    def entry(self):

        end = len(self.T1.get())
        self.T1.delete(0,end)
        tcf1 = int(self.var1.get()) * int(self.mds.get())
        self.T1.insert(0,tcf1)
        end = len(self.T2.get())
        self.T2.delete(0, end)
        tcf2 = int(self.var2.get()) * int(self.oper.get())
        self.T2.insert(0, tcf2)
        end = len(self.T3.get())
        self.T3.delete(0, end)
        tcf3 = int(self.var3.get()) * int(self.penu.get())
        self.T3.insert(0, tcf3)
        end = len(self.T4.get())
        self.T4.delete(0, end)
        tcf4 = int(self.var4.get()) * int(self.qcip.get())
        self.T4.insert(0, tcf4)
        end = len(self.T5.get())
        self.T5.delete(0, end)
        tcf5 = int(self.var5.get()) * int(self.rreu.get())
        self.T5.insert(0, tcf5)
        end = len(self.T6.get())
        self.T6.delete(0, end)
        tcf6 = float(self.var6.get()) * int(self.seti.get())
        self.T6.insert(0, tcf6)
        end = len(self.T7.get())
        self.T7.delete(0, end)
        tcf7 = float(self.var7.get()) * int(self.tetu.get())
        self.T7.insert(0, tcf7)
        end = len(self.T8.get())
        self.T8.delete(0, end)
        tcf8 = int(self.var8.get()) * int(self.uport.get())
        self.T8.insert(0, tcf8)
        end = len(self.T9.get())
        self.T9.delete(0, end)
        tcf9 = int(self.var9.get()) * int(self.vetc.get())
        self.T9.insert(0, tcf9)
        end = len(self.T10.get())
        self.T10.delete(0, end)
        tcf10 = int(self.var10.get()) * int(self.wconc.get())
        self.T10.insert(0, tcf10)
        end = len(self.T11.get())
        self.T11.delete(0, end)
        tcf11 = int(self.var11.get()) * int(self.xssf.get())
        self.T11.insert(0, tcf11)
        end = len(self.T12.get())
        self.T12.delete(0, end)
        tcf12 = int(self.var12.get()) * int(self.ypdated.get())
        self.T12.insert(0, tcf12)
        end = len(self.T13.get())
        self.T13.delete(0, end)
        tcf13 = int(self.var13.get()) * int(self.zspl.get())
        self.T13.insert(0, tcf13)
        global com_TCF

        com_TCF = int(self.T1.get()) + int(self.T2.get()) + int(self.T3.get()) + int(self.T4.get()) + int(
            self.T5.get()) + float(self.T6.get()) + float(self.T7.get()) + int(self.T8.get()) + int(
            self.T9.get()) + int(self.T10.get()) + int(self.T11.get()) + int(self.T12.get()) + int(self.T13.get())
        end = len(self.T14.get())
        self.T14.delete(0, end)
        self.T14.insert(0, com_TCF)

    def TCF_done(self):
        global com_TCF
        self.compute_TCF()
        self.TCF_dict = {"TCF2":self.comboExample2ds.get(),'TCF3':self.comboExample3per.get(),"TCF4":self.comboExample4enu.get(),\
                         "TCF5":self.comboExample5cip.get(),"TCF6":self.comboExample6reu.get(),"TCF7":self.comboExample7eti.get(),"TCF8":self.comboExample8etu.get(),\
                         "TCF9":self.comboExample9port.get(),"TCF10":self.comboExample10etc.get(),"TCF11":self.comboExample11conc.get(),"TCF12":self.comboExample12ssf.get(),"TCF13":self.comboExample13pdated.get(),"TCF14":self.comboExample14spl.get(),\
                         "T1":self.T1.get(),"T2":self.T2.get(),"T3":self.T3.get(),"T4":self.T4.get(),"T5":self.T5.get(),"T6":self.T6.get(),"T7":self.T7.get(),"T8":self.T8.get(),"T9":self.T9.get(),"T10":self.T10.get(),"T11":self.T11.get(),"T12":self.T12.get(),"T13":self.T13.get(),"T14":self.T14.get()}
        self.newwin.destroy()
        end = len(self.TCF_value.get())
        self.TCF_value.delete(0, end)
        res1 = 0.6 + (0.01 * com_TCF)
        self.TCF_value.insert(0, res1)

    def compute_TCF(self):
        pass

    def ECF(self):
        self.newwin2 = Toplevel(root)
        self.newwin2.title('New Window')
        self.newwin2.geometry("800x800")
        self.newwin2.resizable(0, 0)

        assign1 = tk.Label(self.newwin2,
                           text="Assign a value from 0 to 5 for each of the following Value Adjustment Factors:")
        EC1 = tk.Label(self.newwin2, text=" E1       Familiarity with UML ")
        EC2 = tk.Label(self.newwin2, text="E2        Application exerience ")
        EC3 = tk.Label(self.newwin2, text="E3        Object oriented experience")
        EC4 = tk.Label(self.newwin2, text="E4        Lead analyst capability")
        EC5 = tk.Label(self.newwin2, text="E5       Motivation")
        EC6 = tk.Label(self.newwin2, text="E6      Stable requirements")
        EC7 = tk.Label(self.newwin2, text="E7     Part-time workers")
        EC8 = tk.Label(self.newwin2, text="E8       Difficult progamming language")

        self.ECF1 = DoubleVar()
        ECFlab1= tk.Label(self.newwin2, textvariable=self.ECF1)
        self.ECF1.set(1.5)
        self.ECF2 = DoubleVar()
        ECFlab2 = tk.Label(self.newwin2, textvariable=self.ECF2)
        self.ECF2.set(0.5)
        self.ECF3 = IntVar()
        ECFlab3 = tk.Label(self.newwin2, textvariable=self.ECF3)
        self.ECF3.set(1)
        self.ECF4 = DoubleVar()
        ECFlab4 = tk.Label(self.newwin2, textvariable=self.ECF4)
        self.ECF4.set(0.5)
        self.ECF5 = IntVar()
        ECFlab5 = tk.Label(self.newwin2, textvariable=self.ECF5)
        self.ECF5.set(1)
        self.ECF6 = IntVar()
        ECFlab6 = tk.Label(self.newwin2, textvariable=self.ECF6)
        self.ECF6.set(2)
        self.ECF7 = IntVar()
        ECFlab7 = tk.Label(self.newwin2, textvariable=self.ECF7)
        self.ECF7.set(0)
        self.ECF8 = IntVar()
        ECFlab8 = tk.Label(self.newwin2, textvariable=self.ECF8)
        self.ECF8.set(2)

        TotalFactors1 = tk.Button(self.newwin2, text="Total Factors", command=self.entry1)
        doneButton1 = tk.Button(self.newwin2, text=f"Done", command=self.ECF_done)

        ECFlab1.place(x=300, y=50)
        ECFlab2.place(x=300, y=80)
        ECFlab3.place(x=300, y=110)
        ECFlab4.place(x=300, y=140)
        ECFlab5.place(x=300, y=170)
        ECFlab6.place(x=300, y=200)
        ECFlab7.place(x=300, y=230)
        ECFlab8.place(x=300, y=260)

        self.CEC1 = tk.IntVar()
        self.CEC2 = tk.IntVar()
        self.CEC3 = tk.IntVar()
        self.CEC4 = tk.IntVar()
        self.CEC5 = tk.IntVar()
        self.CEC6 = tk.IntVar()
        self.CEC7 = tk.IntVar()
        self.CEC8 = tk.IntVar()

        self.CEC1.set(0)
        self.CEC2.set(0)
        self.CEC3.set(0)
        self.CEC4.set(0)
        self.CEC5.set(0)
        self.CEC6.set(0)
        self.CEC7.set(0)
        self.CEC8.set(0)

        self.comboExample2EC1 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC1)
        self.comboExample3EC2 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC2)
        self.comboExample4EC3 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC3)
        self.comboExample5EC4 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC4)
        self.comboExample6EC5 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC5)
        self.comboExample7EC6 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC6)
        self.comboExample8EC7 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC7)
        self.comboExample9EC8 = ttk.Combobox(self.newwin2, width=5, values=([0, 1, 2, 3, 4, 5]), textvariable=self.CEC8)
        assign1.place(x=0, y=20)
        EC1.place(x=0, y=50)
        EC2.place(x=0, y=80)
        EC3.place(x=0, y=110)
        EC4.place(x=0, y=140)
        EC5.place(x=0, y=170)
        EC6.place(x=0, y=200)
        EC7.place(x=0, y=230)
        EC8.place(x=0, y=260)
        TotalFactors1.place(x=0, y=470)
        doneButton1.place(x=0, y=500)

        self.comboExample2EC1.place(x=500, y=50)
        self.comboExample3EC2.place(x=500, y=80)
        self.comboExample4EC3.place(x=500, y=110)
        self.comboExample5EC4.place(x=500, y=140)
        self.comboExample6EC5.place(x=500, y=170)
        self.comboExample7EC6.place(x=500, y=200)
        self.comboExample8EC7.place(x=500, y=230)
        self.comboExample9EC8.place(x=500, y=260)

        self.comboExample2EC1.current(0)
        self.comboExample3EC2.current(0)
        self.comboExample4EC3.current(0)
        self.comboExample5EC4.current(0)
        self.comboExample6EC5.current(0)
        self.comboExample7EC6.current(0)
        self.comboExample8EC7.current(0)
        self.comboExample9EC8.current(0)

        if self.saved_data and self.saved_data["ECF_dict"]:
            self.comboExample2EC1.current(int(self.saved_data['ECF_dict']['EC1']))
            self.comboExample3EC2.current(int(self.saved_data['ECF_dict']['EC2']))
            self.comboExample4EC3.current(int(self.saved_data['ECF_dict']['EC3']))
            self.comboExample5EC4.current(int(self.saved_data['ECF_dict']['EC4']))
            self.comboExample6EC5.current(int(self.saved_data['ECF_dict']['EC5']))
            self.comboExample7EC6.current(int(self.saved_data['ECF_dict']['EC6']))
            self.comboExample8EC7.current(int(self.saved_data['ECF_dict']['EC7']))
            self.comboExample9EC8.current(int(self.saved_data['ECF_dict']['EC8']))

        E1 = IntVar()
        if self.saved_data:
            E1.set(self.saved_data['ECF_dict']['E1'])

        E2 = IntVar()
        if self.saved_data:
            E2.set(self.saved_data['ECF_dict']['E2'])

        E3 = IntVar()
        if self.saved_data:
            E3.set(self.saved_data['ECF_dict']['E3'])

        E4 = IntVar()
        if self.saved_data:
            E4.set(self.saved_data['ECF_dict']['E4'])

        E5 = IntVar()
        if self.saved_data:
            E5.set(self.saved_data['ECF_dict']['E5'])

        E6 = IntVar()
        if self.saved_data:
            E6.set(self.saved_data['ECF_dict']['E6'])

        E7 = IntVar()
        if self.saved_data:
            E7.set(self.saved_data['ECF_dict']['E7'])

        E8 = IntVar()
        if self.saved_data:
            E8.set(self.saved_data['ECF_dict']['E8'])

        E14 = IntVar()
        if self.saved_data:
            E14.set(self.saved_data['ECF_dict']['E14'])

        self.E1 = Entry(self.newwin2, width=7,textvariable =E1)
        self.E2 = Entry(self.newwin2, width=7,textvariable=E2)
        self.E3 = Entry(self.newwin2, width=7,textvariable=E3)
        self.E4 = Entry(self.newwin2, width=7,textvariable=E4)
        self.E5 = Entry(self.newwin2, width=7,textvariable=E5)
        self.E6 = Entry(self.newwin2, width=7,textvariable=E6)
        self.E7 = Entry(self.newwin2, width=7,textvariable=E7)
        self.E8 = Entry(self.newwin2, width=7,textvariable=E8)
        self.E14 = Entry(self.newwin2,width=7,textvariable=E14)

        self.E1.place(x=600, y=50)
        self.E2.place(x=600, y=80)
        self.E3.place(x=600, y=110)
        self.E4.place(x=600, y=140)
        self.E5.place(x=600, y=170)
        self.E6.place(x=600, y=200)
        self.E7.place(x=600, y=230)
        self.E8.place(x=600, y=260)
        self.E14.place(x=600, y=470)

    def entry1(self):

        end = len(self.E1.get())
        self.E1.delete(0, end)
        varEC1 = float(self.ECF1.get()) * int(self.CEC1.get())
        self.E1.insert(0, varEC1)
        end = len(self.E2.get())
        self.E2.delete(0, end)
        varEC2 = float(self.ECF2.get()) * int(self.CEC2.get())
        self.E2.insert(0, varEC2)
        end = len(self.E3.get())
        self.E3.delete(0, end)
        varEC3 = int(self.ECF3.get()) * int(self.CEC3.get())
        self.E3.insert(0, varEC3)
        end = len(self.E4.get())
        self.E4.delete(0, end)
        varEC4 = float(self.ECF4.get()) * int(self.CEC4.get())
        self.E4.insert(0, varEC4)
        end = len(self.E5.get())
        self.E5.delete(0, end)
        varEC5 = int(self.ECF5.get()) * int(self.CEC5.get())
        self.E5.insert(0, varEC5)
        end = len(self.E6.get())
        self.E6.delete(0, end)
        varEC6 = int(self.ECF6.get()) * int(self.CEC6.get())
        self.E6.insert(0, varEC6)
        end = len(self.E7.get())
        self.E7.delete(0, end)
        varEC7 = int(self.ECF7.get()) * int(self.CEC7.get())
        self.E7.insert(0, varEC7)
        end = len(self.E8.get())
        self.E8.delete(0, end)
        varEC8 = int(self.ECF8.get()) * int(self.CEC8.get())
        self.E8.insert(0, varEC8)

        global com_ECF

        com_ECF = float(self.E1.get()) + float(self.E2.get()) + int(self.E3.get()) + float(self.E4.get()) + int(
            self.E5.get()) + int(self.E6.get()) + int(self.E7.get()) + int(self.E8.get())
        end = len(self.E14.get())
        self.E14.delete(0, end)
        self.E14.insert(0, com_ECF)

    def ECF_done(self):
        global com_TCF
        self.ECF_dict = {"EC1":self.comboExample2EC1.get(),"EC2":self.comboExample3EC2.get(),"EC3":self.comboExample4EC3.get(),\
                         "EC4":self.comboExample5EC4.get(),"EC5":self.comboExample6EC5.get(),"EC6":self.comboExample7EC6.get(),"EC7":self.comboExample8EC7.get(),"EC8":self.comboExample9EC8.get(),"E1":self.E1.get(),"E2":self.E2.get(),\
                         "E3":self.E3.get(),"E4":self.E4.get(),"E5":self.E5.get(),"E6":self.E6.get(),"E7":self.E7.get(),"E8":self.E8.get(),"E14":self.E14.get()}

        self.newwin2.destroy()
        end = len(self.ECF_value.get())
        self.ECF_value.delete(0, end)
        res2 = 1.4 + (-0.03 * com_ECF)
        self.ECF_value.insert(0, res2)

    def UUCW(self):
        self.newwin3 = Toplevel(root)
        self.newwin3.title('New Window')
        self.newwin3.geometry("800x800")
        self.newwin3.resizable(0, 0)

        UUlab1 = tk.Label(self.newwin3,text="simple_count")
        UUlab2 = tk.Label(self.newwin3,text="average_count")
        UUlab3 = tk.Label(self.newwin3,text="complex_count")

        UUEnt1 = IntVar()
        if self.saved_data:
            UUEnt1.set(self.saved_data['UUCW_dict']["UUCW1"])
        UUEnt2 = IntVar()
        if self.saved_data:
            UUEnt2.set(self.saved_data['UUCW_dict']["UUCW2"])
        UUEnt3 = IntVar()
        if self.saved_data:
            UUEnt3.set(self.saved_data['UUCW_dict']["UUCW3"])
        UUEnt4 = IntVar()
        if self.saved_data:
            UUEnt4.set(self.saved_data['UUCW_dict']["UUCW4"])
        UUEnt5 = IntVar()
        if self.saved_data:
            UUEnt5.set(self.saved_data['UUCW_dict']["UUCW5"])
        UUEnt6 = IntVar()
        if self.saved_data:
            UUEnt6.set(self.saved_data['UUCW_dict']["UUCW6"])

        self.UUEnt1 = Entry(self.newwin3,width=7,textvariable=UUEnt1)
        self.UUEnt2 =Entry(self.newwin3,width=7,textvariable=UUEnt2)
        self.UUEnt3 = Entry(self.newwin3,width=7,textvariable=UUEnt3)

        UUlab1.place(x=0,y=50)
        UUlab2.place(x=0,y=80)
        UUlab3.place(x=0,y=110)

        self.UUEnt1.place(x=100,y=50 )
        self.UUEnt2.place(x=100,y=80)
        self.UUEnt3.place(x=100,y=110)

        self.UUCW1 = IntVar()
        UUlabel1 = tk.Label(self.newwin3, textvariable=self.UUCW1)
        self.UUCW1.set(5)
        self.UUCW2 = IntVar()
        UUlabel2 = tk.Label(self.newwin3, textvariable=self.UUCW2)
        self.UUCW2.set(10)
        self.UUCW3 = IntVar()
        UUlabel3 = tk.Label(self.newwin3, textvariable=self.UUCW3)
        self.UUCW3.set(15)
        UUlabel1.place(x=200,y=50)
        UUlabel2.place(x=200,y=80)
        UUlabel3.place(x=200,y=110)

        self.UUEnt4 = Entry(self.newwin3, width=7,textvariable=UUEnt4)
        self.UUEnt5 = Entry(self.newwin3, width=7,textvariable=UUEnt5)
        self.UUEnt6 = Entry(self.newwin3, width=7,textvariable=UUEnt6)

        self.UUEnt4.place(x=300,y=50)
        self.UUEnt5.place(x=300,y=80)
        self.UUEnt6.place(x=300,y=110)
        UUCW_but = tk.Button(self.newwin3, text="UUCW_Button", command=self.UUCW_fun)
        UUCW_but.place(x=0,y=200)


    def UUCW_fun(self):
        end = len(self.UUEnt4.get())
        self.UUEnt4.delete(0, end)
        UUCWres1 = int(self.UUEnt1.get()) * int(self.UUCW1.get())
        self.UUEnt4.insert(0,UUCWres1)
        end = len(self.UUEnt5.get())
        self.UUEnt5.delete(0, end)
        UUCWres2 = int(self.UUEnt2.get()) * int(self.UUCW2.get())
        self.UUEnt5.insert(0, UUCWres2)
        end = len(self.UUEnt6.get())
        self.UUEnt6.delete(0, end)
        UUCWres3 = int(self.UUEnt3.get()) * int(self.UUCW3.get())
        self.UUEnt6.insert(0, UUCWres3)
        global UUCW_comp
        UUCW_comp = int(self.UUEnt4.get()) + int(self.UUEnt5.get()) + int(self.UUEnt6.get())
        end = len(self.UUCW_value.get())
        self.UUCW_value.delete(0, end)
        self.UUCW_value.insert(0, UUCW_comp)
        self.UUCW_dict = {"UUCW1": self.UUEnt1.get(),"UUCW2":self.UUEnt2.get(),"UUCW3":self.UUEnt3.get(),"UUCW4":self.UUEnt4.get(),"UUCW5":self.UUEnt5.get(),"UUCW6":self.UUEnt6.get()}
        self.newwin3.destroy()

    def UAW(self):
        self.newwin4 = Toplevel(root)
        self.newwin4.title('New Window')
        self.newwin4.geometry("800x800")
        self.newwin4.resizable(0, 0)

        UAlab1 = tk.Label(self.newwin4, text="simple_count")
        UAlab2 = tk.Label(self.newwin4, text="average_count")
        UAlab3 = tk.Label(self.newwin4, text="complex_count")
        UAEnt1 = IntVar()
        if self.saved_data:
            UAEnt1.set(self.saved_data['UAW_dict']["UAW1"])
        UAEnt2 = IntVar()
        if self.saved_data:
            UAEnt2.set(self.saved_data['UAW_dict']["UAW2"])
        UAEnt3 = IntVar()
        if self.saved_data:
            UAEnt3.set(self.saved_data['UAW_dict']["UAW3"])
        UAEnt4 = IntVar()
        if self.saved_data:
            UAEnt4.set(self.saved_data['UAW_dict']["UAW4"])
        UAEnt5 = IntVar()
        if self.saved_data:
            UAEnt5.set(self.saved_data['UAW_dict']["UAW5"])
        UAEnt6 = IntVar()
        if self.saved_data:
            UAEnt6.set(self.saved_data['UAW_dict']["UAW6"])

        self.UAEnt1 = Entry(self.newwin4, width=7,textvariable = UAEnt1)
        self.UAEnt2 = Entry(self.newwin4, width=7,textvariable = UAEnt2)
        self.UAEnt3 = Entry(self.newwin4, width=7,textvariable = UAEnt3)

        UAlab1.place(x=0, y=50)
        UAlab2.place(x=0, y=80)
        UAlab3.place(x=0, y=110)

        self.UAEnt1.place(x=100, y=50)
        self.UAEnt2.place(x=100, y=80)
        self.UAEnt3.place(x=100, y=110)

        self.UACW1 = IntVar()
        UAlabel1 = tk.Label(self.newwin4, textvariable=self.UACW1)
        self.UACW1.set(1)
        self.UACW2 = IntVar()
        UAlabel2 = tk.Label(self.newwin4, textvariable=self.UACW2)
        self.UACW2.set(2)
        self.UACW3 = IntVar()
        UAlabel3 = tk.Label(self.newwin4, textvariable=self.UACW3)
        self.UACW3.set(3)
        UAlabel1.place(x=200, y=50)
        UAlabel2.place(x=200, y=80)
        UAlabel3.place(x=200, y=110)

        self.UAEnt4 = Entry(self.newwin4, width=7,textvariable = UAEnt4)
        self.UAEnt5 = Entry(self.newwin4, width=7,textvariable = UAEnt5)
        self.UAEnt6 = Entry(self.newwin4, width=7,textvariable = UAEnt6)

        self.UAEnt4.place(x=300, y=50)
        self.UAEnt5.place(x=300, y=80)
        self.UAEnt6.place(x=300, y=110)

        UACW_but = tk.Button(self.newwin4, text="UACW_Button", command=self.UACW_fun)
        UACW_but.place(x=0, y=200)

    def UACW_fun(self):
        end = len(self.UAEnt4.get())
        self.UAEnt4.delete(0, end)
        UACWres1 = int(self.UAEnt1.get()) * int(self.UACW1.get())
        self.UAEnt4.insert(0,UACWres1)
        end = len(self.UAEnt5.get())
        self.UAEnt5.delete(0, end)
        UACWres2 = int(self.UAEnt2.get()) * int(self.UACW2.get())
        self.UAEnt5.insert(0, UACWres2)
        end = len(self.UAEnt6.get())
        self.UAEnt6.delete(0, end)
        UACWres3 = int(self.UAEnt3.get()) * int(self.UACW3.get())
        self.UAEnt6.insert(0, UACWres3)
        global UACW_comp
        UACW_comp = int(self.UAEnt4.get()) + int(self.UAEnt5.get()) + int(self.UAEnt6.get())
        end = len(self.UAW_value.get())
        self.UAW_value.delete(0, end)
        self.UAW_value.insert(0, UACW_comp)
        self.UAW_dict = {"UAW1":self.UAEnt1.get(),"UAW2":self.UAEnt2.get(),"UAW3":self.UAEnt3.get(),"UAW4":self.UAEnt4.get(),"UAW5":self.UAEnt5.get(),"UAW6":self.UAEnt6.get()}
        self.newwin4.destroy()
    def UCP(self):
        global UCP_comp
        UCP_comp = (int(self.UAW_value.get()) + int(self.UUCW_value.get()) * float(self.TCF_value.get()) *float(self.ECF_value.get()))
        # * float(self.TCF_value.get()) *  float(self.ECF_value.get())
        print(type(UCP_comp), UCP_comp)
        end = len(self.UCP_value.get())
        self.UCP_value.delete(0,end)
        self.UCP_value.insert(0,UCP_comp)

    def Est_hrs1(self):
        global UCP_comp
        Est_hrs2 = (float(self.UCP_value.get()) * float(self.PF_value.get()))
        # * float(self.TCF_value.get()) *  float(self.ECF_value.get())
        end = len(self.Est_hrs.get())
        self.Est_hrs.delete(0,end)
        self.Est_hrs.insert(0,Est_hrs2)

    def Est_LOC1(self):
        Est_LOC2 = (float(self.UCP_value.get()) * float(self.LOC_PER.get()))
        # * float(self.TCF_value.get()) *  float(self.ECF_value.get())
        end = len(self.Est_Loc.get())
        self.Est_Loc.delete(0, end)
        self.Est_Loc.insert(0, Est_LOC2)

    def Per_Mon1(self):
        Per_Mon2 = (float(self.Est_Loc.get()) / float(self.LOC_PM.get()))
        # * float(self.TCF_value.get()) *  float(self.ECF_value.get())
        end = len(self.Per_Mon.get())
        self.Per_Mon.delete(0, end)
        self.Per_Mon.insert(0, Per_Mon2)


    def changeLanguage(self):
        self.newwin1 = Toplevel(root)
        self.newwin1.title('Programming language')
        self.newwin1.geometry("400x400")
        self.newwin1.resizable(0, 0)

        def close_window():
            global language
            self.newwin1.destroy()
            if self.current_language:
                self.current_language.delete(0, len(self.current_language.get()))
                self.current_language.insert(0, language)


        self.lang1 = Radiobutton(self.newwin1, text="Assembler", command=self.myRadios1, variable=self.mycheck1,
                                 value="Assembler")
        self.lang2 = Radiobutton(self.newwin1, text="Ada", command=self.myRadios1, variable=self.mycheck1, value="Ada")
        self.lang3 = Radiobutton(self.newwin1, text="C", command=self.myRadios1, variable=self.mycheck1, value="C")
        self.lang4 = Radiobutton(self.newwin1, text="C++", command=self.myRadios1, variable=self.mycheck1, value="C++")
        self.lang5 = Radiobutton(self.newwin1, text="C#", command=self.myRadios1, variable=self.mycheck1, value="C#")
        self.lang6 = Radiobutton(self.newwin1, text="COBOL", command=self.myRadios1, variable=self.mycheck1, value="COBOL")
        self.lang7 = tk.Radiobutton(self.newwin1, text="FORTRAN", command=self.myRadios1, variable=self.mycheck1,value="FORTRAN")
        self.lang8 = tk.Radiobutton(self.newwin1, text="HTML", command=self.myRadios1, variable=self.mycheck1, value="HTML")
        self.lang9 = tk.Radiobutton(self.newwin1, text="JAVA", command=self.myRadios1, variable=self.mycheck1,value="JAVA")
        self.lang10 = tk.Radiobutton(self.newwin1, text="JavaScript", command=self.myRadios1, variable=self.mycheck1,value="JavaScript")
        self.lang11 = tk.Radiobutton(self.newwin1, text="VBScript", command=self.myRadios1, variable=self.mycheck1,value="VBScript")
        self.lang12 = tk.Radiobutton(self.newwin1, text="VisualBasic", command=self.myRadios1, variable=self.mycheck1,value="VisualBasic")
        self.w = tk.Label(self.newwin1, text="select one Language")

        self.done = tk.Button(self.newwin1, text=f"Done n.", command=close_window)
        display = Label(self.newwin1, text="Hello, " + self.query.get())  # getting parameter via query var
        self.w.place(x=10,y =20)
        self.lang1.place(x=10,y=40)
        self.lang2.place(x=10,y=60)
        self.lang3.place(x=10,y=80)
        self.lang4.place(x=10,y=100)
        self.lang5.place(x=10,y=120)
        self.lang6.place(x=10,y=140)
        self.lang7.place(x=10,y=160)
        self.lang8.place(x=10,y=180)
        self.lang9.place(x=10,y=200)
        self.lang10.place(x=10,y=220)
        self.lang11.place(x=10,y=240)
        self.lang12.place(x=10,y=260)
        self.done.place(x=10,y=280)



    def myRadios1(self):
        global language
        language = str(self.mycheck1.get())
        print(language)

    def mainFrame(self, root):
        global project_name
        self.query = StringVar()
        self.query1 = StringVar()# passing parameter via query var

        root.title('CECS 543 Metrics Suite' + self.proj_name.get() )
        root.geometry("1000x800")
        root.resizable(0, 0)

        menubar = Menu(root)
        root.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New",command=self.project)
        filemenu.add_command(label="Open",command=self.browse_file )
        filemenu.add_command(label="Save", command=self.save_fn)



        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)


        editmenu.add_separator()



        menubar.add_cascade(label="Edit", menu=editmenu)

        preferencemenu = Menu(menubar,tearoff=0)
        preferencemenu.add_command(label="Languages", command=self.changeLanguage)
        menubar.add_cascade(label="Preferences",menu=preferencemenu)



        metricsmenu = Menu(menubar,tearoff=0)
        a = Menu(metricsmenu, tearoff=0)
        metricsmenu.add_cascade(label="Function point",menu=a)

        a.add_command(label="Enter FP Data",command=self.data_point)
        menubar.add_cascade(label="Metrics",menu=metricsmenu)
        metricsmenu.add_cascade(label="UCP",command=self.tab1)
        metricsmenu.add_cascade(label="SMI", command=self.tab2)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help")


    def project(self):
        self.prowin = Toplevel(root)
        self.prowin.title('Project Window')
        self.prowin.geometry("400x400")
        Label(self.prowin, text="Metrics Suite New Project").grid(row=5, column=6)
        Label(self.prowin, text="Project Name").grid(row=9, column=6)
        Label(self.prowin, text="Product Name").grid(row=13, column=6)
        Label(self.prowin, text="Creator").grid(row=17, column=6)
        Label(self.prowin, text="Comments").grid(row=21, column=6)
        proj_name = StringVar()
        #if proj_name.get() == "":
         #   messagebox.showwarning("warning","Create a project")
        #else:
        self.projna = Entry(self.prowin,width=10,textvariable =self.proj_name)
        self.prodna = Entry(self.prowin, width=10)
        self.creator = Entry(self.prowin, width=10)
        self.comments = Entry(self.prowin, width=10)
        self.projna.grid(row=9,column=10)
        self.prodna.grid(row=13, column=10)
        self.creator.grid(row=17, column=10)
        self.comments.grid(row=21, column=10)
        self.doneButton = tk.Button(self.prowin, text="Ok",command=self.proj_ok)
        self.doneButton.grid(row=24,column=10)
        self.cancel = tk.Button(self.prowin, text=f"Cancel.",command=self.close_proj)
        self.cancel.grid(row=24,column=15)

    def proj_ok(self):
        global project_name
        project_name = (self.projna.get())
        root.title('CECS 543 Metrics Suite' + '-' + self.proj_name.get() + '.ms')
        self.prowin.destroy()


    def close_proj(self):
        self.prowin.destroy()



    def data_point(self):
        self.fpwin = Toplevel(root)
        self.fpwin.title('Input')
        self.fpwin.geometry("400x400")
        Label(self.fpwin,text="Name of this FP").grid(row=10,column=15)
        self.fpname = Entry(self.fpwin,width=10).grid(row=12,column=15)
        self.doneButton1 = tk.Button(self.fpwin, text="Ok",command=self.tab)
        self.doneButton1.grid(row=14, column=15)
        self.cancel1 = tk.Button(self.fpwin, text="Cancel")
        self.cancel1.grid(row=14, column=17)

        tabControl = ttk.Notebook(root)
        global tab1
        global tab2
        global tab3
        tab1 = ttk.Frame(tabControl, width=600, height=600)
        tabControl.add(tab1, text='Tab 1')

        tab2 = ttk.Frame(tabControl, width=600, height=600)
        tabControl.add(tab2, text='Tab 2')
        tab3 = ttk.Frame(tabControl, width=600, height=600)
        tabControl.add(tab3, text='Tab 3')
        tabControl.pack(expand=1, fill="both")


    def tab(self):
        global project_name
        self.fpwin.destroy()

        Label(tab1, text="Weighting Factors").grid(row=5, column=6)
        myLabel8 = Label(tab1, text="Simple").grid(row=6, column=6)
        myLabel9 = Label(tab1, text="Average").grid(row=6, column=7)
        myLabel10 = Label(tab1, text="Complex").grid(row=6, column=8)
        myLabel2 = Label(tab1, text="External Input").grid(row=8, column=0)
        myLabel3 = Label(tab1, text="External Output").grid(row=9, column=0)
        myLabel4 = Label(tab1, text="External Inquries").grid(row=10, column=0)
        myLabel5 = Label(tab1, text="Internal Logical Files").grid(row=11, column=0)
        myLabel6 = Label(tab1, text="External Interface files").grid(row=12, column=0)
        myLabel7 = Label(tab1, text="Total Count").grid(row=13, column=0)
        mylabel8 = Label(tab1, text="Current Languages").grid(row=20, column=5)

        # TODO: Complete the fill for all values
        external_input = IntVar()
        if self.saved_data:
            external_input.set(self.saved_data['external_input'])
        else:
            external_input.set(0)
        external_output_inp = IntVar()
        if self.saved_data:
            external_output_inp.set(self.saved_data['external_output_inp'])
        else:
            external_output_inp.set(0)
        external_inquries_inp = IntVar()
        if self.saved_data:
            external_inquries_inp.set(self.saved_data['external_inquries_inp'])
        else:
            external_inquries_inp.set(0)
        internal_logical_files_inp = IntVar()
        if self.saved_data:
            internal_logical_files_inp.set(self.saved_data['internal_logical_files_inp'])
        else:
            internal_logical_files_inp.set(0)

        ext_interface_files_inp = IntVar()
        if self.saved_data:
            ext_interface_files_inp.set(self.saved_data['ext_interface_files_inp'])
        else:
            ext_interface_files_inp.set(0)
        external_inp_output = IntVar()
        if self.saved_data:
            external_inp_output.set(self.saved_data['external_inp_output'])
        else:
            external_inp_output.set(0)
        external_op_output = IntVar()
        if self.saved_data:
            external_op_output.set(self.saved_data['external_op_output'])
        else:
            external_op_output.set(0)
        external_inq_output = IntVar()
        if self.saved_data:
            external_inq_output.set(self.saved_data['external_inq_output'])
        else:
            external_inq_output.set(0)
        internal_logical_ouptut = IntVar()
        if self.saved_data:
            internal_logical_ouptut.set(self.saved_data['internal_logical_ouptut'])
        else:
            internal_logical_ouptut.set(0)
        ext_interface_files_output = IntVar()
        if self.saved_data:
            ext_interface_files_output.set(self.saved_data['ext_interface_files_output'])
        else:
            ext_interface_files_output.set(0)
        total_count = IntVar()
        if self.saved_data:
            total_count.set(self.saved_data['total_count'])
        else:
            total_count.set(0)
        compute_fp_entry = IntVar()
        if self.saved_data:
            compute_fp_entry.set(self.saved_data['compute_fp_entry'])
        else:
            compute_fp_entry.set(0)
        value_adjustment = IntVar()
        if self.saved_data:
            value_adjustment.set(self.saved_data['value_adjustment'])
        else:
            value_adjustment.set(0)
        code_size = IntVar()
        if self.saved_data:
            code_size.set(self.saved_data['code_size'])
        else:
            code_size.set(0)

        #vcmd = tab1.register(callback)
        vcmd = (tab1.register(self.validate1),
                 '%d', '%i','% P', '%s', '%S', '%v', '%V', '%W')
        self.external_input = Entry(tab1, width=5, textvariable=external_input,validate="key",validatecommand=vcmd)

        self.external_output_inp = Entry(tab1, width=5, textvariable=external_output_inp)
        self.external_inquries_inp = Entry(tab1, width=5, textvariable=external_inquries_inp)
        self.internal_logical_files_inp = Entry(tab1, width=5, textvariable=internal_logical_files_inp)
        self.ext_interface_files_inp = Entry(tab1, width=5, textvariable=ext_interface_files_inp)
        self.external_inp_output = Entry(tab1, width=5, textvariable=external_inp_output)
        self.external_op_output = Entry(tab1, width=5, textvariable=external_op_output)
        self.external_inq_output = Entry(tab1, width=5, textvariable=external_inq_output)
        self.internal_logical_output = Entry(tab1, width=5, textvariable=internal_logical_ouptut)
        self.ext_interface_files_output = Entry(tab1, width=5, textvariable=ext_interface_files_output)
        #print(self.saved_data.get('current_language'))
        if language and not self.saved_data['current_language']:
            self.lang.set("None")
        elif self.saved_data:
            self.lang.set(self.saved_data['current_language'])
        else:
            self.lang.set(language)
        self.current_language = Entry(tab1, width=5, textvariable=self.lang)
        self.current_language.delete(0, len(language))
        self.current_language.insert(0, language)
        self.total_count = Entry(tab1, width=5, textvariable=total_count)
        self.compute_fp_entry = Entry(tab1, width=5, textvariable=compute_fp_entry)
        if not self.saved_data:
            self.text_entry.set(0)
        else:
            self.text_entry.set(self.saved_data['value_adjustment'])
        self.value_adjustment = Entry(tab1, width=5, textvariable=self.text_entry)
        self.code_size = Entry(tab1, width=5, textvariable=code_size)

        self.external_input.grid(row=8, column=1)
        self.external_output_inp.grid(row=9, column=1)
        self.external_inquries_inp.grid(row=10, column=1)
        self.internal_logical_files_inp.grid(row=11, column=1)
        self.ext_interface_files_inp.grid(row=12, column=1)
        self.external_inp_output.grid(row=8, column=30)
        self.external_op_output.grid(row=9, column=30)
        self.external_inq_output.grid(row=10, column=30)
        self.internal_logical_output.grid(row=11, column=30)
        self.ext_interface_files_output.grid(row=12, column=30)
        self.current_language.grid(row=20, column=7)
        self.total_count.grid(row=13, column=30)
        self.compute_fp_entry.grid(row=16, column=30)
        self.value_adjustment.grid(row=18, column=30)
        self.code_size.grid(row=20, column=30)
        #self.external_input.config(validate="key",
#                                   validatecommand=(vcmd, '% P'))
        self.myradio1 = IntVar()
        self.myradio2 = IntVar()
        self.myradio3 = IntVar()
        self.myradio4 = IntVar()
        self.myradio5 = IntVar()
        self.myradio1.set(4)
        self.myradio2.set(5)
        self.myradio3.set(4)
        self.myradio4.set(10)
        self.myradio5.set(7)
        Radiobutton(tab1, text='3', command=self.radioGroup1, variable=self.myradio1, padx=20, value=3).grid(row=8,
                                                                                                             column=6)
        Radiobutton(tab1, text='4', command=self.radioGroup1, variable=self.myradio1, padx=20, value=4).grid(row=8,
                                                                                                             column=7)
        Radiobutton(tab1, text='6', command=self.radioGroup1, variable=self.myradio1, padx=20, value=6).grid(row=8,
                                                                                                             column=8)
        Radiobutton(tab1, text='4', command=self.radioGroup2, variable=self.myradio2, padx=20, value=4).grid(row=9,
                                                                                                             column=6)
        Radiobutton(tab1, text='5', command=self.radioGroup2, variable=self.myradio2, padx=20, value=5).grid(row=9,
                                                                                                             column=7)
        Radiobutton(tab1, text='7', command=self.radioGroup2, variable=self.myradio2, padx=20, value=7).grid(row=9,
                                                                                                             column=8)
        Radiobutton(tab1, text='3', command=self.radioGroup3, variable=self.myradio3, padx=20, value=3).grid(row=10,
                                                                                                             column=6)
        Radiobutton(tab1, text='4', command=self.radioGroup3, variable=self.myradio3, padx=20, value=4).grid(row=10,
                                                                                                             column=7)
        Radiobutton(tab1, text='6', command=self.radioGroup3, variable=self.myradio3, padx=20, value=6).grid(row=10,
                                                                                                             column=8)
        Radiobutton(tab1, text='7', command=self.radioGroup4, variable=self.myradio4, padx=20, value=7).grid(row=11,
                                                                                                             column=6)
        Radiobutton(tab1, text='10', command=self.radioGroup4, variable=self.myradio4, padx=20, value=10).grid(row=11,
                                                                                                               column=7)
        Radiobutton(tab1, text='15', command=self.radioGroup4, variable=self.myradio4, padx=20, value=15).grid(row=11,
                                                                                                               column=8)
        Radiobutton(tab1, text='5', command=self.radioGroup5, variable=self.myradio5, padx=20, value=5).grid(row=12,
                                                                                                             column=6)
        Radiobutton(tab1, text='7', command=self.radioGroup5, variable=self.myradio5, padx=20, value=7).grid(row=12,
                                                                                                             column=7)
        Radiobutton(tab1, text='10', command=self.radioGroup5, variable=self.myradio5, padx=20, value=10).grid(row=12,
                                                                                                               column=8)

        myButton = Button(tab1, text="Compute FP", command=self.compute_FP)
        myButton.grid(row=16, column=0)
        button1 = Button(tab1, text="Value Adjustment", command=self.valueAdjustment)
        button1.grid(row=18, column=0)
        myButton = Button(tab1, text="Compute Code Size", command=self.compute_code_size)
        myButton.grid(row=20, column=0)
        button2 = Button(tab1, text=" Change Language", command=self.changeLanguage)
        button2.grid(row=22, column=0)

    def validate1(self, action, index, value_if_allowed,
                  prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
    def validate(self, field):
        try:
            value = int(field)
            if value < 0:
                messagebox.showwaring("Show warning", "this is invalid")
                return True
        except Exception as e:
            messagebox.showwarning("Showwarning", "this is invalid")
            return False


    def close_window(self):
        pass


    def radioGroup1(self):
        self.validate(self.external_input.get())
        # Get the length of the string  self.e1.get()
        end = len(self.external_inp_output.get())
        # Deletes the existing content
        self.external_inp_output.delete(0, end)
        if self.external_input.get():
            external_input = self.external_input.get()
        else:
            external_input = 0
        res = int(self.myradio1.get()) * int(external_input)
        self.external_inp_output.insert(0, res)
        tc_len = len(self.total_count.get())
        self.total_count.delete(0, tc_len)
        self.total_count.insert(0, self.calculate_total_count())


    def radioGroup2(self):
        valid = self.validate(self.external_op_output.get())
        end = len(self.external_op_output.get())
        # Deletes the existing content
        self.external_op_output.delete(0, end)
        if self.external_output_inp.get():
            external_input = self.external_output_inp.get()
        else:
            external_input = 0
        res = int(self.myradio2.get()) * int(external_input)
        self.external_op_output.insert(0, res)
        tc_len = len(self.total_count.get())
        self.total_count.delete(0, tc_len)
        self.total_count.insert(0, self.calculate_total_count())


    def radioGroup3(self):
        valid = self.validate(self.external_inq_output.get())
        end = len(self.external_inq_output.get())
        # Deletes the existing content
        self.external_inq_output.delete(0, end)
        if self.external_inquries_inp.get():
            external_input = self.external_inquries_inp.get()
        else:
            external_input = 0
        res = int(self.myradio3.get()) * int(external_input)
        self.external_inq_output.insert(0, res)
        tc_len = len(self.total_count.get())
        self.total_count.delete(0, tc_len)
        self.total_count.insert(0, self.calculate_total_count())


    def radioGroup4(self):
        valid = self.validate(self.internal_logical_output.get())
        end = len(self.internal_logical_output.get())
        # Deletes the existing content
        self.internal_logical_output.delete(0, end)
        if self.internal_logical_files_inp.get():
            external_input = self.internal_logical_files_inp.get()
        else:
            external_input = 0
        res = int(self.myradio4.get()) * int(external_input)
        self.internal_logical_output.insert(0, res)
        tc_len = len(self.total_count.get())
        self.total_count.delete(0, tc_len)
        self.total_count.insert(0, self.calculate_total_count())


    def radioGroup5(self):
        valid = self.validate(self.ext_interface_files_output.get())
        end = len(self.ext_interface_files_output.get())
        # Deletes the existing content
        self.ext_interface_files_output.delete(0, end)
        if self.ext_interface_files_inp.get():
            external_input = self.ext_interface_files_inp.get()
        else:
            external_input = 0
        res = int(self.myradio5.get()) * int(external_input)
        self.ext_interface_files_output.insert(0, res)
        tc_len = len(self.total_count.get())
        self.total_count.delete(0, tc_len)
        self.total_count.insert(0, self.calculate_total_count())


    def calculate_total_count(self):
        res = 0
        if self.external_inp_output.get() and self.external_op_output.get() and self.external_inq_output.get and self.internal_logical_output.get() and self.ext_interface_files_output.get():
            res = int(self.external_inp_output.get()) + int(self.external_op_output.get()) + int(
                self.external_inq_output.get()) + int(self.internal_logical_output.get()) + int(
                self.ext_interface_files_output.get())
        return res


    def compute_FP(self):
        global com_vaf
        self.radioGroup1()
        self.radioGroup2()
        self.radioGroup3()
        self.radioGroup4()
        self.radioGroup5()
        self.fp = self.calculate_total_count() * (0.65 + (0.01 * com_vaf))
        round(self.fp, 4)
        if self.compute_fp_entry:
            self.compute_fp_entry.delete(0, len(self.compute_fp_entry.get()))
        self.compute_fp_entry.insert(0, self.fp)


    def compute_code_size(self):
        try:
            global language

            # get the value from json
            # change the local path to global path
            print(self.dir_path)
            file_path = os.path.join(self.dir_path, 'ProgrammingLanguages.json')
            print(file_path)
            avg = 0
            with open(file_path) as f:
                data = json.load(f)
                avg = data[language]["Avg"]
            print(avg)
            # function formula
            compute_code_size1 = self.fp * avg

            # return value OF A language
            if self.code_size:
                self.code_size.delete(0, len(self.code_size.get()))
            self.code_size.insert(0, round(compute_code_size1, 4))
        except Exception as e:
            print("Encountered an error")


    def save_fn(self):
        name = tk.filedialog.asksaveasfilename(defaultextension='.ms', initialdir=self.dir_path)
        print(name)
        # Convert the dictionary from tuple to string
        smi_values = {}

        for k, v in self.d1.items():
            for key, value in v.items():
                if key != "obj":
                    smi_values[str(k)] = value
        print(smi_values)
        d = {"external_input": self.external_input.get(),
             "external_output_inp": self.external_output_inp.get(),
             "external_inquries_inp": self.external_inquries_inp.get(),
             "internal_logical_files_inp": self.internal_logical_files_inp.get(),
             "ext_interface_files_inp": self.ext_interface_files_inp.get(),
             "external_inp_output": self.external_inp_output.get(),
             "external_op_output": self.external_op_output.get(),
             "external_inq_output": self.external_inq_output.get(),
             "internal_logical_ouptut": self.internal_logical_output.get(),
             "ext_interface_files_output": self.ext_interface_files_output.get(),
             "total_count": self.total_count.get(),
             "compute_fp_entry": self.fp,
             "value_adjustment": self.value_adjustment.get(),
             "code_size": self.code_size.get(),
             "current_language": self.lang.get(),
             "value_adjustment_window" : self.a2,
             "smi_row_count": self.starting_row_count-1,
             "smi_column_count": 5,

             "smi_values": smi_values,
              "TCF_value":self.TCF_value.get(),
              "ECF_value": self.ECF_value.get(),
              "UUCW_value": self.UUCW_value.get(),
              "UAW_value": self.UAW_value.get(),
              "Est_hrs": self.Est_hrs.get(),
              "Est_Loc": self.Est_Loc.get(),
              "Per_Mon":self.Per_Mon.get(),
              "UCP_value": self.UCP_value.get(),
              "UUCW_dict":self.UUCW_dict,
               "UAW_dict":self.UAW_dict,
               "TCF_dict": self.TCF_dict,
               "ECF_dict": self.ECF_dict
             }
        # Serializing json
        json_object = json.dumps(d, indent=4)
        file_path = os.path.join(self.dir_path, name)

        # Writing to sample.json
        # opens a file path as outfile in write mode
        with open(file_path, "w") as outfile:
            # writes the json object in outfile
            outfile.write(json_object)
        self.save = True


    def browse_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            with open(os.path.join(self.dir_path, self.filename), 'r') as f:
                self.saved_data = json.load(f)
        print("=====================")
        print(self.saved_data)




    def exitProgram(self):
        exit()


    def tab1(self):
        global project_name
        Label(tab2, text="PF").grid(row=28, column=0)
        Label(tab2, text="LOC_per_UCP" ).grid(row=30,column=0)
        Label(tab2, text="LOC/pm").grid(row=32,column=0)
        UUCW_value = IntVar()
        if self.saved_data:
            UUCW_value.set(self.saved_data['UUCW_value'])
        else:
            UUCW_value.set(0)

        TCF_value = IntVar()
        if self.saved_data:
            TCF_value.set(self.saved_data['TCF_value'])
        else:
            TCF_value.set(0)
        ECF_value = IntVar()
        if self.saved_data:
            ECF_value.set(self.saved_data['ECF_value'])
        else:
            ECF_value.set(0)
        UAW_value = IntVar()
        if self.saved_data:
            UAW_value.set(self.saved_data['UAW_value'])
        else:
            UAW_value.set(0)
        UCP_value = IntVar()
        if self.saved_data:
            UCP_value.set(self.saved_data['UCP_value'])
        else:
            UCP_value.set(0)

        Est_hrs = IntVar()
        if self.saved_data:
            Est_hrs.set(self.saved_data['Est_hrs'])
        else:
            Est_hrs.set(0)
        Est_Loc = IntVar()
        if self.saved_data:
            Est_Loc.set(self.saved_data['Est_Loc'])
        else:
            Est_Loc.set(0)
        Per_Mon = IntVar()
        if self.saved_data:
            Per_Mon.set(self.saved_data['Per_Mon'])

        self.UUCW_value = Entry(tab2, width=5, textvariable=UUCW_value)
        self.UAW_value = Entry(tab2, width=5, textvariable=UAW_value)

        self.UCP_value = Entry(tab2, width=5, textvariable=UCP_value)
        self.Est_hrs = Entry(tab2, width=5, textvariable=Est_hrs)
        self.Est_Loc = Entry(tab2, width=5, textvariable=Est_Loc)
        self.Per_Mon = Entry(tab2, width=5, textvariable =Per_Mon)

        textEntry = tk.StringVar()
        textEntry.set("20")
        textEntry1 = tk.StringVar()
        textEntry1.set("100")
        textEntry2 = tk.StringVar()
        textEntry2.set("700")
        self.TCF_value = Entry(tab2, width=5, textvariable=TCF_value)
        self.ECF_value = Entry(tab2, width=5, textvariable=ECF_value)

        self.PF_value = Entry(tab2, width=5,textvariable=textEntry)
        self.LOC_PER = Entry(tab2, width=5, textvariable=textEntry1)
        self.LOC_PM = Entry(tab2, width=5, textvariable=textEntry2)


        self.TCF_value.grid(row=18, column=300)
        self.ECF_value.grid(row=20, column=300)
        self.UUCW_value.grid(row=22, column=300)
        self.UAW_value.grid(row=24, column=300)
        self.UCP_value.grid(row=26, column=300)
        self.PF_value.grid(row=28,column=300)
        self.LOC_PER.grid(row=30,column=300)
        self.LOC_PM.grid(row=32,column=300)
        self.Est_hrs.grid(row=34,column=300)
        self.Est_Loc.grid(row=36,column=300)
        self.Per_Mon.grid(row=38,column=300)

        button1 = Button(tab2, text="Technical comp factor", command=self.TCF)
        button1.grid(row=18, column=0)
        myButton = Button(tab2, text="ECF",command=self.ECF)
        myButton.grid(row=20, column=0)
        myButton = Button(tab2, text="UUCW", command=self.UUCW)
        myButton.grid(row=22, column=0)
        myButton1 = Button(tab2, text="UAW", command=self.UAW)
        myButton1.grid(row=24, column=0)
        myButton3 = Button(tab2, text="UCP", command=self.UCP)
        myButton3.grid(row=26, column=0)
        myButton4 = Button(tab2, text="EstimatedHours", command=self.Est_hrs1)
        myButton4.grid(row=34, column=0)
        myButton5 = Button(tab2, text="EstimatedLOC", command=self.Est_LOC1)
        myButton5.grid(row=36,column=0)
        myButton6 = Button(tab2, text="PersonMonth", command=self.Per_Mon1)
        myButton6.grid(row=38,column=0)

    def but(self):
        global tab3

        self.ending_row_count = self.starting_row_count + 1

        for row in range(self.starting_row_count, self.ending_row_count):
            for column in range(5):
                t = {}
                if row == 0:
                    label = Entry(tab3, text="Heading :" + str(column))
                    label.config(font=("Arial", 14))
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                else:
                    self.label1 = Entry(tab3, text="Row" + str(row) + ",column:" + str(column))
                    self.label1.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    if (row, column) not in self.d1:
                        t["obj"] = self.label1
                        self.d1[(row, column)] = t


        print(self.d1)
        # print(d[(row,column)].get())
        self.current_row = self.starting_row_count
        self.starting_row_count += 1

    def showData(self, btn):
        global tab3

        for i in range(5):
            t1 = {}
            t1 = self.d1.get((self.current_row, i))
            print(t1)
            add_value_to_t1 = {"value": self.d1.get((self.current_row, i)).get("obj").get()}
            t1.update(add_value_to_t1)
            self.d1[(self.current_row, i)] = t1
        print(self.d1)

        if self.d1:

            self.compute()
            # tkinter entry object and insert into entry box
            self.d1.get((self.current_row, 4)).get("obj").insert(0, self.total_modules)
            # t2.update(add_value_to_t2)
            self.d1[(self.current_row, 4)]["value"] = self.total_modules



    def tab2(self):
        global tab3
        # if saved data
        # generate a table using for loop
        smi_from_saved_data = {}
        Label(tab3, text="Software Maturity Index").grid(row=0, column=0)
        Label(tab3, text="SMI").grid(row=1, column=0)
        Label(tab3, text="Modules added").grid(row=1, column=1)
        Label(tab3, text="Modules changed").grid(row=1, column=2)
        Label(tab3, text="Modules deleted").grid(row=1, column=3)
        Label(tab3, text="Total Modules").grid(row=1, column=4)
        if self.saved_data and self.saved_data["smi_values"]:
            for key, value in self.saved_data["smi_values"].items():
                k = tuple(int(num) for num in key.replace('(', '').replace(')', '').replace('..', '').split(', '))
                smi_from_saved_data[k] = value
                # smi_saved_values = self.saved_data["smi_values"]
            print(smi_from_saved_data)
            for row in range(2, self.saved_data["smi_row_count"]+1):
                for column in range(5):

                    label1 = Entry(tab3, text="Row" + str(row) + ",column:" + str(column))
                    label1.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    label1.insert(0, smi_from_saved_data[(row, column)])
                    # if (row, column) not in self.d1:
                    #     t["obj"] = self.label1
                    #     self.d1[(row, column)] = t
        else:
            but1 = Button(tab3, text="Add Row", command=self.but)
            but1.grid(row=500, column=500)
            but2 = Button(tab3, text="Compute")
            but2.grid(row=500, column=550)
            but2['command'] = lambda btn=but2: self.showData(btn)


    def compute(self):

        if self.current_row == 2:
            self.total_modules=int(self.d1.get((self.current_row, 1)).get("value")) - \
                               int(self.d1.get((self.current_row, 3)).get("value"))
        else:
            previous_row = self.current_row - 1
            print(previous_row)
            self.total_modules = int(self.d1.get((previous_row, 4)).get("value")) + \
                                 int(self.d1.get((self.current_row, 1)).get("value")) - \
                                 int(self.d1.get((self.current_row, 3)).get("value"))



            print(self.total_modules)

    def save_fn1(self):
        pass
        # name = tk.filedialog.asksaveasfilename(defaultextension='.ms', initialdir=self.dir_path)
        # json_object = json.dumps(, indent=4)
        # file_path = os.path.join(self.dir_path, name)
        # with open(file_path, "w") as outfile:
        #     outfile.write(json_object)

    def exit(self):
        MsgBox = tk.messagebox.askquestion('Save Project','Yes - Save the file or No-Close the file')
        if MsgBox =='yes' and self.save == False:
            messagebox.showwarning("Warning","Save the file")
        elif self.save == True:
            root.quit()
        else:
            root.quit()




#def callback(input):
 #   if input.isdigit():
  #      print("test")
   # if type(input) != int or input < 0:
    #    messagebox.showwarning("Showwarning", "this is invalid")
    #if input.isdigit():
     #   print(input)
      #  return True

    #elif input is "":
     #   print(input)
      #  return True

    #else:
     #   print(input)
      #  return False

root = Tk()
app = Frames()
app.mainFrame(root)

root.mainloop()