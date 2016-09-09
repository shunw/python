##Left Join More than 2 Tables

resource: http://stackoverflow.com/questions/7980052/how-to-do-left-join-with-more-than-2-tables

select a.x, b.x, c.x 
from number as a
left join customer as b on a.b = b.b
left join numbergroup as c on a.c = c.c and c.b = b.b

