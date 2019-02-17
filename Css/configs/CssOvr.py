

class CssDivBoxWithDotBorder(object):
  """ CSS Style for a Div item with a border with dots"""
  __style = [{'attr': 'margin', 'value': '25px'}]

  def customize(self, style, eventsStyles):
    """ Enhance the different static configurations """
    style.update({"border": '1px dashed %s' % self.getColor('greys', 9)})