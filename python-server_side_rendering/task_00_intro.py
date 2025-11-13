#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template is not a string.")
        return
    if not isinstance(attendees, list):
        print("Error: attendees is not a list of dictionaries.")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: an attendee item is not a dictionary.")
            return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        value = attendee.get("name")
        if value is None:
            value = "N/A"
        content = content.replace("{name}", value)

        value = attendee.get("event_title")
        if value is None:
            value = "N/A"
        content = content.replace("{event_title}", value)

        value = attendee.get("event_date")
        if value is None:
            value = "N/A"
        content = content.replace("{event_date}", value)

        value = attendee.get("event_location")
        if value is None:
            value = "N/A"
        content = content.replace("{event_location}", value)

        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w") as file:
                file.write(content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
