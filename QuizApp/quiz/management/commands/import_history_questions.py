import csv
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Import quiz questions from a CSV file into the database'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\91975\Documents\Quize-Project\QuizApp\quiz\utils\indian_history.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            for row in csv_reader:
                # text, option_a, option_b, option_c, option_d, correct_option = row
                text = row[0]
                subject = "History"
                option_a = row[1]
                option_b = row[2]
                option_c = row[3]
                option_d = row[4]
                correct_option = row[5]
                # Create a new Question object for each row in the CSV
                Question.objects.create(
                    text=text,
                    subject=subject,
                    option_a=option_a,
                    option_b=option_b,
                    option_c=option_c,
                    option_d=option_d,
                    correct_option=correct_option
                )
                
            self.stdout.write(self.style.SUCCESS('Successfully imported quiz questions of Indian History Subject'))
