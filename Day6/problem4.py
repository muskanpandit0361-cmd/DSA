def sort(d, by='keys', order='asc'):
    reverse = (order == 'desc')
    if by == 'keys':
        return dict(sorted(d.items(), reverse=reverse))
    else:
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

data = {'C': 3, 'B': 2, 'A': 1}

print("Original:", data)
print("Sort by keys asc:", sort(data, 'keys', 'asc'))
print("Sort by keys desc:", sort(data, 'keys', 'desc'))
print("Sort by values asc:", sort(data, 'values', 'asc'))
print("Sort by values desc:", sort(data, 'values', 'desc'))



