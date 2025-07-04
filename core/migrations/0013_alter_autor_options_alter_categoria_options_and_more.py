# Generated by Django 5.2 on 2025-06-03 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_dnome_editora_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nome'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['descricao'], 'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='editora',
            options={'ordering': ['nome'], 'verbose_name': 'Editora', 'verbose_name_plural': 'Editoras'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'ordering': ['titulo'], 'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterUniqueTogether(
            name='autor',
            unique_together={('nome', 'email')},
        ),
        migrations.AlterUniqueTogether(
            name='livro',
            unique_together={('titulo', 'isbn')},
        ),
    ]
