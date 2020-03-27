join_keys = [
    # [Left table, Right Table, Left on, Right on]
    ['TAB_Raw_Data','TAB_Sequencing','Sequencing_Raw_Data','Id_Sequencing'],
    ['TAB_Sequencing','TAB_Sequencing_Setup','Setup_Sequencing','Id_Sequencing_Setup'],
    ['TAB_Sequencing','TAB_Capture','Capture_Sequencing', 'Id_Capture'],
    ['TAB_Capture','TAB_Library','Library_Capture', 'Id_Library'],
    ['TAB_Library','TAB_Protocol','Protocol_Library','Id_Protocol'],
    ['TAB_Library','TAB_Extract','Extract_Library','Id_Extract'],
    ['TAB_Extract','TAB_Sample','Sample_Extract', 'Id_Sample'],
    ['TAB_Extract','TAB_Protocol','Protocol_Extract', 'Id_Protocol'],
    ['TAB_Sample','TAB_Type_Group','Type_Group_Sample','Id_Type_Group'],
    ['TAB_Sample','TAB_Individual','Individual_Sample','Id_Individual'],
    ['TAB_Individual','TAB_Site','Site_Individual','Id_Site'],
    ['TAB_Individual','TAB_Organism','Organism_Individual','Id_Organism'],
]
tables = {
    # table : suffix
    'TAB_Raw_Data': '_Raw_Data',
    'TAB_Sequencing':'_Sequencing',
    'TAB_Sequencing_Setup':'_Sequencing_Setup',
    'TAB_Capture':'_Capture',
    'TAB_Library':'_Library',
    'TAB_Protocol':'_Protocol',
    'TAB_Extract':'_Extract',
    'TAB_Type_Group':'_Type_Group',
    'TAB_Sample':'_Sample',
    'TAB_Individual':'_Individual',
    'TAB_Site':'_Site',
    'TAB_Organism':'_Organism'
}