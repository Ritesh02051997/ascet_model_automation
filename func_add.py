import itertools

def sort_md(df_ed) :
    """Sorting the Model Details part"""
    def pt1(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'x' :
                    df_md['Connection_No/ASL type'][eid] = 0
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 't1' :
                    df_md['Connection_No/ASL type'][eid] = 1
                else :
                    df_md['Connection_No/ASL type'][eid] = 2
    
    def bp(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'bitleiste' :
                    df_md['Connection_No/ASL type'][eid] = 0
                else :
                    df_md['Connection_No/ASL type'][eid] = 1

    def ct1d(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                df_md['Connection_No/ASL type'][eid] = 0
    
    def ct2d(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'x' :
                    df_md['Connection_No/ASL type'][eid] = 0
                else :
                    df_md['Connection_No/ASL type'][eid] = 1
    
    def rs(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'r' :
                    df_md['Connection_No/ASL type'][eid] = 0
                else :
                    df_md['Connection_No/ASL type'][eid] = 1

    def srvdeb_p(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'thighlow' :
                    df_md['Connection_No/ASL type'][eid] = 0
                else :
                    df_md['Connection_No/ASL type'][eid] = 1

    def bwao(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'in1' :
                    df_md['Connection_No/ASL type'][eid] = 0
                else :
                    df_md['Connection_No/ASL type'][eid] = 1

    def hys(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'x' :
                    df_md['Connection_No/ASL type'][eid] = 0
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 'lsp' :
                    df_md['Connection_No/ASL type'][eid] = 1
                else :
                    df_md['Connection_No/ASL type'][eid] = 2
    
    def tod(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'signal' :
                    df_md['Connection_No/ASL type'][eid] = 0
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 'delaytime' :
                    df_md['Connection_No/ASL type'][eid] = 1
                else :
                    df_md['Connection_No/ASL type'][eid] = 2

    def srvdeb(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'x' :
                    df_md['Connection_No/ASL type'][eid] = 0
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 'param' :
                    df_md['Connection_No/ASL type'][eid] = 1
                else :
                    df_md['Connection_No/ASL type'][eid] = 2

    def debrep(entity_id, df_md) :
        for eid in range(0,len(df_md)) :
            if df_md['Entity_2'][eid] == entity_id :
                if str(df_md['Connection_No/ASL type'][eid]).lower() == 'dfc_id' :
                    df_md['Connection_No/ASL type'][eid] = 0
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 'stresult' :
                    df_md['Connection_No/ASL type'][eid] = 1
                elif str(df_md['Connection_No/ASL type'][eid]).lower() == 'stattrib':
                    df_md['Connection_No/ASL type'][eid] = 2
                else :
                    df_md['Connection_No/ASL type'][eid] = 3

    global df_md
    for entity in range(0,len(df_ed['Entity_Name'])) :
        ct1d_type = ['chartable1d','dsm_Getdscpermission','dsm_resetdebounce','ParamUnused_UDISC','edgerising','edgefalling','Srv_Abs']
        bandor = ['bitwiseor','bitwiseand']
        if str(df_ed['Entity Class'][entity]).lower() == 'srv_pt1':
            pt1(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'getbit' :
            bp(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'hysteresis_lsp_rsp' :
            hys(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'srv_trnondly' :
            tod(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'chartable2d' :
            ct2d(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'dsm_debrepcheck' :
            debrep(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'rsflipflop' :
            rs(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'srv_debounce' :
            srvdeb(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() == 'srv_debounceparam_t' :
            srvdeb_p(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() in ct1d_type  :
            ct1d(df_ed['Entity_ID'][entity], df_md)
        elif str(df_ed['Entity Class'][entity]).lower() in bandor  :
            bwao(df_ed['Entity_ID'][entity], df_md)
 
    df_md['Connection_No/ASL type'] = pd.to_numeric(df_md['Connection_No/ASL type'])
    df_md = df_md.sort_values(by='Connection_No/ASL type')

def gen_comb(df_ed,df_ss):
    in_list = [n for n in df_ed[(df_ed['No.of inputs'] == 0) & (df_ed['No. of outputs'] != 0)]['Entity_Name']]
    cu_list = []
    ip_list = []
    raster = 10
    binaries = [0, 1]
    for inp in in_list:
        for i in range(0,len(df_ss)):
            if df_ss['Signal'][i] in inp:
                if(df_ss['Data Type'][i]== "bool"):
                    cu_list.append(binaries)
                else:
                    cu_list.append([df_ss['Min_Range'][i],(df_ss['Min_Range'][i]+df_ss['Max_Range'][i])/2,df_ss['Max_Range'][i]])
                ip_list.append(inp)
    remain = set(in_list).symmetric_difference(set(ip_list))
    combinations = list(itertools.product(*cu_list))
    df = pd.DataFrame(combinations, columns =ip_list)
    df.insert(0, "time", range(1,len(df)+1))
    df['time']=df['time']/raster
    for item in remain :
        df[item]=df['time'].iat[0]
    with pd.ExcelWriter("C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/Input.xlsx") as writer:
        df.to_excel(writer, sheet_name="input", index=False) 

def output(excel_file) :
    """For generating a .csv file which can be viewed in mda"""
    df = pd.read_excel(excel_file, sheet_name="input")
    df.to_csv('meas.tsv', sep="\t", index=False)  

output(excel_file_dir)
gen_comb(df_ed,df_ss)
sort_md(df_ed)