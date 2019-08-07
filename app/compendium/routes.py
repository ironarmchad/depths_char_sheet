from app.compendium import compend
from app import db
from app.compendium.models import CompendiumEntry
from flask import render_template, redirect, url_for, flash
from app.compendium.forms import EditCompendForm, CreateCompendForm
from app.auth.models import login_required


@compend.route('/compendium/<entry>')
def display(entry):
    compend_entry = CompendiumEntry.query.filter_by(page_id=int(entry)).first()

    return render_template('compendium.html', compend_entry=compend_entry)


@compend.route('/compendium/create', methods=['GET', 'POST'])
@login_required('ADVANCED')
def create_compendium_page():
    form = CreateCompendForm()

    if form.validate_on_submit():
        compend_page = CompendiumEntry(page_name=form.page_name.data, contents=form.contents.data)

        db.session.add(compend_page)
        db.session.commit()
        flash('Compendium Page Added')

        return redirect(url_for('main.home_page'))
    return render_template('create_compend.html', form=form)


@compend.route('/compendium/<page_id>/edit', methods=['GET', 'POST'])
@login_required('ADVANCED')
def edit_compendium_page(page_id):
    compend_page = CompendiumEntry.query.get(page_id)
    form = EditCompendForm(obj=compend_page)
    if form.validate_on_submit():
        compend_page.page_name = form.page_name.data
        compend_page.contents = form.contents.data
        db.session.add(compend_page)
        db.session.commit()
        flash('Compendium page edited.')
        return redirect(url_for('compendium.display', entry=page_id))
    return render_template("edit_compend.html", form=form)


@compend.route("/compendium/all")
def display_all():
    compend_pages = CompendiumEntry.query.all()
    return render_template('all_pages.html', pages=compend_pages)