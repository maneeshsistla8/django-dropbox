import csv
import pandas as pd
from players.models import Player

result = Player.objects.values()
player_list = [entry for entry in result]
fields = [f.name for f in Player._meta.get_fields()]

df = pd.DataFrame.from_records(player_list)
df.to_csv('players.csv', sep='\t', encoding='utf-8', index=False, header = fields)
