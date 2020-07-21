# Iwaenogu project

Goal: Keep track of nihonga pigments to avoid wasting money.

What is Nihonga?
Nihonga 日本画 is a style of painting created in 20th century Japan. After opening to the west in the Meiji era, Japan sought to differentiate between Western style paintings (Yoga) and Japanese style (Nihonga). Thus this style of is very recent, but looks back at the history of Japanese art.

Why are there so many damn colors?

Because of the nature of the pigments, which are traditionally made from ground minerals. The pigments are not mixed, rather layered. Each color comes in a variety of grain sizes, from the coarse 5-6 to fine 12 - 13 and Byaku. The grain size determines saturation, with finer sizes having a lower saturation.

Is it cheap?

No, why do you think I write software? To pay for art classes ;)

How can I learn more about Nihonga?

The best place to see Nihonga paintings is at the Yamatane Museum in Shibuya.

If you'd like to try a lesson, check out my Sensei Maria Tanikawa. PIGMENT Tokyo also offers great classes on a variety of Japanese arts.

Where can I get supplies?

I recommend trying a class before investing in materials, but my favorite places are:

- Uematsu Art Supply in Shibuya (No English)
- Seikaido in Shinjuku
- Pigment Tokyo in Shinagawa Seaside
- Kremer Pigment -- Supplies limited but pretty good for outside Japan. NYC, Germany


And here we start the code parts...

#DB Setup

```
psql
CREATE DATABASE iwaenogu;
CREATE USER otto password 'letmeinnow';
GRANT ALL ON DATABASE iwaenogu TO otto;
```
