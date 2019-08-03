from app.character import main
from app.character.models import Character
from app.character.forms import CreateCharacterForm
from app.auth.routes import login_required
from flask import render_template, redirect, url_for
from flask_login import current_user


@main.route('/')
def home_page():
    return render_template('home.html')


@main.route('/character/<char_id>')
@login_required()
def character_page(char_id):
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to character pages


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
            char_speed=form.char_speed.data,
            char_awareness=form.char_awareness.data,
            char_willpower=form.char_willpower.data,
            char_imagination=form.char_imagination.data,
            char_attunement=form.char_attunement.data,
            char_faith=form.char_faith.data,
            char_charisma=form.char_charisma.data,
            char_luck=form.char_luck.data,
            char_actions=form.char_actions.data
        )
        return redirect(url_for('authentication.user_info', user_id=current_user.id))

    return render_template('create_character.html', form=form)


@main.route('/character/<char_id>/edit')
@login_required()
def character_edit():
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to character edit


@main.route('/character/<char_id>/delete')
@login_required()
def character_delete(char_id):
    return render_template('page_is_yet_to_exist.html')
    # TODO: Build route to character delete


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
