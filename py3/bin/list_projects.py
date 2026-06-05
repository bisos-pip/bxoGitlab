import gitlab

gl = gitlab.Gitlab.from_config('groupName', ['/home/bystar/.python-gitlab.cfg'])

group = gl.groups.get('groupName/subGroupName')
projects = group.projects.list(get_all=True)

for p in projects:
    print(p.id, p.path_with_namespace)
