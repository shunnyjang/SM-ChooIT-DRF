# Generated by Django 3.1.7 on 2021-06-13 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210614_0423'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO accounts_nickname
            (part, content) VALUES 
            ('a', '행복한'),
            ('a', '홀가분한'),
            ('a', '사랑스러운'),
            ('a', '즐거운'),
            ('a', '자랑스러운'),
            ('a', '설레는'),
            ('a', '활기찬'),
            ('a', '뿌듯한'),
            ('a', '통쾌한'),
            ('a', '게으른'),
            ('a', '소심한'),
            ('a', '엉뚱한'),
            ('a', '심각한'),
            ('a', '솔직한'),
            ('a', '솔직한'),
            ('a', '느긋한'),
            ('a', '분노한'),
            ('a', '아찔한'),
            ('a', '정신없는'),
            ('a', '혼란스러운');
            INSERT INTO accounts_nickname
            (part, content, emoji) VALUES
            ('n', '딸기', '🍓'),
            ('n', '키위', '🥝'),
            ('n', '포도', '🍇'),
            ('n', '복숭아', '🍑'),
            ('n', '레몬', '🍋'),
            ('n', '아보카도', '🥑'),
            ('n', '사과', '🍏'),
            ('n', '수박', '🍉'),
            ('n', '쿠키', '🍪');
            """
        )
    ]
