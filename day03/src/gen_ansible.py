import yaml

with open('../materials/todo.yml', 'r') as file:
    todo = yaml.safe_load(file)
        
playbook = [
    {
        'name': 'Deploy project',
        'hosts': 'all',
        'become': True,
        'tasks': []
    }
]

install_packages_task = {
    'name': 'Install packages',
    'apt': {
        'name': '{{ item }}',
        'state': 'present',
        'update_cache': True
    },
    'loop': todo['server']['install_packages']
}
playbook[0]['tasks'].append(install_packages_task)

copy_files_task = {
    'name': 'Copy files',
    'copy': {
        'src': '{{ item }}',
        'dest': '/remote/path/{{ item  }}'
    },
    'loop': todo['server']['exploit_files']
}
playbook[0]['tasks'].append(copy_files_task)

run_file_consumer_task = {
    'name': 'Run consumer',
    'command': f"python3 {todo['server']['exploit_files'][1]} \
        {{ todo['server']['bad_guys'] | join(',') }}"
}
playbook[0]['tasks'].append(run_file_consumer_task)

run_file_exploit_task = {
    'name': 'Run exploit',
    'command': f"python3 {todo['server']['exploit_files'][0]}"
}
playbook[0]['tasks'].append(run_file_exploit_task)

with open('deploy.yml', 'w') as file:
    yaml.dump(playbook, file, default_flow_style=False)