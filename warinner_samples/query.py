def build_query(tags, projects):
    query = f"""
    SELECT *
    FROM `TAB_Analysis_Result_String` ars

    INNER JOIN `TAB_Analysis` an 
    ON ars.`Analysis`= an.`Id`
    
    INNER JOIN `TAB_Raw_Data` rd 
    ON an.`Raw_Data` = rd.`Id`

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

    WHERE samp.`Projects` in (
    '{"','".join([t for t in tags])}')
    OR samp.Tags REGEXP('{"|".join([t for t in tags])}')
    AND an.Deleted = 'false'
    """

    return(query)