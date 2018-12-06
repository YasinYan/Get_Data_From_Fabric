from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRateiOS

engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=False)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=False)
Base = declarative_base()
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
country = argv[1]


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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree AU')
        query = session.query(CrashReportAU).order_by(CrashReportAU.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportAU(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Kijiji CA')
        query = session.query(CrashReportCA).order_by(CrashReportCA.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportCA(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Kijiji IT')
        query = session.query(CrashReportIT).order_by(CrashReportIT.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportIT(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree ZA')
        query = session.query(CrashReportZA).order_by(CrashReportZA.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportZA(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Vivanuncios MX')
        query = session.query(CrashReportMX).order_by(CrashReportMX.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportMX(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for UK
class CrashReportUK(Base):
    __tablename__ = 'TestTableForiOSUK'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree UK')
        query = session.query(CrashReportUK).order_by(CrashReportUK.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportUK(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Alamaula AR')
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportAR(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for IE
class CrashReportIE(Base):
    __tablename__ = 'TestTableForiOSIE'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree IE')
        query = session.query(CrashReportIE).order_by(CrashReportIE.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update , Latest version is "+app_version+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportIE(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()
    # return next release and current release
    def getReleaseData(self):
        currentRelease = query.ReleaseBuild
        firstDigitBuildVersion = int(query.ReleaseBuild.split(".")[0])
        middleDigitBuildVersion = int(query.ReleaseBuild.split(".")[1])
        lastDigitBuildVersion = int(query.ReleaseBuild.split(".")[2])
        if middleDigitBuildVersion ==9:
            middleDigitBuildVersion=0
            firstDigitBuildVersion = firstDigitBuildVersion+1
        else:
            middleDigitBuildVersion = middleDigitBuildVersion+1
        NextRelease = str(firstDigitBuildVersion)+"."+str(middleDigitBuildVersion)+"."+str(lastDigitBuildVersion)
        return currentRelease,NextRelease




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
    crashReportPL = CrashReportUK()
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
