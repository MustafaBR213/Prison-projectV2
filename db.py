import sqlite3
import openpyxl
import os
import pandas as pd

class DataBase:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        sqlP="""
        CREATE TABLE IF NOT EXISTS Persons(
            id integer primary key,
            firstName text,
            father text,
            lastName text,
            gender text,
            birthYear text,
            address text
        )
        """
        sqlV="""
        CREATE TABLE IF NOT EXISTS Visitings(
            id integer primary key,
            DateVisited text,
            PersonId integer,
            VisitorName text,
            mountOfMinuts integer,
            CONSTRAINT fk_personId  
            FOREIGN KEY (PersonId)  
            REFERENCES Persons(id)  
        )
        """
        sqlO="""
        CREATE TABLE IF NOT EXISTS Offense(
            id integer primary key,
            name text
        )
        """
        sqlC="""
        CREATE TABLE IF NOT EXISTS Convicts(
            id integer primary key,
            fromDate text,
            toDate text,
            PersonId integer,
            OffenseId integer,
            CONSTRAINT fk_perosnId  
            FOREIGN KEY (PersonId)  
            REFERENCES Persons(id),

            CONSTRAINT fk_offencId  
            FOREIGN KEY (OffenseId)  
            REFERENCES Offense(id)    
        )
        """
        sqlD="""
        CREATE TABLE IF NOT EXISTS Dungeon(
            id integer primary key,
            name text,
            size text
        )
        """
        sqlDM="""
        CREATE TABLE IF NOT EXISTS DungeonMoves(
            id integer primary key,
            DungeonId integer,
            PersonId integer,
            fromDate text,
            CONSTRAINT fk_perosnId  
            FOREIGN KEY (PersonId)  
            REFERENCES Persons(id),

            CONSTRAINT fk_dungeonId FOREIGN KEY (DungeonID) REFERENCES Dungeon(id)
        )
        """
        self.cur.execute(sqlP)
        self.cur.execute(sqlV)
        self.cur.execute(sqlO)
        self.cur.execute(sqlC)
        self.cur.execute(sqlD)
        self.cur.execute(sqlDM)

        self.con.commit()
    # def insertVisitor(self,DateVisited,personId,VisitorName,MountOfMinutes):
    #     self.cur.execute("insert into Visitings values(NULL,?,?,?,?")
    
    #for Prisoners
    def insert(self,firstName,father,lastName,gender,birthYear,address):
        self.cur.execute("insert into Persons values(NULL,?,?,?,?,?,?)",
                        (firstName,father,lastName,gender,birthYear,address)
        )
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM Persons")
        rows=self.cur.fetchall()
        return rows
    def remove(self,id): 
        self.cur.execute("delete from Persons where id=?",(id,))
        self.con.commit()
    def update(self,Id,firstName,father,lastName,gender,birthYear,address):
        self.cur.execute("update Persons set firstName=?,father=?,lastname=?,gender=?,birthyear=?,address=? where id=?",
                        (firstName,father,lastName,gender,birthYear,address, Id))
        self.con.commit()
    def printToExcel(self):
        sql = "select * from Persons;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("PrisonerFile.xlsx",index=False)
    #End Prisoners
    #for Visitings
    def insertV(self,dateVisited,personId,visitorName,MountOfMinutes):
        self.cur.execute("insert into Visitings values(NULL,?,?,?,?)",
                        (dateVisited,personId,visitorName,MountOfMinutes)
        )
        self.con.commit()
    def fetchV(self):
        self.cur.execute("SELECT * FROM Visitings")
        rows=self.cur.fetchall()
        return rows
    def removeV(self,id): 
        self.cur.execute("delete from Visitings where id=?",(id,))
        self.con.commit()
    def updateV(self,Id,dateVisited,personId,visitorName,MountOfMinutes):
        self.cur.execute("update Visitings set DateVisited=?,PersonId=?,VisitorName=?,mountOfMinuts=? where id=?",
                        (dateVisited,personId,visitorName,MountOfMinutes, Id))
        self.con.commit()
    def printToExcelV(self):
        sql = "select * from Visitings;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("VisitingsFile.xlsx",index=False)
    #End Visitings
    #for Offence
    def insertO(self,name):
        self.cur.execute("insert into Offence values(NULL,?)",
                        (name)
        )
        self.con.commit()
    def fetchO(self):
        self.cur.execute("SELECT * FROM Offence")
        rows=self.cur.fetchall()
        return rows
    def removeO(self,id): 
        self.cur.execute("delete from Offence where id=?",(id,))
        self.con.commit()
    def updateO(self,Id,name):
        self.cur.execute("update Offence set name=? where id=?",
                        (name, Id))
        self.con.commit()
    def printToExcelO(self):
        sql = "select * from Offence;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("OffenceFile.xlsx",index=False)
    #End Offence
    #for Convicts
    def insertC(self,fromDate,toDate,personId,offenceId):
        self.cur.execute("insert into Persons values(NULL,?,?,?,?)",
                        (fromDate,toDate,personId,offenceId)
        )
        self.con.commit()
    def fetchC(self):
        self.cur.execute("SELECT * FROM Convicts")
        rows=self.cur.fetchall()
        return rows
    def removeC(self,id): 
        self.cur.execute("delete from Convicts where id=?",(id,))
        self.con.commit()
    def updateC(self,Id,fromDate,toDate,personId,offenceId):
        self.cur.execute("update Convicts set fromDate=?,toDate,PersonId=?,OffenceId=? where id=?",
                        (fromDate,toDate,personId,offenceId, Id))
        self.con.commit()
    def printToExcelC(self):
        sql = "select * from Convicts;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("ConvictsFile.xlsx",index=False)
    #End Convicts
    #for Dungeon
    def insertD(self,name,size):
        self.cur.execute("insert into Dungeon values(NULL,?,?)",
                        (name,size)
        )
        self.con.commit()
    def fetchD(self):
        self.cur.execute("SELECT * FROM Dungeon")
        rows=self.cur.fetchall()
        return rows
    def removeD(self,id): 
        self.cur.execute("delete from Dungeon where id=?",(id,))
        self.con.commit()
    def updateD(self,Id,name,size):
        self.cur.execute("update Dungeon set name=?,size=? where id=?",
                        (name,size, Id))
        self.con.commit()
    def printToExcelD(self):
        sql = "select * from Dungeon;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("DungeonFile.xlsx",index=False)
    #End Dungeon
    #for DungeonMoves
    def insertdm(self,DungeonID,PersonId,fromDate):
        self.cur.execute("insert into DungeonMoves values(NULL,?,?,?)",
                        (DungeonID,PersonId,fromDate)
        )
        self.con.commit()
    def fetchdm(self):
        self.cur.execute("SELECT * FROM DungeonMoves")
        rows=self.cur.fetchall()
        return rows
    def removedm(self,id): 
        self.cur.execute("delete from DungeonMoves where id=?",(id,))
        self.con.commit()
    def updatedm(self,Id,DungeonID,PersonId,fromDate):
        self.cur.execute("update DungeonMoves set DungeonID=?,PersonId=?,fromDate=? where id=?",
                        (DungeonID,PersonId,fromDate, Id))
        self.con.commit()
    def printToExcelDunMov(self):
        sql = "select * from DungeonMoves;"
        df=pd.read_sql(sql,self.con)

        df.head()
        df.to_excel("DungeonMovesFile.xlsx",index=False)
    #End DungeonMoves











class Person:
    def __init__(self,Id,firstName,father,lastName,Gender,BirthYear,Address):
            if Id>0 and len(firstName)>1 and len(father)>1 and len(lastName)>1:
                self._Id=Id
                self._firstName=firstName
                self._father=father
                self._lastName=lastName
                self._Gender=Gender
                self._BirthYear=BirthYear
                self._Address=Address
            else:
                raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._Id
    #end id
    #start fn
    def setFn(self,newFn):
        if len(newFn)>1:
            self._firstName=newFn
        else:
            raise Exception("Invalid FirstName")
    def getFn(self):
        return self._firstName
    #end fn
    #start fa
    def setFa(self,newFa):
        if len(newFa)>1:
            self._father=newFa
        else:
            raise Exception("Invalid Father")
    def getFa(self):
        return self._father
    #end fa
    #start ln
    def setln(self,newln):
        if len(newln)>1:
            self._lastName=newln
        else:
            raise Exception("Invalid LastName")
    def getLn(self):
        return self._firstName
    #end ln
    #start Gender
    def setGn(self,newGn):
        if newGn=="male" or newGn=="female":
            self._Gender=newGn
        else:
            raise Exception("Invalid Gender")
    def getGn(self):
        return self._Gender
    #end Gender
    # #start By
    # def setBy(self,newBy):
    #     if newBy>1900:
    #    self._BirthYear=newBy
    #     else:
    #         raise Exception("Invalid Birthyear")
    def getBy(self):
        return self._BirthYear
    # #end By
    
    #start address
    def setAd(self,newAd):
        if len(newAd)>1:
            self._Address=newAd
        else:
            raise Exception("Invalid Address")
    def getAd(self):
        return self._Address
    #end address
class Visitings:#Person ?????????? ???? 
    def __init__(self,Id,DateVisited,PersonId,VisitorName,MountinMinutes):
            if Id>0 and PersonId>0 and len(VisitorName)>1 :
                self._Id=Id
                self._DateVisited=DateVisited
                self._PersonId=PersonId
                self._VisitorName=VisitorName
                self._MountinMinutes=MountinMinutes
            else:
                raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._Id
    #end id
    #start Vn
    def setVn(self,newVn):
        if len(newVn)>1:
            self._VisitorName=newVn
        else:
            raise Exception("Invalid FirstName")
    def getVn(self):
        return self._VisitorName
    #end Vn
    #start DT
    def setDt(self,newDt):
        self._DateVisited=newDt
    def getDt(self):
        return self._DateVisited
    #end DT
    #start PID
    def setPId(self,newPId):
        if newPId>0:
            self._PersonId=newPId
        else:
            raise Exception("Invalid Id")
    def getPId(self):
        return self._PersonId
    #end PID
    #start MoM
    def setMom(self,newMom):
        if newMom>0 and newMom<30:
            self._MountinMinutes=newMom
        else:
            raise Exception("Invalid Id")
    def getMom(self):
        return self._MountinMinutes
    #end MoM
    
class Convicts:#Person ?????????? ???? 
    def __init__(self,Id,fromDate,toDate,personId,offenseId):
        if Id>0 and personId>0 and offenseId>0:     
            self._Id=Id
            self._fromDate=fromDate
            self._toDate=toDate
            self._personId=personId
            self._offenseId=offenseId
        else:
            raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._Id
    #end id
    #start fromDate
    def setFd(self,newFd):
        #if len(newFd)>4:
        self._fromDate=newFd
        #else:
         #   raise Exception("Invalid From Date")
    def getFd(self):
        return self._fromDate
    #end fromDate
    
    #start toDate
    def setTd(self,newTd):
        #if len(newTd)>4:
        self._toDate=newTd
        #else:
        #    raise Exception("Invalid To Date")
    def getTd(self):
        return self._toDate
    #end toDate
    #start Pid
    def setPId(self,newPId):
        if newPId>0:
            self._personId=newPId
        else:
            raise Exception("Invalid PersonId")
    def getPId(self):
        return self._personId
    #end Pid
    #start Oid
    def setOId(self,newOId):
        if newOId>0:
            self._personId=newOId
        else:
            raise Exception("Invalid Offence Id")
    def getOId(self):
        return self._offenseId
    #end Oid
    
class Offense:#Convicts ?????????? ???? 
    def __init__(self,Id,name):
        if Id>0 and len(name)>1:
            self._Id=Id
            self._name=name
        else:
            raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._Id
    #end id
    #start fn
    def setOn(self,newOn):
        if len(newOn)>1:
            self._name=newOn
        else:
            raise Exception("Invalid OffencName")
    def getOn(self):
        return self._name
    #end fn
    
class DungeonMoves:
    def __init__(self,Id,dungeonId,personId,fromDate):
        if Id>0 and dungeonId>0 and personId>0:
            self._Id=Id
            self._dungeonId=dungeonId#Dungeon
            self._personId=personId #Person
            self._fromDate=fromDate
        else:
            raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._dungeonId
    #end id
    #start Duid
    def setDuId(self,newDuId):
        if newDuId>0:
            self._dungeonId=newDuId
        else:
            raise Exception("Invalid dungeon Id")
    def getDuId(self):
        return self._dungeonId
    #end Duid
    #start Pid
    def setPId(self,newPId):
        if newPId>0:
            self._personId=newPId
        else:
            raise Exception("Invalid PersonId")
    def getPId(self):
        return self._personId
    #end Pid
    #start fromDate
    def setFd(self,newFd):
        if len(newFd)>4:
            self._fromDate=newFd
        else:
            raise Exception("Invalid From Date")
    def getFd(self):
        return self._fromDate
    #end fromDate
class Dungeon:
    def __init__(self,Id,name,size):
        if Id>0 and len(name)>1:
            self._Id=Id
            self._name=name
            self._size=size
        else:
            raise Exception("Invalid Data")
    #start id
    def setId(self,newId):
        if newId>0:
            self._Id=newId
        else:
            raise Exception("Invalid Id")
    def getId(self):
        return self._Id
    #end id
    #start Vn
    def setNa(self,newNa):
        if len(newNa)>1:
            self._name=newNa
        else:
            raise Exception("Invalid Name")
    def getNa(self):
        return self._name
    #end Vn
    #start size
    def setSize(self,newSize):
        if newSize>0:
            self._size=newSize
        else:
            raise Exception("Invalid Size")
    def getSize(self):
        return self._size
    #end size
