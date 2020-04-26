from django import forms

CHARACTER_CHOICES = [
    ('helmet', 'Helmet'),
    ('lone starr', 'Lone Starr'),
    ('barf', 'Barf'),
    ('vespa', 'Vespa'),
    ('dot', 'Dot'),
    ('skroob', 'Skroob'),
    ('rico', 'Rico'),
    ('dinks', 'Dink'),
    ('sandurz', 'Sandurz'),
    ('usher', 'Usher'),
    ('roland', 'Roland'),
    ('pizza', 'Pizza'),
    ('vinnie', 'Vinnie'),
    ('commanderette', 'Comanderette'),
    ('snotty', 'Snotty'),
    ('charlene', 'Charlene'),
    ('marlene', 'Marlene'),
    ('radar tech.', 'Radar Tech.'),
    ('corporal', 'Corporal'),
    ('yogurt', 'Yogurt'),
    ('pizza guy', 'Pizza Guy'),
    ('bearded lady', 'Bearded Lady'),
    ("ship's voice", "Ship's Voice"),
    ('waitress', 'Waitress'),
    ('alien', 'Alien'),
]

class SearchForm(forms.Form):
    line = forms.CharField(max_length=1024, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Quote to search...'}))
    character = forms.CharField(required=False, label='', widget=forms.Select(choices=CHARACTER_CHOICES))

