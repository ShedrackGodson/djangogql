import graphene
from graphene_django import DjangoObjectType

from accounts.models import User as UserModel
from decks.models import Deck as DeckModel
from cards.models import Card as CardModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Deck(DjangoObjectType):
    class Meta:
        model = DeckModel


class DeckMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.ID()
        title = graphene.String(required=True)
        description = graphene.String()

    deck = graphene.Field(Deck)

    @classmethod
    def mutate(cls, root, info, title, description, pk=None):
        if pk:
            deck = DeckModel.objects.get(id=pk)
            deck.title = title
            deck.description = description
            # deck.last_reviewed_at = timezone.now()
            # deck.updated_at = timezone.now()
            deck.save()

        else:
            DeckModel.objects.create(
                title=title, description=description
            )

        return DeckMutation(deck=deck)


class Card(DjangoObjectType):
    class Meta:
        model = CardModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    decks = graphene.List(Deck)
    cards = graphene.List(Card)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_decks(self, info):
        return DeckModel.objects.all()

    def resolve_cards(self, info):
        return CardModel.objects.all()


class Mutation(graphene.ObjectType):
    save_deck = DeckMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
