# How to extend / shrink map to a certain direction (N|S|W|E|Center) 
This is a tutorial on how to extend / shrink map using an advacedly written script. Don't fret it, just run the program! Final result file will be named "ScenarioParser - ChangeMapSize Parser Result2.aoe2scenario"

I might compile this into a separate program - apart from the parser in the future. For now, enjoy!
## Step by step (How it works)

Terrains / unit location / trigger areas, locations will be retained in their core location after extension / shrinkage.

![image](https://user-images.githubusercontent.com/40296674/161837018-bb22140f-578e-40f3-8ce5-b984f36f824e.png)


... You can extend to many different direction with 8 different options:

![image](https://user-images.githubusercontent.com/40296674/161836512-a656f533-d678-4de5-955f-e5732d49d1f2.png)
![image](https://user-images.githubusercontent.com/40296674/161836526-4ecdb2bf-a9e8-44c9-99b3-d745749bbc65.png)
![image](https://user-images.githubusercontent.com/40296674/161836560-77319e49-7b32-4540-a56c-8bb5ad98d3db.png)


This is a 10x10 shrunken map.

![image](https://user-images.githubusercontent.com/40296674/161836277-0a59244a-ee3b-4099-87d3-7b57f7cf412f.png)

This is a 1x1 shrunken map. Have fun and go wild!

![image](https://user-images.githubusercontent.com/40296674/161836165-bfa56ac9-a93b-4909-9e79-1d66214fc418.png)

## Important note: 
- Remove any unwanted unit that clip through the map borders, they can probably cause crash when you load your scenarios.
- Possible map size range is from (16x16) to (480x480). Any map size above or below that range will crash after you test it.
