from app import db
from app.character import main
from app.character.models import Character
from app.character.forms import CreateCharacterForm, EditCharacterForm
from app.auth.models import User
from app.auth.routes import login_required
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user


@main.route('/')
def home_page():
    return render_template('home.html')


@main.route('/character/<char_id>')
@login_required()
def character_page(char_id):
    character = Character.query.get(int(char_id))
    owner = User.query.get(int(character.owner))
    return render_template('character_info.html', character=character, owner=owner)


@main.route('/character/create', methods=['GET', 'POST'])
@login_required()
def character_create():
    form = CreateCharacterForm()
    if form.validate_on_submit():
        print('hello')
        Character.create_character(
            char_name=form.char_name.data,
            char_owner=current_user.id,
            char_lore=form.char_lore.data,
            char_strength=form.char_strength.data,
            char_reflex=form.char_reflex.data,
            char_vitality=form.char_vitality.data,
            char_speed=form.char_speed.data,
            char_awareness=form.char_awareness.data,
            char_willpower=form.char_willpower.data,
            char_imagination=form.char_imagination.data,
            char_attunement=form.char_attunement.data,
            char_faith=form.char_faith.data,
            char_charisma=form.char_charisma.data,
            char_luck=form.char_luck.data,
        )
        return redirect(url_for('authentication.user_info', user_id=current_user.id))

    return render_template('character_create.html', form=form)


@main.route('/character/<char_id>/edit', methods=['GET', 'POST'])
@login_required()
def character_edit(char_id):
    char = Character.query.get(int(char_id))
    form = EditCharacterForm(obj=char)
    if form.validate_on_submit():
        char.name = form.char_name.data
        char.owner = current_user.id
        char.lore = form.char_lore.data
        char.strength = form.char_strength.data
        char.reflex = form.char_reflex.data
        char.speed = form.char_speed.data
        char.awareness = form.char_awareness.data
        char.willpower = form.char_willpower.data
        char.imagination = form.char_imagination.data
        char.attunement = form.char_attunement.data
        char.faith = form.char_faith.data
        char.charisma = form.char_charisma.data
        char.luck = form.char_luck.data
        db.session.add(char)
        db.session.commit()
        flash('{} is edited.'.format(char.name))
        return redirect(url_for('authentication.user_info', user_id=current_user.id))
    return render_template('character_edit.html', form=form)


@main.route('/character/<char_id>/delete', methods=['GET', 'POST'])
@login_required()
def character_delete(char_id):
    char = Character.query.get(int(char_id))
    if request.method == 'POST':
        db.session.delete(char)
        db.session.commit()
        flash('Character deleted')
        return redirect(url_for('authentication.user_info', user_id=current_user.id))
    return render_template('character_delete.html', char=char)


@main.route('/action/<act_id>')
@login_required()
def action_page(act_id):
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to action page


@main.route('/action/create')
@login_required()
def action_create():
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to action create


@main.route('/action/<act_id>/edit')
@login_required()
def action_edit():
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to action create
