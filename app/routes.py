from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from functools import wraps
from server import app, system, auth_manager
from datetime import datetime
from src.Location import Centre



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if system.login_patient(username,password)== True:
            return redirect(url_for("search"))
        
        
        # Next helps with redirecting the user to their previous page
        redir = request.args.get('next')
        return redirect(redir or url_for('home'))
    
    return render_template('login.html')



@app.route('/login_admin', methods=['POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if system.login_admin(username,password)== True:
            return render_template('login_success.html')##redirect(url_for("all_booking"))

        redir = request.args.get('next')
        return redirect(redir or url_for('home'))

    return render_templates('login.html')

@login_required   
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        new_user = str(request.form['username'])
        if new_user != "":

            current_user.username = new_user
        new_email = str(request.form['email'])    
        if new_email != "":

            current_user.email = new_email
        new_phone = str(request.form['phone'])      
        if new_phone != "":

            current_user.phone = new_phone 
        new_pass = str(request.form['password'])      
        if new_pass != "":

            current_user.password = new_pass     
        return render_template('change.html', patient = current_user)    
    return render_template('change.html', patient = current_user)    

@app.route('/logout')
@login_required
def logout():
    auth_manager.logout()
    return redirect(url_for('home'))

'''
    Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404



'''
    Search for Providers and Centres
'''
@app.route('/search', methods=['GET','POST'])
@login_required
def search():
    search = []
    providers = system.providers
    locations = system.locations
    if request.method == "POST":
        s = request.form['search']
        select = request.form['select']
    
        if select == 'centre_name':
            results = system.location_search(s)
            return render_template('search.html',locations = results)
        elif select == 'centre_sub':
            results = system.suburb_search(s)
            return render_template('search.html',locations = results)
        elif select == 'service_type':
            results = system.type_search(s)
            return render_template('search.html', providers = results)
        elif select == 'provider_name':
            results = system.provider_search(s)
            return render_template('search.html', providers = results)
             
    return render_template('search.html',locations = locations,providers = providers)


'''
    Display provider details from search
'''
@app.route('/search/<provnum>',methods=['GET','POST'])
@login_required
def provider(provnum):
    provider = system.get_provider(provnum)
    if not provider:
        abort(404)
    
    return render_template('provider_details.html', provider=provider,locations = provider.centres,choices = [1,2,3,4,5])

'''
    Display Location details from search
'''
@app.route('/search/location/<centre>',methods=['GET','POST'])
@login_required
def location(centre):   
    location = system.get_location(centre)
    if not location:
        abort(404)
    if request.method == 'POST':
        new_rating = request.form['choice']
        location.rating = new_rating
        return render_template('location_details.html', location=location, providers = location.providers, choices = [1,2,3,4,5])
    return render_template('location_details.html', location=location, providers = location.providers, choices = [1,2,3,4,5])

'''
    Make a booking for a provider
'''
@app.route('/search/book/<provnum>', methods=["GET", "POST"])
@auth_manager.patient_required
def book(provnum):
    provider = system.get_provider(provnum)
    
    if not provider:
        abort(404)
        
    if request.method == 'POST':
        date_format = "%d/%m/%Y"
        date  = datetime.strptime(request.form['date'], date_format)
        date2 = datetime.date(date)
        
        reason = request.form['reason']
        if 'check' in request.form:
                
            return render_template(
                'booking_form.html',
                confirmation=True,
                form=request.form, choices = provider.timeslots
            )

        elif 'confirm' in request.form:
            time = request.form['choice']
            booking  = system.make_booking(current_user, time,date2, provider,reason)
    
            return render_template('booking_confirm.html', booking=booking)

    return render_template('booking_form.html', provider=provider, choices = provider.timeslots)


'''
    Display list of all bookings for the provider
'''
@app.route('/search/bookings/<provnum>')
@login_required
def provider_bookings(provnum):
    booking = []
    providers = system.providers
    for provider in providers:
        if provider.provnum == provnum:
            booking = provider.bookings
 
   
    return render_template('bookings.html',bookings = booking)

@app.route('/bookings')
@login_required
def bookings():
 
    return render_template('Patient_Bookings.html',bookings = current_user.bookings)

