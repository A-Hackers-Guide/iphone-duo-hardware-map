# `CUIThemeRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 9 properties, 101 instance methods, 2 class methods

## Instance variables

```
[22{_renditionkeytoken="identifier"S"value"S}] _stackKey;
^{_renditionkeytoken=SS} _key;
q _type;
I _subtype;
I _scale;
i _exifOrientation;
i _blendMode;
{cuithemerenditionrenditionflags="isVectorBased"b1"isOpaque"b1"bitmapEncoding"b4"optOutOfThinning"b1"isFlippable"b1"isTintable"b1"preservedVectorRepresentation"b1"preserveForArchiveOnly"b1"reserved"b21} _renditionFlags;
q _templateRenderingMode;
Q _colorSpaceID;
@"NSString" _name;
@"NSData" _srcData;
d _opacity;
@"NSString" _utiType;
^{CGImage=} _uncroppedImage;
{CGSize="width"d"height"d} _physicalSizeInMeters;
@"NSDictionary" _properties;
S _sourceObjectVersion;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (TI,N,V_subtype) subtype;
@property (TI,N,V_scale) internalScale;
@property (Tq,N,V_templateRenderingMode) internalTemplateRenderingMode;
@property (T@"NSString",&,N) internalName;
@property (T@"NSData",R,N,V_srcData) srcData;
@property (Td,N,V_opacity) opacity;
@property (Ti,N,V_blendMode) blendMode;
@property (Ti,N,V_exifOrientation) exifOrientation;
```

## Class methods

```
+[CUIThemeRendition displayNameForRenditionType:];
+[CUIThemeRendition renditionClassForRenditionType:andPixelFormat:];
```

## Instance methods

```
-[CUIThemeRendition setSubtype:];
-[CUIThemeRendition gradient];
-[CUIThemeRendition subtype];
-[CUIThemeRendition colorSpaceID];
-[CUIThemeRendition properties];
-[CUIThemeRendition isScaled];
-[CUIThemeRendition svgDocument];
-[CUIThemeRendition isTiled];
-[CUIThemeRendition unslicedImage];
-[CUIThemeRendition vectorGlyphCapLine];
-[CUIThemeRendition exifOrientation];
-[CUIThemeRendition edgesOnly];
-[CUIThemeRendition data];
-[CUIThemeRendition dealloc];
-[CUIThemeRendition systemColorName];
-[CUIThemeRendition transformation];
-[CUIThemeRendition _initalizeMetadataFromCSIData:version:];
-[CUIThemeRendition isOpaque];
-[CUIThemeRendition pdfDocument];
-[CUIThemeRendition sliceInformation];
-[CUIThemeRendition linkingToRendition];
-[CUIThemeRendition opacity];
-[CUIThemeRendition cgColor];
-[CUIThemeRendition _sourceRendition];
-[CUIThemeRendition vectorGlyphRenderingMode];
-[CUIThemeRendition vectorGlyphReferencePointSize];
-[CUIThemeRendition vectorGlyphAvailableSizes];
-[CUIThemeRendition provideTextureInfo];
-[CUIThemeRendition setOpacity:];
-[CUIThemeRendition utiType];
-[CUIThemeRendition scale];
-[CUIThemeRendition _setStructuredThemeStore:];
-[CUIThemeRendition setType:];
-[CUIThemeRendition isInternalLink];
-[CUIThemeRendition bitmapEncoding];
-[CUIThemeRendition type];
-[CUIThemeRendition imageForSliceIndex:];
-[CUIThemeRendition mipLevels];
-[CUIThemeRendition templateRenderingMode];
-[CUIThemeRendition createImageFromPDFRenditionWithScale:];
-[CUIThemeRendition contentNames];
-[CUIThemeRendition alphaCroppedRect];
-[CUIThemeRendition isInterpolatable];
-[CUIThemeRendition originalUncroppedSize];
-[CUIThemeRendition description];
-[CUIThemeRendition vectorGlyphTemplateVersion];
-[CUIThemeRendition setName:];
-[CUIThemeRendition vectorGlyphAlignmentRectInsets];
-[CUIThemeRendition setExifOrientation:];
-[CUIThemeRendition unslicedSize];
-[CUIThemeRendition pixelFormat];
-[CUIThemeRendition _destinationFrame];
-[CUIThemeRendition sizeIndexes];
-[CUIThemeRendition layerReferences];
-[CUIThemeRendition _initWithCSIHeader:version:];
-[CUIThemeRendition metrics];
-[CUIThemeRendition externalTags];
-[CUIThemeRendition maskForSliceIndex:];
-[CUIThemeRendition blendMode];
-[CUIThemeRendition vectorGlyphBaseline];
-[CUIThemeRendition textureIntepretation];
-[CUIThemeRendition name];
-[CUIThemeRendition internalName];
-[CUIThemeRendition setBlendMode:];
-[CUIThemeRendition key];
-[CUIThemeRendition sourceRowbytes];
-[CUIThemeRendition initWithCSIData:forKey:version:];
-[CUIThemeRendition substituteWithSystemColor];
-[CUIThemeRendition objectVersion];
-[CUIThemeRendition isFlippable];
-[CUIThemeRendition preservedVectorRepresentation];
-[CUIThemeRendition srcData];
-[CUIThemeRendition _initWithCSIData:forKey:version:];
-[CUIThemeRendition _initializeCompositingOptionsFromCSIData:version:];
-[CUIThemeRendition _initializePropertiesFromCSIData:version:];
-[CUIThemeRendition _initializeRenditionKey:];
-[CUIThemeRendition _initializeTypeIdentifiersWithLayout:];
-[CUIThemeRendition _setFlippable:];
-[CUIThemeRendition assetPackIdentifier];
-[CUIThemeRendition csiTextStyle];
-[CUIThemeRendition effectPreset];
-[CUIThemeRendition gradientDrawingAngle];
-[CUIThemeRendition gradientStyle];
-[CUIThemeRendition internalScale];
-[CUIThemeRendition internalTemplateRenderingMode];
-[CUIThemeRendition isTintable];
-[CUIThemeRendition isVectorBased];
-[CUIThemeRendition modelAsset];
-[CUIThemeRendition modelMesh];
-[CUIThemeRendition modelSubmesh];
-[CUIThemeRendition optOutOfThinning];
-[CUIThemeRendition physicalSizeInMeters];
-[CUIThemeRendition preserveForArchiveOnly];
-[CUIThemeRendition renditionFlags];
-[CUIThemeRendition setInternalName:];
-[CUIThemeRendition setInternalScale:];
-[CUIThemeRendition setInternalTemplateRenderingMode:];
-[CUIThemeRendition sourceObjectVersion];
-[CUIThemeRendition textureImages];
-[CUIThemeRendition uncroppedImage];
-[CUIThemeRendition valueForTokenIdentifier:];
```
