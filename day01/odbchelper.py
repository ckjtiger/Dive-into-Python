def buildConnectionString(params):
       """ Build a connection string from a dictionary of parameters.
       
       Returns string. """
       return ";".join(["%s=%s"%(k,v) for k,v in params.items()])

if __name__=="__main__":
        myParams = {"serve":"mpilgrim",\
                    "database":"master",\
                    "uid":"sa",\
                    "pwd":"secret"\
                   }
        #print "Hello world"
        print buildConnectionString(myParams)
