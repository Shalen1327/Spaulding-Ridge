SELECT TOP (1000) [Location]
      ,[Role]
      ,[Average Industry Compensation]
  FROM [SR].[dbo].[Average Industry Compensation]
      UPDATE dbo.[Average Industry Compensation]
SET Location = 'Bangalore'
WHERE Location = 'Banglore'