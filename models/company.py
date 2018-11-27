from odoo import models, fields, api


class Hajjcompany(models.Model):
    _name = 'hajj.company'
   
    name = fields.Char("Company Name")
    licence = fields.Char("Licence")
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    licence_nbr = fields.Char("Licence Number")
    
    
    
    
class Civilcompany(models.Model):
    _name = 'civil.company'
   
    name = fields.Char("Company Name")
    licence = fields.Char("Licence")
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    licence_nbr = fields.Char("Licence Number")    