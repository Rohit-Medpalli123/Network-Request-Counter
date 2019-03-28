# Import ConfigParser(to allow us to save and retrieve code related data)
from configparser import ConfigParser

# Import all the required modules
from SeleniumLogic import BrowserAutomation
from VerificationLogic import NetworkRequests
from EmailNotification import EmailOperation
import os

if __name__ == '__main__':

    # Navigate to project root directory
    os.chdir('..')

    # By using the parser we can access(read/modify) the configuration file
    parser = ConfigParser()
    parser.read('config.ini')

    # Perform Desired operations using selenium like clicking on button,submitting a form,uploading a file etc.
    browserops = BrowserAutomation(parser)
    browserops.visit_url()
    tracker_list = browserops.resource_timing_api()
    print(tracker_list)

    # Validate the network requests
    validatereq = NetworkRequests(parser,tracker_list)
    validatereq.fetch_conditions()
    result = validatereq.network_request_counter()

    # Send email report to team
    send_email = EmailOperation(result, parser)
    blank_gen_rows = send_email.row_generator()
    rows_with_data = send_email.fill_data_into_rows(blank_gen_rows)
    html_template_path = os.path.join(os.getcwd(), ".\\Templates\\html_template.txt")
    html_template = send_email.gen_html_template(rows_with_data, html_template_path)
    Subject, receiver, sender = send_email.email_details()
    send_email.send_email_to_team(Subject, html_template, receiver, sender)
    # send_email.ses_email_to_team(Subject, html_template, multiple_recipients)

    # Close the browser once operation is completed
    browserops.close_browser()




