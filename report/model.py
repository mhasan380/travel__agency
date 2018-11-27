from datetime import datetime

from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import time
import requests
from datetime import date
from datetime import datetime
import logging
from pytz import timezone


_logger = logging.getLogger(__name__)

class AttendanceRportWizard(models.TransientModel):
    _name = "hajj.wizard"
    _description = "Hajj Report Wizard"
    hajj_id = fields.Many2one('op.haji', string="Haji")

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['hajj_id'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['hajj_id'])[0])
        return self.env.ref('travel__agency.travel_haji').report_action(self, data=data)

class ReportAttendance(models.AbstractModel):
    _name = 'report.travel__agency.travel_haji'
    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('travel__agency.travel_haji')
        
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))

        if(docs.hajj_id.id):
            hajj = self.env['op.haji'].search([('id', '=', hajj_id.id)])
            _logger.info(hajj)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'hajis': hajj,
        }
        return report_obj.render('travel__agency.travel_haji', docargs)
