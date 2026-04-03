/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class SocialDashboard extends Component {
    setup() {
        this.action = useService("action");
        this.orm = useService("orm");

        this.state = useState({
            studentCount: 0,
            ngoCount: 0,
            donorCount: 0,
            csrCount: 0,
            pendingCount: 0,
            pendingProjects: 0,
            pendingEvents: 0,
            pendingBlogs: 0,
            pendingArticles: 0,
            pendingOpps: 0,
            pendingGrants: 0,
            pendingTrainings: 0,
            pendingTestimonials: 0,
        });

        onWillStart(async () => {
            await this.fetchDashboardData();
        });
    }

    /**
     * Helper to fetch counts safely.
     * If a user lacks permission for one model, it returns 0 instead of crashing the dashboard.
     */
    async safeSearchCount(model, domain) {
        try {
            return await this.orm.searchCount(model, domain);
        } catch (error) {
            console.warn(`Access Denied or Model Missing for ${model}:`, error.message);
            return 0;
        }
    }

    async fetchDashboardData() {
        // 1. Fetch User Counts
        this.state.studentCount = await this.safeSearchCount("res.users", [['user_role', '=', 'student']]);
        this.state.ngoCount = await this.safeSearchCount("res.users", [['user_role', '=', 'ngo']]);
        this.state.donorCount = await this.safeSearchCount("res.users", [['user_role', '=', 'donor']]);
        this.state.csrCount = await this.safeSearchCount("res.users", [['user_role', '=', 'csr']]);

        // 2. Count PENDING REGISTRATIONS
        this.state.pendingCount = await this.safeSearchCount("res.partner", [['approval_status', '=', 'pending']]);

        // 3. Content Counts (Individually protected)
        this.state.pendingProjects = await this.safeSearchCount("youth.project", [['state', '=', 'submitted']]);
        this.state.pendingEvents = await this.safeSearchCount("youth.event", [['state', '=', 'submitted']]);
        this.state.pendingBlogs = await this.safeSearchCount("youth.blog", [['state', '=', 'submitted']]);
        this.state.pendingArticles = await this.safeSearchCount("youth.article", [['state', '=', 'under_review']]);

        // This was the specific line causing your AccessError crash
        this.state.pendingOpps = await this.safeSearchCount("youth.opportunity", [['state', '=', 'draft']]);

        this.state.pendingGrants = await this.safeSearchCount("youth.grant", [['state', '=', 'submitted']]);
        this.state.pendingTrainings = await this.safeSearchCount("youth.skill.dev", [['state', '=', 'draft']]);

        // 4. Testimonials (This will now run even if 'Opportunities' failed)
        const testimonialCount = await this.safeSearchCount("youth.testimonial", [['state', '=', 'draft']]);
        this.state.pendingTestimonials = testimonialCount;

        console.log("Dashboard Data Sync Complete. Testimonials found:", testimonialCount);
    }

    openAction(xmlId) {
        this.action.doAction(xmlId);
    }

    openPendingUsers() {
        this.action.doAction({
            type: 'ir.actions.act_window',
            name: 'Pending Approvals',
            res_model: 'res.partner',
            view_mode: 'list,form',
            views: [[false, 'list'], [false, 'form']],
            domain: [['approval_status', '=', 'pending']],
            target: 'current',
        });
    }

    openPendingContent(modelName, stateName, title) {
        this.action.doAction({
            type: 'ir.actions.act_window',
            name: title,
            res_model: modelName,
            view_mode: 'list,form',
            views: [[false, 'list'], [false, 'form']],
            domain: [['state', '=', stateName]],
            target: 'current',
        });
    }
}

SocialDashboard.template = "admin_system.SocialDashboard";
registry.category("actions").add("social_dashboard_client_action", SocialDashboard);