import xmlschema

xml_file = "employee.xml"
xsd_file = "employee_schema.xsd"

validator = xmlschema.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid against the XSD schema.")
else:
    print("XML file is not valid against the XSD schema.")
    validation_errors = validator.validate(xml_file)
    for error in validation_errors:
        print("Validation Error:")
        print(" Message:", error)
        print("  ErrorLine:", error.line)
        print("  ErrorColumn:", error.column)
    
