import sublime, sublime_plugin
import re
# vim: asdf noaardvark beans=4 imho tbqh

SEARCH_LINES = 5
VIM_MODELINE_REGEX = "^(\/\*|\/\/|#+)?(\s*vi(m?):\s*)(?P<payload>(?:(?!\*\/|\s+$).)*)"

class modelinetestCommand( sublime_plugin.TextCommand ):
   def run( self, edit ):
      view = self.view
      r = sublime.Region( 0, view.full_line( view.size() ).end() )                     # inefficient
      lines = view.lines( r )
      mylines = []

      for line in range( 0, SEARCH_LINES ):
         mylines.append( lines[line] )
      for line in range(( len( lines ) - SEARCH_LINES ), len( lines )):
         mylines.append( lines[line] )

      for line in mylines:
         x = re.match( VIM_MODELINE_REGEX, view.substr( line ))
         if x:
            z = x.group('payload').split()
            for mode in z:
               self.handle( mode )

   def handle( self, mode ):
      try:
         function = getattr( modelinetestCommand, mode )
      except AttributeError:
         print( 'No handler for modeline command "%s"' % mode )
      else:
         function( mode )

   def asdf( self ):
      print( "xxx" )
         

