import datetime

#Create a class of member storing information from each member including name date of birth and ip address (will be using local ip for testing).
memberDict = {'John': [str(datetime.date(1989, 10, 20).strftime('%d/%m')), b"192.168.0.1"],
            'Terry': [str(datetime.date(2000, 4, 25).strftime('%d/%m')), b"192.168.247.1"],
            'Andrew': [str(datetime.date(2001, 8, 3).strftime('%d/%m')), b"192.168.0.3"],
            'Adrian': [str(datetime.date(2001, 2, 3).strftime('%d/%m')), b"192.168.0.4"]
}
