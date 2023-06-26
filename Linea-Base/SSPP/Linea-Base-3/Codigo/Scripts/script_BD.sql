-- Active: 1687131645689@@127.0.0.1@3306

USE [SSPP]
GO
/****** Object:  Table [dbo].[Celda]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Celda](
	[Cod_celda] [numeric](18, 0) NOT NULL,
	[Numero] [int] NOT NULL,
	[Capacidad] [varchar](150) NOT NULL,
	[Cod_prision] [numeric](18, 0) NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_celda] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Clientes]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Clientes](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Empresa] [nvarchar](100) NULL,
	[Usuario] [nvarchar](50) NULL,
	[Contraseña] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Conducta]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Conducta](
	[Cod_conducta] [numeric](18, 0) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
	[Descripcion] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_conducta] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Crimen]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Crimen](
	[Cod_crimen] [numeric](18, 0) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
	[Descripcion] [varchar](150) NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_crimen] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Curso]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Curso](
	[Cod_curso] [numeric](18, 0) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_curso] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Prision]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Prision](
	[Cod_prision] [numeric](18, 0) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
	[Direccion] [varchar](150) NOT NULL,
	[Capacidad] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_prision] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Recluso]    Script Date: 18 Jun. 2023 17:52:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Recluso](
	[Cod_recluso] [numeric](18, 0) NOT NULL,
	[Nombre] [varchar](20) NOT NULL,
	[Apellido] [varchar](20) NOT NULL,
	[Fecha_nacimiento] [date] NULL,
	[Cod_crimen] [numeric](18, 0) NULL,
	[Cod_curso] [numeric](18, 0) NULL,
	[Cod_conducta] [numeric](18, 0) NULL,
	[Cod_celda] [numeric](18, 0) NULL,
	[Peligrosidad] [int] NULL,
	[Comentario] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[Cod_recluso] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Celda]  WITH CHECK ADD FOREIGN KEY([Cod_prision])
REFERENCES [dbo].[Prision] ([Cod_prision])
GO
ALTER TABLE [dbo].[Recluso]  WITH CHECK ADD FOREIGN KEY([Cod_celda])
REFERENCES [dbo].[Celda] ([Cod_celda])
GO


