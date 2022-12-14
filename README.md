# POP-FE 98DEMAKE

A theme for POP-FE (https://github.com/sahlberg/pop-fe).

Hand curated graphics to make your PS1 games look really nice in XMB. 

Currently covers around 70 PS1 games, intends to cover most popular titles. Updated actively.

![screenshot_2022_12_05_13_05_50](https://user-images.githubusercontent.com/118309446/205892216-36003652-1292-48ec-bb14-327ff672f26f.jpg)
![screenshot_2022_12_05_13_05_31](https://user-images.githubusercontent.com/118309446/205892262-553210e2-cbbc-4bce-8a04-12a958c4ba25.jpg)
![screenshot_2022_12_05_13_08_46](https://user-images.githubusercontent.com/118309446/205892339-cb18b989-73b8-4764-b471-eedb6068633a.jpg)
![screenshot_2022_12_05_13_57_29](https://user-images.githubusercontent.com/118309446/205892467-37cba54e-594b-4f3f-90d5-c3a4ecb32f5f.jpg)
![Untitled-1](https://user-images.githubusercontent.com/118309446/205892397-75c5d039-12e3-4eac-9238-4de8c6290c5e.jpg)

Tools
=====
tools/pw.py : A python script that will show what the game will look like
              on the XMB. When run it will open two windows, one for 4:3 and
	      one for 16:9 aspect ratios.
	      Example: cd data/SCUS94455
	               python ../../tools/pw.py
tools/list-games.py : A python script that translates all the disc-ids in
              'data' into the name of the corresponding game.
	      Example: cd data
	               python ../../tools/list-games.py


# Want to help?

File structure is data/SLUS01476

Folder needs to have 3 .PNG files. ICON0, PIC0, PIC1.

(preferably via pull request, or alternatively to 98demake@gmail.com with "PS1 PIX" title)

## ICON0 176x176.

PAL covers usually look the best. Personally I've also left the upper left Playstation logo and what ever developer logos there are, intact


![ICON0](https://user-images.githubusercontent.com/118309446/206944230-040b51d4-a599-48ec-b3fe-a70b7a45dad1.png)
![ICON0x](https://user-images.githubusercontent.com/118309446/206944371-0a133870-8dc2-4faa-ab1b-a246a0fbc372.png)
![ICON0](https://user-images.githubusercontent.com/118309446/206947047-5d56b3e7-c902-4664-a417-026637d2f5b1.png)
![ICON0](https://user-images.githubusercontent.com/118309446/206947132-844c2413-86c0-4418-a462-1629c0557b0d.png)
![ICON0](https://user-images.githubusercontent.com/118309446/206947211-0d88ee08-21f6-4991-8af7-0e4f32bd9fe7.png)


You can find covers either via google, or for example at: https://psxdatacenter.com/

## PIC0 is 1000x560.

In this theme, consists of a high resolution, transparent logo for the game. Again, try Google search https://www.google.com/advanced_image_search or for example https://www.mobygames.com/ or https://psxdatacenter.com/

Preferably with a slight drop shadow effect as demonstrated below
![PIC0x](https://user-images.githubusercontent.com/118309446/206944943-a9a9b89e-6390-42ae-b07f-093378c5a51d.png)

Final result should look somewhat like this:
![PIC0x2](https://user-images.githubusercontent.com/118309446/206945101-26a54872-8aa6-4870-a5d3-e282918bc033.png)

## PIC1 is 1920x1080.

Can be anything era appropriate to the game. Magazine ads, protomotional art etc. Try Google advanced image search (https://www.google.com/advanced_image_search) at *"larger than 4 MP"*. Since we live in an era of remakes and remasters, I recommend adding the year in the search, e.g *"tenchu 2 1998"*.

Another fine resource for PIC1 art is MobyGames. https://www.mobygames.com/game/playstation/tenchu-2-birth-of-the-stealth-assassins/promo.

PIC1 in this theme consists of three layers. 

- An overlay gradient at 75% opacity
- The actual art at 25% opacity
- And a black background

Like so:

![xx](https://user-images.githubusercontent.com/118309446/206946599-7186e9df-2797-4049-aa1c-642e3f7eea2d.PNG)

However, this is just how I do it and I'll accept good looking things regardless of whether they go by this template.

Below is the overlay I use for PIC1:
![bgtemplate1](https://user-images.githubusercontent.com/118309446/206946833-933fc34d-01a3-4d32-805f-3f0e3375c016.png)

All in all, the end result should look sleek, clean and "official".

![screenshot_2022_12_05_13_05_31](https://user-images.githubusercontent.com/118309446/206947658-da010eaf-f3be-436c-99e2-73fd53e94b9f.png)
![screenshot_2022_12_05_13_51_53](https://user-images.githubusercontent.com/118309446/206947680-f6f343fb-dd33-40f1-8d9b-2f7334c16a47.png)
![screenshot_2022_12_05_13_50_27](https://user-images.githubusercontent.com/118309446/206947686-c3bff2e6-91f0-408f-b5fe-e6e438c8ab0e.png)










