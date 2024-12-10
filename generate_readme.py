"""
The script is to generate the BioEco resource list README.md

The resource list is mirroring the https://psl.noaa.gov/data/fisheries/
search tool which provide a quick way to view the entire list and provide 
a alternative platform for contributing the resource to be included in the 
search tool.

Package used:
- mdutils (creating the markdown file from python)

Conda env:
- cefilist (only mdutils is installed)

"""
import json
from mdutils.mdutils import MdUtils

def get_bioeco_list():
    """
    Read json data (soft link to the original source file)
    """

    json_file = open('data/bioeco_list.json', encoding="utf-8")

    return json.load(json_file)

if __name__ == '__main__':

    data = get_bioeco_list()

    # create markdown file
    mdFile = MdUtils(file_name='README')

    # start markdown structure
    mdFile.new_header(level=1, title='BioEco resource list')

    mdFile.new_paragraph(
        "This repo is a test for generating metadata JSON-LD files for BioEco EOVs within the "+
        mdFile.new_inline_link(
            link='https://bioecoocean.org/',
            text='BioEcoOcean'
            )+
        "project. It is still in development and because it was forked from the NOAA CEFI info hub repo " +
        "there may still be unrelated info in this repo. Big thank you to the contributors who " +
        "developed the original metadata generators this repo this is based on, their developments there are invaluable for this project! \n"
        )

    mdFile.new_header(level=2, title='How it (will) work')

    mdFile.new_line(
        'The idea is to submit a new GitHub issue with the "Contribute BioEco Metadata" issue template, '+
         "fill in the fields, submit, and then JSON-LD files as well as a sitemap will be generated for you in a folder named according to your programme's title. "+
         "The link to the sitemap file can then be used to link the metadata to ODIS through the "+
        mdFile.new_inline_link(
            link='https://catalogue.odis.org/',
            text='ODIS Catalgoue of Sources'
            )+
        '. Metadata entered in this template will focus more on project metadata rather than dataset specific metadata, which will be associated with datasets published to '+
          mdFile.new_inline_link(
            link='https://obis.org/',
            text='OBIS'
            )+
        '. \n')

    mdFile.new_header(level=3, title='Metadata required')
    
    mdFile.new_line('The following information should be included in any metadata file generated to ensure full interoperability and transparency. We encourage the use of controlled vocabulary as much as possible and incorporated places to provide such links in the template. \n'
                    '- Project details: title, description, links \n'+
                    '- License \n' +
                    '- Point of contact(s) \n' +
                    '- EOV(s) targeted \n' +
                    '- Methods used \n' +
                    '- Taxonomic scope \n' +
                    '- Temporal scope \n' +
                    '- ... \n')

    # include the list
    mdFile.new_header(level=2, title='List of EOV Programmes')

    for bioeco_list in data['lists']:
        mdFile.new_line(mdFile.new_inline_link(link=bioeco_list['url'], text=bioeco_list['title'])+' \n')
        mdFile.new_line('> '+bioeco_list['desc'] +'\n')

    # include the table of content at the top of the file
    mdFile.new_table_of_contents(table_title='Contents', depth=2)

    # finalize the markdown file and output
    mdFile.create_md_file()

    ###### adding link check badge
    # Read the existing content of readme.md
    with open('README.md', 'r', encoding='utf-8') as file:
        existing_content = file.read()

    # New line of text to add at the top
    badge = "![Resource Link Checked](https://github.com/BioEcoOcean/metadata-tracking-dev/actions/workflows/gha_check_link_daily.yml/badge.svg)\n"

    # Combine the new line and existing content
    updated_content = badge + existing_content

    # Write the updated content back to readme.md
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(updated_content)
