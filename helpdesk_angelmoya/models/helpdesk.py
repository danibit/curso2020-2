from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "Helpesk Ticket"

    name = fields.Char(
        string='Name')
    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')
