from django import forms
from blog.models import StorageUpdate
from .models import Bottles
from .models import Shelves


class StorageUpdateForm(forms.ModelForm):

    def save(self, commit=True):
        updates = self.cleaned_data.get('entry_content', None)
        update_split = updates.splitlines()

        for entry in update_split:
            if 'cat' in entry.lower():
                bottle_queries = Bottles.objects.filter(barcode__iexact=entry)
                for bottle in bottle_queries:
                    bottle.shelf = current_shelf
                    bottle.registered_date = self.cleaned_data.get('entry_date', None);
                    bottle.save()
            else:
                shelf_queries = Shelves.objects.filter(shortname__iexact=entry)
                for shelf in shelf_queries:
                    current_shelf = shelf

        return super(StorageUpdateForm, self).save(commit=commit)

    class Meta:
        model = StorageUpdate
        fields = ['entry_date', 'entry_content', 'entry_author']
