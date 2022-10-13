/****** Object:  Table [dbo].[clima]    Script Date: 10/10/2022 12:02:27 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[clima](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[temperatura] [float] NULL,
	[porcentaje_lluvia] [float] NULL,
	[indice_UV] [float] NULL,
	[calidad_aire] [float] NULL,
	[fecha] [datetime] NOT NULL,
 CONSTRAINT [PK_clima] PRIMARY KEY CLUSTERED 
(
	[fecha] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

