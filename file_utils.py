def get_urls(leaders_list):
    return {
        f"{leader['first_name']} {leader['last_name']} ({leader.get('start_mandate', 'unknown')} - {leader.get('end_mandate', 'present')})": leader["wikipedia_url"]
        for leader in leaders_list
    }
