SELECT TOP (1000) [Name]
      ,[Role]
      ,[Location]
      ,[Years of Experience]
      ,[Active?]
      ,[Current Comp (INR)]
  FROM [SR].[dbo].[Employee Data]
  UPDATE dbo.[Employee Data]
set Role = 'Senior Associate'
WHERE Role LIKE '%Senor' OR Role LIKE '%Senir Associate%' OR Role LIKE '%Sr Analyst%';
  UPDATE dbo.[Employee Data]
SET Location = 'Bangalore'
WHERE Location = 'Banglore'
UPDATE dbo.[Employee Data]
SET [Last Working Day] = NULL
WHERE [Last Working Day] = 'Active';
UPDATE dbo.[Employee Data]
SET [Years of Experience] = '4-5'
WHERE [Years of Experience] IS NULL;
Alter table dbo.[Employee Data]
DROP COLUMN [Last Working Day];
