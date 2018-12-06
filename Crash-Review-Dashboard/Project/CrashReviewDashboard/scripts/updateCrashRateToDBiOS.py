from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRateiOS

engine = create_engine("sqlite:///scripts/CrashRateData.db", echo=False)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=True)
Base = declarative_base()
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
country = argv[1]


# update the crash rate of the last version for AU
class CrashReportAU(Base):
    __tablename__ = 'CrashDataiOSAU'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        query = session.query(CrashReportAU).order_by(CrashReportAU.Id.desc()).first()
        crashRate ,app_version,ReleaseNumber= getCrashRateiOS.get_crash_rate_for_country('Gumtree AU')
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportAU(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for CA
class CrashReportCA(Base):
    __tablename__ = 'CrashDataiOSCA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportCA).order_by(CrashReportCA.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Kijiji CA')
     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportCA(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for IT
class CrashReportIT(Base):
    __tablename__ = 'CrashDataiOSIT'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportIT).order_by(CrashReportIT.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Kijiji IT')
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportCA(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for ZA
class CrashReportZA(Base):
    __tablename__ = 'CrashDataiOSZA'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportZA).order_by(CrashReportZA.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree ZA')
     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportZA(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for MX
class CrashReportMX(Base):
    __tablename__ = 'CrashDataiOSMX'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportMX).order_by(CrashReportMX.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Vivanuncios MX')
     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportMX(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for UK
class CrashReportUK(Base):
    __tablename__ = 'CrashDataiOSUK'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportUK).order_by(CrashReportUK.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Gumtree UK')
     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportUK(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
        session.commit()


# update the crash rate of the last version for AR
class CrashReportAR(Base):
    __tablename__ = 'CrashDataiOSAR'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):  
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()
        crashRate,app_version,ReleaseNumber = getCrashRateiOS.get_crash_rate_for_country('Alamaula AR')
     
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if app_version == query.ReleaseBuild:
            print("Build not update, Latest version is"+app_version+", DB version is"+query.ReleaseBuild+", no need to save into DB")
        else:
            newVersion = CrashReportAR(ReleaseBuild=app_version, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
