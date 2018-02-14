class OutPuter(object):

    def show(self,authors):
	    for i in range(0,len(authors)):
		    print('rank ' + str(i+1) + ':' + authors[i]['name'] +'------'+authors[i]['num'])