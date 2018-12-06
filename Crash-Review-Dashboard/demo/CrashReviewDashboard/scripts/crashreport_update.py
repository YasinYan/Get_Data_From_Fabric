from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRate

engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=False)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=False)
Base = declarative_base()
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
country = argv[1]


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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Gumtree AU')
        query = session.query(CrashReportAU).order_by(CrashReportAU.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportAU(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Kijiji CA')
        query = session.query(CrashReportCA).order_by(CrashReportCA.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Data is 0% ,no need to save into DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportCA(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Kijiji IT')
        query = session.query(CrashReportIT).order_by(CrashReportIT.Id.desc()).first()
        if crashRate =="0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportIT(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Gumtree ZA')
        query = session.query(CrashReportZA).order_by(CrashReportZA.Id.desc()).first()
        if crashRate =="0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportZA(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Vivanuncios MX')
        query = session.query(CrashReportMX).order_by(CrashReportMX.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportMX(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Gumtree PL')
        query = session.query(CrashReportPL).order_by(CrashReportPL.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportPL(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
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
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Alamaula AR')
        query = session.query(CrashReportAR).order_by(CrashReportAR.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportAR(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
            session.add(newVersion)
            session.commit()


# update the crash rate of the last version for IE
class CrashReportIE(Base):
    __tablename__ = 'TestTableForIE'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)
    ReleaseNumber = Column(String,nullable=False)
    Notes = Column(String, nullable=True)

    # update crash rate up to date
    def updateData(self):
        crashRate,ReleaseBuild,ReleaseNumber = getCrashRate.get_crash_rate_for_country('Gumtree IE')
        query = session.query(CrashReportIE).order_by(CrashReportIE.Id.desc()).first()
        if crashRate == "0%":
            print("Crash Rate collect is 0%, no need to save DB")
        if ReleaseBuild == query.ReleaseBuild:
            print("Build not update , Latest version is "+ReleaseBuild+",DB version is "+query.ReleaseBuild+ ", no need to save into DB")
        else:
            newVersion = CrashReportIE(ReleaseBuild=ReleaseBuild, CrashRate=crashRate,ReleaseNumber=ReleaseNumber)
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
