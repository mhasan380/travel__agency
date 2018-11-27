from odoo import models, fields, api
from odoo.exceptions import ValidationError
from _cffi_backend import string

class SoudiInfo(models.Model):
    _name = 'soudi.info'
   
    name = fields.Char("Company Name")
    contact_nbr = fields.Char("Contact Number")
    monajjem_nbr = fields.Char("Monajjem Number")
    iban_no = fields.Char( required=True, string="IBAN Number")
    moktob_info = fields.Text("Moktob Info")
    moktob_no = fields.Char("Moktob Number")
    haji_nbr = fields.Char("Total Haji Number")
    hajj_year = fields.Char("Hajj Year")
    
    