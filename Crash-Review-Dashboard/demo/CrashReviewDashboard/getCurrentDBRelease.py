from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
import fileinput
import sys
import getCurrentRelease


Base = declarative_base()
engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=False)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class TestDB(object):
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    Notes = Column(String, nullable=True)

    def __init__(self, Id, ReleaseBuild, ReleaseNumber, CrashRate, Notes):
    	self.Id = Id
    	self.ReleaseBuild = ReleaseBuild
    	self.ReleaseNumber = ReleaseNumber
    	self.CrashRate = CrashRate
    	self.Notes = Notes


class DBiOSZA(TestDB,Base):
	__tablename__ = "TestTableForiOSZA"

class DBiOSAU(TestDB,Base):
	__tablename__="TestTableForiOSAU"

class DBiOSAR(TestDB,Base):
	__tablename__="TestTableForiOSAR"

class DBiOSCA(TestDB,Base):
	__tablename__="TestTableForiOSCA"

class DBiOSIT(TestDB,Base):
	__tablename__="TestTableForiOSIT"

class DBiOSIE(TestDB,Base):
	__tablename__="TestTableForiOSIE"

class DBiOSMX(TestDB,Base):
	__tablename__="TestTableForiOSMX"

class DBiOSUK(TestDB,Base):
	__tablename__="TestTableForiOSUK"

class DBZA(TestDB,Base):
    __tablename__ = "TestTableForZA"

class DBAU(TestDB,Base):
    __tablename__="TestTableForAU"

class DBAR(TestDB,Base):
    __tablename__="TestTableForAR"

class DBCA(TestDB,Base):
    __tablename__="TestTableForCA"

class DBIT(TestDB,Base):
    __tablename__="TestTableForIT"

class DBIE(TestDB,Base):
    __tablename__="TestTableForIE"

class DBMX(TestDB,Base):
    __tablename__="TestTableForMX"

class DBPL(TestDB,Base):
    __tablename__="TestTableForPL"


def getReleaseData(Platform):
    if Platform =="iOS":
        DBList = [DBiOSCA,DBiOSAU,DBiOSZA,DBiOSUK,DBiOSMX,DBiOSIT,DBiOSAR]
        currentReleaseList=getCurrentRelease.get_all_current_release_build_number_for_ios_country()
        currentDBReleaseList=[]
        for DB in DBList:
            query = session.query(DB).order_by(DB.Id.desc()).first()
            currentDBRelease = query.ReleaseBuild
            currentDBReleaseList.append(currentDBRelease)
        print(currentReleaseList,currentDBReleaseList)
        return currentReleaseList,currentDBReleaseList
    if Platform =="Android":
        DBList = [DBCA,DBAU,DBZA,DBMX,DBIT,DBAR,DBIE,DBPL]
        currentReleaseList=getCurrentRelease.get_all_current_release_build_number_for_and_country()
        currentDBReleaseList=[]
        for DB in DBList:
            query = session.query(DB).order_by(DB.Id.desc()).first()
            currentDBRelease = query.ReleaseBuild
            currentDBReleaseList.append(currentDBRelease)
        print(currentReleaseList,currentDBReleaseList)
        return currentReleaseList,currentDBReleaseList