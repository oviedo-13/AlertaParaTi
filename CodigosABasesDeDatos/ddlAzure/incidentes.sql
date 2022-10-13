/****** Object:  Table [dbo].[incidentes]    Script Date: 10/10/2022 12:02:43 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[incidentes](
	[id] [varchar](200) NOT NULL,
	[tipo_id] [int] NULL,
	[tiempo_inicio] [datetime] NULL,
	[tiempo_final] [datetime] NULL,
	[desde_lugar] [varchar](1000) NULL,
	[hasta_lugar] [varchar](1000) NULL,
	[longitud_metros] [float] NULL,
 CONSTRAINT [PK_incidentes] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

