{
    'name': 'Admin Management System',
    'version': '1.0',
    'summary': 'Admin module to manage Users, Projects, Funds, and Content',
    'category': 'Administration',
    'author': 'Your Name',
    'depends': ['base', 'web', 'mail', 'website', 'project', 'event', 'account', 'website_blog','cy_whatsapp_connector',],

    'data': [
        # 1. SECURITY (Order is Critical: Groups -> Rules -> Access Rights)
        'security/social_security.xml',    # Defines Groups (MUST BE FIRST)
        'security/content_security.xml',   # Defines Rules using Groups
        'security/approval_security.xml',  # Defines Rules using Groups
        'security/ir.model.access.csv',    # Grants Access to Models

        'views/testimonial_template.xml',
        'views/testimonial_backend_views.xml',
        # 2. VIEWS (Actions must be defined BEFORE Menus)
        'views/project_views.xml',
        'views/social_views.xml',
        'views/fund_views.xml',
        'views/content_views.xml',
        'views/award_views.xml',
        'views/event_views.xml',
        # 'views/audit_views.xml',     # <-- COMMENTED OUT (Since you deleted the audit model)
        'views/opportunity_views.xml', # <-- Defines 'action_social_opportunity'
        'views/approval_views.xml',
        'views/blog_views.xml',
        'views/website_landing.xml',
        'views/grant_views.xml',    # <--- NEW
        'views/skill_views.xml',

        # 3. MENUS (Must be LAST because it uses IDs/Actions from files above)
        'views/menus.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # Path matches your folder name 'admin_dashsystem'
            'admin_dashsystem/static/src/xml/dashboard_home.xml',
            'admin_dashsystem/static/src/js/dashboard_home.js',
            'admin_dashsystem/static/src/xml/systray_home.xml',
            'admin_dashsystem/static/src/js/systray_home.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}