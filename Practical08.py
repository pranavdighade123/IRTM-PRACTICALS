import xml.dom.minidom

def main():
    # Parse the XML file
    doc = xml.dom.minidom.parse("emp.xml")

    # Display the root node and the first child tag name
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # Get the list of expertise elements
    expertise_elements = doc.getElementsByTagName("expertise")

    # Display the number of expertise elements
    print("%d expertise:" % len(expertise_elements))

    # Display the names of each expertise
    for skill in expertise_elements:
        print(skill.getAttribute("name"))

    # Create a new expertise element and set its attribute
    new_expertise = doc.createElement("expertise")
    new_expertise.setAttribute("name", "BigData")

    # Append the new expertise element to the root
    doc.firstChild.appendChild(new_expertise)

    # Save the modified XML back to a file
    with open("modified_emp.xml", "w") as file:
        doc.writexml(file)

if __name__ == "__main__":
    main()
