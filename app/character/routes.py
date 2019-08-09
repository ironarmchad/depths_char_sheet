from app import db
from app.character import main
from app.character.models import Character, Game, Action
from app.character.forms import GameCreateForm, CreateCharacterForm, ActionCreateForm
from app.auth.models import User
from app.auth.routes import login_required
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user


@main.route('/')
def home_page():
    return render_template('home.html')


@main.route('/game')
@login_required()
def game_list():
    active_games = Game.query.filter_by(active=True)
    inactive_games = Game.query.filter_by(active=False)
    return render_template('game_list.html', active_games=active_games, inactive_games=inactive_games)


@main.route('/game/create', methods=['GET', 'POST'])
@login_required()
def game_create():
    form = GameCreateForm()
    if form.validate_on_submit():
        game = Game.create_game(game_name=form.game_name.data,
                                st_id=current_user.id, game_lore=form.game_lore.data)
        return redirect(url_for('main.game_info', game_id=game.id))
    return render_template('game_create.html', form=form)


@main.route('/game/<game_id>')
@login_required()
def game_info(game_id):
    game = Game.query.get(int(game_id))
    st_name = User.query.get(game.st_id).user_name
    return render_template('game_info.html', game=game, st_name=st_name)


@main.route('/game/<game_id>/edit', methods=['GET', 'POST'])
@login_required()
def game_edit(game_id):
    game = Game.query.get(game_id)
    form = GameCreateForm(obj=game)
    if form.validate_on_submit():
        game.name = form.game_name.data
        game.lore = form.game_lore.data
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('main.game_info', game_id=game_id))
    return render_template('game_edit.html', form=form)


@main.route('/game/<game_id>/edit', methods=['GET', 'POST'])
@login_required
def game_delete(game_id):
    game = Game.query.get(game_id)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        flash('Game has been deleted.')
        return redirect('main.game_list')
    return render_template('game_delete.html', game=game, game_id=game_id)


@main.route('/character/<char_id>', methods=['GET', 'POST'])
@login_required()
def character_info(char_id):
    character = Character.query.get(int(char_id))
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


@main.route('/character/create', methods=['GET', 'POST'])
@login_required()
def character_create():
    form = CreateCharacterForm()
    if form.validate_on_submit():
        character = Character.create_character(
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
        flash('Character created')
        return redirect(url_for('main.character_info', char_id=character.id))

    return render_template('character_create.html', form=form)


@main.route('/character/<char_id>/edit', methods=['GET', 'POST'])
@login_required()
def character_edit(char_id):
    character = Character.query.get(char_id)
    form = CreateCharacterForm(obj=character)
    if form.validate_on_submit():
        character.name = form.char_name.data
        character.owner = current_user.id
        character.lore = form.char_lore.data
        character.strength = form.char_strength.data
        character.reflex = form.char_reflex.data
        character.speed = form.char_speed.data
        character.awareness = form.char_awareness.data
        character.willpower = form.char_willpower.data
        character.imagination = form.char_imagination.data
        character.attunement = form.char_attunement.data
        character.faith = form.char_faith.data
        character.charisma = form.char_charisma.data
        character.luck = form.char_luck.data
        db.session.add(character)
        db.session.commit()
        flash('{} is edited.'.format(character.name))
        return redirect(url_for('main.character_info', char_id=char_id))
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
def action_info(act_id):
    action = Action.query.get(act_id)
    return render_template('action_info.html', action=action)


@main.route('/character/<char_id>/actioncreate', methods=['GET', 'POST'])
@login_required()
def action_create(char_id):
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
    if request.method == 'POST':
        db.session.delete(action)
        db.session.commit()
        flash('Action deleted')
        return redirect(url_for('main.character_info', char_id=action.char_id))
    return render_template('action_delete.html')
