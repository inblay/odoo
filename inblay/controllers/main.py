from werkzeug.utils import redirect

from odoo import http
from odoo.http import request


class BackBackground(http.Controller):

    @http.route(['/back_background'], type='http', auth='user', website=False)
    def dashboard(self, **post):
        user = request.env.user
        company = user.company_id
        url = '/web_enterprise/static/src/img/home-menu-bg-overlay.svg'
        formats = ('.jpge', '.jpg', '.png', '.gif', '.svg')
        if company.back_background and (company.back_background
                                        .endswith(formats)):
            url = company.back_background

        return redirect(url)
