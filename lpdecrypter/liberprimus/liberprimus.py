from .lp_section_data import lp_start_end_data, lp_rr, lp_sections_by_red_runes

def get_section(section_index):
    """
        Returns the start and end data of the lp section
        indexed by section_index in runes
    """
    return lp_start_end_data[section_index]

def get_sections(section_indices):
    """
        Returns a batch of sections from a batch of indices
    """
    return [get_section(index) for index in section_indices]

def get_section_words(section_index):
    return lp_start_end_data[section_index]['all_words']

def get_section_start(section_index):
    return lp_start_end_data[section_index]['start_words']

def get_section_end(section_index):
    return lp_start_end_data[section_index]['end_words']

def get_section_red_runes(section_index):
    return lp_rr[section_index]

def get_sections_red_runes(section_indices):
    return [get_section_red_runes(index) for index in section_indices]
