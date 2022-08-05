# PII: files/november_statement.pdf: Name: John Smith
# NO_PII: files/november_statement.pdf: MyBank.com - Banking Statement
from scan import get_file_text, scan_files
from team3_pii import find_us_phone_numbers, find_twitter_handles, \
    find_us_ss_numbers, find_email_addresses

def find_pii(text):
    detected_pii_list = []

    if find_us_phone_numbers(text):
        detected_pii_list.append('us_phone_number')

    if find_twitter_handles(text):
        detected_pii_list.append('twitter_handles')

    if find_us_ss_numbers(text):
        detected_pii_list.append('us_ss_numbers')

    if find_email_addresses(text):
        detected_pii_list.append('us_email_addresses')
    return detected_pii_list


def main():
    #get list of files to be scanned
    file_list = scan_files()
    for f in file_list:
        # get the text from the file
        for text in get_file_text(f):
            result = find_pii(text)
            if result:
                #PII was found
                print(': '.join(['PII', f, text]))
                print(result)
            else:
                # NO PII found in this file
                print(': '.join(['NO PII', f, text]))



if __name__ == '__main__':
    main()