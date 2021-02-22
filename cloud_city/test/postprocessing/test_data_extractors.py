from cloud_city.postprocessing import extract_star_wars_set_num


def test_extract_set_num():
    examples = [
        ("Lego Star Wars 75050 B-Wing", 75050),
        ("Lego STAR WARS 40176 Scarif Stormtrooper", 40176),
        ("LEGO Star Wars 8085 Letoun Freeco", 8085),
        ("LEGO Star Wars 40288 BB-8", 40288),
        ("LEGO BrickHeadz 41619 Darth Vader", 41619),
        ("LEGO Star Wars 9490 Únik droidů", 9490),
        ("LEGO 30381 Imperial TIE Fighter polybag", 30381),
        ("LEGO Star Wars 40333 Bitva o planetu Hoth", 40333)
    ]

    for string, set_num in examples:
        assert extract_star_wars_set_num(string) == set_num
