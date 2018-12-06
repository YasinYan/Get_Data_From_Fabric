from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
import getCrashRate

engine = create_engine('sqlite:///PoltDemo.db', echo=True)
Base = declarative_base()
#versionNumebr = getCrashRate.app_version
crashRate = 0
Session = sessionmaker(bind=engine)
session = Session()
Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM = getCrashRate.ReformatBuildVersion(argv[1])


# update the crash rate of the last version for AU
class CrashReportAU(Base):
    __tablename__ = 'TestTableForAU'
    Id = Column(Integer,primary_key=True)
    ReleaseBuild = Column(String,nullable=False)
    CrashRate = Column(String, nullable=False)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Gumtree AU',Build_CA_IT,Build_AU_AR_ZA_PL,Build_MX_IE,APP_BUILD_NUM)

        query = session.query(CrashReportAU).order_by(CrashReportAU.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportAU(ReleaseBuild=versionNumebr, CrashRate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for CA
class CrashReportCA(Base):
    __tablename__ = 'crash_report_CA'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Kijiji CA')

        query = session.query(CrashReportCA).order_by(CrashReportCA.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportCA(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for IT
class CrashReportIT(Base):
    __tablename__ = 'crash_report_IT'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Kijiji IT')

        query = session.query(CrashReportIT).order_by(CrashReportIT.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportIT(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for ZA
class CrashReportZA(Base):
    __tablename__ = 'crash_report_ZA'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Gumtree ZA')

        query = session.query(CrashReportZA).order_by(CrashReportZA.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportZA(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for MX
class CrashReportMX(Base):
    __tablename__ = 'crash_report_MX'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Vivanuncios MX')

        query = session.query(CrashReportMX).order_by(CrashReportMX.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportMX(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for PL
class CrashReportPL(Base):
    __tablename__ = 'crash_report_PL'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Gumtree PL')

        query = session.query(CrashReportPL).order_by(CrashReportPL.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportPL(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for AR
class CrashReportAR(Base):
    __tablename__ = 'crash_report_AR'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Alamaula AR')

        query = session.query(CrashReportAR).order_by(CrashReportAR.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportAR(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


# update the crash rate of the last version for IE
class CrashReportIE(Base):
    __tablename__ = 'crash_report_IE'
    app_version = Column(String(50), primary_key=True)
    crash_rate = Column(String)

    # update crash rate up to date
    def updateData(self):
        crashRate = getCrashRate.get_crash_rate_for_country('Gumtree IE')

        query = session.query(CrashReportIE).order_by(CrashReportIE.app_version.desc()).first()
        dotVersion = query.app_version.split(".")
        if dotVersion[1] == versionNumebr.split(".")[1]:
            query.app_version = versionNumebr
            query.crash_rate = crashRate
        else:
            newVersion = CrashReportIE(app_version=versionNumebr, crash_rate=crashRate)
            session.add(newVersion)

        session.commit()


crashReportAU = CrashReportAU()
# crashReportCA = CrashReportCA()
# crashReportIT = CrashReportIT()
# crashReportZA = CrashReportZA()
# crashReportMX = CrashReportMX()
# crashReportPL = CrashReportPL()
# crashReportAR = CrashReportAR()
# crashReportIE = CrashReportIE()
crashReportAU.updateData()
# crashReportCA.updateData()
# crashReportZA.updateData()
# crashReportMX.updateData()
# crashReportPL.updateData()
# crashReportAR.updateData()
# crashReportIE.updateData()

for instance in session.query(CrashReportAU).order_by(CrashReportAU.app_version.desc())[0:5]:
    print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportCA).order_by(CrashReportCA.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportIT).order_by(CrashReportIT.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportZA).order_by(CrashReportZA.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportMX).order_by(CrashReportMX.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportPL).order_by(CrashReportPL.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportAR).order_by(CrashReportAR.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)

# for instance in session.query(CrashReportIE).order_by(CrashReportIE.app_version.desc())[0:5]:
#     print(instance.app_version, instance.crash_rate)