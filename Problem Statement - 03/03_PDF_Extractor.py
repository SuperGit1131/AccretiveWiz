import io
import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            
            text = fake_file_handle.getvalue()
            yield text
    
            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    
    # json_exporter
    if sys.argv[2] == 'JSON':

        import json

        def export_as_json(pdf_path, json_path):

            filename = os.path.splitext(os.path.basename(pdf_path))[0]
            data = {'Filename': filename}
            data['Pages'] = []

            counter = 1
            for page in extract_text_by_page(pdf_path):
                text = page[0:]
                page = {'Page_{}'.format(counter): text}
                data['Pages'].append(page)
                counter += 1

            with open(json_path, 'w') as fh:
                json.dump(data, fh)

        # Driver code
        pdf_path = filename
        json_path = r'Exports\JSON_Export.json'
        export_as_json(pdf_path, json_path)

    # xml_exporter
    elif sys.argv[2] == 'XML':
        import xml.etree.ElementTree as xml
        from xml.dom import minidom

        def export_as_xml(pdf_path, xml_path):
            filename = os.path.splitext(os.path.basename(pdf_path))[0]
            root = xml.Element('{filename}'.format(filename=filename))
            pages = xml.Element('Pages')
            root.append(pages)

            counter = 1
            for page in extract_text_by_page(pdf_path):
                text = xml.SubElement(pages, 'Page_{}'.format(counter))
                text.text = page[0:3000]
                counter += 1

            xml_string = xml.tostring(root, 'utf-8')
            parsed_string = minidom.parseString(xml_string)
            pretty_string = parsed_string.toprettyxml(indent='  ')

            with open(xml_path, 'w') as fh:
                fh.write(pretty_string)

        # Driver code
        pdf_path = filename
        xml_path = r'Exports\XML_Export.xml'
        export_as_xml(pdf_path, xml_path)
    
    else:
        print('Please provide valid output export format - JSON or XML')
