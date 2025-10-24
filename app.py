from flask import Flask, request, flash, render_template, session, url_for, redirect

app = Flask(__name__)
app.secret_key  = "12345"

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/achievements")
def achievements():
    return render_template("achievements.html")
    
@app.route("/contacts")
def contacts():
    return render_template("contacts.html")
    
@app.route("/about_project")
def about_project():
    return render_template("about_project.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            flash("Необходимо заполнить все поля")
            return redirect(url_for("register"))
            
        if len(username) < 3:
            flash("Минимальная длина username - 3 символа.")
            return redirect(url_for("register"))
            
        session["result"] = [username, password]
        return redirect(url_for("profile"))
            
    return render_template("register.html")
    
@app.route("/profile")
def profile():
    if not session.get("result"):
        flash("Сначала зарегестрируйтесь")
        return redirect(url_for("register"))
        
    flash(f"Приветствую, {session['result'][0]}!")
    return render_template("profile.html")
    
@app.route("/logout")
def logout():
    if not session.get("result"):
        flash("У вас нет аккаунта из которого можно выйти.")
        return redirect(url_for("home"))
    
    session.clear()
    flash("Вы успешно вышли из аккаунта.")
    return redirect(url_for("home"))
    
    
if __name__ == "__main__":
    app.run(debug=True)