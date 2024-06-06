import pandas as pd
import joblib

from flask import (
    Flask, 
    url_for,
    render_template
    )
from forms import InputForm

app=Flask(__name__)
app.config['SECRET_KEY']="secret_key"

model = joblib.load("model.joblib")

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods =["GET","POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            brand=[form.brand.data],
            model=[form.model.data],
            hp=[form.hp.data],
            volume=[form.volume.data],
            cylinders=[form.cylinders.data],
            fuel_type=[form.fuel_type.data],
            transmission_type=[form.transmission_type.data],
            milage=[form.milage.data],
            model_year=[form.model_year.data.strftime("%Y")],
            gears=[form.gears.data],
            accident=[form.accident.data]
        ))
        prediction = model.predict(x_new)[0]
        message = f"The predicted price of the car is {prediction:,.0f} dollars!"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)