from odoo import models, fields, api
from odoo.exceptions import ValidationError

class umrahGuide(models.Model):
    _name = 'umrah.guide'
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
    visa_info = fields.Char('Visa Info' )
    id_number = fields.Char('ID Card Number')
    already_partner = fields.Boolean('Already Partner')
    partner_id = fields.Many2one(
        'res.partner', 'Partner', required=True, ondelete="cascade")
    pass_no = fields.Char('Passport Number')
    hajj_yr = fields.Char('Umrah Year')
    pid_no = fields.Char('PID Number')
    mobile_no = fields.Char('Mobile Number')
    nid_no = fields.Char('NID Number')
    guide_contact = fields.Many2one(
        'res.partner', 'Guide Name')
    replacement_contact = fields.Many2one(
        'res.partner', 'Replacement Name')
    hajj_category = fields.Selection(
       [('1', 'Category 1'), ('2', 'Category 2'),
       ('3', 'Category 3')], 'Hajj Category')
    hajj_guide = fields.Boolean('Hajj Guide')
    attendee_ids = fields.Many2many('op.umrah', string="Attendees")
    total_haji = fields.Integer(string="Total haji", compute='_total_haji')
    mofa = fields.Integer('Mofa Amount')
    hajj_no = fields.Integer('Haji Amount')
    total_amount = fields.Integer(string="Total Amount", compute='_total_amount')

    @api.depends( 'attendee_ids')
    def _total_haji(self):
        for r in self:
            
            r.total_haji = len(r.attendee_ids) 
    
    @api.depends( 'mofa' ,'hajj_no')
    def _total_amount(self):
        for r in self:
            
            r.total_amount = r.mofa*r.hajj_no 
