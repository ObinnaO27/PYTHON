import os
import argparse
from xml.etree import ElementTree as ELT
from zwift_crc32_signature import calculate_crc32_signature
from zwift_uuid import get_uuid_string

k_unique_id_elem = "uniqueId"
k_legacy_id_hash_elem = "legacyIdHash"
k_baseWorkoutsPath = 'data/Workouts/'

# dictionary with pairs of tokens that need to be replaced before XML parsing
# and re-replaced before the XML structure is saved again
# this is needed because certain entities like &apos; are automatically converted
# when parsing and writing the XML with ElementTree
k_pre_process_tokens = {
    '&apos;': '$$APOS$$',
    '&quot;': '$$QUOT$$',
    '&#8216;': '$$LQUOT$$',
    '&#8217;': '$$RQUOT$$',
    '&#8221;': '$$RDQUOT$$',
    '&#8220;': '$$LDQUOT$$'
}

# indexes used to validate any possible id collisions
global_id_index = {
    k_unique_id_elem: dict(),
    k_legacy_id_hash_elem: dict()
}


def preprocess_xml(xml_file):
    with open(xml_file, 'r') as file:
        xml_data = file.read()

    # Replace special character entities with custom tokens
    for k, v in k_pre_process_tokens.items():
        xml_data = xml_data.replace(k, v)

    # Return the preprocessed XML in string format
    return xml_data


def postprocess_xml(tree):
    # Get the serialized XML string
    xml_data = ELT.tostring(tree.getroot(), encoding='unicode')

    # Replace custom tokens with the original character entities
    for k, v in k_pre_process_tokens.items():
        xml_data = xml_data.replace(v, k)

    # return the modified XML string
    return xml_data


def parse_workout_xml_file(file_path):
    """
    Parses a specific Workout XML file and returns the XML tree structure
    :param file_path:
    :return: an ElementTree instance or None if an error occurs while parsing
    """
    try:
        # Create an ElementTree object from the preprocessed XML
        return ELT.ElementTree(ELT.fromstring(preprocess_xml(file_path)))
    except Exception as ex:
        print("Error parsing %s: %s" % (file_path, str(ex)))
        return None


def handle_workout_file_save(file_path, xml_tree):
    """
    Handles the writing of the XML workout file into the defined path
    :param file_path:
    :param xml_tree: ElementTree object with the structure to write
    :return:
    """
    try:
        if xml_tree:
            # This line makes sure the new inserted elements are correctly formatted/indented
            # however, this will also affect the formatting of rest of the entire file, causing a larger git diff
            ELT.indent(xml_tree, '    ')

            xml_data = postprocess_xml(xml_tree)

            with open(file_path, 'w') as file:
                file.write(xml_data)

            return True
    except Exception as ex:
        print("Error writing to %s: %s" % (file_path, str(ex)))

    return False


def insert_element_in_workout_root(wk_root_element, element_name, element_value, element_index):
    """
    Checks if the Workout XML file root element already contains a certain element tag
    If not, inserts a new one
    :param wk_root_element:
    :param element_name:
    :param element_value:
    :param element_index:
    :return:
    """
    if wk_root_element.find(element_name) is not None:
        return False

    new_uid_element = ELT.Element(element_name)
    new_uid_element.text = element_value
    wk_root_element.insert(element_index, new_uid_element)

    return True


def generate_workout_id(file_path, only_search=False):
    # parse the XML first
    xml_tree = parse_workout_xml_file(file_path)

    if xml_tree is None:
        return False  # invalid XML file

    root_element = xml_tree.getroot()

    # Checks if it's a Zwift Workout file
    if not root_element or root_element.tag != 'workout_file':
        return False

    xml_struct_changed = False

    # generates a unique ID and inserts it in the XML structure if it doesn't exist already
    unique_id = get_uuid_string()
    if insert_element_in_workout_root(root_element, k_unique_id_elem, unique_id, 0):
        xml_struct_changed = True
    else:
        unique_id = root_element.find(k_unique_id_elem).text

    if unique_id in global_id_index[k_unique_id_elem]:
        # id already exists, we can't continue with updating the file if it's a new insertion. Show warning and exit
        print("##### WARNING #####\nUnique Id %s already exists for file %s. Clashing with workout %s. "
              "Aborting file update." % (unique_id, global_id_index[k_unique_id_elem][unique_id], file_path))
        if xml_struct_changed:
            return False
    else:
        # saves the current unique Id in the global index to check for possible collisions
        global_id_index[k_unique_id_elem][unique_id] = file_path

    # generates the legacy id hash if it doesn't exist in the file
    legacy_hash_seed = file_path.replace('../', k_baseWorkoutsPath)  # if using the default workouts path, we need to
                                                                     # replace it with the base path for the generated
                                                                     # hash to be equal to the Game
    legacy_hash_id = calculate_crc32_signature(legacy_hash_seed)  # 32 bit integer

    legacy_id = str(legacy_hash_id)
    if insert_element_in_workout_root(root_element, k_legacy_id_hash_elem, str(legacy_hash_id), 1):
        xml_struct_changed = True
    else:
        legacy_id = root_element.find(k_legacy_id_hash_elem).text

    if legacy_id in global_id_index[k_legacy_id_hash_elem]:
        # id already exists, we can't continue with updating the file. Show warning and exit if it's a new insertion
        print("##### WARNING #####\nLegacy Id %s already exists for file %s. Clashing with workout %s. "
              "Aborting file update." % (legacy_id, global_id_index[k_legacy_id_hash_elem][legacy_id], file_path))
        if xml_struct_changed:
            return False
    else:
        # saves the current legacy id in the global index to check for possible collisions
        global_id_index[k_legacy_id_hash_elem][legacy_id] = file_path

    if xml_struct_changed:
        # if the flag to only search is passed, just prints a message and don't change the file
        if only_search is True:
            print(f"Workout {file_path} is missing a Unique Id.")
            return False

        handle_workout_file_save(file_path, xml_tree)
        print(f"Generated unique Id for {file_path}")

        return True
    else:
        return False


def check_workout_files_for_unique_id(target_path, only_search_missing=False):
    if os.path.isdir(target_path):
        for root, dirs, files in os.walk(target_path):
            for file_name in files:
                    if file_name.endswith(".xml"):
                        file_path = os.path.join(root, file_name)

                        generate_workout_id(file_path, only_search_missing)

    elif os.path.isfile(target_path):
        generate_workout_id(target_path, only_search_missing)
    else:
        print("Invalid path.")


def main():
    parser = argparse.ArgumentParser(description="Generates unique IDs for Zwift Workout files if a unique ID is "
                                                 "not present. It also generate the legacy Id hash")
    parser.add_argument("-f", "--file", help="Relative path to a specific Workout file")
    parser.add_argument("-s", "--search", help="Search files with missing IDs only. Does not generate any new ID.",
                        action='store_true')

    args = parser.parse_args()

    if args.file is not None and os.path.isdir(args.file):
        check_workout_files_for_unique_id(args.file)
    else:
        only_search_missing_ids = False
        if args.search:
            only_search_missing_ids = True
        # if neither options are used, defaults to the current location if no path specified
        check_workout_files_for_unique_id("../", only_search_missing_ids)


if __name__ == "__main__":
    main()
