def tableData(filename, end_date):
    table_data = []
    with open (filename, 'r') as f:
        lines = f.readlines()
        lines.reverse()
        if end_date == "0":
            for line in lines:
                fields = line.strip().split(':')
                table_data.append(fields)
        else:
            for line in lines:
                fields = line.strip().split(':')
                if fields[5] == end_date:
                    table_data.append(fields)
    return table_data
