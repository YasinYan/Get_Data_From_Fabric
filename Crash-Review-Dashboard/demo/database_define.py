from sqlalchemy import create_engine, Text
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
this file is to define 8 tables for Android countries report.
more info about sqlalchemy Object Relational: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''
engine = create_engine('sqlite:///crashreport.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class CrashReportAU(Base):
    __tablename__ = 'crash_report_AU'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportAU.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportAU(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportCA(Base):
    __tablename__ = 'crash_report_CA'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportCA.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportCA(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportIT(Base):
    __tablename__ = 'crash_report_IT'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportIT.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportIT(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportZA(Base):
    __tablename__ = 'crash_report_ZA'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportZA.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportZA(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportMX(Base):
    __tablename__ = 'crash_report_MX'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportMX.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate,):
        session.add(CrashReportMX(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportIE(Base):
    __tablename__ = 'crash_report_IE'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportIE.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportIE(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportPL(Base):
    __tablename__ = 'crash_report_PL'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportPL.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportPL(app_version=appVersion, crash_rate=crashRate))
        session.commit()


class CrashReportAR(Base):
    __tablename__ = 'crash_report_AR'
    app_version = Column(String, primary_key=True)
    crash_rate = Column(String)

    def createSchema(self):
        Base.metadata.create_all(engine)    # create table

    def dropTable(self):
        CrashReportAR.__table__.drop(engine)  # drop table

    def addData(self, appVersion, crashRate):
        session.add(CrashReportAR(app_version=appVersion, crash_rate=crashRate))
        session.commit()


CrashReportAU().dropTable()
CrashReportAU().createSchema()

CrashReportCA().dropTable()
CrashReportCA().createSchema()

CrashReportIT().dropTable()
CrashReportIT().createSchema()

CrashReportZA().dropTable()
CrashReportZA().createSchema()

CrashReportMX().dropTable()
CrashReportMX().createSchema()

CrashReportPL().dropTable()
CrashReportPL().createSchema()

CrashReportAR().dropTable()
CrashReportAR().createSchema()

CrashReportIE().dropTable()
CrashReportIE().createSchema()

CrashReportAU().addData("5.11.0", "0.00015")
CrashReportAU().addData("5.12.0", "0.00011")
CrashReportAU().addData("5.13.0", "0.00067")
CrashReportAU().addData("5.14.0", "0.00032")
CrashReportAU().addData("5.15.0", "0.00022")

CrashReportCA().addData("6.11.0", "0.00012")
CrashReportCA().addData("6.12.0", "0.00012")
CrashReportCA().addData("6.13.0", "0.00006")
CrashReportCA().addData("6.14.0", "0.00049")
CrashReportCA().addData("6.15.0", "0.00015")

CrashReportIT().addData("6.11.0", "0.00017")
CrashReportIT().addData("6.13.0", "0.00016")
CrashReportIT().addData("6.14.0", "0.00015")

CrashReportZA().addData("5.11.0", "0.00019")
CrashReportZA().addData("5.13.0", "0.00013")
CrashReportZA().addData("5.14.0", "0.00027")

CrashReportMX().addData("4.11.0", "0.00116")
CrashReportMX().addData("4.13.0", "0.00047")
CrashReportMX().addData("4.14.0", "0.00028")

CrashReportPL().addData("5.11.0", "0.00057")
CrashReportPL().addData("5.14.0", "0.00006")

CrashReportAR().addData("5.11.0", "0.00102")
CrashReportAR().addData("5.14.0", "0.00069")

CrashReportIE().addData("4.11.0", "0.00022")
CrashReportIE().addData("4.14.0", "0.00009")

for instance in session.query(CrashReportAU).order_by(CrashReportAU.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportCA).order_by(CrashReportCA.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportIT).order_by(CrashReportIT.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportZA).order_by(CrashReportZA.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportMX).order_by(CrashReportMX.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportPL).order_by(CrashReportPL.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportAR).order_by(CrashReportAR.app_version.desc()):
    print(instance.app_version, instance.crash_rate)

for instance in session.query(CrashReportIE).order_by(CrashReportIE.app_version.desc()):
    print(instance.app_version, instance.crash_rate)