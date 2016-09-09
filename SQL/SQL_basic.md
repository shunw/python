##Left Join More than 2 Tables

###Example 1
resource: http://stackoverflow.com/questions/7980052/how-to-do-left-join-with-more-than-2-tables

select a.x, b.x, c.x   
from number as a  
left join customer as b on a.b = b.b  
left join numbergroup as c on a.c = c.c and c.b = b.b  



###Example 2
resource: http://stackoverflow.com/questions/14260860/multiple-left-joins-on-multiple-tables-in-one-query  

SELECT something  
FROM   master      parent  
JOIN   master      child ON child.parent_id = parent.id  
LEFT   JOIN second parentdata ON parentdata.id = parent.secondary_id  
LEFT   JOIN second childdata ON childdata.id = child.secondary_id  
WHERE  parent.parent_id = 'rootID'  

