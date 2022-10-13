/****** Object:  Table [dbo].[sismo]    Script Date: 10/10/2022 12:03:59 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[sismo](
	[id] [varchar](100) NOT NULL,
	[ubicacion] [varchar](1000) NULL,
	[magnitud] [float] NULL,
	[longitud] [float] NULL,
	[latitud] [float] NULL,
	[fecha_actualizacion] [datetime] NULL,
	[fecha] [datetime] NULL,
 CONSTRAINT [PK_sismo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


