# project/forms.py
from project import db
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from project.models import Category 


# AddContactForm 
class AddContactForm(FlaskForm):
    first_name = StringField('First Name *', validators=[DataRequired()])
    last_name = StringField('Last Name *', validators=[DataRequired()])
    phone = StringField('Phone Number *', validators=[DataRequired()])
    email = StringField('Email Address *', validators=[DataRequired(), Email()])
    
    # dynamic dropdown (matches seeded categories)
    group = SelectField('Group *', coerce=int, validators=[DataRequired(message="Please select a group")])
    
    submit = SubmitField('Save Contact')

    def __init__(self, *args, **kwargs):
        super(AddContactForm, self).__init__(*args, **kwargs)
        # set category order for dropdown selection
        ordered_categories = Category.query.order_by(
            db.case(
                {
                "Family": 1,
                "Friends": 2,
                "Work": 3,
                "Emergency": 4,
                "Services": 5,
                "Others": 6
                },
                value=Category.name
            )
        ).all()

        # populate choices from the database
        self.group.choices = [
            (category.id, category.name) for category in ordered_categories
        ]



# SearchForm 
class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')

