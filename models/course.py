from odoo import models, fields

class Course(models.Model):
    _name = 'courses.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    cost = fields.Float(string='Cost')
    teacher = fields.Char(string='Teacher')
    responsible_id = fields.Many2one('res.users', string='Responsible')
