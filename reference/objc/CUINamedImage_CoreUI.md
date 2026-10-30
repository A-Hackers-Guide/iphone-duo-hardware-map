# `CUINamedImage`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 2 instance variables, 20 properties, 30 instance methods, 0 class methods

## Instance variables

```
d _scale;
{_cuiniproperties="isVectorBased"b1"hasSliceInformation"b1"hasAlignmentInformation"b1"resizingMode"b2"templateRenderingMode"b3"exifOrientation"b4"isAlphaCropped"b1"isFlippable"b1"isTintable"b1"preservedVectorRepresentation"b1"_reserved"b16} _imageProperties;
```

## Properties

```
@property (T^{CGImage=},R,N) image;
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N) scale;
@property (Tq,R,N) imageType;
@property (T{?=dddd},R,N) edgeInsets;
@property (Tq,R,N) resizingMode;
@property (Td,R,N) opacity;
@property (T{?=dddd},R,N) alignmentEdgeInsets;
@property (Ti,R,N) blendMode;
@property (TB,R,N) hasSliceInformation;
@property (TB,R,N) hasAlignmentInformation;
@property (TB,R,N) isVectorBased;
@property (TB,R,N) preservedVectorRepresentation;
@property (TB,R,N) isTemplate;
@property (Tq,R,N) templateRenderingMode;
@property (TB,R,N) isStructured;
@property (TB,R,N) isFlippable;
@property (Ti,R,N) exifOrientation;
@property (TB,R,N) isAlphaCropped;
@property (T^{CGImage=},R,N) croppedImage;
```

## Instance methods

```
-[CUINamedImage imageType];
-[CUINamedImage exifOrientation];
-[CUINamedImage baseKey];
-[CUINamedImage opacity];
-[CUINamedImage initWithName:usingRenditionKey:fromTheme:];
-[CUINamedImage size];
-[CUINamedImage scale];
-[CUINamedImage templateRenderingMode];
-[CUINamedImage createImageFromPDFRenditionWithScale:];
-[CUINamedImage alphaCroppedRect];
-[CUINamedImage originalUncroppedSize];
-[CUINamedImage description];
-[CUINamedImage edgeInsets];
-[CUINamedImage positionOfSliceBoundary:];
-[CUINamedImage resizingMode];
-[CUINamedImage image];
-[CUINamedImage alignmentEdgeInsets];
-[CUINamedImage blendMode];
-[CUINamedImage isTemplate];
-[CUINamedImage _setScale:];
-[CUINamedImage hasSliceInformation];
-[CUINamedImage isFlippable];
-[CUINamedImage preservedVectorRepresentation];
-[CUINamedImage isStructured];
-[CUINamedImage _cacheRenditionProperties];
-[CUINamedImage croppedImage];
-[CUINamedImage hasAlignmentInformation];
-[CUINamedImage isAlphaCropped];
-[CUINamedImage isVectorBased];
-[CUINamedImage resizingModeWithSubtype:];
```
