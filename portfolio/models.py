# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from photologue.models import Gallery, GalleryUpload, Photo

 
class Portfolio(models.Model):
    class Meta:
        db_table = 'portfolio'
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')
    
    titulo              = models.CharField("Titulo do Portfolio",max_length=255,
                              help_text=u'Titulo do Portfolio',default='Hitallo e Elan')    
    imagem              = models.ImageField(upload_to='imagem_portfolio/', blank=False, help_text=u'Imagem representativa')
    descricao           = models.CharField("Descricao do Portfolio",max_length=255,
                              help_text=u'Descricao do Portfolio',default='Lorem ipsum dolor sit amet! Lorem ipsum dolor sit amet!')
    ordem               = models.IntegerField(default=0, blank=True)
    slug                = models.SlugField(unique=True)             
    meta_keywords       = models.CharField('Palavras Chaves usadas no Google',max_length=255, 
                                            help_text=u'portfolio sonorah artista equipe',default='Lorem ipsum dolor sit amet! Lorem ipsum dolor sit amet!')
    meta_description    = models.CharField('Descricao do site usado no Google',max_length=255, 
                                            help_text=u'Produção de carreiras musicais, vencedoras em varios estilos',default='Lorem ipsum dolor sit amet! Lorem ipsum dolor sit amet!')
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    
    #teste = models.ForeignKey('self')
    
    def __unicode__(self):
        return self.titulo
    
    # def get_absolute_url(self):
    #     return reverse('noticias', kwargs={'noticia_slug': self.pk})
    def get_absolute_url(self):
        return reverse('portfolio', kwargs={'portfolio_slug': self.slug})
#    def get_absolute_url(self):
#        return (u'noticias', (), { u'noticia_slug': self.slug })


class Galeria(models.Model):
    galeria             = models.ForeignKey(Gallery)
    portfolios          = models.ForeignKey(Portfolio)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    position            = models.PositiveSmallIntegerField("Position")
    #ordem               = models.IntegerField(default=0, blank=True)
    tipo                = models.CharField(max_length=1,default='G')
    
    def __unicode__(self):
        return self.galeria.title
    
    class Meta:
        ordering = ['position']

class Foto(models.Model):
    foto                = models.ForeignKey(Photo)
    portfolios          = models.ForeignKey(Portfolio)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    position            = models.PositiveSmallIntegerField("Position")
    #ordem               = models.IntegerField(default=0, blank=True)
    tipo                = models.CharField(max_length=1,default='F')
    
    def __unicode__(self):
        return self.foto.title
    
    class Meta:
        ordering = ['position']
    
class Site(models.Model):
    url_site            = models.URLField(u"Endereço na web",max_length=255,
                              help_text=u'http://sitedoportfolio.com', blank=True)
    portfolios          = models.ForeignKey(Portfolio)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    position            = models.PositiveSmallIntegerField("Position")
    #ordem               = models.IntegerField(default=0, blank=True)
    tipo                = models.CharField(max_length=1,default='S')
    
    def __unicode__(self):
        return self.url_site
    
    class Meta:
        ordering = ['position']
    
class Video(models.Model):
    url_video           = models.URLField(u"Link YouTube",max_length=255,
                              help_text=u'http://www.youtube.com/watch?v=65B6qyz6IQ4', blank=True)
    portfolios          = models.ForeignKey(Portfolio)
    criado_em           = models.DateTimeField(auto_now_add=True)
    atualizado_em       = models.DateTimeField(auto_now=True)
    position            = models.PositiveSmallIntegerField("Position")
    tipo                = models.CharField(max_length=1,default='V')
    
    def __unicode__(self):
        return self.url_video

    class Meta:
        ordering = ['position']

