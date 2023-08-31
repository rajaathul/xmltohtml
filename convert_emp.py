from lxml import etree

def validate_xml(xml_file, xsd_file, xslt_file):
    try:
        xml_tree = etree.parse(xml_file)
        
        xslt_tree = etree.parse(xslt_file)

        schema_doc = etree.parse(xsd_file)
        
        schema = etree.XMLSchema(schema_doc)
        
        is_valid = schema.validate(xml_tree)
        
        if is_valid:
            print("XML document is valid.")
            transformer = etree.XSLT(xslt_tree)

            result_tree = transformer(xml_tree)

            output_filename = "Lab4/employee_data.html"
            with open(output_filename, "wb") as output_file:
                output_file.write(result_tree)

            print(f"XML to HTML transformation complete. HTML saved to {output_filename}")

        else:
            print("XML to HTML transformation failed. XML document is not valid.")
            print("Validation errors:")
            for error in schema.error_log:
                print(f"Line {error.line}, Column {error.column}: {error.message}")
                
    except etree.XMLSyntaxError as e:
        print("Error parsing XML document:", e)

    except:
        print("Error")

if __name__ == "_main_":
    xml_file = "Lab4/employee_data.xml"  
    xsd_file = "Lab4/employee_schema.xsd" 
    xslt_file = "Lab4/employee_transform.xslt" 
    
    validate_xml(xml_file, xsd_file, xslt_file)