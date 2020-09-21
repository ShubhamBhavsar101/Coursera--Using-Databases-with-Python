# First Run Assignment4.py which will create Assignment4.sqlite file.
# Open the Assignment4.sqlite file in db Browser.
# Use the code below to execute in db Browser and submit the first row data which is a number for Assignment 

SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X

## Thanks