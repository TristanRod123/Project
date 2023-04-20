
def getHistory(filename, employee_id):
    with open(filename, 'r') as f:
        lines = f.readlines()

    extracted_fields = []
    for line in lines:
        fields = line.strip().split(':')
        if fields[0] == employee_id:
            extracted_fields.append(fields[1]+ ':' + fields[2] + ':' + fields[6] + ':' + fields[5])

    return extracted_fields.reverse()


def displayHistory(filename, employee_id,):
    with open('outputHistory.html', 'w') as f:
        f.write('')

    extracted_fields = getHistory(filename, employee_id)

    html_table = '<table>\n'
    html_table += '<tr><th>Name</th><th>Pay</th><th>Date</th><tr>\n'

    for line in extracted_fields:
        data = line.split(':')
        html_table += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(data[0] + ' ' + data[1], data[2], data[3])
    html_table = '</table>\n'

    with open('outputHistory.html', 'w') as f:
        f.write(html_table)
    