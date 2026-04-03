/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

class HomeSystray extends Component {
    setup() {
        this.action = useService("action");
    }

    _onClick() {
        // This ID must match the client action tag in your dashboard_home.js
        this.action.doAction("social_dashboard_client_action");
    }
}

HomeSystray.template = "admin_system.HomeSystray";

// Add to the 'systray' category (Top Right Menu)
// Sequence 1 puts it near the left side of the systray (near Activities/Settings)
registry.category("systray").add("admin_system.HomeSystray", { Component: HomeSystray }, { sequence: 1 });