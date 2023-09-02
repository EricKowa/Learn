from django.test import TestCase
from django.urls import reverse

# Create your tests here.

import datetime

from django.utils import timezone

from .models import FirstDatabase  

#First Test: checking that the "created_recently" function in the FirstDatabase only is True for entries created in the past

class FirstDatabaseModelTest(TestCase):
    def test_created_recently_with_future_entry_created_date(self):
        """
        created_recently() returns False for entries whose entry_created is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_entry =FirstDatabase(entry_created=time)
        self.assertIs(future_entry.created_recently(), False)

    def test_created_recently_with_entry_created_recently(self):
        """
        created_recently() returns True for entries whose entry_created is within the last two days.
        """
        time = timezone.now() - datetime.timedelta(hours=47, minutes=59, seconds=59)
        recent_entry = FirstDatabase(entry_created = time)
        self.assertIs(recent_entry.created_recently(), True)
    
    def test_created_recently_with_old_entry(self):
        """
        created_recently() returns False for entries with entry_created > 2 days ago.
        """
        time = timezone.now() - datetime.timedelta(days=2, seconds=1)
        old_entry = FirstDatabase(entry_created = time)
        self.assertIs(old_entry.created_recently(), False)


def create_entry(e_name, days):
    """
    Create an entry with the given name and created offset to now by the numbers of days given (negative
      for entries created in the past and positive for entries created in the future).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return FirstDatabase(name=e_name, entry_created=time)

class FirstDatabaseIndexViewTests(TestCase):
    def test_no_entries(self):
        """
        If no entries exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No entries are available.")
        
        self.assertQuerySetEqual(response.context["latest_entries_list"], [])

    def test_past_entry(self):
        """
        Entry with a entry_created in the past are displayed on the
        index page.
        """
        entry = create_entry(e_name="Past entry", days=-30)
        response = self.client.get(reverse("app:index"))
        self.assertQuerySetEqual(response.context["latest_entries_list"],[entry])

    def test_future_entry(self):
        """
        Entries with a entry_created in the future aren't displayed on
        the index page.
        """
        create_entry(e_name="Future Question.", days=30)
        response = self.client.get(reverse("app:index"))
        self.assertContains(response, "No entries are available.")

        self.assertQuerySetEqual(response.context["latest_entries_list"], [])


    def test_future_entry_and_past_entry(self):
        """ Even if both past and future entries exist, only past entries are displayed. """
        entry= create_entry(e_name="Past entry.", days=-30)
        create_entry(e_name="Future entry.", days=30)
        response = self.client.get(reverse("app:index"))
        self.assertQuerySetEqual(
            response.context["latest_entries_list"],
            [entry],
        )

    def test_two_past_entries(self):
        """
        The FirstDatabase index page may display multiple entries.
        """
        entry1 = create_entry(e_name="Past entry 1.", days=-30)
        entry2 = create_entry(e_name="Past entry 2.", days=-5)
        response = self.client.get(reverse("app:index"))
        self.assertQuerySetEqual(
            response.context["latest_entries_list"],
            [entry2, entry1],
        )