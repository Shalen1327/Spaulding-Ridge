SELECT TOP (1000) [Name]
      ,[Role]
      ,[Location]
      ,[Years of Experience]
      ,[L3Q Average Self Rating]
      ,[L3Q Average Manager Rating]
  FROM [SR].[dbo].[Employee Rating]
    UPDATE dbo.[Employee Rating]
SET Location = 'Bangalore'
WHERE Location = 'Banglore'
UPDATE [Employee Rating]
SET Years of Experience = (
    SELECT [Years of Experience]
    FROM [Employee Data]
    WHERE [Employee Data].Name = [Employee Rating].Name
)
WHERE YoE IS NULL;
UPDATE dbo.[Employee Rating]
set Role = 'Senior Associate'
WHERE Role LIKE '%Senor' OR Role LIKE '%Senir Associate%' OR Role LIKE '%Sr Analyst%';
UPDATE dbo.[Employee Rating]
EXEC sp_rename '[Employee Rating].YoE', 'Years of Experience', 'COLUMN';

