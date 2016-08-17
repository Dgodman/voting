from __future__ import unicode_literals
import json
import base64

us_parties = (
    ('D', 'Democratic'),
    ('R', 'Republican'),
    ('L', 'Libertarian'),
    ('G', 'Green'),
    ('O', 'Other'),
)
us_states = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)
us_states_dict = {
    'AL': {
        'name_long': 'Alabama',
        'absentee_type': 'none'
    },
    'AK': {
        'name_long': 'Alaska',
        'absentee_type': 'early'
    },
    'AZ': {
        'name_long': 'Arizona',
        'absentee_type': 'early'
    },
    'AR': {
        'name_long': 'Arkansas',
        'absentee_type': 'early'
    },
    'CA': {
        'name_long': 'California',
        'absentee_type': 'early'
    },
    'CO': {
        'name_long': 'Colorado',
        'absentee_type': 'all'
    },
    'CT': {
        'name_long': 'Connecticut',
        'absentee_type': 'none'
    },
    'DC': {
        'name_long': 'District of Columbia',
        'absentee_type': 'early'
    },
    'DE': {
        'name_long': 'Delaware',
        'absentee_type': 'none'
    },
    'FL': {
        'name_long': 'Florida',
        'absentee_type': 'early'
    },
    'GA': {
        'name_long': 'Georgia',
        'absentee_type': 'early'
    },
    'HI': {
        'name_long': 'Hawaii',
        'absentee_type': 'early'
    },
    'ID': {
        'name_long': 'Idaho',
        'absentee_type': 'early'
    },
    'IL': {
        'name_long': 'Illinois',
        'absentee_type': 'early'
    },
    'IN': {
        'name_long': 'Indiana',
        'absentee_type': 'early'
    },
    'IA': {
        'name_long': 'Iowa',
        'absentee_type': 'early'
    },
    'KS': {
        'name_long': 'Kansas',
        'absentee_type': 'early'
    },
    'KY': {
        'name_long': 'Kentucky',
        'absentee_type': 'none'
    },
    'LA': {
        'name_long': 'Louisiana',
        'absentee_type': 'early'
    },
    'ME': {
        'name_long': 'Maine',
        'absentee_type': 'early'
    },
    'MD': {
        'name_long': 'Maryland',
        'absentee_type': 'early'
    },
    'MA': {
        'name_long': 'Massachusetts',
        'absentee_type': 'early'
    },
    'MI': {
        'name_long': 'Michigan',
        'absentee_type': 'none'
    },
    'MN': {
        'name_long': 'Minnesota',
        'absentee_type': 'early'
    },
    'MS': {
        'name_long': 'Mississippi',
        'absentee_type': 'none'
    },
    'MO': {
        'name_long': 'Missouri',
        'absentee_type': 'none'
    },
    'MT': {
        'name_long': 'Montana',
        'absentee_type': 'early'
    },
    'NE': {
        'name_long': 'Nebraska',
        'absentee_type': 'early'
    },
    'NV': {
        'name_long': 'Nevada',
        'absentee_type': 'early'
    },
    'NH': {
        'name_long': 'New Hampshire',
        'absentee_type': 'none'
    },
    'NJ': {
        'name_long': 'New Jersey',
        'absentee_type': 'early'
    },
    'NM': {
        'name_long': 'New Mexico',
        'absentee_type': 'early'
    },
    'NY': {
        'name_long': 'New York',
        'absentee_type': 'none'
    },
    'NC': {
        'name_long': 'North Carolina',
        'absentee_type': 'early'
    },
    'ND': {
        'name_long': 'North Dakota',
        'absentee_type': 'early'
    },
    'OH': {
        'name_long': 'Ohio',
        'absentee_type': 'early'
    },
    'OK': {
        'name_long': 'Oklahoma',
        'absentee_type': 'early'
    },
    'OR': {
        'name_long': 'Oregon',
        'absentee_type': 'all'
    },
    'PA': {
        'name_long': 'Pennsylvania',
        'absentee_type': 'none'
    },
    'RI': {
        'name_long': 'Rhode Island',
        'absentee_type': 'none'
    },
    'SC': {
        'name_long': 'South Carolina',
        'absentee_type': 'none'
    },
    'SD': {
        'name_long': 'South Dakota',
        'absentee_type': 'early'
    },
    'TN': {
        'name_long': 'Tennessee',
        'absentee_type': 'early'
    },
    'TX': {
        'name_long': 'Texas',
        'absentee_type': 'early'
    },
    'UT': {
        'name_long': 'Utah',
        'absentee_type': 'early'
    },
    'VT': {
        'name_long': 'Vermont',
        'absentee_type': 'early'
    },
    'VA': {
        'name_long': 'Virginia',
        'absentee_type': 'none'
    },
    'WA': {
        'name_long': 'Washington',
        'absentee_type': 'all'
    },
    'WV': {
        'name_long': 'West Virginia',
        'absentee_type': 'early'
    },
    'WI': {
        'name_long': 'Wisconsin',
        'absentee_type': 'early'
    },
    'WY': {
        'name_long': 'Wyoming',
        'absentee_type': 'early'
    },
}
us_states_short = ('AL','AK', 'AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN','IA',
                'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
                'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY',)
us_territories = (
    ('AS', 'American Samoa'),
    ('FM', 'Federated States of Micronesia'),
    ('GU', 'Guam'),
    ('MH', 'Marshall Islands'),
    ('MP', 'Northern Mariana Islands'),
    ('PW', 'Palau'),
    ('PR', 'Puerto Rico'),
    ('VI', 'Virgin Islands'),
)
ENCODE_KEY = 'd$#sbo61#fvq+z(c_6_-7&zf=yo51vwj*3+((a+-6@+d#vwm5_'


def get_absentee(state_id):
    if state_id in us_states_dict.keys():
        return us_states_dict[state_id]['absentee_type']
    else:
        return 'uknown'


def fillcolor(state_id):
    if state_id == "early":
        return "green"
    elif state_id == "none":
        return "red"
    elif state_id == "all":
        return "blue"
    else:
        return "gray"


def states_fill_json():
    state_fill = {}
    for state_id in us_states_dict:
        state_fill[state_id] = {'fill': fillcolor(get_absentee(state_id))}
    with open('state.fill.json', 'w') as outfile:
        json.dump(state_fill, outfile)


def encode(clear):
    key = ENCODE_KEY
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = unichr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf-8'))


def decode(enc):
    key = ENCODE_KEY
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    enc = enc.decode('utf-8')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = unichr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def encode_test(max_range):
    # fake last 4 digits of ssn
    for num in range(1, max_range):
        # convert to string
        ssn = str(num)
        # prepend zeros
        for num_zeros in range(4 - len(ssn)):
            ssn = "0" + ssn
        # encode
        encoded_ssn = encode(ssn)
        # decode
        decoded_ssn = decode(encoded_ssn)
        print "%s : %s : %s" % (ssn, encoded_ssn, decoded_ssn)
