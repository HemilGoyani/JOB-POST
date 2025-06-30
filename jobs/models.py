from django.db import models
from users.models import User
# Create your models here.

class jobs(models.Model):

    RANGE_1_25 = "1-25"
    RANGE_26_50 = "26-50"
    RANGE_51_75 = "51-75"
    RANGE_76_100 = "76-100"

    RATIO_CHOICES = (
        (RANGE_1_25, "1 - 25"),
        (RANGE_26_50, "26 - 50"),
        (RANGE_51_75, "51 - 75"),
        (RANGE_76_100, "76 - 100"),
    )

    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_post_ratio = models.CharField(
        choices=RATIO_CHOICES,
        max_length=10,
        db_index=True,
        default=RANGE_1_25
    )

    def __str__(self):
        return self.job_title


class UserProposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proposals")
    job = models.ForeignKey(jobs, on_delete=models.CASCADE, related_name="proposals")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposal by {self.user.email} for {self.job.job_title}"

