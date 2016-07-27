$(document).ready(function() {
    // json data created from script
    var state_data = {
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
    // state fill color
    function state_color (absentee_type) {
        if (absentee_type == "early") {
            return "#99badd";   // light blue
        }
        else if (absentee_type == "none") {
            //return "#c9605e"    // light red
            return "#f5f5f5"
        }
        else if (absentee_type == "all") {
            return "#f5f5f5"    // light gray
        }
        else {
            return "#7F7F7F"
        }
    }
    // state hover color
    function state_hover_color(absentee_type) {
        if (absentee_type == "early") {
            return "#003366";   // dark blue
        }
        else if (absentee_type == "none") {
            return "#c9605e"    // light red
        }
        else if (absentee_type == "all") {
            return "#badd99"    // light green
        }
        else {
            return "#262626"
        }
    }
    // state long name
    function state_long(state_id){
        var state_name = state_data[state_id].name_long
        if (state_name == "" || state_name == null) {
            return "Uknown"
        }
        else {
            return state_name
        }
    }
    function get_absentee_type (state_id) {
        if (state_id in state_data) {
            return state_data[state_id].absentee_type
        }
        else {
            return ""
        }
    }
    function click_state(state_id) {
        var absentee_type = get_absentee_type(state_id)
        if (absentee_type == "early") {
            var url = '../register/' + state_id + '/'
            window.location.href = url;
            //$('#state_name').text(url);
            /*$('#state_name')
                .text(state_long(state_id))
                .stop()
                .css('backgroundColor', '#af0')
                .animate({backgroundColor: '#ddd'}, 1000);*/
        }
    }
    // state color list
    var state_fill = {}
    // state hover list
    var state_hover_fill = {}
    // fill lists
    $.each(state_data, function(state_id, v) {
        absentee_type = state_data[state_id].absentee_type
        state_fill[state_id] = {"fill": state_color(absentee_type)}
        state_hover_fill[state_id] = {"fill": state_hover_color(absentee_type)}
    });
    // start map
    $('#map').usmap({
        'showLabels': false,
        'stateStyles': {
            'stroke-width': 1.5,
            'stroke' : '#1e252c'
        },
        'stateSpecificHoverStyles': state_hover_fill,
        'stateSpecificStyles': state_fill,
        'click' : function(event, data) {
            click_state(data.name)
        },
        'mouseover' : function(event, data) {
            $('#state_name')
            .text(state_long(data.name))
        }
    });
});