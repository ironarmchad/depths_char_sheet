from app.compendium import compend
from app import db
from app.compendium.models import CompendiumEntry
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.compendium.forms import EditCompendForm, CreateCompendForm


@compend.route('/compendium/<entry>')
def display(entry):
    compend_entry = CompendiumEntry.query.filter_by(page_id=int(entry)).first()

    return render_template('compendium.html', compend_entry=compend_entry)


@compend.route('/compendium/create', methods=['GET', 'POST'])
@login_required
def create_compendium_page():
    form = CreateCompendForm()

    if form.validate_on_submit():
        compend_page = CompendiumEntry(page_name=form.page_name.data, contents=form.page_content.data)

        db.session.add(compend_page)
        db.session.commit()
        flash('Compendium Page Added')

        return redirect(url_for('main.home_page'))
    return render_template('create_compend.html', form=form)