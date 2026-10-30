# `CUINamedImageDescription`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 34 instance methods, 0 class methods

## Instance variables

```
d _scale;
q _idiom;
q _subtype;
q _sizeClassHorizontal;
q _sizeClassVertical;
q _displayGamut;
q _layoutDirection;
i _blendMode;
q _templateRenderingMode;
q _imageType;
{?="top"d"left"d"bottom"d"right"d} _edgeInsets;
{?="top"d"left"d"bottom"d"right"d} _alignmentEdgeInsets;
q _resizingMode;
i _exifOrientation;
@"NSString" _appearanceName;
```

## Properties

```
@property (Td,N,V_scale) scale;
@property (Tq,N,V_idiom) idiom;
@property (Tq,N,V_subtype) subtype;
@property (Tq,N,V_sizeClassHorizontal) sizeClassHorizontal;
@property (Tq,N,V_sizeClassVertical) sizeClassVertical;
@property (Ti,N,V_blendMode) blendMode;
@property (TB,N) isTemplate;
@property (Tq,N,V_templateRenderingMode) templateRenderingMode;
@property (Tq,N,V_imageType) imageType;
@property (T{?=dddd},N,V_edgeInsets) edgeInsets;
@property (T{?=dddd},N,V_alignmentEdgeInsets) alignmentEdgeInsets;
@property (Tq,N,V_resizingMode) resizingMode;
@property (Ti,N,V_exifOrientation) exifOrientation;
@property (Tq,N,V_displayGamut) displayGamut;
@property (Tq,N,V_layoutDirection) layoutDirection;
@property (T@"NSString",C,N,V_appearanceName) appearanceName;
```

## Instance methods

```
-[CUINamedImageDescription setSubtype:];
-[CUINamedImageDescription subtype];
-[CUINamedImageDescription displayGamut];
-[CUINamedImageDescription appearanceName];
-[CUINamedImageDescription setResizingMode:];
-[CUINamedImageDescription imageType];
-[CUINamedImageDescription setDisplayGamut:];
-[CUINamedImageDescription exifOrientation];
-[CUINamedImageDescription setImageType:];
-[CUINamedImageDescription setIdiom:];
-[CUINamedImageDescription setAppearanceName:];
-[CUINamedImageDescription setLayoutDirection:];
-[CUINamedImageDescription dealloc];
-[CUINamedImageDescription setEdgeInsets:];
-[CUINamedImageDescription layoutDirection];
-[CUINamedImageDescription sizeClassHorizontal];
-[CUINamedImageDescription setTemplateRenderingMode:];
-[CUINamedImageDescription setScale:];
-[CUINamedImageDescription setAlignmentEdgeInsets:];
-[CUINamedImageDescription setSizeClassVertical:];
-[CUINamedImageDescription setSizeClassHorizontal:];
-[CUINamedImageDescription scale];
-[CUINamedImageDescription sizeClassVertical];
-[CUINamedImageDescription templateRenderingMode];
-[CUINamedImageDescription description];
-[CUINamedImageDescription edgeInsets];
-[CUINamedImageDescription setExifOrientation:];
-[CUINamedImageDescription resizingMode];
-[CUINamedImageDescription setIsTemplate:];
-[CUINamedImageDescription alignmentEdgeInsets];
-[CUINamedImageDescription blendMode];
-[CUINamedImageDescription setBlendMode:];
-[CUINamedImageDescription isTemplate];
-[CUINamedImageDescription idiom];
```
