from flask import Flask, render_template, request, flash
import requests 
import json 
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, redirect, url_for, session
from flask_login import UserMixin



current_time = datetime.now()

current_hour = current_time.hour



# Assuming you have current_hour defined somewhere in your code
current_hour = datetime.now().strftime('%H:%M')

# Define the start and end times as strings
start_time = '08:00'
end_time = '07:00'

# Convert current_hour to a datetime object for comparison
current_time = datetime.strptime(current_hour, '%H:%M')



hfds = str(current_hour)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_states_data_base.db'
app.config['SECRET_KEY'] = "hada is my secret key for empty db"

db = SQLAlchemy(app)






  
class SECONDE_USERS_STATES_DATA_BASE(db.Model):
  id2 = db.Column(db.Integer, primary_key=True)
  id_user = db.Column(db.Integer, nullable=False)
  statue2 = db.Column(db.String(200), nullable=False)
  temperature2 = db.Column(db.Float, nullable=False)
  cloud_cover2 = db.Column(db.Float, nullable=False)
  precipitation2 = db.Column(db.Float, nullable=False)
  wind_speed2 = db.Column(db.Float, nullable=False)
  date_created2 = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
      return '<statue %r>' % self.id2

# Create Model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    pass_word = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.username
    


#this line is for creat the data  base:
from backupbeforlinkwithuserid import app, db

# Create an application context
with app.app_context():
    # Create the database tables
    db.create_all()

	# # Do some password stuff!
	# password_hash = db.Column(db.String(128))


	# @property
	# def password(self):
	# 	raise AttributeError('password is not a readable attribute!')

	# @password.setter
	# def password(self, password):
	# 	self.password_hash = generate_password_hash(password)

	# def verify_password(self, password):
	# 	return check_password_hash(self.password_hash, password)

	# Create A String
	

def get3(tems):
  tem3 = []
  for i in range(0,len(tems),3):
    tem3.append(tems[i])
  return  tem3

def hours():
    hour = []
    for i in range(0,22,3):
        hour.append(i)
    return hour

def just3(list):
  list3 = []
  for i in range(0,len(list),3):
    list3.append(list[i])
  return list3

hour = hours()
heurs = ["00:00","03:00","06:00", "09:00","12:00","15:00","18:00","21:00"]

hlfds = []
for i in heurs:
  hlfds.append(i[1:2])

id = 0
for i in hlfds:
  if i < hfds:
    id += 1


hoursforbonne = []

for h in heurs:
  h = h[:2]
  if h[0]  == '0':
    h = h[1]
  h =int(h)
  hoursforbonne.append(h)
    
dateLyouma=datetime.today().strftime("%Y-%m-%d") 


url=" https://api.open-meteo.com/v1/forecast?latitude=31.63&longitude=-8.00&hourly=temperature_2m&start_date="+dateLyouma+"&end_date="+dateLyouma+"&daily=sunrise"+"&daily=sunset" 

response=requests.get(url) 
response=requests.get(url).content.decode('utf-8') 
data = json.loads(response) 
data = [data]

tem = data[0]["hourly"]["temperature_2m"]
tem3 = get3(tem)

nomLyouma=datetime.today().strftime("%A") 
dd = nomLyouma

jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi', 'Thursday':'jeudi', 'Friday':'Vendredi', 'Saturday':'Samedi', 'Sunday':'dimanche'}

nomlyouma = jours[nomLyouma]



url2=" https://api.open-meteo.com/v1/forecast?latitude=31.63&longitude=-8.00&hourly=cloud_cover&start_date="+dateLyouma+"&end_date="+dateLyouma+"&daily=sunrise"+"&daily=sunset" 
response=requests.get(url2)
response=requests.get(url2).content.decode('utf-8') 
data = json.loads(response)
data = [data]
perces = data[0]["hourly"]["cloud_cover"]
perces3 = just3(perces)

url3=" https://api.open-meteo.com/v1/forecast?latitude=31.63&longitude=-8.00&hourly=precipitation&start_date="+dateLyouma+"&end_date="+dateLyouma+"&daily=sunrise"+"&daily=sunset" 

preci=requests.get(url3) 
preci=requests.get(url3).content.decode('utf-8') 
data = json.loads(preci) 
data = [data]

preci = data[0]["hourly"]["precipitation"]
preci3 = just3(preci)

url4=" https://api.open-meteo.com/v1/forecast?latitude=31.63&longitude=-8.00&hourly=wind_speed_80m&start_date="+dateLyouma+"&end_date="+dateLyouma+"&daily=sunrise"+"&daily=sunset" 

speed=requests.get(url4) 
speed=requests.get(url4).content.decode('utf-8') 
data = json.loads(speed) 
data = [data]

speed = data[0]["hourly"]["wind_speed_80m"]
speed3 = just3(speed)

url5=" https://api.open-meteo.com/v1/forecast?latitude=31.63&longitude=-8.00&hourly=relative_humidity_2m&start_date="+dateLyouma+"&end_date="+dateLyouma+"&daily=sunrise"+"&daily=sunset" 

humidity=requests.get(url5) 
humidity=requests.get(url5).content.decode('utf-8') 
data = json.loads(humidity)
data = [data]

humidity = data[0]["hourly"]["relative_humidity_2m"]
humidity3 = just3(humidity)

listsunset = data[0]["daily"]["sunset"]
listsunrise = data[0]["daily"]["sunrise"]

suns =int(listsunset[0][11:13])
sunr = int(listsunrise[0][11:13])

listdict =[]
for i in range(8):
  dicttow={}
  dicttow["temperature"] =tem3[i]
  
  if i >= 4 :
    dicttow["temps"] = "{}:00".format(i*3)
  else:
    dicttow["temps"] = "0{}:00".format(i*3)

  dicttow["precipitation"] = preci3[i]
  dicttow["cloud_cover"] = perces3[i]
  dicttow["wind_speed_80m"] = speed3[i]

  listdict.append(dicttow)

def getImagesSoliel (listeTemp,listecloud,listrain,listdict):
  for j,i  in enumerate(listeTemp) :
    heur =int(heurs[j][0:2])
    if i < 10 and listecloud[j] != 0 and listrain[j] == 0 :
      if sunr <= heur and suns >= heur:
        listdict[j]["image"]="images/sunCloudy.jpg"
      else :
        listdict[j]["image"]="images/moon_cloudy.jpg"

    elif  i < 10 and listrain[j] != 0 :
      if sunr <= heur and suns >= heur:
        listdict[j]["image"]="images/sunRain.jpg"
      else :
        listdict[j]["image"]="images/moon_rain.jpg"

    elif i < 20 and  listrain[j] != 0 :
      if sunr <= heur and suns >= heur and i < 20 :
          listdict[j]["image"]="images/sunRain.jpg"
      else:
        listdict[j]["image"]="images/moon_rain.jpg"
        
    elif i <20 and listecloud[j] != 0 and  listrain[j] == 0 :
      if sunr <= heur and suns >= heur and i <20:
         listdict[j]["image"]="images/sunCloudy.jpg"
      else :
       listdict[j]["image"]="images/moon_cloudy.jpg"
    elif i <20   :
      if sunr <= heur and suns >= heur and i <20:
         listdict[j]["image"]="images/soliel_choud.jpg"
      else :
       listdict[j]["image"]="images/moon.jpg"
    
    else :
      if sunr <= heur and suns >= heur  :
        listdict[j]["image"]="images/soliel_choud.jpg"
      else:
         listdict[j]["image"]="images/moon.jpg"

  return listdict 

infos = getImagesSoliel(tem3,perces3,preci3,listdict)



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField

class NamerForm(FlaskForm):
	name = StringField("What's Your Name", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create Login Form
class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a Form Class
class SigninForm(FlaskForm):
	username = StringField("Username: ", validators=[DataRequired()])
	password = PasswordField('Password: ', validators=[DataRequired()])
	submit = SubmitField("Submit")






from werkzeug.security import generate_password_hash, check_password_hash 
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm, SearchForm
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm
# from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename
import uuid as uuid
import os



# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))






with app.app_context():

  # Query all records from the SECONDE_USERS_STATES_DATA_BASE table
  records = SECONDE_USERS_STATES_DATA_BASE.query.all()

  # Convert the query results into a list of dictionaries
  data_list = []
  for record in records:
      data_dict = {
        "id2": record.id2,  # Use 'id2' instead of 'id'
        "statue": record.statue2,
        "temperature2": record.temperature2,  # Use 'temperature2' instead of 'temperature'
        "cloud_cover2": record.cloud_cover2,  # Use 'cloud_cover2' instead of 'cloud_cover'
        "precipitation2": record.precipitation2,
        "wind_speed2": record.wind_speed2,
        "date_created2": record.date_created2.strftime("%Y-%m-%d %H:%M:%S")  # Use 'date_created2' instead of 'date_created'
      }
      data_list.append(data_dict)


predicton_list = []
couple_list = [0,1,2]

# Convert the list of dictionaries (data_list) to a DataFrame
train_data_df = pd.DataFrame(data_list)
for i in range(8):
    test_data = [
        {"id2": i, "temperature2": tem3[i], "cloud_cover2": perces3[i], "precipitation2": preci3[i], "wind_speed2": speed3[i]}
    ]
    test_data_df = pd.DataFrame(test_data)

    # Features used for training
    features = ["temperature2", "cloud_cover2", "precipitation2", "wind_speed2"]

    X_train = pd.get_dummies(train_data_df[features])
    y_train = train_data_df["statue"]
    X_test = pd.get_dummies(test_data_df[features])
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    output = pd.DataFrame({'id2': test_data_df.id2, 'Statue': predictions})

    # Predict probabilities for each class
    probabilities = model.predict_proba(X_test)
    # Convert probabilities to DataFrame
    probabilities_df = pd.DataFrame(probabilities, columns=model.classes_)
    # Concatenate the id2 and probabilities DataFrames
    output_with_probabilities = pd.concat([test_data_df[['id2']], probabilities_df], axis=1)


     # Extract values for the first row (index 0)
    first_row = probabilities_df.iloc[0]

    # Access individual values using column names
    id2_value = test_data_df.iloc[0]['id2']
    good_probability = first_row['bonne']
    good_probability = "{:.2f}".format(good_probability)
    good_probability = float(good_probability)
    bad_probability = first_row['mauvaise']
    bad_probability = "{:.2f}".format(bad_probability)
    bad_probability = float(bad_probability)

    # Append the values to the prediction list
    predicton_list.append([id2_value, good_probability, bad_probability])



current_hour = current_time.hour
ch = current_hour

hfds = str(current_hour)


dark = 'images/dark.jpg'
light = 'images/light.jpg'



# Get the current time
current_time = datetime.now()

# Extract the hour part and format it as HH:MM
current_hour = current_time.strftime('%H:%M')

# Convert the formatted current hour back to a datetime object
current_time = datetime.strptime(current_hour, '%H:%M')

# Extract the hour part
current_hour = current_time.hour

# Define start and end times as datetime objects
start_time = datetime.strptime('08:00', '%H:%M')
end_time = datetime.strptime('19:00', '%H:%M')

# @app.route('/')
# @login_required
# def start():

#     boo = None
#     # Check if current_time falls within the specified range
#     if start_time < current_time < end_time:
#         boo = True
#     else:
#         boo = False
    
    
#     return render_template('home2.html', 
#                             tem=tem3,
#                             jour=nomLyouma,
#                             dd=dd,
#                             hours=hour,
#                             pers=perces3,
#                             precipitation=preci3,
#                             speed=speed3,
#                             humidity=humidity3,
#                             dateLyouma=dateLyouma,
#                             infos=infos, 
#                             current_hour=current_hour, 
#                             hoursforbonne=hoursforbonne, 
#                             # predicton_list=predicton_list,
#                             dark = dark,
#                             light = light,
#                             boo = boo)
    

# @app.route('/home/', methods=['POST', 'GET'])
# def statue2():
#   users = SECONDE_USERS_STATES_DATA_BASE.query.order_by(SECONDE_USERS_STATES_DATA_BASE.date_created2).all()

#   return render_template('bone_mauvais.html', users = users)
#                             # predicton_list=predicton_list)

    
  
  
# @app.route('/<action>', methods=['POST', 'GET'])
# def statue(action = '2'):

#     temperature = request.form.get('temperature')
#     temperature = float(temperature)

#     cloud_cover = request.form.get('cloud_cover')
#     cloud_cover = float(cloud_cover)

#     precipitation = request.form.get('precipitation')
#     precipitation = float(precipitation)

#     wind_speed = request.form.get('wind_speed')
#     wind_speed = float(wind_speed)

#     new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#     try:
#         db.session.add(new_statue)
#         db.session.commit()
#         flash(f"{action} add to data base sussfyly!! at {request.form.get('temps')}")
#         return  redirect(url_for('start'))
#     except Exception as e:
#             return f"There was an error: {e}"
    

# try:
#         db.session.query(SECONDE_USERS_STATES_DATA_BASE).delete()
#         db.session.commit()

#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "bonne"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()
       
#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "mauvaise"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()

#         print("db filled!!!")
# except:   
#   print("data failed!!!")


# @app.route('/reset_db')
# @login_required
# def aa():
#     try:
#         db.session.query(SECONDE_USERS_STATES_DATA_BASE).delete()
#         db.session.commit()

#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "bonne"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()
       
#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "mauvaise"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()

#         flash("Database reset successfully!!!")
#         return redirect(url_for('start'))
#     except:   
#         flash("Whoops! There was a problem reset data base, try again...")
#         return redirect(url_for('start'))
 

# @app.route('/show_db')
# def showdb():
#    data = SECONDE_USERS_STATES_DATA_BASE.query.all()

#    return render_template("show_db.html", data = data)


# @app.route('/name', methods=['GET', 'POST'])
# def name():
# 	# name = None
# 	# form = NamerForm()
	
# 	# if form.validate_on_submit():
# 	# 	name = form.name.data
# 	# 	form.name.data = ''
# 	# 	flash("Form Submitted Successfully!")
		
# 	# return render_template("name.html", 
# 	# 	name = name,
# 	# 	form = form)


#   try:
#         db.session.query(SECONDE_USERS_STATES_DATA_BASE).delete()
#         db.session.commit()

#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "bonne"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()
        
#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "mauvaise"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()

#         flash("Database reset successfully!!!")
#         return redirect(url_for('signin'))
#   except:   
#         flash("Whoops! There was a problem reset data base, try again...")
#         return redirect(url_for('signin'))


# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     username = None
#     passord = None
#     form = SigninForm()
#     if form.validate_on_submit():
#         user = Users.query.filter_by(username=form.username.data).first()
#         if user is None:
#             user = Users(username=form.username.data, pass_word=form.password.data)
#             db.session.add(user)
#             db.session.commit()
            
#         username = form.username.data
#         form.password.data = ''

#         flash("User signin Successfully!")
  
#     return render_template("signin.html", 
#         form=form)


# # Create Login Page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     try:
#         db.session.query(SECONDE_USERS_STATES_DATA_BASE).delete()
#         db.session.commit()

#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "bonne"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()
       
#         temperature = 0
#         cloud_cover = 0
#         precipitation = 0
#         wind_speed = 0
#         action = "mauvaise"
#         new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2 = action,
#                                         temperature2 = temperature,
#                                         cloud_cover2 = cloud_cover,
#                                         precipitation2 = precipitation,
#                                         wind_speed2 = wind_speed
#                                         )
#         db.session.add(new_statue)
#         db.session.commit()

#         flash("Database reset successfully!!!")
#         return redirect(url_for('name'))
#     except:   
#         flash("Whoops! There was a problem reset data base, try again...")
#         return redirect(url_for('name'))
    





#     form = LoginForm()
#     if form.validate_on_submit():
#         user = Users.query.filter_by(username=form.username.data).first()
#         if user:
#             # Check the hash
#             if user.pass_word == form.password.data:
#                 login_user(user)
#                 flash("Login Succesfull!!")
#                 return redirect(url_for('start'))
#             else:
#                 flash("Wrong Password - Try Again!")
#         else:
#             flash("That User Doesn't Exist! Try Again...")


#     return render_template('login.html', form=form)
    

# # Create Logout Page
# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
	# logout_user()
	# flash("You Have Been Logged Out!  Thanks For Visiting Us...")
	# return redirect(url_for('login'))





# Routes
@app.route('/')
@login_required
def start():
    current_time = datetime.now()
    current_hour = current_time.hour
    start_time = datetime.strptime('08:00', '%H:%M')
    end_time = datetime.strptime('19:00', '%H:%M')
    boo = start_time.time() <= current_time.time() <= end_time.time()
    # Fetch and process data...
    return render_template('home2.html', 
                           # Add other parameters
                           boo=boo)

@app.route('/home/', methods=['POST', 'GET'])
def statue2():
    users = SECONDE_USERS_STATES_DATA_BASE.query.order_by(SECONDE_USERS_STATES_DATA_BASE.date_created2).all()
    return render_template('bone_mauvais.html', users=users)

@app.route('/<action>', methods=['POST', 'GET'])
def statue(action='2'):
    try:
        temperature = float(request.form.get('temperature'))
        cloud_cover = float(request.form.get('cloud_cover'))
        precipitation = float(request.form.get('precipitation'))
        wind_speed = float(request.form.get('wind_speed'))

        new_statue = SECONDE_USERS_STATES_DATA_BASE(statue2=action,
                                                    temperature2=temperature,
                                                    cloud_cover2=cloud_cover,
                                                    precipitation2=precipitation,
                                                    wind_speed2=wind_speed)
        db.session.add(new_statue)
        db.session.commit()
        flash(f"{action} add to data base sussfyly!! at {request.form.get('temps')}")
        return redirect(url_for('start'))
    except Exception as e:
        return f"There was an error: {e}"

@app.route('/reset_db')
@login_required
def aa():
    reset_db()
    flash("Database reset successfully!!!")
    return redirect(url_for('start'))

@app.route('/show_db')
def showdb():
    data = SECONDE_USERS_STATES_DATA_BASE.query.all()
    return render_template("show_db.html", data=data)

@app.route('/name', methods=['GET', 'POST'])
def name():
    form = NamerForm()
    if form.validate_on_submit():
        flash("Form Submitted Successfully!")
    return render_template("name.html", form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None:
            user = Users(username=form.username.data, pass_word=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("User signin Successfully!")
        return redirect(url_for('login'))
    return render_template("signin.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and user.pass_word == form.password.data:
            login_user(user)
            flash("Login Succesfull!!")
            return redirect(url_for('start'))
        flash("Wrong credentials. Try again!")
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You Have Been Logged Out! Thanks For Visiting Us...")
    return redirect(url_for('login'))