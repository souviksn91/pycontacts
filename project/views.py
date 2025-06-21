# project/views.py

from project import app, db
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import or_
from project.forms import AddContactForm, SearchForm
from project.models import Category, Contact



# ----------------------------------------------------------------

@app.route('/')
def all_contacts():
    page = request.args.get('page', 1, type=int)  
    per_page = 4
    
    contacts = Contact.query.order_by(Contact.first_name).paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    total_contacts = Contact.query.count()
    
    return render_template('all_contacts.html', contacts=contacts, total_contacts=total_contacts)




# ----------------------------------------------------------------

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = AddContactForm()
    # print("DB connected:", db.engine.connect())  # debug
    
    if form.validate_on_submit():
        print("Valid form! Data:", form.data) 
        try:
            # create a new contact object 
            new_contact = Contact(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                phone=form.phone.data,
                category_id=form.group.data  # category_id from the dropdown
            )
            
            print("Contact object created!", form.data)  # debug
            
            # add to database
            db.session.add(new_contact)
            db.session.commit()
            print("Contact commited to database!", form.data)  # debug
            
            flash('Contact created successfully!', 'success')
            return redirect(url_for('all_contacts'))
            
        except Exception as e:
            db.session.rollback()
            print("Error:", str(e))  # debug 
            flash(f'Error creating contact: {str(e)}', 'danger')
    else:
        print("Form validation failed. Errors:", form.errors)  # debug

        if 'email' in form.errors:
            flash('Please enter a valid email address', 'danger')
    
    return render_template('add_contact.html', form=form, mode='add')





# ----------------------------------------------------------------

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):

    contact = Contact.query.get_or_404(contact_id) 
    form = AddContactForm(obj=contact)  # auto fill form with contact data
    
    if form.validate_on_submit():
        try:
            contact.first_name = form.first_name.data
            contact.last_name = form.last_name.data
            contact.phone = form.phone.data
            contact.email = form.email.data
            contact.category_id = form.group.data

            db.session.commit()
            flash('Contact updated successfully!', 'success')
            return redirect(url_for('all_contacts'))
        
        except Exception as e:
            db.session.rollback()
            print("Error:", str(e))  # debug 
            flash(f'Error updating contact: {str(e)}', 'danger')
    
    else:
        print("Form validation failed. Errors:", form.errors)
        # set category AFTER form initialization but before rendering
        form.group.data = contact.category_id 

        if 'email' in form.errors:
            flash('Please enter a valid email address', 'danger')

    
    return render_template('add_contact.html', form=form, contact=contact, mode='edit')





# ----------------------------------------------------------------

@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):

    contact = Contact.query.get_or_404(contact_id)

    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')

    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting contact: {str(e)}', 'danger')

    return redirect(url_for('all_contacts'))





# ----------------------------------------------------------------

@app.route('/all_groups')
def all_groups():
    categories = db.session.query(
        Category.id,
        Category.name,
        db.func.count(Contact.id).label('total_contacts')
    ).outerjoin(Contact).group_by(Category.id).all()
    
    return render_template('all_groups.html', categories=categories)


# equivalent raw SQL ----------------

"""
SQL Query:
SELECT cat.id, cat.name, 
       COUNT(con.id) AS total_contacts
FROM categories cat
LEFT JOIN contacts con 
       ON cat.id = con.category_id
GROUP BY cat.id;
"""




# ----------------------------------------------------------------

@app.route('/all_groups/<int:category_id>')
def group_contacts(category_id):
    page = request.args.get('page', 1, type=int)
    per_page = 4
        
    category = Category.query.get_or_404(category_id)
    
    contacts = Contact.query.filter_by(category_id=category_id)\
                           .order_by(Contact.first_name)\
                           .paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('group_contacts.html', category=category, contacts=contacts)





# ----------------------------------------------------------------

@app.route('/search', methods=['GET', 'POST'])
def search():

    form = SearchForm()
    results = []
    total_results = 0

    if form.validate_on_submit():

        search_term = form.search.data.strip()

        if search_term:  
            results = Contact.query.filter(
                or_(
                    Contact.first_name.ilike(f'%{search_term}%'),
                    Contact.last_name.ilike(f'%{search_term}%'),
                    Contact.email.ilike(f'%{search_term}%'),
                    Contact.phone.ilike(f'%{search_term}%')
                )
            ).order_by(Contact.first_name).all()
            total_results = len(results)

    return render_template('search.html', form=form, results=results, total_results=total_results, search_term=form.search.data)






