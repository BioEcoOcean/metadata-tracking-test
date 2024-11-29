"""
The script is to generate the YAML file 
which helps GitHub to generate a issue template 
for BioEco metadata contribution.
"""
import yaml
import generate_readme

# read source json file (data type definition)
bioeco_data = generate_readme.get_bioeco_list()

# read the title part of the issue template
ISSUE_TEMP = ".github/ISSUE_TEMPLATE/header_file/add_bioeco_metadata_head.yml"
with open(ISSUE_TEMP,'r',encoding='utf8') as f:
    issue_temp_head = yaml.load(f,Loader=yaml.loader.SafeLoader)

# solve the unique name issue in ISSUE_TEMPLATE
issue_temp_head['name'] = 'Contribute BioEco metadata'

# loop over all categories (variable is skipped at the moment)
for cat in bioeco_data['categories_definition'].keys():
    options = [
        f"{key}-{value['name']}" 
        for key, value in bioeco_data['categories_definition'][cat]['options'].items()
    ]

    issue_temp_head['body'].append({
        'type': 'dropdown',
        'id': cat,
        'attributes': {
            'label': bioeco_data['categories_definition'][cat]['name'],
            'description': bioeco_data['categories_definition'][cat].get('description', ''),
            'multiple': True,
            'options': options  # Use the extracted options directly
        },
        'validations': {
            'required': False
        }
    })

# output yml file
OUT_FNAME = '.github/ISSUE_TEMPLATE/add_bioeco_metadata.yml'
with open(OUT_FNAME, 'w',encoding='utf8') as f:
    data = yaml.dump(issue_temp_head, f, sort_keys=False, default_flow_style=False)
