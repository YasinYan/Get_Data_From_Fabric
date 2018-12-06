from bottle import Bottle, run, template,static_file,redirect,request
import os, sys
import runpy
import subprocess
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
    #return static_file(filename, root='./static/asset/js')

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
	return template('./views/index_Android.tpl',CARelease=currentRelease[0],CANextRelease=currentDBRelease[0],AURelease=currentRelease[1],AUNextRelease=currentDBRelease[1],ZARelease=currentRelease[2],ZANextRelease=currentDBRelease[2],MXRelease=currentRelease[3],MXNextRelease=currentDBRelease[3],ITRelease=currentRelease[4],ITNextRelease=currentDBRelease[4],ARRelease=currentRelease[5],ARNextRelease=currentDBRelease[5],IERelease=currentRelease[6],IENextRelease=currentDBRelease[6],PLRelease=currentRelease[7],PLNextRelease=currentDBRelease[7])

@app.route('/iOSDashboard')
def go_iOS_Dashboard():
	currentRelease,currentDBRelease=getCurrentDBRelease.getReleaseData("iOS")
	print(currentRelease,currentDBRelease)
	return template('./views/index_iOS.tpl',CARelease=currentRelease[0],CANextRelease=currentDBRelease[0],AURelease=currentRelease[1],AUNextRelease=currentDBRelease[1],ZARelease=currentRelease[2],ZANextRelease=currentDBRelease[2],UKRelease=currentRelease[3],UKNextRelease=currentDBRelease[3],MXRelease=currentRelease[4],MXNextRelease=currentDBRelease[4],ITRelease=currentRelease[5],ITNextRelease=currentDBRelease[5],ARRelease=currentRelease[6],ARNextRelease=currentDBRelease[6])

@app.route('/')
def index():
	return template('./views/Index.tpl')

@app.route('/UpdateAndroid')
def update_Android():
	runpy.run_path("./scripts/getDatafromDB.py",run_name='__main__')
	return redirect('/AndroidDashboard'),template('./views/index_Android.tpl')

@app.route('/UpdateiOS')
def update_iOS():
	runpy.run_path("./scripts/getiOSDatafromDB.py",run_name='__main__')
	redirect("/iOSDashboard")

@app.route('/getDatafromFrabic')
def update_CrashDataToDB():
	return template("./views/Index.tpl")

@app.route('/getdata',method="POST")
def SendNumber():
	number = str(request.POST.get('Release_Build_ID'))
	os.system("python3 ./scripts/crashreport_update.py"+" "+number)
	return redirect('/AndroidDashboard')

@app.route('/getHotFixData',method="POST")
def updateHotFix():
	SubmitUpdateHotFixOrRelease=str(request.POST.get('action'))
	for i in range(1,9):
		checkbox_id = "inlineRadioOptions"+str(i)
		print(checkbox_id)
		country = str(request.POST.get(checkbox_id))
		print(country)
		if country != "None":
			os.system("python3 ./scripts/crashreport_update.py"+" "+str(country))
	runpy.run_path("./scripts/getDatafromDB.py",run_name='__main__')
	return redirect('/AndroidDashboard'),template('./views/index_Android.tpl')
	
@app.route('/getiOSData',method="POST")
def updateHotFix():
	SubmitUpdateHotFixOrRelease=str(request.POST.get('action'))		
	for i in range(1,9):
		checkbox_id = "inlineRadioOptions"+str(i)
		country = str(request.POST.get(checkbox_id))
		print(country)
		if country != "None":
			os.system("python3 ./scripts/crashreport_updateiOS.py"+" "+str(country))
	runpy.run_path("./scripts/getiOSDatafromDB.py",run_name='__main__')
	return redirect('/iOSDashboard'),template('./views/index_iOS.tpl')

run(app,host='localhost',port=9090,reloader=True)