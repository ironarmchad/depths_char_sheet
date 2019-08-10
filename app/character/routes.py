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
        game = Game.create_game(game_name=form.name.data,
                                st_id=current_user.id, game_lore=form.lore.data)
        return redirect(url_for('main.game_info', game_id=game.id))
    return render_template('game_create.html', form=form)


@main.route('/game/<game_id>')
@login_required()
def game_info(game_id):
    game = Game.query.get(int(game_id))
    st = User.query.get(game.st_id)
    npc_list = Character.query.filter_by(char_type='npc').filter_by(game_id=game.id).order_by(Character.name)
    player_list = Character.query.filter_by(char_type='player').filter_by(game_id=game.id).order_by(Character.name)
    return render_template('game_info.html', game=game, st=st, npc_list=npc_list, player_list=player_list)


@main.route('/game/<game_id>/edit', methods=['GET', 'POST'])
@login_required()
def game_edit(game_id):
    game = Game.query.get(game_id)
    form = GameCreateForm(obj=game)
    if form.validate_on_submit():
        game.name = form.name.data
        game.lore = form.lore.data
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
    form.game_id.choices = [(game.id, game.name) for game in Game.query.filter_by(active=True).order_by(Game.name)]
    form.game_id.data = Game.query.filter_by(name='No Game').first().id
    print(form.game_id.default)
    if form.validate_on_submit():
        character = Character.create_character(
            name=form.name.data,
            char_type=form.char_type.data,
            game_id=form.game_id.data,
            owner=current_user.id,
            lore=form.lore.data,
            strength=form.strength.data,
            reflex=form.reflex.data,
            vitality=form.vitality.data,
            speed=form.speed.data,
            awareness=form.awareness.data,
            willpower=form.willpower.data,
            imagination=form.imagination.data,
            attunement=form.attunement.data,
            faith=form.faith.data,
            charisma=form.charisma.data,
            luck=form.luck.data,
        )
        flash('Character created')
        return redirect(url_for('main.character_info', char_id=character.id))

    return render_template('character_create.html', form=form)


@main.route('/character/<char_id>/edit', methods=['GET', 'POST'])
@login_required()
def character_edit(char_id):
    character = Character.query.get(char_id)
    form = CreateCharacterForm(obj=character)
    form.game_id.choices = [(game.id, game.name) for game in Game.query.filter_by(active=True).order_by(Game.name)]

    if form.validate_on_submit():
        character.name = form.name.data
        character.char_type = form.char_type.data
        character.game_id = form.game_id.data
        character.lore = form.lore.data
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
        flash('{} is edited.'.format(character.name))
        return redirect(url_for('main.character_info', char_id=char_id))
    return render_template('character_create.html', form=form)


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
