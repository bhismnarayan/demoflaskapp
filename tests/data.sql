INSERT into Product values(11,'Product3','Product3 Description');
INSERT into Issue ('Title','category')values('Issue1','Low');
INSERT into Metric ('Title','Description')values('Metric','Metric 1 Description');

INSERT into Product values(33,'Product33','Product33 Description');
INSERT into Issue ('Title','category','Product_ID')values('Issue333','Low',33);
INSERT into Metric ('Title','Description','Product_ID','MetricID')values('Metric3333','Metric 3333 Description',33,2);