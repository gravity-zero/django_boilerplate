from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),  
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userID',
            field=models.ForeignKey(to="auth.User", on_delete=models.CASCADE), 
        ),
    ]
