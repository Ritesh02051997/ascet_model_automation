#Modules used
import pandas as pd
import networkx as nx
import warnings
# from sklearn.linear_model import LogisticRegression
import re
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import itertools

# Link of config files :
if True :
    elementdetails_loc = "C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/ProblemStatementandArtifacts/Day1/PFlt_DdRgnInhbDrvr_1.0.0/PFlt_DdRgnInhbDrvr_1.0.0_ElementDetails.csv"
    signalsheet_loc = "C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/ProblemStatementandArtifacts/Day1/PFlt_DdRgnInhbDrvr_1.0.0/PFlt_DdRgnInhbDrvr_1.0.0_FILTER_0_SignalSheet.csv"
    modeldetails_loc = "C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/ProblemStatementandArtifacts/Day1/PFlt_DdRgnInhbDrvr_1.0.0/PFlt_DdRgnInhbDrvr_1.0.0_ModelDetails.csv"
    training_data = "C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Training_data.xlsx"
    df_ed =  pd.read_csv(elementdetails_loc)
    df_ss = pd.read_csv(signalsheet_loc)
    df_md = pd.read_csv(modeldetails_loc)
    df_tr = pd.read_excel(training_data, sheet_name='Training')

#Functions
def button_click():
    """5 problems click one button"""
    
    # network_bc(df_md, df_ed)
    outputs =[n for n in df_ed[(df_ed['No.of inputs'] != 0) & (df_ed['No. of outputs'] == 0)]['Entity_Name']]
    inputs = [n for n in df_ed[(df_ed['No.of inputs'] == 0) & (df_ed['No. of outputs'] != 0)]['Entity_Name']]

    # while (len(df_ed['Entity_Name']) == (len(inputs) + len(outputs))) :
    for i in range(0,len(df_ed['Entity_Name'])) :
        if df_ed['Entity_Name'][i] not in (inputs + outputs) :
            if ('greater' or 'equal') in str(df_ed['Entity_Name'][i]).lower() :
                print
            
    print(outputs)
    print(inputs)

    # print(df_fin_out)


def network_bc(df_md, df_ed) :
    """This block makes the ASCET model visualization"""
    G = nx.DiGraph()
    for i in range(0,len(df_md['Entity_1'])) :
        for k in range(0,len(df_ed['Entity_ID'])) :
            if df_ed['Entity_ID'][k] == df_md['Entity_1'][i] :
                from_para = df_ed['Entity_Name'][k]
            if df_ed['Entity_ID'][k] == df_md['Entity_2'][i] :
                to_para = df_ed['Entity_Name'][k]
        G.add_edge(from_para,to_para)
    nx.draw(G, with_labels=True)
    plt.show()

def input_excel(df_ed) :
    """This function is for generating the input excel sheet"""
    outputs =[n for n in df_ed[(df_ed['No.of inputs'] != 0) & (df_ed['No. of outputs'] == 0)]['Entity_Name']]
    inputs = [n for n in df_ed[(df_ed['No.of inputs'] == 0) & (df_ed['No. of outputs'] != 0)]['Entity_Name']]
    df_input = pd.DataFrame()
    df_cal = pd.DataFrame()
    df_input['time']= ''
    
    for element in (inputs+outputs) :
        df_input[element] = ''
    for element in df_ed['Entity_Name'] :
        if 'cur' in str(element).lower() :
            df_cal[element] = ''
    with pd.ExcelWriter("C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/Input.xlsx") as writer:
        df_input.to_excel(writer, sheet_name="input", index=False)  
        df_cal.to_excel(writer, sheet_name="cal", index=False)  

def output(excel_file, raster) :
    """For generating a .csv file which can be viewed in mda"""
    df = pd.read_excel(excel_file, sheet_name="input")
    df.to_csv('meas.tsv', sep="\t", index=False)

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

def gen_inp(excel, graph) :
    df_input = pd.read_excel(excel)
    inputs = [n for n in df_ed[(df_ed['No.of inputs'] == 0) & (df_ed['No. of outputs'] != 0)]['Entity_Name']]
    for inp in inputs :
        graph.add_edge(inp, tuple(list(df_input[inp])))

def gen_comb(df_ed,df_ss):
    in_list = [n for n in df_ed[(df_ed['No.of inputs'] == 0) & (df_ed['No. of outputs'] != 0)]['Entity_Name']]
    print(len(in_list))
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
    print(remain)
    combinations = list(itertools.product(*cu_list))
    df = pd.DataFrame(combinations, columns =ip_list)
    df.insert(0, "time", range(1,len(df)+1))
    df['time']=df['time']/raster
    for item in remain :
        df[item]=df['time'].iat[0]
    df.head(10)
    # with pd.ExcelWriter("C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/Input.xlsx") as writer:
    #     df.to_excel(writer, sheet_name="input", index=False) 
    
# gen_comb(df_ed,df_ss)

def sort_inp(node,list, df_md, df_ed) :
    new_list = []
    for i in range(0,len(df_ed)) :
        if node == df_ed['Entity_Name'][i] :
            for item in df_md[df_md['Entity_2']==df_ed['Entity_ID'][i]]['Entity_1'] :
                for k in range(0,len(df_ed)) :
                    if df_ed['Entity_ID'][k] == item :
                        new_list.append(df_ed['Entity_Name'][k])
    return new_list
    
# sort_md(df_ed)
# print(sort_inp('PFlt_DdRgnInhbDrvr_PT1_9_0', ['MUX_0_0', 'dT_107_0', 'PFlt_Time_Parameter_C_117_0'], df_md, df_ed))
# temp = network_bc(df_md, df_ed)
# gen_inp("C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/Input.xlsx",temp)

# nx.draw(temp, with_labels=True)
# plt.show()

# sort_md(df_ed)
# input_excel(df_ed)
# button_click()
# output('C:/Users/IIH3KOR/Documents/Python Automation/Fit_Fest_23/Final/Input.xlsx')

network_bc(df_md, df_ed)