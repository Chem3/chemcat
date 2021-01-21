from django import forms
from blog.models import StorageUpdate
from .models import Bottles
from .models import Shelves
from .models import Chemicals
import pubchempy as pcp
import chemicals as chem


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


class ChemicalForm(forms.ModelForm):

    def save(self, commit=True):
        return super(ChemicalForm, self).save(commit=commit)

    def clean(self):
        iupac_name = self.cleaned_data.get('iupac_name')
        trivial_name = self.cleaned_data.get('trivial_name')
        cas_number = self.cleaned_data.get('cas')
        override = self.cleaned_data.get('override_iupac')

        if not(override) or not override:
            cids = pcp.get_cids(iupac_name, 'name')
            if not cids:
                raise forms.ValidationError("No PubChem match on suggested iupac name. "
                                            "Are you sure this is a chemical? "
                                            "If so, check CAS, trivial name, "
                                            "molecular formula and then use override below. "
                                            "An email will be sent to notify admin.")
            out = ""
            for cid in cids:
                out = out + pcp.Compound.from_cid(cid).iupac_name + ", "
            cmp = pcp.Compound.from_cid(cids[0])
            if not cmp.synonyms:
                trivial = ""
            else:
                trivial = cmp.synonyms[0]
            try:
                cas = chem.CAS_from_any(iupac_name)
            except ValueError:
                cas = "Non found"
            formula = cmp.isomeric_smiles

            if pcp.Compound.from_cid(cids[0]).iupac_name.lower() != iupac_name.lower():
                raise forms.ValidationError("Iupac Name is not registered in Pubchem, try: "
                                            + out + ", suggested trivial name " + trivial
                                            + ", cas "+ cas
                                            + ", suggested formula (SMILES) " + formula)

        return self.cleaned_data

    class Meta:
        model = Chemicals
        fields = ['iupac_name', 'override_iupac', 'trivial_name', 'cas', 'formula', 'property']