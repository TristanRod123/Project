def getHistory(filename, employee_id):
    with open(filename, 'r') as f:
        lines = f.readlines()

    extracted_fields = []
    for line in lines:
        fields = line.strip().split(':')
        if fields[0] == employee_id:
            extracted_fields.append(fields[1]+ ':' + fields[2] + ':' + fields[6] + ':' + fields[5])

    extracted_fields.reverse()
    return extracted_fields


def displayHistory(filename, employee_id):
    with open('outputHistory.html', 'w') as f:
        f.truncate(0)

    extracted_fields = getHistory(filename, employee_id)

    html_table = '<div style="margin-top: 20px; float: right;">\n'  # add margin-top of 20px and float to right
    html_table += '<table>\n'
    html_table += '<tr><th>Name</th><th>Pay</th><th>Date</th><tr>\n'

    for line in extracted_fields:
        data = line.split(':')
        html_table += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(data[0] + ' ' + data[1], data[2], data[3])
    html_table += '</table>\n'
    html_table += '</div>\n'

    f.write(html_table)

def getAllHistory(filename, end_date):
    with open(filename, 'r') as f:
        lines = f.readlines()

    extracted_fields = []
    for line in lines:
        fields = line.strip().split(':')
        if fields[5] == end_date:
            extracted_fields.append(fields[0]+ ':' + fields[1] + ':' + fields[2] + ':' + fields[6])

    extracted_fields.reverse()
    return extracted_fields

def displayAllHistory(filename, end_date):
    with open('outputAllHistory.html', 'w') as f:
        f.truncate(0)

    extracted_fields = getAllHistory(filename, end_date)

    html_table = '<div style="margin-top: 10px; float: right;">\n'  # add margin-top of 10px and float to right
    html_table += '<table>\n'
    html_table += '<tr><th>ID</th><th>Name</th><th>Pay</th><tr>\n'

    for line in extracted_fields:
        data = line.split(':')
        html_table += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(data[0], data[1] + ' ' + data[2], data[6])
    html_table += '</table>\n'
    html_table += '</div>\n'

    f.write(html_table)