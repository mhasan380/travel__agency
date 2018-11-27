from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpUmrah(models.Model):
    _name = 'op.umrah'
    _inherits = {'res.partner': 'partner_id'}

    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128)
    birth_date = fields.Date('Birth Date')
    middle_name = fields.Char('Middle Name', size=128)
    last_name = fields.Char('Last Name', size=128)
    birth_date = fields.Date('Birth Date')
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Blood Group')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ('o', 'Other')], 'Gender')
    nationality = fields.Many2one('res.country', 'Nationality')
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    already_partner = fields.Boolean('Already Partner')
    partner_id = fields.Many2one(
        'res.partner', 'Partner', required=True, ondelete="cascade")
    pass_no = fields.Char("Passport Number")
    category_id = fields.Many2one('op.category', 'Category')
    track_no = fields.Char('Tracking Number', size=10)
    hajj_yr = fields.Char('Hajj Year', size=4)
    pid_no = fields.Char('PID Number', size=7)
    mobile_no = fields.Char('Mobile Number', size=11)
    nid_no = fields.Char('NID Number', size=17)
    ref_contact = fields.Many2one(
        'res.partner', 'Reference Name')
    
    um_package = fields.Selection(
       [('dir', 'Direct'), ('loc', 'Local')], 'Umrah Packages')
    hajj_guide = fields.Boolean('Hajj Guide')
    house = fields.Boolean('House')
    food = fields.Boolean('Food')
    sightings = fields.Boolean('Sightings')
    payments = fields.Boolean('Payment')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    visa = fields.Boolean('Only Visa')
    soudi_no = fields.Char('Soudi Contact Number')
    
    

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))


   