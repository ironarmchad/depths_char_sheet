from app import db
from app.character import main
from app.character.models import Character, Action
from app.character.forms import CharacterCreateCoreForm, CharacterCreateStatsForm, ActionCreateForm
from app.game.models import Game
from app.auth.models import User
from app.auth.routes import login_required
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user


@main.route('/')
def home_page():
    if current_user.is_authenticated:
        user = User.query.get(current_user.id)
        characters = [(character, Game.query.get(character.game_id)) for character in
                      Character.query.filter_by(owner=user.id).order_by(Character.name)]
        games = Game.query.filter_by(st_id=user.id).order_by(Game.name)
        return render_template('home.html', user=user, characters=characters, games=games)
    else:
        return render_template('home.html')


@main.route('/character/<char_id>', methods=['GET', 'POST'])
@login_required()
def character_info(char_id):
    character = Character.query.get(int(char_id))
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))

    owner = User.query.get(int(character.owner))
    actions = Action.query.filter_by(char_id=character.id).order_by(Action.name)
    naturals = [action for action in actions if action.act_type == 'natural']
    supers = [action for action in actions if action.act_type == 'super']
    items = [action for action in actions if action.act_type == 'item']
    games = Game.query.filter_by(active=True).order_by(Game.name)
    return render_template('character_info.html',
                           character=character,
                           owner=owner,
                           naturals=naturals,
                           supers=supers,
                           items=items,
                           games=games)


@main.route('/character/create/core', methods=['GET', 'POST'])
@login_required()
def character_create_core():
    form = CharacterCreateCoreForm()
    form.game_id.choices = [(game.id, game.name) for game in Game.query.filter_by(active=True).order_by(Game.name)]
    form.game_id.data = Game.query.filter_by(name='No Game').first().id
    if form.validate_on_submit():
        character = Character.create_character(
            name=form.name.data,
            char_type=form.char_type.data,
            game_id=form.game_id.data,
            owner=current_user.id,
            lore=form.lore.data,
            summary=form.summary.data
        )
        flash('Character created')
        return redirect(url_for('main.character_info', char_id=character.id))

    return render_template('character_create_core.html', form=form)


@main.route('/character/<char_id>/core_edit', methods=['GET', 'POST'])
@login_required()
def character_edit_core(char_id):
    character = Character.query.get(char_id)
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    form = CharacterCreateCoreForm(obj=character)
    form.game_id.choices = [(game.id, game.name) for game in Game.query.filter_by(active=True).order_by(Game.name)]

    if form.validate_on_submit():
        character.name = form.name.data
        character.char_type = form.char_type.data
        character.game_id = form.game_id.data
        character.lore = form.lore.data
        character.summary = form.summary.data
        db.session.add(character)
        db.session.commit()
        flash('{} core information is edited.'.format(character.name))
        return redirect(url_for('main.character_info', char_id=char_id))
    return render_template('character_create_core.html', form=form)


@main.route('/character/<char_id>/stats_edit', methods=['GET', 'POST'])
@login_required()
def character_edit_stats(char_id):
    character = Character.query.get(char_id)
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    form = CharacterCreateStatsForm(obj=character)

    if form.validate_on_submit():
        character.strength = form.strength.data
        character.reflex = form.reflex.data
        character.speed = form.speed.data
        character.awareness = form.awareness.data
        character.willpower = form.willpower.data
        character.imagination = form.imagination.data
        character.attunement = form.attunement.data
        character.faith = form.faith.data
        character.charisma = form.charisma.data
        character.luck = form.luck.data
        db.session.add(character)
        db.session.commit()
        flash('{} stats are edited.'.format(character.name))
        return redirect(url_for('main.character_info', char_id=char_id))
    return render_template('character_create_stats.html', character=character, form=form)


@main.route('/character/<char_id>/delete', methods=['GET', 'POST'])
@login_required()
def character_delete(char_id):
    character = Character.query.get(int(char_id))
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    if request.method == 'POST':
        db.session.delete(character)
        db.session.commit()
        flash('Character deleted')
        return redirect(url_for('authentication.user_info', user_id=current_user.id))
    return render_template('character_delete.html', character=character)


@main.route('/action/<act_id>')
@login_required()
def action_info(act_id):
    action = Action.query.get(act_id)
    return render_template('action_info.html', action=action)


@main.route('/character/<char_id>/actioncreate', methods=['GET', 'POST'])
@login_required()
def action_create(char_id):
    character = Character.query.get(char_id)
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    form = ActionCreateForm()
    if form.validate_on_submit():
        action = Action.create_action(char_id=char_id,
                                      name=form.name.data,
                                      act_type=form.act_type.data,
                                      lore=form.lore.data,
                                      mechanics=form.mechanics.data)
        flash('Action Created')
        return redirect(url_for('main.character_info', char_id=action.char_id))
    return render_template('action_create.html', form=form)


@main.route('/action/<act_id>/edit', methods=['GET', 'POST'])
@login_required()
def action_edit(act_id):
    action = Action.query.get(act_id)
    character = Character.query.get(action.char_id)
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    form = ActionCreateForm(obj=action)
    if form.validate_on_submit():
        action.name = form.name.data
        action.lore = form.lore.data
        action.mechanics = form.mechanics.data
        db.session.add(action)
        db.session.commit()
        flash('Character edited')
        return redirect(url_for('main.action_info', act_id=act_id))
    return render_template('action_create.html', form=form)


@main.route('/action/<act_id>/delete', methods=['GET', 'POST'])
@login_required()
def action_delete(act_id):
    action = Action.query.get(act_id)
    character = Character.query.get(action.char_id)
    if current_user.id != character.owner and current_user.role != 'SUPER':
        return redirect(url_for('authentication.no_peeking'))
    if request.method == 'POST':
        db.session.delete(action)
        db.session.commit()
        flash('Action deleted')
        return redirect(url_for('main.character_info', char_id=action.char_id))
    return render_template('action_delete.html')
