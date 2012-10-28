# coding: utf-8
import random
from django.dispatch import receiver

from game.bills import signals as bills_signals
from game import signals as game_signals

from portal.newspaper.prototypes import NewspaperEventPrototype
from portal.newspaper import events


@receiver(bills_signals.bill_created, dispatch_uid="newspaper_bill_created")
def newspaper_bill_created(sender, bill, **kwargs):
    NewspaperEventPrototype.create(events.EventBillCreated(bill_id=bill.id, bill_type=bill.type, caption=bill.caption))


@receiver(bills_signals.bill_edited, dispatch_uid="newspaper_bill_edited")
def newspaper_bill_edited(sender, bill, **kwargs):
    NewspaperEventPrototype.create(events.EventBillEdited(bill_id=bill.id, bill_type=bill.type, caption=bill.caption))


@receiver(bills_signals.bill_processed, dispatch_uid="newspaper_bill_processed")
def newspaper_bill_processed(sender, bill, **kwargs):
    NewspaperEventPrototype.create(events.EventBillProcessed(bill_id=bill.id, bill_type=bill.type, caption=bill.caption, accepted=bill.state.is_accepted))


@receiver(game_signals.day_started, dispatch_uid='newspaper_day_started')
def newspaper_day_started(sender, **kwargs):
    from game.heroes.prototypes import HeroPrototype
    from game.heroes.models import Hero
    from game.angels.prototypes import AngelPrototype

    heroes_number = Hero.objects.filter(is_fast=False).count()

    if heroes_number < 1:
        return

    hero_model = Hero.objects.filter(is_fast=False)[random.randint(0, heroes_number-1)]

    hero = HeroPrototype(hero_model)
    angel = AngelPrototype.get_by_id(hero.angel_id)
    account = angel.get_account()

    NewspaperEventPrototype.create(events.EventHeroOfTheDay(hero_id=hero.id, hero_name=hero.name, race=hero.race,
                                                            gender=hero.gender, level=hero.level, power=hero.power,
                                                            account_id=angel.id, nick=account.nick, might=hero.might))
