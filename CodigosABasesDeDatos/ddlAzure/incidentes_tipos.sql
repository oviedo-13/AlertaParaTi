/****** Object:  Table [dbo].[incidentes_tipos]    Script Date: 10/10/2022 12:03:19 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[incidentes_tipos](
	[id] [int] NOT NULL,
	[tipo_incidente] [varchar](100) NULL,
 CONSTRAINT [PK_tipos_incidentes] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

