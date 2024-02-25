favorite_places = {
    'Edgar': {
        'first': 'Edgar',
        'last': 'Hawkings',
        'places': ['USA', 'Canada']
    },
    'Eduardo': {
        'first': 'Eduardo',
        'last': 'Brandao',
        'places': ['India, Japan']
    },
    'Arli': {
        'first': 'Arli',
        'last': 'Sobrinho',
        'places': ['France', 'Italy', 'Spain']
    }
}

for person, info in favorite_places.items():
    print(f"\nUsername: {person}")
    full_name = f"{info['first']} {info['last']}"
    print(f"\tFull name: {full_name.title()}")
    print("\tFavorite places:")
    for place in info['places']:
        print(f"\t- {place}")