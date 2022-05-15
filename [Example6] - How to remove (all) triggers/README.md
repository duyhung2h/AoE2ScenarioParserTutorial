# How to extend / shrink map to a certain direction (N|S|W|E|Center) 
Have you ever got any moment that your map was so laggy, or your map just downright crash when you test it, that you want to troubleshoot it? The problem could be hidden within your trigger! So for a map with thousands of triggers, specifically working with tools like Parser, could be hard to pinpoint your bug by deleting them. Unless...?
## Step by step (How it works)

Terrains / unit location / trigger areas, locations will be retained in their core location after extension / shrinkage.
(16x16) to (480x480) is the maximum dimension, anything above or below that value your map will crash when you test it (not in editor)

![image](https://user-images.githubusercontent.com/40296674/163688921-b8285470-c196-4e76-a920-129a27623e0f.png)


... You can extend to many different direction with 8 different options:

![image](https://user-images.githubusercontent.com/40296674/161836512-a656f533-d678-4de5-955f-e5732d49d1f2.png)
![image](https://user-images.githubusercontent.com/40296674/161836526-4ecdb2bf-a9e8-44c9-99b3-d745749bbc65.png)
![image](https://user-images.githubusercontent.com/40296674/161836560-77319e49-7b32-4540-a56c-8bb5ad98d3db.png)


## Important note: 
- Remove any unwanted unit that clip through the map borders, they can probably cause crash when you load your scenarios.
- Possible map size range is from (16x16) to (480x480). Any map size above or below that range will crash after you test it.
- Don't leave any player to have 0 unit in the map if the newly generated map is small - Scenario will crash if the map attempted to generate a `Town Center` for those said players, that could clips through map's borders.

![image](https://user-images.githubusercontent.com/40296674/163688623-971237f8-1f53-4812-84c8-6dff13a30806.png)
(16x16 map, the recommended minimum)

![image](https://user-images.githubusercontent.com/40296674/163692658-63989367-c5e5-4aeb-8c2d-173e8dbd0035.png)
(6x6 map, the ABSOLUTE MINIMUM, could be really unstable if you have any unit clipping through the map borders or AI would crash your game by their weird pathing)

