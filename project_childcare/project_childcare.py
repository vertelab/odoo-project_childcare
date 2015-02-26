# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from datetime import datetime
import werkzeug
import pytz

class website_childcare(http.Controller):
        
    @http.route(['/childcare/<model("res.users"):user>', ], type='http', auth="user", website=True)
    def childcare_loggedin(self, user=False, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        return request.render('project_childcare.fee_calc',{})
        
    @http.route(['/childcare'], type='http', auth="none", website=True)
    def childcare_anon(self, **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        return request.render('project_childcare.fee_calc', {})
        
class res_users(models.Model):
    _inherit = ['res.users']
    
    childcare_income = field.Integer()
	def _income_max(self):
		if (self.childcare_income > self.company_id.childcare_maxincome):
			return self.company_id.childcare_maxincome
		if (self.childcare_income < self.company_id.childcare_mincharge):
			return 0
		return self.childcare_income
    childcare_income_max = field.Integer(compute="_income_max")
    childcare_type1 = field.One2many(comodel_name="childcare.type")
    childcare_time1 = field.One2many(comodel_name="childcare.time_of_residence")
	def _monthly_type1(self):
		sum = 0
		if self.childcare_type1.id == 1: # Förskola/familjedaghem 1-3 år
			sum = round(0.03 * self.childcare_income)
		elif self.childcare_type1.id == 2: # Allmän förskola 4-5 år
			if self.childcare_time1.id == 1: # Över 15 tim
				sum round((0.03 * self.childcare_income)* 0.7)
			elif self.childcare_time1.id == 2: # Upp till 15 tim
				sum round((0.03 * self.childcare_income)* 0.17)
		elif self.childcare_type1.id == 3:  # Frididshem 6 -9 år
			sum round(0.02 * self.childcare_income)
		elif self.childcare_type1.id == 4: # Öppen fritidsverksamehet 10 -12 år
			sum round(0.01 * self.childcare_income)
		if sum < 50:
			sum = 0
		return sum
    childcare_sum1 = field.Integer(compute="_monthly_type1")

	def _monthly_type2(self):
		sum = 0
		if self.childcare_type2.id == 1: # Förskola/familjedaghem 1-3 år
			sum = round(0.02 * self.childcare_income)
		elif self.childcare_type2.id == 2: # Allmän förskola 4-5 år
			if self.childcare_time2.id == 1: # Över 15 tim
				sum round((0.02 * self.childcare_income)* 0.7)
			elif self.childcare_time2.id == 2: # Upp till 15 tim
				sum round((0.02 * self.childcare_income)* 0.17)
		elif self.childcare_type2.id == 3:  # Frididshem 6 -9 år
			sum round(0.01 * self.childcare_income)
		elif self.childcare_type2.id == 4: # Öppen fritidsverksamehet 10 -12 år
			sum round(0.005 * self.childcare_income)
		if sum < 50:
			sum = 0
		return sum	
    childcare_sum2 = field.Integer(compute="_monthly_type2")
    childcare_time1 = field.One2many(comodel_name="childcare.type")
    childcare_type2 = field.One2many(comodel_name="childcare.time_of_residence")

	def _monthly_type3(self):
		sum = 0
		if self.childcare_type3.id == 1: # Förskola/familjedaghem 1-3 år
			sum = round(0.01 * self.childcare_income)
		elif self.childcare_type3.id == 2: # Allmän förskola 4-5 år
			if self.childcare_time3.id == 1: # Över 15 tim
				sum round((0.01 * self.childcare_income)* 0.7)
			elif self.childcare_time3.id == 2: # Upp till 15 tim
				sum round((0.01 * self.childcare_income)* 0.17)
		elif self.childcare_type3.id == 3:  # Frididshem 6 -9 år
			sum round(0.01 * self.childcare_income)
		elif self.childcare_type3.id == 4: # Öppen fritidsverksamehet 10 -12 år
			sum round(0.005 * self.childcare_income)
		if sum < 50:
			sum = 0
		return sum			
	childcare_sum3 = field.Integer(compute="_monthly_type3")
    childcare_type3 = field.One2many(comodel_name="childcare.type")
    childcare_time3 = field.One2many(comodel_name="childcare.time_of_residence")

	def _monthly(self):
		return self.childcare_sum1 + self.childcare_sum2 + self.childcare_sum3
    childcare_monthly = field.Integer(compute="_monthly")

    
class childcare_type(models.Model):
	_name = "childcare.type"
    _description = "Childcare Types"

	name = fields.Char()
	
class childcare_tor(models.Model):
	_name = "childcare.time_of_residence"
    _description = "Childcare Time of Residence"

	name = fields.Char()
	
	
class res_company(models.Model):
	_inherit = ['res.company']
	
	childcare_maxincome = fields.Integer(default=42000)
	childcare_mincharge = fields.Integer(default=0)

	

	else
		document.all['sum3'].innerHTML = 0;
//Totalsumma
	document.all['totalsum'].innerHTML = Math.round(iSum1 + iSum2 + iSum3);
