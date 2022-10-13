/****** Object:  Table [dbo].[incidentes_coordenadas]    Script Date: 10/10/2022 12:02:57 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[incidentes_coordenadas](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_incidente] [varchar](100) NULL,
	[longitud] [float] NULL,
	[latitud] [float] NULL,
	[fecha_actualizacion] [datetime] NULL,
 CONSTRAINT [PK_incidentes_coordenadas] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

