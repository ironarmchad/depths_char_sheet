from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user
from app import db
from app.game import game_pages
from app.game.forms import GameCreateForm
from app.game.models import Game
from app.auth.routes import login_required
from app.auth.models import User
from app.character.models import Character


@game_pages.route('/game')
@login_required()
def game_list():
    active_games = Game.query.filter_by(active=True)
    inactive_games = Game.query.filter_by(active=False)
    return render_template('game_list.html', active_games=active_games, inactive_games=inactive_games)


@game_pages.route('/game/create', methods=['GET', 'POST'])
@login_required()
def game_create():
    form = GameCreateForm()
    if form.validate_on_submit():
        game = Game.create_game(game_name=form.name.data,
                                st_id=current_user.id, game_lore=form.lore.data)
        return redirect(url_for('game.game_info', game_id=game.id))
    return render_template('game_create.html', form=form)


@game_pages.route('/game/<game_id>')
@login_required()
def game_info(game_id):
    game = Game.query.get(int(game_id))
    st = User.query.get(game.st_id)
    characters = Character.query.filter_by(game_id=game.id)
    return render_template('game_info.html', game=game, st=st, characters=characters)


@game_pages.route('/game/<game_id>/edit', methods=['GET', 'POST'])
@login_required()
def game_edit(game_id):
    game = Game.query.get(game_id)
    form = GameCreateForm(obj=game)
    if form.validate_on_submit():
        game.name = form.name.data
        game.lore = form.lore.data
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('game.game_info', game_id=game_id))
    return render_template('game_edit.html', form=form)


@game_pages.route('/game/<game_id>/edit', methods=['GET', 'POST'])
@login_required()
def game_delete(game_id):
    game = Game.query.get(game_id)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        flash('Game has been deleted.')
        return redirect('game.game_list')
    return render_template('game_delete.html', game=game, game_id=game_id)
