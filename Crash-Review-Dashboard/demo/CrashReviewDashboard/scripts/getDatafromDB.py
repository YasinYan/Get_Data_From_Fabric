from sqlalchemy import create_engine, Column, Boolean, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
import fileinput
import sys


Base = declarative_base()
engine = create_engine("sqlite:///scripts/PoltDemoDB.db", echo=False)
#engine = create_engine("sqlite:///PoltDemoDB.db", echo=True)

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

		
def getSprintDatafromDB():
	AUReleaseFromDB =[]
	ZAReleaseFromDB =[]
	ARReleaseFromDB =[]
	CAReleaseFromDB =[]
	ITReleaseFromDB =[]
	IEReleaseFromDB =[]
	MXReleaseFromDB =[]
	PLReleaseFromDB =[]
	Base.metadata.create_all(engine)
	create_session = sessionmaker(bind=engine)
	session = create_session()
	ZARelese = session.query(DBZA).order_by(DBZA.Id.desc())[0:10]
	for u in ZARelese:
		ZAReleaseFromDB.append(u.ReleaseBuild)
	AURelease = session.query(DBAU).order_by(DBAU.Id.desc())[0:10]
	for u in AURelease:
		AUReleaseFromDB.append(u.ReleaseBuild)
	ARRelease = session.query(DBAR).order_by(DBAR.Id.desc())[0:10]
	for u in ARRelease:
		ARReleaseFromDB.append(u.ReleaseBuild)
	CARelease = session.query(DBCA).order_by(DBCA.Id.desc())[0:10]
	for u in CARelease:
		CAReleaseFromDB.append(u.ReleaseBuild)
	ITRelease = session.query(DBIT).order_by(DBIT.Id.desc())[0:10]
	for u in ITRelease:
		ITReleaseFromDB.append(u.ReleaseBuild)
	IERelease = session.query(DBIE).order_by(DBIE.Id.desc())[0:10]
	for u in IERelease:
		IEReleaseFromDB.append(u.ReleaseBuild)
	MXRelease = session.query(DBMX).order_by(DBMX.Id.desc())[0:10]
	for u in MXRelease:
		MXReleaseFromDB.append(u.ReleaseBuild)
	PLRelease = session.query(DBPL).order_by(DBPL.Id.desc())[0:10]
	for u in PLRelease:
		PLReleaseFromDB.append(u.ReleaseBuild)

	ZAReleaseFromDB = ZAReleaseFromDB[::-1]
	AUReleaseFromDB = AUReleaseFromDB[::-1]
	ARReleaseFromDB = ARReleaseFromDB[::-1]
	CAReleaseFromDB = CAReleaseFromDB[::-1]
	ITReleaseFromDB = ITReleaseFromDB[::-1]
	IEReleaseFromDB = IEReleaseFromDB[::-1]
	MXReleaseFromDB = MXReleaseFromDB[::-1]
	PLReleaseFromDB = PLReleaseFromDB[::-1]

	#print(ZAReleaseFromDB,AUReleaseFromDB,ARReleaseFromDB,CAReleaseFromDB,ITReleaseFromDB,IEReleaseFromDB,MXReleaseFromDB,PLReleaseFromDB)
	return ZAReleaseFromDB,AUReleaseFromDB,ARReleaseFromDB,CAReleaseFromDB,ITReleaseFromDB,IEReleaseFromDB,MXReleaseFromDB,PLReleaseFromDB

def getCrashRateFromDB():
	CrashRateZA =[]
	CrashRateAU =[]
	CrashRateAR =[]
	CrashRateCA =[]
	CrashRateIT =[]
	CrashRateIE =[]
	CrashRateMX =[]
	CrashRatePL =[]
	Base.metadata.create_all(engine)
	create_session = sessionmaker(bind=engine)
	session = create_session()
	AUCrashResult=session.query(DBAU).order_by(DBAU.Id.desc())[0:10]
	for u in AUCrashResult:
		CrashRateAU.append(u.CrashRate.split("%")[0])
	ZACrashResult = session.query(DBZA).order_by(DBZA.Id.desc())[0:10]
	for u in ZACrashResult:
		CrashRateZA.append(u.CrashRate.split("%")[0])
	ARCrashResult = session.query(DBAR).order_by(DBAR.Id.desc())[0:10]
	for u in ARCrashResult:
		CrashRateAR.append(u.CrashRate.split("%")[0])
	CACrashResult = session.query(DBCA).order_by(DBCA.Id.desc())[0:10]
	for u in CACrashResult:
		CrashRateCA.append(u.CrashRate.split("%")[0])
	ITCrashResult = session.query(DBIT).order_by(DBIT.Id.desc())[0:10]
	for u in ITCrashResult:
		CrashRateIT.append(u.CrashRate.split("%")[0])
	IECrashResult = session.query(DBIE).order_by(DBIE.Id.desc())[0:10]
	for u in IECrashResult:
		CrashRateIE.append(u.CrashRate.split("%")[0])
	MXCrashResult = session.query(DBMX).order_by(DBMX.Id.desc())[0:10]
	for u in MXCrashResult:
		CrashRateMX.append(u.CrashRate.split("%")[0])
	PLCrashResult = session.query(DBPL).order_by(DBPL.Id.desc())[0:10]
	for u in PLCrashResult:
		CrashRatePL.append(u.CrashRate.split("%")[0])
	CrashRateAU = CrashRateAU[::-1]
	CrashRateZA = CrashRateZA[::-1]
	CrashRateAR = CrashRateAR[::-1]
	CrashRateCA = CrashRateCA[::-1]
	CrashRateIT = CrashRateIT[::-1]
	CrashRateIE = CrashRateIE[::-1]
	CrashRateMX = CrashRateMX[::-1]
	CrashRatePL = CrashRatePL[::-1]
	return CrashRateZA,CrashRateAU,CrashRateAR,CrashRateCA,CrashRateIT,CrashRateIE,CrashRateMX,CrashRatePL

def ReplaceInJS_UpdateSprint(ZAReleaseFromDB,AUReleaseFromDB,ARReleaseFromDB,CAReleaseFromDB,ITReleaseFromDB,IEReleaseFromDB,MXReleaseFromDB,PLReleaseFromDB):
	for line in fileinput.input("./static/asset/js/CrashReview_chart_androidCopy.js",backup=0,inplace=1):
		if "var AULabel" in line:
			old_data = line
			new_data = "	var AULabel = " + str(AUReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var ZALabel" in line:
			old_data = line
			new_data = "	var ZALabel = " + str(ZAReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var ARLabel" in line:
			old_data = line
			new_data = "	var ARLabel = " + str(ARReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var CALabel" in line:
			old_data = line
			new_data = "	var CALabel = " + str(CAReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var MXLabel" in line:
			old_data = line
			new_data = "	var MXLabel = " + str(MXReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var IELabel" in line:
			old_data = line
			new_data = "	var IELabel = " + str(IEReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var ITLabel" in line:
			old_data = line
			new_data = "	var ITLabel = " + str(ITReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		if "var PLLabel" in line:
			old_data = line
			new_data = "	var PLLabel = " + str(PLReleaseFromDB)+"\r\n"
			line = line.replace(old_data,new_data)
		sys.stdout.write(line)	
	fileinput.close()

def ReplaceInJS_UpdateCrashRate(ZACrashResult,AUCrashResult,ARCrashResult,CACrashResult,ITCrashResult,IECrashResult,MXCrashResult,PLCrashResult):
	print("start update crashrate")
	for line in fileinput.input("./static/asset/js/CrashReview_chart_androidCopy.js",backup=0,inplace=1):
		if "var ZAresult" in line:
			resultStr = ReformatCrashData(ZACrashResult,"ZA")
			old_data = line
			new_data = "	var ZAresult = " +resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var AUresult" in line:
			resultStr = ReformatCrashData(AUCrashResult,"AU")
			old_data = line
			new_data = "	var AUresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var ARresult" in line:
			resultStr = ReformatCrashData(ARCrashResult,"AR")
			old_data = line
			new_data = "	var ARresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var CAresult" in line:
			resultStr = ReformatCrashData(CACrashResult,"CA")
			old_data = line
			new_data = "	var CAresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var ITresult" in line:
			resultStr = ReformatCrashData(ITCrashResult,"IT")
			old_data = line
			new_data = "	var ITresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var IEresult" in line:
			resultStr = ReformatCrashData(IECrashResult,"IE")
			old_data = line
			new_data = "	var IEresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var MXresult" in line:
			resultStr = ReformatCrashData(MXCrashResult,"MX")
			old_data = line
			new_data = "	var MXresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		if "var PLresult" in line:
			resultStr = ReformatCrashData(PLCrashResult,"PL")
			old_data = line
			new_data = "	var PLresult = " + resultStr+"\r\n"
			line = line.replace(old_data,new_data)
		sys.stdout.write(line)	
	fileinput.close()

def ReformatCrashData(CrashRateData,country):
	str = ",".join(CrashRateData)
	if country == "CA":
		new_data = "[" +"'"+"KijijiCA"+"'"+","+ str +"]"
	if country == "AU":
		new_data = "[" +"'"+"GumtreeAU"+"'"+","+ str +"]"
	if country == "ZA":
		new_data = "[" +"'"+"GumtreeZA"+"'"+","+ str +"]"
	if country == "IT":
		new_data = "[" +"'"+"KijijiIT"+"'"+","+ str +"]"
	if country == "MX":
		new_data = "[" +"'"+"VivanunciosMX"+"'"+","+ str +"]"
	if country == "AR":
		new_data = "[" +"'"+"AlamaulaAR"+"'"+","+ str +"]"
	if country == "IE":
		new_data = "[" +"'"+"GumtreeIE"+"'"+","+ str +"]"
	if country == "PL":
		new_data = "[" +"'"+"GumtreePL"+"'"+","+ str +"]"
	return new_data


if __name__ == "__main__":
	ZAReleaseFromDB,AUReleaseFromDB,ARReleaseFromDB,CAReleaseFromDB,ITReleaseFromDB,IEReleaseFromDB,MXReleaseFromDB,PLReleaseFromDB = getSprintDatafromDB()
	ReplaceInJS_UpdateSprint(ZAReleaseFromDB,AUReleaseFromDB,ARReleaseFromDB,CAReleaseFromDB,ITReleaseFromDB,IEReleaseFromDB,MXReleaseFromDB,PLReleaseFromDB)
	ZACrashResult,AUCrashResult,ARCrashResult,CACrashResult,CrashRateIT,CrashRateIE,CrashRateMX,CrashRatePL=getCrashRateFromDB()
	ReplaceInJS_UpdateCrashRate(ZACrashResult,AUCrashResult,ARCrashResult,CACrashResult,CrashRateIT,CrashRateIE,CrashRateMX,CrashRatePL)