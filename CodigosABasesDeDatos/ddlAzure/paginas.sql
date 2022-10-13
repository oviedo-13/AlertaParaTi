/****** Object:  Table [dbo].[paginas]    Script Date: 10/10/2022 12:03:35 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[paginas](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[pagina] [varchar](100) NULL,
	[fecha] [datetime] NULL,
 CONSTRAINT [PK_paginas] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

