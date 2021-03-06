from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpGuide(models.Model):
    _name = 'op.guide'
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
    gr_no = fields.Char("GR Number", size=20)
    category_id = fields.Many2one('op.category', 'Category')
    tracking_no = fields.Char('Tracking Number', size=10)
    hajj_yr = fields.Char('Hajj Year', size=4)
    pid_no = fields.Char('PID Number', size=7)
    mobile_no = fields.Char('Mobile Number', size=11)
    nid_no = fields.Char('NID Number', size=17)
    replacement_contact = fields.Many2one(
        'res.partner', 'Replacement Name')
    hajj_category = fields.Selection(
       [('1', 'Category 1'), ('2', 'Category 2'),
       ('3', 'Category 3')], 'Hajj Category')
    hajj_guide = fields.Boolean('Hajj Guide')
    attendee_ids = fields.Many2many('op.haji', string="Attendees")
    total_haji = fields.Integer(string="Total haji", compute='_total_haji')

    @api.depends( 'attendee_ids')
    def _total_haji(self):
        for r in self:
            
            r.total_haji = len(r.attendee_ids) 
    
   

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))


