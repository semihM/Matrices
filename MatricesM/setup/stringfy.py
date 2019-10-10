def _stringfy(mat,dtyps,retbounds,grid):
    import re
    nullname = mat.DEFAULT_NULL.__name__

    indbound = [0]
    d0,d1 = mat.dim
    decimals = mat.decimal
    m = mat.matrix
    feats = mat.features[:]

    pre = "0:.{}f".format(decimals)
    st = "{"+pre+"}"    
    string = ""

    #Dtypes check
    if dtyps == None:
        dtyps = mat.coldtypes[:]

    #Empty matrix check
    if mat.matrix in [ [], None ]:
        return "Empty matrix"

    ##########Tab sizes##########

    ##########
    #Dataframe
    ##########
    if mat._dfMat:
        bounds=[]
        indices = mat.index

        #Bounds for index columns
        indbound = [max([len(str(label)) for label in indices.get_level(i+1)]+[len(indices.names[i])]) for i in range(indices.level)]
        #Bounds from values
        for cols in range(d1):
            colbounds=[]

            if dtyps[cols] == float:
                for rows in range(d0):
                    try:
                        val = m[rows][cols]
                        colbounds.append(len(st.format(val)))
                    except:#Invalid value
                        colbounds.append(len(str(val)))

            elif dtyps[cols] == complex:
                for rows in range(d0):
                    try:
                        val = m[rows][cols]
                        if type(val).__name__ == nullname:
                            colbounds.append(len(nullname)) #Length of the null object
                        else:#Complex number
                            colbounds.append(len(st.format(val)))
                    except:#Invalid values
                        colbounds.append(len(str(val)))

            else:#Any non-complex and non-float column
                colbounds.append(max([len(str(a)) for a in mat.col(cols+1,0)]))

            colbounds.append(len(feats[cols]))
            bounds.append(max(colbounds))
    ##############        
    #Complex/Float
    ##############
    elif mat._cMat or mat._fMat:
        try:
            bounds=[]
            typ = [float,complex][mat._cMat]
            for cols in range(d1):
                comps = []
                for rows in range(d0):
                    val = m[rows][cols]
                    if type(val).__name__ == nullname:
                        comps.append(len(nullname)) 
                    else:
                        comps.append(len(st.format(typ(val))))
            
                bounds.append(max(comps))

        except Exception as err:
            msg = f"Invalid value for {['float','complex'][mat._cMat]} dtype matrix: '{val}'. "+", ".join(err.args)
            raise TypeError(msg)

    ########       
    #Integer
    ########
    else:
        try:
            bounds=[]
            for cols in range(d1):
                colbounds=[]
                for rows in range(d0):
                    val = m[rows][cols]
                    if type(val).__name__ == nullname:
                        colbounds.append(len(nullname))
                    else:
                        colbounds.append(len(str(int(val))))

                bounds.append(max(colbounds))
        except Exception as err:
            msg = f"Invalid value for int dtype matrix: '{val}'. "+", ".join(err.args)
            raise TypeError(msg)
    
    if retbounds:
        ind_bound = [indbound] if isinstance(indbound,int) else indbound
        _bounds = [bounds for _ in range(mat.d1)] if isinstance(bounds,int) else bounds
        return ind_bound+_bounds

    #-0.0 error interval set    
    if mat._fMat or mat._cMat:
        interval=[float("-0."+"0"*(decimals-1)+"1"),float("0."+"0"*(decimals-1)+"1")] 

    ##########Create the string#########

    ##########
    #Dataframe
    ##########
    if mat._dfMat:

        #Add features
        if not grid:
            string += "\n" + " "*(sum(indbound)+indices.level)
            for cols in range(d1-1):
                name = feats[cols]
                s = len(name)
                string += " "*(bounds[cols]-s)+name+"  "

            string += " "*(bounds[-1]-len(feats[-1]))+feats[-1]

            #Add index name row
            string += "\n" 
            lvl = indices.level - 1
            for i,name in enumerate(mat.index.names):
                if name == "":
                    string += " "*indbound[i]
                else:
                    string += " "*(indbound[i]-len(name)) + name
                
                if i != lvl:
                    string += ","

            string += "+" + "-"*(sum(bounds) + 2*(d1-1) )

        else:
            string += "\n"
                 
        #Add rows
        mm = mat.matrix
        labels = mat.index.labels
        for rows in range(d0):
            current_labels = labels[rows]
            #Add labels
            if not grid:
                string += "\n"

                for i,lbl in enumerate(current_labels):
                    lbl = str(lbl)
                    if lbl == "":
                        string += " "*indbound[i]
                    else:
                        string += " "*(indbound[i]-len(lbl)) + lbl
                    
                    if i != lvl:
                        string += ","

                string += "|"
            else:
                string += "\n"
                    
            #Add values
            for cols in range(d1):
                num = mm[rows][cols]
                #float column
                if dtyps[cols] == float:
                    try:
                        item = st.format(num)
                    except:
                        item = str(num)
                    finally:
                        s = len(item)
                #integer column
                elif dtyps[cols] == int:
                    if type(num).__name__ == nullname:
                        item = nullname
                        s = 4
                    else:    
                        try:
                            item = str(int(num))
                        except:
                            item = str(num)
                        finally:
                            s = len(item)
                #complex column
                elif dtyps[cols] == complex:
                    if type(num).__name__ == nullname:
                        item = nullname
                        s = 4
                    else:
                        try:
                            num = complex(num)
                            if num.imag == 0:
                                num = num.real
                            item = st.format(num)
                        except:
                            item = str(num)
                        finally:
                            s = len(item)
                #Any other type column
                else:
                    item = str(num)
                    s = len(item)

                endtab = 0 if cols+1 == d1 else 2
                string += " "*(bounds[cols]-s)+item+" "*endtab

    ##################
    #int/float/complex
    ##################
    else:
        for rows in range(d0):
            string+="\n"
            for cols in range(d1):
                num=mat._matrix[rows][cols]

                #complex
                if mat._cMat:
                    if type(num).__name__ == nullname:
                        item = nullname
                        s = 4
                    else:
                        item = st.format(num)
                        s=len(item)
                    string += " "*(bounds[cols]-s)+item+" "
                    continue

                #float
                elif mat._fMat:
                    if num>interval[0] and num<interval[1]:
                        num=0.0
                    item = st.format(num)
                    s = len(item)

                #integer
                else:
                    if type(num).__name__ == nullname:
                        item = nullname
                        s = 4
                    else:
                        item = str(int(num))
                        s = len(item)
                        
                endtab = 0 if cols+1 == d1 else 1
                string += " "*(bounds[cols]-s)+item+" "*endtab

    return string