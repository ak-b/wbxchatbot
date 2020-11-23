from wibot.cards.firewallinc import get_incident_triage_card
from wibot.cards.docs import get_misc_docs
from wibot.cards.help import get_menu
from wibot.cards.cards_inc import get_incident_triage_card
from wibot.cards.cards_docs import get_misc_docs
from wibot.cards.cards_gen import get_gen_msg
from wibot.cards.cards_helpmenu import get_menu
from wibot.cards.cards_input import get_input  
from wibot.cards.cards_searchipi import search_ipi  
from wibot.cards.cards_searchacl import search_acl
from wibot.cards.cards_inlineaction import get_in
from wibot.cards.cards_alerts import alerts


def handle_doc(args):
    if 'firewall-incident-triage' == args:
        return get_incident_triage_card()

    if 'misc' == args:
        return get_misc_docs()

    if 'gen' == args:
    	return get_gen_msg()

    if 'help' == args:
    	return get_menu()

    if 'input' == args:
        return get_input()

    if 'ipi' == args:
        return search_ipi()

    if 'acl' == args:
        return search_acl()

    if 'inline' == args:
        return get_in()

    if 'alert' == args:
        return alerts()