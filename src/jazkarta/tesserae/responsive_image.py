from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.tiles import PersistentTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.component import queryMultiAdapter
from . import _


class IResponsiveImageTile(model.Schema):

    image = NamedBlobImage(
        title=_(u'Upload an image to use for desktop and tablet widths'),
        required=False,
    )

    mobile_image = NamedBlobImage(
        title=_(u'Upload an image to use for mobile widths'),
        required=False,
    )

    scale = schema.Choice(
        title=_(u'Select maximum display size'),
        description=_(u'Leave unset for original image size'),
        vocabulary='plone.app.vocabularies.ImagesScales',
        default='large',
        required=False,
    )

    alt_text = schema.Text(
        title=_(u'Image Alt Text'),
        description=_(u'Enter a description of the image for screen readers, etc.'),
        default=u' ',
        required=True,
    )


class ResponsiveImageTile(PersistentTile):

    template = ViewPageTemplateFile('templates/responsive_image.pt')

    @property
    def alt_text(self):
        return self.data.get('alt_text', u'').replace(u'"', u'\\"')

    def image_url(self, fname='image'):
        scale_name = self.data.get('scale', 'banner')
        images_view = queryMultiAdapter((self, self.context.REQUEST),
                                        name=u'images')
        if images_view is not None:
            try:
                scale = images_view.scale(fieldname=fname, scale=scale_name)
            except AttributeError:
                return None
            if scale is not None:
                return scale.url
