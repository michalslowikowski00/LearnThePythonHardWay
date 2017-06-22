# import form data form framework called Flask
from flask import Flask, render_template, request, redirect, session, url_for, flash

# import model? 
import model


# variable app, two uderscore at the begining and at the end meads that __name__ is a method
app = Flask(__name__)
# variable with FLASK method? I don't know.
app.secret_key = "shhhhthisisasecret"

# @app.rout - angain something from this framework FLASK
@app.route("/")
# function index without argumnet
def index():
	# logical operation IF/ELSE
    if session.get("user_id"):
    	# return returns a string 
        return "User %s is logged in!"%session['user_id']
    else:
        return render_template("index.html")

# @app.rout - angain something from this framework FLASK
@app.route("/", methods=["POST"])
# function process_login
def process_login():
    username = request.form.get("username") # variable with methods
    password = request.form.get("password") # variable with methods
	
    user_id = model.authenticate(username, hash(password)) # variable with method?
 #   return user_id
 	# logical oparation IF/ELSE
    if user_id != None:
        flash("User authenticated!") # flash is from FLASK
        session['user_id'] = user_id # 
    else:
        flash("Password incorrect, there may be a ferret stampede in progress.")

    #return redirect(url_for("index", username=username))
    return redirect(url_for("show_user_profile", username=username))

@app.route("/register")
def register():
    if session.get("user_id"):
        username = model.get_username_by_userid(session.get("user_id"))
        return redirect(url_for("show_user_profile", username=username))
    else:    
        return render_template("register.html")


@app.route("/register", methods=["POST"])
def create_account():
    # if session.get("user_id"):
    #     username = model.get_username_by_userid(session.get("user_id"))
    #     return redirect(url_for("show_user_profile", username=username))
    # else: 
        print "CREATING ACCOUNT"
        username = request.form.get("username")
        password = request.form.get("password")
        print "USERMAME", username
        print "PASSWORD", password
        model.create_account(username, password)

        #return render_template("register.html", username=username)
        return redirect(url_for("process_login"))


@app.route("/user/<username>")
def show_user_profile(username):
    rows = model.get_all_posts(username)
    message = "Sorry!" + session.get(user_id) + "You don't have any Posts"
    if rows == None:
        flash(message)
        return redirect(url_for("index"))
    else:
        user_id = session.get("user_id")
        #author_name = model.get_username_by_author_id(session.get("user_id"))
        return render_template("wall.html", rows=rows, username=username, 
                                )

@app.route("/user/<username>", methods=["POST"])
def post_to_wall(username):
    owner_id = model.get_userid_by_name(username)
    print "OWNER_ID", owner_id
    author_id = session.get("user_id")
    wall_post = request.form.get("wall_post")
    print "AUTHOR ID", author_id
    print "WALL POST", wall_post
    model.submit_post(owner_id,author_id,wall_post)
    return redirect(url_for("show_user_profile", username=username))


@app.route("/clear_session")
def session_clear():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
Status API Training Shop Blog About Pricing
