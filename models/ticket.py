from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ticket(models.Model):
    _name = 'op.ticket'
   
    
    name = fields.Char("Name")
    route = fields.Char("Route")
    mobile_no = fields.Char( string="Mobile Number")
    ar_name = fields.Char("Airline Name")
    ticket_no = fields.Char("Ticket Number")
    period = fields.Selection(
       [('1', '1-15'), ('2', '16-31'),('3', '16-28'),('4', '16-30')], 'Period')
    ticket_date = fields.Date( string='Ticket Date', default=fields.Date.today )
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ('o', 'Other')], 'Gender')
    seller_id = fields.Many2one('res.users', 
    string="Booked By")
    fare = fields.Float("Net Bill")
    tax = fields.Float("Tax")
    total_bill = fields.Float(string="Gross Bill", compute='_total_bill')
    ita_bill = fields.Float(string="IATA Bill", compute='_ita_bill')
    commision = fields.Float(string="Com", compute='_comision')
    profit = fields.Float(string="Profit", compute='_profit')
    payment_method = fields.Selection(
       [('1', 'Cash'), ('2', 'Check'), ('3', 'Online')], 'Payment Method')
    due = fields.Float('Due')
    pay_date = fields.Date('Payment Date')
    reference = fields.Char("Reference")
    
    @api.depends('fare', 'tax')
    def _total_bill(self):
        for r in self:
            r.total_bill= r.fare+r.tax
            
    @api.depends('fare')
    def _comision(self):
        for r in self:
            r.commision= r.fare*0.07
    
    
    @api.depends('fare', 'tax')
    def _ita_bill(self):
        for r in self:
            r.ita_bill= ((r.fare-r.commision+(r.commision*0.04))+r.tax)
            
    @api.depends('total_bill' , 'ita_bill')
    def _profit(self):
        for r in self:
            r.profit= r.total_bill - r.ita_bill        
    