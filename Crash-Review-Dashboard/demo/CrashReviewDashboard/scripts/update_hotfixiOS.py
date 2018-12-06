from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRateiOS

engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=True)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=True)
Base = declarative_base()
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
Hotfix_Buildnumber = argv[2]
country=argv[1]


# update the crash rate of the last version for AU
class CrashReportAU(Base):
    __tablename__ = 'TestTableForiOSAU'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportAU).order_by(CrashReportAU.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Gumtree AU',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for CA
class CrashReportCA(Base):
    __tablename__ = 'TestTableForiOSCA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportCA).order_by(CrashReportCA.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Kijiji CA',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = Update_Version
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Build_Number
        session.commit()



# update the crash rate of the last version for IT
class CrashReportIT(Base):
    __tablename__ = 'TestTableForiOSIT'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)


    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportIT).order_by(CrashReportIT.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Kijiji IT',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for ZA
class CrashReportZA(Base):
    __tablename__ = 'TestTableForiOSZA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportZA).order_by(CrashReportZA.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Gumtree ZA',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for MX
class CrashReportMX(Base):
    __tablename__ = 'TestTableForiOSMX'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportMX).order_by(CrashReportMX.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Vivanuncios MX',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for PL
class CrashReportUK(Base):
    __tablename__ = 'TestTableForiOSUK'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportUK).order_by(CrashReportUK.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Gumtree UK',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for AR
class CrashReportAR(Base):
    __tablename__ = 'TestTableForiOSAR'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Alamaula AR',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for IE
class CrashReportIE(Base):
    __tablename__ = 'TestTableiOSIE'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()
        Build_Number = Hotfix_Buildnumber
        Hotfix_Version = int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)
        HotFix_crashRate = getCrashRateiOS.get_crash_rate_for_country('Gumtree IE',Build_Number,Update_Version)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


if country =="GumtreeAU":
        crashReportAU = CrashReportAU()
        crashReportAU.updateData()
if country =="GumtreeZA":
        crashReportZA = CrashReportZA()
        crashReportZA.updateData()
if country =="GumtreeIE":
        crashReportIE = CrashReportIE()
        crashReportIE.updateData()
if country =="GumtreeUK":
        crashReportUK = CrashReportUK()
        crashReportUK.updateData()
if country =="KijijiCA":
        crashReportCA = CrashReportCA()
        crashReportCA.updateData()
if country =="KijijiIT":
        crashReportIT = CrashReportIT()
        crashReportIT.updateData()
if country =="AlamaulaAR":
        crashReportAR = CrashReportAR()
        crashReportAR.updateData()
if country =="VivanunciosMX":
        crashReportMX = CrashReportMX()
        crashReportMX.updateData()
