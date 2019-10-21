import json

data = {}
data ['people'] = []
data['people'].append({
    'name':'Lucas',
    'website':'santos@workers',
    'from':'Brasil',
    'degree': [
        {
            "college" : "Computer Engineer",
            "Year" : "2013",
            "Area" : "Web Optimization"
        },
        {
            "college" : "Software Engineer",
            "Year" : "2019",
            "Area" : "WCAG 2.0"
        } 
    ]
})


data['people'].append({
    'name':'Gabriel',
    'website':'santos@workers',
    'from':'Ireland'
})
def main():
    print('Executing JSON writting...')

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    with open('data.json') as json_file:
        room = json.load(json_file)
        for p in room['people']:
            print('Name: {}'.format(p['name']))
            print('Website: {}'.format(p['website']))
            print('From: {}'.format(p['from']))
            print('')
            
if __name__ == "__main__":
    main()