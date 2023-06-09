import os
import django
import unittest
import datetime

# Set up the Django settings module for testing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TA_Scheduling_Project.settings')
django.setup()

from TA_Scheduling_App.models.User import User


class TestUserInit(unittest.TestCase):
    def test_init_valid_input(self):
        try:
            User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                 PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))
        except ValueError:
            self.fail("User init failed with valid input values.")


#     Please note setters will handle all additional checking on initialization.


class TestSetRole(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setRole_valid_admin(self):
        self.assertTrue(self.user.setRole("ADMIN"), "Valid role 'ADMIN' failed to be set.")

    def test_setRole_valid_instructor(self):
        self.assertTrue(self.user.setRole("INSTRUCTOR"), "Valid role 'INSTRUCTOR' failed to be set.")

    def test_setRole_valid_ta(self):
        self.assertTrue(self.user.setRole("TA"), "Valid role 'TA' failed to be set.")

    def test_setRole_invalid_empty_string(self):
        self.assertFalse(self.user.setRole(""), "Empty role string was incorrectly set.")

    def test_setRole_invalid_whitespace(self):
        self.assertFalse(self.user.setRole("   "), "Role with only whitespace was incorrectly set.")

    def test_setRole_invalid_lowercase(self):
        self.assertFalse(self.user.setRole("admin"), "Lowercase role string was incorrectly set.")

    def test_setRole_invalid_mixed_case(self):
        self.assertFalse(self.user.setRole("AdMiN"), "Mixed case role string was incorrectly set.")

    def test_setRole_invalid_numbers(self):
        self.assertFalse(self.user.setRole("1234"), "Role with numbers was incorrectly set.")

    def test_setRole_invalid_special_characters(self):
        self.assertFalse(self.user.setRole("#$%@"), "Role with special characters was incorrectly set.")

    def test_setRole_invalid_other_string(self):
        self.assertFalse(self.user.setRole("STUDENT"), "Invalid role string was incorrectly set.")

    def test_setRole_invalid_spaces_before_after(self):
        self.assertFalse(self.user.setRole("  ADMIN  "), "Role with spaces before and after was incorrectly set.")

    def test_setRole_invalid_combination(self):
        self.assertFalse(self.user.setRole("ADMIN123"), "Role with letters and numbers was incorrectly set.")

    def test_setRole_invalid_unicode(self):
        self.assertFalse(self.user.setRole("ÄDMIN"), "Role with unicode characters was incorrectly set.")

    def test_setRole_invalid_long_string(self):
        self.assertFalse(self.user.setRole("A" * 256), "Role with too long string was incorrectly set.")

    def test_setRole_invalid_one_letter(self):
        self.assertFalse(self.user.setRole("A"), "Role with only one letter was incorrectly set.")

    def test_setRole_invalid_null(self):
        self.assertFalse(self.user.setRole(None), "Null role was incorrectly set.")


class TestSetFirstName(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setFirstName_valid(self):
        self.assertTrue(self.user.setFirstName("John"), "Valid first name failed to be set.")

    def test_setFirstName_valid_with_spaces(self):
        self.assertTrue(self.user.setFirstName("John Smith"), "Valid first name with spaces failed to be set.")

    def test_setFirstName_valid_with_hyphen(self):
        self.assertTrue(self.user.setFirstName("John-Smith"), "Valid first name with hyphen failed to be set.")

    def test_setFirstName_valid_with_apostrophe(self):
        self.assertTrue(self.user.setFirstName("John's"), "Valid first name with apostrophe failed to be set.")

    def test_setFirstName_invalid_empty_string(self):
        self.assertFalse(self.user.setFirstName(""), "Empty first name was incorrectly set.")

    def test_setFirstName_invalid_whitespace(self):
        self.assertFalse(self.user.setFirstName("   "), "First name with only whitespace was incorrectly set.")

    def test_setFirstName_invalid_special_characters(self):
        self.assertFalse(self.user.setFirstName("#$%@"), "First name with special characters was incorrectly set.")

    def test_setFirstName_invalid_numbers(self):
        self.assertFalse(self.user.setFirstName("1234"), "First name with numbers was incorrectly set.")

    def test_setFirstName_invalid_combination(self):
        self.assertFalse(self.user.setFirstName("John1234"), "First name with numbers and letters was incorrectly set.")

    def test_setFirstName_invalid_unicode(self):
        self.assertFalse(self.user.setFirstName("Élodie"), "Invalid first name with unicode characters set.")

    def test_setFirstName_valid_mixed_case(self):
        self.assertTrue(self.user.setFirstName("jOhN"), "Valid first name with mixed case failed to be set.")

    def test_setFirstName_valid_spaces_before_after(self):
        self.assertTrue(self.user.setFirstName("  John  "),
                        "Valid first name with spaces before and after failed to be set.")

    def test_setFirstName_invalid_only_numbers(self):
        self.assertFalse(self.user.setFirstName("1234"), "First name with only numbers was incorrectly set.")

    def test_setFirstName_invalid_long_string(self):
        self.assertFalse(self.user.setFirstName("a" * 256), "First name that is too long was incorrectly set.")

    def test_setFirstName_valid_one_letter(self):
        self.assertTrue(self.user.setFirstName("J"), "Valid first name with only one letter failed to be set.")

    def test_setFirstName_invalid_null(self):
        self.assertFalse(self.user.setFirstName(None), "Null first name was incorrectly set.")


class TestSetLastName(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setLastName_valid(self):
        self.assertTrue(self.user.setLastName("Smith"), "Valid last name failed to be set.")

    def test_setLastName_valid_with_spaces(self):
        self.assertTrue(self.user.setLastName("Smith Johnson"), "Valid last name with spaces failed to be set.")

    def test_setLastName_valid_with_hyphen(self):
        self.assertTrue(self.user.setLastName("Smith-Johnson"), "Valid last name with hyphen failed to be set.")

    def test_setLastName_valid_with_apostrophe(self):
        self.assertTrue(self.user.setLastName("O'Connor"), "Valid last name with apostrophe failed to be set.")

    def test_setLastName_invalid_empty_string(self):
        self.assertFalse(self.user.setLastName(""), "Empty last name was incorrectly set.")

    def test_setLastName_invalid_whitespace(self):
        self.assertFalse(self.user.setLastName("   "), "Last name with only whitespace was incorrectly set.")

    def test_setLastName_invalid_special_characters(self):
        self.assertFalse(self.user.setLastName("#$%@"), "Last name with special characters was incorrectly set.")

    def test_setLastName_invalid_numbers(self):
        self.assertFalse(self.user.setLastName("1234"), "Last name with numbers was incorrectly set.")

    def test_setLastName_invalid_combination(self):
        self.assertFalse(self.user.setLastName("Smith1234"), "Last name with numbers and letters was incorrectly set.")

    def test_setLastName_invalid_unicode(self):
        self.assertFalse(self.user.setLastName("Åström"), "Invalid last name with unicode characters set.")

    def test_setLastName_valid_mixed_case(self):
        self.assertTrue(self.user.setLastName("sMitH"), "Valid last name with mixed case failed to be set.")

    def test_setLastName_valid_spaces_before_after(self):
        self.assertTrue(self.user.setLastName("  Smith  "),
                        "Valid last name with spaces before and after failed to be set.")

    def test_setLastName_invalid_only_numbers(self):
        self.assertFalse(self.user.setLastName("1234"), "Last name with only numbers was incorrectly set.")

    def test_setLastName_invalid_long_string(self):
        self.assertFalse(self.user.setLastName("a" * 256), "Last name that is too long was incorrectly set.")

    def test_setLastName_valid_one_letter(self):
        self.assertTrue(self.user.setLastName("S"), "Valid last name with only one letter failed to be set.")

    def test_setLastName_invalid_null(self):
        self.assertFalse(self.user.setLastName(None), "Null last name was incorrectly set.")


class TestSetEmail(unittest.TestCase):
    def setUp(self):
        self.user1 = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                          PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setEmail_valid(self):
        self.assertTrue(self.user1.setEmail("john.smith@yahoo.com"), "Valid email failed to be set.")

    def test_setEmail_invalid_empty_string(self):
        self.assertFalse(self.user1.setEmail(""), "Empty email was incorrectly set.")

    def test_setEmail_invalid_no_at_symbol(self):
        self.assertFalse(self.user1.setEmail("john.smithexample.com"), "Email without @ symbol was incorrectly set.")

    def test_setEmail_invalid_no_domain(self):
        self.assertFalse(self.user1.setEmail("john.smith@"), "Email without domain was incorrectly set.")

    def test_setEmail_invalid_no_username(self):
        self.assertFalse(self.user1.setEmail("@example.com"), "Email without username was incorrectly set.")

    def test_setEmail_invalid_multiple_at_symbols(self):
        self.assertFalse(self.user1.setEmail("john@smith@outlook.com"),
                         "Email with multiple @ symbols was incorrectly set.")

    def test_setEmail_invalid_whitespace(self):
        self.assertFalse(self.user1.setEmail("john.smith @yahoo.com"), "Email with whitespace was incorrectly set.")

    def test_setEmail_invalid_missing_tld(self):
        self.assertFalse(self.user1.setEmail("john.smith@gmail"),
                         "Email with missing top-level domain was incorrectly set.")

    def test_setEmail_invalid_domain_start_with_period(self):
        self.assertFalse(self.user1.setEmail("john.smith@.gmail.com"),
                         "Email with domain starting with a period was incorrectly set.")

    def test_setEmail_invalid_domain_end_with_period(self):
        self.assertFalse(self.user1.setEmail("john.smith@yahoo.com."),
                         "Email with domain ending with a period was incorrectly set.")

    def test_setEmail_invalid_domain_multiple_periods(self):
        self.assertFalse(self.user1.setEmail("john.smith@gmail..com"),
                         "Email with domain containing multiple periods was incorrectly set.")

    def test_setEmail_valid_mixed_case(self):
        self.assertTrue(self.user1.setEmail("JOHN.Smith@yahoo.com"), "Valid email with mixed case failed to be set.")

    def test_setEmail_invalid_unicode(self):
        self.assertFalse(self.user1.setEmail("jane.åström@gmail.com"),
                         "Invalid email with unicode characters set.")

    def test_setEmail_valid_subdomain(self):
        self.assertTrue(self.user1.setEmail("jane.doe@mail.hive.com"),
                        "Valid email with subdomain failed to be set.")

    def test_setEmail_invalid_long_string(self):
        self.assertFalse(self.user1.setEmail("a" * 256 + "@gmail.com"), "Email that is too long was incorrectly set.")

    def test_setEmail_valid_underscore(self):
        self.assertTrue(self.user1.setEmail("john_smith@gmail.com"), "Valid email with underscore failed to be set.")

    def test_setEmail_valid_dash(self):
        self.assertTrue(self.user1.setEmail("john-smith@yahoo.com"), "Valid email with dash failed to be set.")

    def test_setEmail_invalid_null(self):
        self.assertFalse(self.user1.setEmail(None), "Null email was incorrectly set.")


class TestSetPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setPhoneNumber_valid(self):
        self.assertTrue(self.user.setPhoneNumber("555-987-6543"), "Valid phone number failed to be set.")

    def test_setPhoneNumber_invalid_parentheses(self):
        self.assertFalse(self.user.setPhoneNumber("(555)-987-6543"), "Invalid phone number set.")

    def test_setPhoneNumber_valid_no_dash(self):
        self.assertTrue(self.user.setPhoneNumber("5559876543"), "Valid phone number without dashes failed to be set.")

    def test_setPhoneNumber_valid_with_spaces(self):
        self.assertTrue(self.user.setPhoneNumber("555 987 6543"), "Valid phone number with spaces failed to be set.")

    def test_setPhoneNumber_invalid_with_country_code(self):
        self.assertFalse(self.user.setPhoneNumber("+1-555-987-6543"),
                         "Invalid phone number with country code set.")

    def test_setPhoneNumber_invalid_empty_string(self):
        self.assertFalse(self.user.setPhoneNumber(""), "Empty phone number was incorrectly set.")

    def test_setPhoneNumber_invalid_whitespace(self):
        self.assertFalse(self.user.setPhoneNumber("  "), "Phone number with only whitespace was incorrectly set.")

    def test_setPhoneNumber_invalid_too_long(self):
        self.assertFalse(self.user.setPhoneNumber("555-987-6543" * 5),
                         "Phone number that is too long was incorrectly set.")

    def test_setPhoneNumber_invalid_special_characters(self):
        self.assertFalse(self.user.setPhoneNumber("555!987$6543"),
                         "Phone number with special characters was incorrectly set.")

    def test_setPhoneNumber_invalid_letters(self):
        self.assertFalse(self.user.setPhoneNumber("555-abc-efgh"), "Phone number with letters was incorrectly set.")

    def test_setPhoneNumber_invalid_combination(self):
        self.assertFalse(self.user.setPhoneNumber("555-abc-1234"),
                         "Phone number with invalid combination was incorrectly set.")

    def test_setPhoneNumber_invalid_long_string(self):
        self.assertFalse(self.user.setPhoneNumber("1" * 21), "Phone number that is too long was incorrectly set.")

    def test_setPhoneNumber_invalid_missing_digits_1(self):
        self.assertFalse(self.user.setPhoneNumber("55-987-6543"),
                         "Phone number with missing digits was incorrectly set.")

    def test_setPhoneNumber_invalid_missing_digits_2(self):
        self.assertFalse(self.user.setPhoneNumber("555-98-6543"),
                         "Phone number with missing digits was incorrectly set.")

    def test_setPhoneNumber_invalid_missing_digits_3(self):
        self.assertFalse(self.user.setPhoneNumber("555-987-643"),
                         "Phone number with missing digits was incorrectly set.")

    def test_setPhoneNumber_invalid_extra_digits_1(self):
        self.assertFalse(self.user.setPhoneNumber("5555-987-6543"),
                         "Phone number with extra digits was incorrectly set.")

    def test_setPhoneNumber_invalid_extra_digits_2(self):
        self.assertFalse(self.user.setPhoneNumber("555-9877-6543"),
                         "Phone number with extra digits was incorrectly set.")

    def test_setPhoneNumber_invalid_extra_digits_3(self):
        self.assertFalse(self.user.setPhoneNumber("555-987-65433"),
                         "Phone number with extra digits was incorrectly set.")

    def test_setPhoneNumber_invalid_null(self):
        self.assertFalse(self.user.setPhoneNumber(None), "Null phone number was incorrectly set.")


class TestSetAddress(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setAddress_valid(self):
        self.assertTrue(self.user.setAddress("5678 Oak St"), "Valid address failed to be set.")

    def test_setAddress_valid_with_numbers(self):
        self.assertTrue(self.user.setAddress("1234 Elm St, Apt 56"), "Valid address with numbers failed to be set.")

    def test_setAddress_valid_with_commas(self):
        self.assertTrue(self.user.setAddress("1234 Elm St, Suite 100"), "Valid address with commas failed to be set.")

    def test_setAddress_valid_with_special_characters(self):
        self.assertTrue(self.user.setAddress("1234 Elm St, #2B"),
                        "Valid address with special characters failed to be set.")

    def test_setAddress_valid_with_long_street_name(self):
        self.assertTrue(self.user.setAddress("1234 This Is A Very Long Street Name St"),
                        "Valid address with long street name failed to be set.")

    def test_setAddress_invalid_empty_string(self):
        self.assertFalse(self.user.setAddress(""), "Empty address was incorrectly set.")

    def test_setAddress_invalid_whitespace(self):
        self.assertFalse(self.user.setAddress("    "), "Address with only whitespace was incorrectly set.")

    def test_setAddress_invalid_only_special_characters(self):
        self.assertFalse(self.user.setAddress("@#$%^&*"), "Address with only special characters was incorrectly set.")

    def test_setAddress_invalid_long_string(self):
        self.assertFalse(self.user.setAddress("a" * 256), "Address that is too long was incorrectly set.")

    def test_setAddress_valid_mixed_case(self):
        self.assertTrue(self.user.setAddress("1234 eLM St"), "Valid address with mixed case failed to be set.")

    def test_setAddress_valid_spaces_before_after(self):
        self.assertTrue(self.user.setAddress("  1234 Elm St  "),
                        "Valid address with spaces before and after failed to be set.")

    def test_setAddress_invalid_unicode(self):
        self.assertFalse(self.user.setAddress("1234 Åvägen"), "Invalid address with unicode characters set.")

    def test_setAddress_valid_with_dash(self):
        self.assertTrue(self.user.setAddress("1234-1236 Elm St"), "Valid address with dash failed to be set.")

    def test_setAddress_valid_with_multiple_lines(self):
        self.assertTrue(self.user.setAddress("1234 Elm St\nApt 9"),
                        "Valid address with multiple lines failed to be set.")

    def test_setAddress_valid_with_po_box(self):
        self.assertTrue(self.user.setAddress("PO Box 123"), "Valid address with PO box failed to be set.")

    def test_setAddress_invalid_null(self):
        self.assertFalse(self.user.setAddress(None), "Null address was incorrectly set.")


class TestSetBirthDate(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30))

    def test_setBirthDate_valid(self):
        self.assertTrue(self.user.setBirthDate(datetime.date(2000, 1, 1)), "Failed to set valid birth date")

    def test_setBirthDate_valid_leap_year(self):
        self.assertTrue(self.user.setBirthDate(datetime.date(2000, 2, 29)),
                        "Failed to set valid birth date on leap year")

    def test_setBirthDate_invalid_leap_year(self):
        with self.assertRaises(ValueError):
            self.user.setBirthDate(datetime.date(1900, 2, 29))
            self.fail("Allowed setting day out of range for a non-leapyear")

    def test_setBirthDate_valid_first_day_of_year(self):
        self.assertTrue(self.user.setBirthDate(datetime.date(2000, 1, 1)),
                        "Failed to set valid birth date on the first day of year")

    def test_setBirthDate_valid_last_day_of_year(self):
        self.assertTrue(self.user.setBirthDate(datetime.date(2000, 12, 31)),
                        "Failed to set valid birth date on the last day of year")

    def test_setBirthDate_valid_min_date(self):
        self.assertTrue(self.user.setBirthDate(datetime.date(1, 1, 1)),
                        "Failed to set valid birth date on the minimum date value")

    def test_setBirthDate_invalid_future_date(self):
        future_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertFalse(self.user.setBirthDate(future_date), "Set birth date on future date")

    def test_setBirthDate_invalid_null_date(self):
        self.assertFalse(self.user.setBirthDate(None), "Set birth date to null value")

    def test_setBirthDate_invalid_negative_year(self):
        with self.assertRaises(ValueError):
            self.user.setBirthDate(datetime.date(-1, 1, 1))
            self.fail("Allowed setting birth date with negative year")

    def test_setBirthDate_invalid_month_out_of_range(self):
        with self.assertRaises(ValueError):
            self.user.setBirthDate(datetime.date(2000, 13, 1))
            self.fail("Allowed setting birth date with month out of range")

    def test_setBirthDate_invalid_day_out_of_range(self):
        with self.assertRaises(ValueError):
            self.user.setBirthDate(datetime.date(2000, 1, 32))
            self.fail("Allowed setting birth date with day out of range")

    def test_setBirthDate_invalid_date_string(self):
        self.assertFalse(self.user.setBirthDate("1995-08-30"), "Set birth date with invalid string format")

    def test_setBirthDate_invalid_null(self):
        self.assertFalse(self.user.setBirthDate(None), "Set birth date to null value")
    # MAKE SURE TO FIX NAMES


class TestSetSkills(unittest.TestCase):
    def setUp(self):
        self.user = User(ROLE='TA', FIRST_NAME='Jane', LAST_NAME='Doe', EMAIL='jane.doe@example.com',
                         PHONE_NUMBER='555-123-4567', ADDRESS='1234 Elm St', BIRTH_DATE=datetime.date(1995, 8, 30),
                         SKILLS='Management')

    def test_setSkills_valid(self):
        self.assertTrue(self.user.setSkills("Java, Python, Django "), "Valid skills failed to be set.")

    def test_setSkills_valid_singular(self):
        self.assertTrue(self.user.setSkills("Java"), "Singular skill failed to be set.")

    def test_setSkills_valid_uppercase(self):
        self.assertTrue(self.user.setSkills("SQL, MANAGEMENT"), "Valid uppercase skills failed to be set.")

    def test_setSkills_valid_lowercase(self):
        self.assertTrue(self.user.setSkills("sql, java"), "Valid lowercase skills failed to be set.")

    def test_setSkills_valid_with_apostrophe(self):
        self.assertTrue(self.user.setSkills("Bash's Command Line Interface, C"), "Valid skills with apostrophe failed "
                                                                                 "to be set.")

    def test_setSkills_valid_combination(self):
        self.assertTrue(self.user.setSkills("HTML5, CSS"), "Skills with numbers and letters failed to be set.")

    def test_setSkills_valid_one_letter(self):
        self.assertTrue(self.user.setSkills("C"), "Valid skill with only one letter failed to be set.")

    def test_setSkills_valid_null(self):
        self.assertTrue(self.user.setSkills(None), "Null skills failed to be set.")

    def test_setSkills_valid_empty_string(self):
        self.assertTrue(self.user.setSkills(""), "Empty skills failed to be set.")

    def test_setSkills_valid_mixed_case(self):
        self.assertTrue(self.user.setSkills("JavaScriPT, MatLAb"), "Valid skills with mixed case failed to be set.")

    def test_setSkills_invalid_whitespace(self):
        self.assertTrue(self.user.setSkills("   "), "Skills with only whitespace was incorrectly set.")

    def test_setSkills_invalid_special_characters(self):
        self.assertFalse(self.user.setSkills("#$%@"), "Skills with special characters was incorrectly set.")

    def test_setSkills_invalid_only_numbers(self):
        self.assertFalse(self.user.setSkills("1234"), "Skills with only numbers was incorrectly set.")

    def test_setSkills_invalid_unicode(self):
        self.assertFalse(self.user.setSkills("JÅvÅ, Pythön"), "Invalid skills with unicode characters set.")

    def test_setSkills_valid_spaces_before_after(self):
        self.assertTrue(self.user.setSkills("  HTML,      CSS,    Javascript  "),
                        "Valid skills with spaces before and after failed to be set.")

    def test_setSkills_invalid_long_string(self):
        self.assertFalse(self.user.setSkills("a" * 256), "Skill that is too long was incorrectly set.")

    def test_setSkills_invalid_only_commas(self):
        self.assertFalse(self.user.setSkills(",,,,,,,,,,"), "Skill with only was incorrectly set.")
