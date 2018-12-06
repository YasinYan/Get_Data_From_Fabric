from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRate

engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=True)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=True)
Base = declarative_base()
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
Hotfix_Buildnumber = argv[2]
country=argv[1]
print(Hotfix_Buildnumber)
BuildVersion_AU = "5."+Hotfix_Buildnumber.split('.')[1]+'.'+Hotfix_Buildnumber.split('.')[2]+'.'+Hotfix_Buildnumber.split('.')[3]
Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(BuildVersion_AU)


# update the crash rate of the last version for AU
class CrashReportAU(Base):
    __tablename__ = 'TestTableForAU'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        # crashRate = getCrashRate.get_crash_rate_for_country('Gumtree AU',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        # ReleaseBuild = Build_AU_AR_ZA_PL.split(' ')[0]
        query = session.query(CrashReportAU).order_by(CrashReportAU.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_AU_AR_ZA_PL.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Gumtree AU',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for CA
class CrashReportCA(Base):
    __tablename__ = 'TestTableForCA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        #crashRate = getCrashRate.get_crash_rate_for_country('Kijiji CA')

        query = session.query(CrashReportCA).order_by(CrashReportCA.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_CA_IT.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Kijiji CA',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for IT
class CrashReportIT(Base):
    __tablename__ = 'TestTableForIT'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)


    # update crash rate up to date
    def updateData(self):
        #crashRate = getCrashRate.get_crash_rate_for_country('Kijiji IT')

        query = session.query(CrashReportIT).order_by(CrashReportIT.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_CA_IT.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Kijiji IT',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for ZA
class CrashReportZA(Base):
    __tablename__ = 'TestTableForZA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportZA).order_by(CrashReportZA.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_AU_AR_ZA_PL.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Gumtree ZA',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for MX
class CrashReportMX(Base):
    __tablename__ = 'TestTableForMX'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportMX).order_by(CrashReportMX.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_MX_IE.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Vivanuncios MX',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for PL
class CrashReportPL(Base):
    __tablename__ = 'TestTableForPL'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportPL).order_by(CrashReportPL.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_AU_AR_ZA_PL.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Gumtree PL',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for AR
class CrashReportAR(Base):
    __tablename__ = 'TestTableForAR'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_AU_AR_ZA_PL.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Alamaula AR',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
        if HotFix_crashRate== "0%":
            print("Crash Data is 0% ,no need to save into DB")
        else:
            query.ReleaseBuild = ReleaseBuild
            query.CrashRate = HotFix_crashRate
            query.ReleaseNumber=Hotfix_Buildnumber
        session.commit()


# update the crash rate of the last version for IE
class CrashReportIE(Base):
    __tablename__ = 'TestTableIE'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportIE).order_by(CrashReportIE.Id.desc()).first()
        Hotfix_Version=int(query.ReleaseBuild.split(".")[2])+1
        Update_Version = query.ReleaseBuild.split(".")[0]+"."+query.ReleaseBuild.split(".")[1]+"."+str(Hotfix_Version)+"."+Hotfix_Buildnumber.split('.')[3]
        Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(Update_Version)
        ReleaseBuild = Build_MX_IE.split(' ')[0]
        HotFix_crashRate = getCrashRate.get_crash_rate_for_country('Gumtree IE',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)
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
if country =="GumtreePL":
        crashReportPL = CrashReportPL()
        crashReportPL.updateData()
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
