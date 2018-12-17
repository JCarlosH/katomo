import wx

class Katomo(wx.Frame):
	
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,-1)
		self.SetSize((500,300))
		self.SetTitle("titulo")
		self.Centre()
		self.Show()

		self.menu()
		self.toolbar()
		self.gui()

		# Connect Events
		self.Bind( wx.EVT_MENU, self.closeApp, id = self.fileMenuClose.GetId() )
		self.Bind( wx.EVT_TOOL, self.connect, id = self.toolConnects.GetId() )

	def menu(self):
		self.menuBar = wx.MenuBar(0)
		
		self.fileMenu = wx.Menu()
		
		self.fileMenuClose = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"&Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.AppendItem( self.fileMenuClose )

		self.menuBar.Append(self.fileMenu,u"&File")

		
		self.SetMenuBar(self.menuBar)

	def toolbar(self):
		self.toolBar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.toolConnects = self.toolBar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"src/icons/connect.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL,'Tooltip','Connect',None) 
		self.toolBar.Realize()

	def gui(self):
		self.SetSizeHintsSz( wx.DefaultSize,wx.DefaultSize)
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		SizerH1 = wx.BoxSizer(wx.HORIZONTAL)
		self.tree = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		SizerH1.Add( self.tree, 0, wx.ALL|wx.EXPAND, 5 )

		root = self.tree.AddRoot('Objects')
		self.tree.Expand(root)

		self.notebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel1 = wx.Panel( self.notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.notebook1.AddPage( self.m_panel1, u"a page" )
		
		SizerH1.Add( self.notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( SizerH1 )
		self.Layout()

	# Virtual event handlers, overide them in your derived class
	def closeApp( self, event ):
		self.Destroy()
	
	def connect( self, event ):
		event.Skip()


app = wx.App()
Katomo(None)
app.MainLoop()