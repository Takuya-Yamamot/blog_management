from django.db import models
from django.forms import ModelForm


class Client(models.Model):
    name = models.CharField(max_length=100)
    task_taker = models.CharField(max_length=50)
    client_industry = models.CharField(max_length=50)
    client_rank = models.CharField(max_length=10)
    old_plan_url = models.CharField(max_length=100, blank=True)
    output_num = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""


class Breif(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    client = models.ForeignKey("Client", on_delete=models.CASCADE, null=True)
    concept_overview = models.CharField(max_length=1000)
    concept_key = models.CharField(max_length=1000)
    contents_aim = models.CharField(max_length=1000)
    conflict_company = models.CharField(max_length=1000)
    main_terget = models.CharField(max_length=1000)
    concept_background = models.CharField(max_length=1000)
    suitable_communication = models.CharField(max_length=1000)
    product_feature = models.CharField(max_length=1000)
    key_messages = models.CharField(max_length=1000)
    free_words = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or ""


class PlanOverView(models.Model):
    client_name = models.CharField(max_length=50, blank=True, null=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    breif = models.ForeignKey("Breif", on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    plan_num = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(PlanOverView, self).save(*args, **kwargs)
        planOverView_id = self.id
        client_name = self.client
        if is_new:
            for i in range(self.plan_num):
                plan_data = {
                    "client_name": client_name,
                    "author": self.author,
                    "client_creative_brief": self.breif,
                }
                Plan.objects.create(**plan_data)


class Plan(models.Model):
    client_name = models.CharField(max_length=50)
    author = models.CharField(max_length=1000)
    plan_overview = models.ForeignKey(
        "PlanOverView", on_delete=models.CASCADE, null=True
    )
    client_creative_brief = models.ForeignKey(
        "Breif", on_delete=models.CASCADE
    )
    client_information = models.CharField(max_length=1000)
    points_to_remember = models.CharField(max_length=1000)
    target_reader = models.CharField(max_length=1000)
    target_issue = models.CharField(max_length=1000)
    why_good_issue = models.CharField(max_length=1000)
    solution_for_issue = models.CharField(max_length=1000)
    why_good_solution = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=1000)
    blog_summary = models.CharField(max_length=1000)
    blog_construct = models.CharField(max_length=1000)
    blog_good_points = models.CharField(max_length=1000)
    blog_title = models.CharField(max_length=1000)
    blog_merit_to_read = models.CharField(max_length=1000)
    blog_biginning = models.CharField(max_length=1000)
    why_good_beginning = models.CharField(max_length=1000)
    free_words_for_writer = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name or ""


class PlanOverViewForm(ModelForm):
    class Meta:
        model = PlanOverView
        exclude = ["client_name"]


class BreifForm(ModelForm):
    class Meta:
        model = Breif
        fields = "__all__"
