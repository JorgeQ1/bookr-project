# exec(open('script.py').read())

# from reviews.models import BookContributor, Book, Contributor, Publisher
# from datetime import date

# publishers = [
#     Publisher.objects.get(name="New Town Publisher"),
#     Publisher.objects.get(name="Byron Bay Press"),
# ]
# publishers[0].website = "www.newsouthwalespublisher.com"
# publishers[1].website = "www.newsouthwalespublisher.com"

# Publisher.objects.bulk_update(publishers, ["website"])


# Publisher.objects.bulk_create(
#     [
#         Publisher(
#             name="New Town Publisher",
#             website="www.newtownexample.com",
#             email="newtow@email.com",
#         ),
#         Publisher(
#             name="Byron Bay Press",
#             website="www.byronbayexample.com",
#             email="byronbayexample@email.com",
#         ),
#         Publisher(
#             name="Katoomba Publisher",
#             website="www.katoombaexample.com",
#             email="katoombaexample@email.com",
#         ),
#     ]
# )


# Contributor.objects.get(last_names='Wharton').delete()
# Contributor.objects.filter(last_names='Tyrrell').update(first_names='Mike')

# Contributor.objects.create(
#     first_names="Peter", last_names="Wharton", email="PeterWharton@example.com"
# )

# Contributor.objects.create(
#     first_names="Peter", last_names="Tyrrell", email="PeterTyrrell@example.com"
# )


# publisher = Publisher.objects.get(id=3)
# print(publisher)

# publisher = Publisher.objects.create(
#     name="Pocket Books",
#     website="https://pocketbookssampleurl.com",
#     email="pocketbook@example.com",
# )

# contributor1 = Contributor.objects.create(
#     first_names="Stephen", last_names="Stephen", email="StephenKing@example.com"
# )

# contributor2 = Contributor.objects.create(
#     first_names="Peter", last_names="Straub", email="PeterStraub@example.com"
# )

# book = Book.objects.create(
#     title="The Talisman",
#     publication_date=date(2012, 9, 25),
#     isbn="9781451697216",
#     publisher=publisher,
# )

# book.contributors.set([contributor1, contributor2], through_defaults={'role': 'CO_AUTHOR'})


# publisher = Publisher(
#     name="Packt Publishing",
#     website="https://www.packtpub.com",
#     email="info@packtpub.com",
# )

# publisher.email = 'info@packtpub.com'
# publisher.email = 'customersupport@packtpub.com'
# publisher.save()

# 

# from reviews.models import Contributor

# contributor = Contributor.objects.create(
#     first_names="Rowel", last_names="Atienza", email="RowelAtienza@example.com"
# )

# from reviews.models import Book, Publisher
# from datetime import date

# publisher =  Publisher.objects.get(name='Packt Publishing')
# book = Book.objects.create(
#     title="Advanced Deep Learning with Keras",
#     publication_date=date(2018, 10, 31),
#     isbn="9781788629416",
#     publisher=publisher,
# )


# contributor = Contributor.objects.get(first_names='Rowel')
# contributor = Contributor.objects.create(
#     first_names="Packt", last_names="Example Editor", email="PacktEditor@example.com"
# )

# book = Book.objects.get(title="Advanced Deep Learning with Keras")
# book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})

# book.contributors.create(
#     first_names="Packtp",
#     last_names="Editor Example",
#     email="PacktEditor2@example.com",
#     through_defaults={"role": "EDITOR"},
# )

# book_contributor = BookContributor(book=book, contributor=contributor, role='AUTHOR')
# book_contributor.save()
