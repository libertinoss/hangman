"""Hangman Words

This module contains:
    * animal_list - a list of 50 animals
    * vegetable_list - a list of 50 vegetables 
    * mineral_list - a list of 50 minerals
    * extreme_list - a list of specially selected words that are extremely tricky to guess in hangman
    * hangman_words_dict - a dictionary containing each of these lists, with their equivalent user selection key
"""

animal_list = ("Dog, Cat, Elephant, Lion, Tiger, Giraffe, Zebra, Kangaroo, Koala, Panda, Bear, Cheetah, Leopard, Gorilla, Chimpanzee, Hippopotamus, Rhinoceros, Crocodile, Alligator, Dolphin, Whale, Shark, Octopus, Penguin, Ostrich, Peacock, Eagle, Hawk, Owl, Toucan, Parrot, Snake, Lizard, Turtle, Frog, Salamander, Newt, Jellyfish, Starfish, Lobster, Crab, Shrimp, Scorpion, Spider, Bee, Ant, Butterfly, Hummingbird, Flamingo").split(", ")
vegetable_list = ("Carrot, Potato, Tomato, Cucumber, Broccoli, Spinach, Lettuce, Kale, Celery, Onion, Garlic, Zucchini, Radish, Peas, Corn, Asparagus, Beets, Cabbage, Okra, Pumpkin, Squash, Turnip, Beetroot, Mushroom, Leek, Sorrel, Thyme, Oregano, Rosemary, Sage, Basil, Eggplant, Shallot, Rutabaga, Arugula, Fennel, Mustard, Kohlrabi, Taro, Endive, Radicchio, Dandelion, Jicama, Bamboo, Watercress, Spinach, Bokchoy, Gherkin, Yam, Horseradish").split(", ")
mineral_list = ("Quartz, Feldspar, Mica, Calcite, Gypsum, Talc, Topaz, Fluorite, Apatite, Orthoclase, Biotite, Halite, Magnetite, Hematite, Sphalerite, Galena, Pyrite, Chalcopyrite, Malachite, Azurite, Dolomite, Graphite, Kaolinite, Calcite, Lepidolite, Magnetite, Gypsum, Barite, Olivine, Selenite, Bauxite, Amber, Celestite, Peridot, Aventurine, Zircon, Sodalite, Amazonite, Serpentine, Agate, Apatite, Larimar, Chrysocolla, Stibnite, Rhodonite, Galena, Gneiss, Obsidian, Rhodochrosite, Pyrolusite, Stilbite, Scheelite").split(", ")
extreme_list = ("Paradox, Labyrinth, Cryptocurrency, Extraterrestrial, Juxtaposition, Schizophrenia, Quicksilver, Hypochondriac, Gobbledygook, Bureaucracy, Pseudopseudohypoparathyroidism, Sesquipedalian, Zephyr, Floccinaucinihilipilification, Antidisestablishmentarianism, Supercalifragilisticexpialidocious, Philoprogenitive, Ineffable, Oxymoron, Discombobulate, Phosphorescent, Quizzaciously, Ziggurat, Flummox, Abecedarian, Cacophony, Anomalistic, Facetious, Hemidemisemiquaver, Epistemology, Conundrum, Perpendicular, Irrevocable, Tchotchke, Paraprosdokian, Penultimate, Xerophthalmia, Syzygy, Ecclesiastical, Higgledypiggledy, Perseverance, Mnemonic, Pneumonoultramicroscopicsilicovolcanoconiosis, Bombastic, Indefatigable, Disestablishmentarianism, Surreptitious, Xylanthrax, Sycophant, Pulchritudinous").split(", ")
hangman_words_dict = {'a' : [item.lower() for item in animal_list],
                      'v' : [item.lower() for item in vegetable_list],
                      'm' : [item.lower() for item in mineral_list],
                      'x' : [item.lower() for item in extreme_list]
                        }       


