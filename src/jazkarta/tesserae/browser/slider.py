import json
from Products.Five import BrowserView
from plone.directives import form
from plone.app.standardtiles.existingcontent import uuidToCatalogBrainUnrestricted
from ..slider import ISliderConfig
from .. import _


class SliderView(BrowserView):
    """Folder view for slider images"""
    height = None
    slider_config = ''

    def listing(self):
        config = ISliderConfig(self.context, alternate=None)
        if config:
            self.height = config.height
            slider_config = {
                'interval': config.interval,
                'wrap': config.wrap,
                'pause': "hover" if config.pause else False,
            }
            self.slider_config = json.dumps(slider_config)

        content = self.context.listFolderContents()
        items = []
        for obj in content:
            item = {}
            if getattr(obj, 'link', None) or getattr(obj, 'content', None):
                if obj.link:
                    item['url'] = obj.link
                else:
                    brain = uuidToCatalogBrainUnrestricted(obj.content)
                    if brain:
                        item['url'] = brain.getURL()

            elif getattr(obj, 'getRemoteUrl', None):
                item['url'] = obj.getRemoteUrl()
            else:
                item['url'] = obj.absolute_url()
            item['title'] = obj.title
            item['description'] = obj.description
            images_view = obj.unrestrictedTraverse('@@images')
            scale = images_view.scale(fieldname='image', scale='banner')
            if scale is not None:
                item['image_url'] = scale.url
            items.append(item)
        return items

    def carousel_id(self):
        return 'carousel-' + self.context.getId()


class SliderConfig(form.SchemaEditForm):
    """Edit form for slider configuration"""
    label = _(u"Edit Slider Configuration")
    schema = ISliderConfig
