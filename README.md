# Iwaenogu project

Goal: Keep track of nihonga pigments to avoid wasting money.

Demo on Heroku: https://iwaenogu.herokuapp.com/

#### What is Nihonga?
Nihonga 日本画 is a style of painting defined in 19th century Japan. After opening to the west in the Meiji era, Japan sought to differentiate between Western style paintings (Yoga) and Japanese style (Nihonga). Thus this style of is very recent, but looks back at the history of Japanese art.

#### Why are there so many damn colors?

Because of the nature of the pigments, which are traditionally made from ground minerals. The pigments are not mixed, rather layered. Each color comes in a variety of grain sizes, from the coarse 5-6 to fine 12 - 13 and Byaku. The grain size determines saturation, with finer sizes having a lower saturation.

#### Is it cheap?

No, why do you think I write software? To pay for art classes ;)

#### How can I learn more about Nihonga?

The best place to see Nihonga paintings is at the [Yamatane Museum](http://www.yamatane-museum.jp/english/) in Shibuya. You might also see some at the Metropolitan Museum of Art in NYC, or the Boston Museum of Fine Art.

If you'd like to try a lesson, check out my Sensei [Maria Tanikawa](https://www.mariatanikawa.com/nihonga-class/) for in-person or online lessons in English or Japanese. [PIGMENT Tokyo](https://pigment.tokyo/) also offers great classes on a variety of Japanese arts. English translation is available for an additional fee.

#### Where can I get supplies?

I recommend trying a class before investing in materials, but major suppliers include the following. (* for my favs)

Tokyo
- [Uematsu Art Supply](https://www.shibuyamiyamasu.jp/uematsu/main.html)* in Shibuya (Very friendly but no English)
- [Seikaido](https://www.sekaido.co.jp/) in Shinjuku, Tokyo
- [Pigment Tokyo](https://pigment.tokyo/)* in Shinagawa Seaside (English friendly)
- [Kinkaido](http://www2.gol.com/users/tokuouken/) in Ueno / Taito
- [Kiya](http://kiya.ehoh.net/) in Bunkyo-ku
- [Matsuyoshi Enoguten](http://www.matsuyoshienogu.co.jp/) in Chiyoda

Kanagawa
- [Sankichi](https://www.sankichi.com/) in Yokohama

Nagoya / Aichi
- [Morisou](https://www.nihongazaimorisou.com/)
- [Tanseido](http://www.tanseido.jp/category/70/)

Kyoto
- [Nakagawa Gofun](http://nakagawa-gofun.co.jp/index.html)
- [Kissho Nihonga](http://www.kissho-nihonga.co.jp/)
- [Saiun-do](https://goo.gl/maps/qHfG8TaKKakGaHrm6)
- [Ebisu Gazai](http://www.ebisuya-gazai.com/)

Osaka
- [Tanseido](http://www.tanseido.jp/category/70/)

Kummamoto
- [Bunrindo](https://www.bunrindou.com/)

Outside Japan
- [Kremer Pigment](https://shop.kremerpigments.com/en/pigments/iwa-enogu-mineral-pigments/) -- Supplies limited but pretty good for outside Japan. NYC, Germany
- [Handelshuset Nidaros](https://nidaros-handel.dk/iwa-enogu-pigmenter-169/) -- Denmark


### Sources & Inspiration

The following sources were very helpful when creating this project. ありがとうございます！！！

- [Nakagawa Gofun Website](http://nakagawa-gofun.co.jp) for understanding the various pigment types.
- [Pigment Tokyo](https://pigment.tokyo/) Another great source for information on pigment types and colors
- [Japanese Colors with Kanji](https://colors.japanesewithanime.com/japanese-colors/) is a brilliant and inspiring site. I really love how many variants of Mouse-gray it features.
- [W3Schools Web Color Picker](https://www.w3schools.com/colors/colors_picker.asp) This is a useful tool for picking web colors.
- [Maria Tanikawa](https://www.mariatanikawa.com/) My Nihonga Sensei who taught me everything and answers a lot of silly questions. 
- [Hamada, Nobuyoshi. 日本の日本の伝統色 - THE TRADITIONAL COLORS OF JAPAN. 株式会社パイ インターナショナル, 2011.](http://pie.co.jp/book/i/4100/) This book helped me match some colors, and gives an excellent understanding of Japanese color combinations.

## Code Info

And here we start the code parts...

### Requirements
- Python 3.7
- Django


### DB Setup

```
psql
CREATE DATABASE iwaenogu;
CREATE USER otto password 'letmeinnow';
GRANT ALL ON DATABASE iwaenogu TO otto;
```
