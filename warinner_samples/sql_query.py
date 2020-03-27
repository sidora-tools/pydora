def build_join_query(tags, projects):
    query = f"""
    SELECT *
    FROM `TAB_Raw_Data` rd 

    INNER JOIN `TAB_Sequencing` seq 
    ON rd.`Sequencing` = seq.`Id`

    INNER JOIN `TAB_Sequencing_Setup` setp 
    ON seq.Setup  = setp.Id

    INNER JOIN `TAB_Capture` cap
    ON seq.`Capture` = cap.Id

    INNER JOIN `TAB_Library` lib
    ON cap.`Library` = lib.`Id`

    INNER JOIN `TAB_Protocol` AS lib_prot
    ON lib.`Protocol` = lib_prot.`Id`

    INNER JOIN `TAB_Extract` ext
    ON lib.`Extract` = ext.`Id`

    INNER JOIN `TAB_Sample` samp
    ON ext.`Sample` = samp.`Id`

    INNER JOIN `TAB_Protocol` AS ext_prot
    ON ext.`Protocol` = ext_prot.`Id`

    INNER JOIN (
        SELECT Id, Name as Sample_Type_Name 
        FROM `TAB_Type_Group`   
    ) AS typ 
    ON samp.`Type_Group` = typ.Id

    INNER JOIN `TAB_Individual` ind
    ON samp.`Individual` = ind.`Id`

    INNER JOIN `TAB_Site` AS sit
    ON ind.`Site` = sit.`Id`
    
    INNER JOIN `TAB_Organism` AS org
    ON ind.`Organism` = org.Id

    WHERE samp.`Projects` REGEXP '{"|".join([p for p in projects])}'
    OR samp.Tags REGEXP '{"|".join([t for t in tags])}'
    """

    return(query)

def build_single_query(table_name):
    query = f"""
    SELECT *
    FROM {table_name}
    """
    return(query)