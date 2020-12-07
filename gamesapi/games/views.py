"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from datetime import datetime

def list_names(objects):
	list = []
	for data in objects:
		list += [data['name']]
	return list

@api_view(['GET','POST'])
def game_list(request):
	if request.method == 'GET':
		games = Game.objects.all()
		games_serializer = GameSerializer(games, many=True)
		return Response(games_serializer.data)

	elif request.method == 'POST':
		games = Game.objects.all()
		gameList = list_names(GameSerializer(games, many=True).data)

		game_serializer = GameSerializer(data=request.data)
		if game_serializer.is_valid():
			name = request.data['name']
			if name in gameList:
				pass
			else:
				game_serializer.save()
				return Response(game_serializer.data, status=status.HTTP_201_CREATED)
		return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def game_detail(request, pk):
	try:
		game = Game.objects.get(pk=pk)
	except Game.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	
	if request.method == 'GET':
		game_serializer = GameSerializer(game)
		return Response(game_serializer.data)
	
	elif request.method == 'PUT':
		games = Game.objects.all()
		gameList = list_names(GameSerializer(games, many=True).data)
		
		game_serializer = GameSerializer(data = request.data)
		if game_serializer.is_valid():
			name = request.data['name']
			if name in gameList or request.data['played'] == True:
				pass
			else:
				game_serializer.save()
				return Response(game_serializer.data, status=status.HTTP_201_UPDATED)
		return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		current_date = datetime.now()
		game_date = datetime.strptime(request.data['release_date'], '%Y-%m-%dT%H:%M:%SZ')

		if current_date > game_date:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			game.delete()
			return Response(status=status.HTTP_201_DELETED)
		return Response(status=status.HTTP_204_NO_CONTENT)