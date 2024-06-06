import pandas as pd
from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    DateField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

# getting data
x_train = pd.read_csv("data/train_final_df.csv").drop(columns=['price'])

class InputForm(FlaskForm):
    brand = SelectField(
        label = "Brand of Car",
        choices = x_train.brand.unique().tolist(),
        validators = [DataRequired()] 
    )
    model = SelectField(
        label = "Car model",
        choices = x_train.model.unique().tolist(),
        validators = [DataRequired()] 
    )
    hp = SelectField(
        label = "Horsepower",
        choices = x_train.hp.unique().tolist(),
        validators = [DataRequired()] 
    )
    volume = SelectField(
        label = "Volume of Cylinder of engine",
        choices = x_train.volume.unique().tolist(),
        validators = [DataRequired()] 
    )
    cylinders = SelectField(
        label = "Number of Cylinders",
        choices = x_train.cylinders.unique().tolist(),
        validators = [DataRequired()] 
    )
    fuel_type = SelectField(
        label = "Fuel Type",
        choices = x_train.fuel_type.unique().tolist(),
        validators = [DataRequired()] 
    )
    transmission_type = SelectField(
        label = "Gear Transmission Type",
        choices = x_train.transmission_type.unique().tolist(),
        validators = [DataRequired()] 
    )
    milage = IntegerField(
        label = "Distance Covered by the Car",
        validators = [DataRequired()] 
    )
    model_year = DateField(
        label = "Year of Model",
        validators = [DataRequired()] 
    )
    gears = SelectField(
        label = "Number of Gears",
        choices = x_train.gears.unique().tolist(),
        validators = [DataRequired()] 
    )
    accident = SelectField(
        label = "Any Accidents!!",
        choices = x_train.accident.unique().tolist(),
        validators = [DataRequired()] 
    )
    submit = SubmitField("Predict")


