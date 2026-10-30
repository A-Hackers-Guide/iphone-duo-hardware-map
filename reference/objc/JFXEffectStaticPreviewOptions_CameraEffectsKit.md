# `JFXEffectStaticPreviewOptions`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXEffectPreviewOptions`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _dontCacheToDisk;
B _dontCache;
B _dontUseThumbnailAssetWhenAvailable;
@"JTImage" _renderBackgroundImage;
@? _renderPropertiesConfigurationBlock;
{?="value"q"timescale"i"flags"I"epoch"q} _renderTime;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _renderedImageCropRect;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _renderRange;
```

## Properties

```
@property (T@"JTImage",&,N,V_renderBackgroundImage) renderBackgroundImage;
@property (TB,N,V_dontCacheToDisk) dontCacheToDisk;
@property (TB,N,V_dontCache) dontCache;
@property (T{?=qiIq},N,V_renderTime) renderTime;
@property (T{?={?=qiIq}{?=qiIq}},N,V_renderRange) renderRange;
@property (TB,N,V_dontUseThumbnailAssetWhenAvailable) dontUseThumbnailAssetWhenAvailable;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_renderedImageCropRect) renderedImageCropRect;
@property (T@?,C,N,V_renderPropertiesConfigurationBlock) renderPropertiesConfigurationBlock;
```

## Instance methods

```
-[JFXEffectStaticPreviewOptions copyWithZone:];
-[JFXEffectStaticPreviewOptions renderTime];
-[JFXEffectStaticPreviewOptions setRenderTime:];
-[JFXEffectStaticPreviewOptions dontCacheToDisk];
-[JFXEffectStaticPreviewOptions setRenderRange:];
-[JFXEffectStaticPreviewOptions dontCache];
-[JFXEffectStaticPreviewOptions dontUseThumbnailAssetWhenAvailable];
-[JFXEffectStaticPreviewOptions initStaticPreviewOptions];
-[JFXEffectStaticPreviewOptions renderBackgroundImage];
-[JFXEffectStaticPreviewOptions renderPropertiesConfigurationBlock];
-[JFXEffectStaticPreviewOptions renderRange];
-[JFXEffectStaticPreviewOptions renderedImageCropRect];
-[JFXEffectStaticPreviewOptions setDontCache:];
-[JFXEffectStaticPreviewOptions setDontCacheToDisk:];
-[JFXEffectStaticPreviewOptions setDontUseThumbnailAssetWhenAvailable:];
-[JFXEffectStaticPreviewOptions setRenderBackgroundImage:];
-[JFXEffectStaticPreviewOptions setRenderPropertiesConfigurationBlock:];
-[JFXEffectStaticPreviewOptions setRenderedImageCropRect:];
```
