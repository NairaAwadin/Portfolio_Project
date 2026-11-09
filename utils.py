from data import PROJECTS

def all_tags(projects):
    tags = set()
    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)
    sorted_tags = sorted(tags)
    return sorted_tags

def filter_projects(projects, chosen):
    list_projets = []

    if not chosen:
        return projects

    for project in projects:
        for tag in project["tags"]:
            if tag in chosen:
                list_projets.append(project)
                break

    return list_projets

#print(len(filter_projects(PROJECTS, [])))                    # 5
#print(len(filter_projects(PROJECTS, ["C++"])))                    # 5

def get_year(project):
    return project["year"]
