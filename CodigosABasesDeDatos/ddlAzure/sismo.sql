/****** Object:  Table [dbo].[sismo]    Script Date: 01/10/2022 04:19:58 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[sismo](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ubicacion] [varchar](1000) NULL,
	[magnitud] [float] NULL,
	[latitud] [float] NULL,
	[longitud] [float] NULL,
	[fecha] [datetime] NULL,
 CONSTRAINT [PK_sismo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

