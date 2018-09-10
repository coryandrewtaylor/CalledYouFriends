import click


TAG_LOOKUP = {
    '|bq|': '<blockquote>',
    '|/bq|': '</blockquote>'
}


@click.command()
@click.option('-i', '--input', 'input_file')
@click.option('-o', '--output', 'output_file')
def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as input_fileobj:
        doc = input_fileobj.read()

    for tag in TAG_LOOKUP:
        doc = doc.replace(tag, TAG_LOOKUP[tag])

    with open(output_file, 'w', encoding='utf-8', errors='ignore') as output_fileobj:
        output_fileobj.write(doc)
