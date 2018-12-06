from bottle import Bottle, run, template,static_file,redirect,request
import os, sys
import runpy
import subprocess
import getCurrentRelease
import getCurrentDBRelease
dirname = os.path.dirname(sys.argv[0])

app = Bottle()

@app.route('/static/asset/css/<filename:re:.*\.css>')
def send_css(filename):
	return static_file(filename, root='./static/asset/css')

@app.route('/static/asset/js/<filename:re:.*\.js>')
def send_js(filename):
	response =static_file(filename, root='./static/asset/js')
	response.set_header("Cache-Control", "public, max-age=5")
	return response

@app.route('/static/asset/fonts/<filename:re:.*\.jpg>')
def send_jpg(filename):
	return static_file(filename, root='./static/asset/fonts')

@app.route('/static/asset/fonts/icon_Android/<filename:re:.*\.png>')
def send_icon_Android(filename):
	return static_file(filename, root='./static/asset/fonts/icon_Android')

@app.route('/static/asset/fonts/icon_iOS/<filename:re:.*\.png>')
def send_icon_iOS(filename):
	return static_file(filename, root='./static/asset/fonts/icon_iOS')

@app.route('/static/asset/css/bootstrap.min.css.map')
def send_map():
	return static_file("bootstrap.min.css.map",root='./static/asset/css')
@app.route('/static/asset/js/bootstrap.min.js.map')
def send_map():
	return static_file("bootstrap.min.js.map",root='./static/asset/js')
@app.route('/static/asset/js/popper.min.js.map')
def send_map():
	return static_file("popper.min.js.map",root='./static/asset/js')
@app.route('/AndroidDashboard')
def go_Android_Dashboard():
	currentRelease,currentDBRelease=getCurrentDBRelease.getReleaseData("Android")
	return template('./views/AndroidCrashRateBoard.tpl',CARelease=currentRelease[0],CANextRelease=currentDBRelease[0],AURelease=currentRelease[1],AUNextRelease=currentDBRelease[1],ZARelease=currentRelease[2],ZANextRelease=currentDBRelease[2],MXRelease=currentRelease[3],MXNextRelease=currentDBRelease[3],ITRelease=currentRelease[4],ITNextRelease=currentDBRelease[4],ARRelease=currentRelease[5],ARNextRelease=currentDBRelease[5],IERelease=currentRelease[6],IENextRelease=currentDBRelease[6],PLRelease=currentRelease[7],PLNextRelease=currentDBRelease[7])

@app.route('/iOSDashboard')
def go_iOS_Dashboard():
	currentRelease,currentiOSDBRelease=getCurrentDBRelease.getReleaseData("iOS")
	return template('./views/iOSCrashRateBoard.tpl',CARelease=currentRelease[0],CANextRelease=currentiOSDBRelease[0],AURelease=currentRelease[1],AUNextRelease=currentiOSDBRelease[1],ZARelease=currentRelease[2],ZANextRelease=currentiOSDBRelease[2],UKRelease=currentRelease[3],UKNextRelease=currentiOSDBRelease[3],MXRelease=currentRelease[4],MXNextRelease=currentiOSDBRelease[4],ITRelease=currentRelease[5],ITNextRelease=currentiOSDBRelease[5],ARRelease=currentRelease[6],ARNextRelease=currentiOSDBRelease[6])

@app.route('/')
def index():
	return template('./views/Index.tpl')

@app.route('/UpdateAndroid')
def update_Android():
	os.system("python3 ./scripts/getDatafromDB.py")
	return redirect('/AndroidDashboard'),template('./views/AndroidCrashRateBoard.tpl')

@app.route('/UpdateiOS')
def update_iOS():
	os.system("python3 ./scripts/getiOSDataFromDB.py")
	redirect("/iOSDashboard"),template('./views/iOSCrashRateBoard.tpl')

@app.route('/getHotFixData',method="POST")
def updateHotFix():
	SubmitUpdateHotFixOrRelease=str(request.POST.get('action'))		
	for i in range(1,9):
		checkbox_id = "inlineRadioOptions"+str(i)
		country = str(request.POST.get(checkbox_id))
		if country != "None":
			os.system("python3 ./scripts/updateCrashRateToDB.py"+" "+str(country))
	runpy.run_path("./scripts/getDatafromDB.py",run_name='__main__')
	return redirect('/AndroidDashboard'),template('./views/AndroidCrashRateBoard.tpl')
	
@app.route('/getiOSData',method="POST")
def updateHotFix():
	SubmitUpdateHotFixOrRelease=str(request.POST.get('action'))
	for i in range(1,9):		
		checkbox_id = "inlineRadioOptions"+str(i)
		country = str(request.POST.get(checkbox_id))
		if country != "None":
			os.system("python3 ./scripts/updateCrashRateToDBiOS.py"+" "+str(country))
	runpy.run_path("./scripts/getiOSDataFromDB.py",run_name='__main__')
	return redirect('/iOSDashboard'),template('./views/iOSCrashRateBoard.tpl')

run(app,host='0.0.0.0',port=8080,reloader=True)
