from datetime import datetime

from termcolor import colored

from lib.list_entries import list_entries


def get_entry_titles(entries):
    return [entry["file_name"] for entry in entries if entry["file_name"] != "index"]


def generate_wikilinks(entries):
    return [f"- [[{entry}]] \n" for entry in entries]


def generate_index_file(target_dir, unique_dir_name, source_dir):
    try:
        print(colored("INFO Creating index file...", "light_blue"))
        index_file = f"{target_dir}/index.md"
        build_date = datetime.now()
        build_date = build_date.strftime("%a %d %b %Y %H:%M:%S")
        build_info = (
            f""" \n**Build ID:** {unique_dir_name}\n\n**Published:** {build_date}\n\n"""
        )

        all_notes = list_entries(f"{target_dir}")
        notes_count = len(all_notes)
        note_titles = sorted(get_entry_titles(all_notes))
        note_titles_formatted = generate_wikilinks(note_titles)

        recent_notes = list_entries(f"{source_dir}/zk")
        recents = sorted(recent_notes, key=lambda item: item["modified"], reverse=True)
        recents = recents[:12]
        recents = get_entry_titles(recents)
        recents_formatted = generate_wikilinks(recents)

        f = open(index_file, "a")
        f.write(build_info)
        f.write("### Recent edits \n\n")

        for recent in recents_formatted:
            f.write(recent)

        f.write("\n\n")
        f.write(f"### All notes ({notes_count}) \n\n")

        for note in note_titles_formatted:
            f.write(note)

        f.close()
        print(colored("SUCCESS Index file created", "light_green"))
    except Exception as e:
        print(
            colored(
                f"ERROR Error occurred when transferring files: {str(e)}", "light_red"
            )
        )
