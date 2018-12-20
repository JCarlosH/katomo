#!/usr/bin/python3
# -*- codign: utf-8 -*-

import wx
import wx.aui
from DBManager import DBManager
from UserSetting import UserSetting

class Katomo(wx.Frame):

	ifOpenConnection = False
	
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,-1)
		self.SetSize((500,300))
		self.SetTitle("titulo")
		self.Centre()
		self.Show()

		self.DBManager = DBManager()
		self.UserSetting = UserSetting()

		self.OpenDatabase()

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


	# Events default
	def OpenDatabase(self):
		e = self.DBManager.ifConnectioToMySQL()
		if e:
			wx.MessageBox(str(e),"Error", wx.OK | wx.ICON_INFORMATION)
		else:
			self.ifOpenConnection = True



###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Connection", pos = wx.DefaultPosition, size = wx.Size( 310,313 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl5, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl6, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	

app = wx.App()
Katomo(None)
app.MainLoop()