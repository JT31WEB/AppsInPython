import sqlite3

def ConnectData():
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS libbooks(id INTEGER PRIMARY KEY,  MType  text, Ref  text, Tit  text, FNa  text, Sna  text, Adr1  text, Adr2  text, PCd  text, MNo  text, BkID  text,  BkT text, Atr  text, DBo  text, DDu  text, SPr  text,LRF  text, DOD  text, DOnL  text)")
	con.commit()
	con.close()

def addDataRec(MType,Ref,Tit,FNa,Sna,Adr1,Adr2,PCd,MNo,BkID,BkT,Atr,DBo,DDu,SPr,LRF,DOD,DOnL):
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("INSERT INTO  libbooks VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (MType,Ref,Tit,FNa,Sna,Adr1,Adr2,PCd,MNo,BkID,BkT,Atr,DBo,DDu,SPr,LRF,DOD,DOnL))
	con.commit()
	con.close()

def viewData():
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM libbooks")
	rows= cur.fetchall()
	con.close()
	return rows

def deleteRec(id):
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("DELETE FROM libbooks WHERE id=?", (id,))
	con.commit()
	con.close()

def SearchData(MType="",Ref="",Tit="",FNa="",Sna="",Adr1="",Adr2="",PCd="",MNo="",BkID="",BkT="",Atr="",DBo="",DDu="",SPr="",LRF="",DOD="",DOnL=""):
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM libbooks WHERE MTYPE=? OR REF=? OR TIT=? OR FNA=? OR SNA=? OR ADR1=? OR ADR2=? OR PCD=? OR MNO=? OR BKID=? OR BKT=? OR ATR=? OR DBO=? OR DDU=? OR SPR=? OR LRF=? OR DOD=? OR DONL=?", (MType,Ref,Tit,FNa,Sna,Adr1,Adr2,PCd,MNo,BkID,BkT,Atr,DBo,DDu,SPr,LRF,DOD,DOnL))
	rows= cur.fetchall()
	con.close()
	return rows

def UpdateData(MType="",Ref="",Tit="",FNa="",Sna="",Adr1="",Adr2="",PCd="",MNo="",BkID="",BkT="",Atr="",DBo="",DDu="",SPr="",LRF="",DOD="",DOnL=""):
	con = sqlite3.connect("libbooks.db")
	cur = con.cursor()
	cur.execute("UPDATE libbooks SET MTYPE=?, REF=?, TIT=?, FNA=?, SNA=?, ADR1=?, ADR2=?, PCD=?, MNO=?, BKID=?, BKT=?, ATR=?, DBO=?, DDU=?, SPR=?, LRF=?, DOD=?, DONL=?", (MType,Ref,Tit,FNa,Sna,Adr1,Adr2,PCd,MNo,BkID,BkT,Atr,DBo,DDu,SPr,LRF,DOD,DOnL,id))
	rows= cur.fetchall()
	con.close()

ConnectData()



