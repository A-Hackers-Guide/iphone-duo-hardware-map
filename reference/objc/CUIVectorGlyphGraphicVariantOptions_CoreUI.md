# `CUIVectorGlyphGraphicVariantOptions`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 13 instance variables, 13 properties, 33 instance methods, 2 class methods

## Instance variables

```
q shape;
q fill;
@"NSArray" fillColors;
q contentEffect;
@ monochromeForegroundColor;
d roundedRectCornerRadius;
q imageCentering;
q imageScaling;
q imageAlignment;
q shapeEffect;
@ borderColor;
d borderWidth;
{CGSize="width"d"height"d} imageOffset;
```

## Properties

```
@property (Tq,N,Vshape) shape;
@property (Tq,N,Vfill) fill;
@property (T@"NSArray",C,N,VfillColors) fillColors;
@property (Tq,N,VcontentEffect) contentEffect;
@property (T@,&,N,VmonochromeForegroundColor) monochromeForegroundColor;
@property (Td,N,VroundedRectCornerRadius) roundedRectCornerRadius;
@property (Tq,N,VimageCentering) imageCentering;
@property (Tq,N,VimageScaling) imageScaling;
@property (Tq,N,VimageAlignment) imageAlignment;
@property (T{CGSize=dd},N,VimageOffset) imageOffset;
@property (Tq,N,VshapeEffect) shapeEffect;
@property (Td,N,VborderWidth) borderWidth;
@property (T@,&,N,VborderColor) borderColor;
```

## Class methods

```
+[CUIVectorGlyphGraphicVariantOptions automaticOffset];
+[CUIVectorGlyphGraphicVariantOptions defaultSymbolPointSizeRatio];
```

## Instance methods

```
-[CUIVectorGlyphGraphicVariantOptions setShape:];
-[CUIVectorGlyphGraphicVariantOptions setBorderColor:];
-[CUIVectorGlyphGraphicVariantOptions setBorderWidth:];
-[CUIVectorGlyphGraphicVariantOptions shape];
-[CUIVectorGlyphGraphicVariantOptions init];
-[CUIVectorGlyphGraphicVariantOptions dealloc];
-[CUIVectorGlyphGraphicVariantOptions setFillColors:];
-[CUIVectorGlyphGraphicVariantOptions borderWidth];
-[CUIVectorGlyphGraphicVariantOptions hash];
-[CUIVectorGlyphGraphicVariantOptions imageScaling];
-[CUIVectorGlyphGraphicVariantOptions setImageScaling:];
-[CUIVectorGlyphGraphicVariantOptions copyWithZone:];
-[CUIVectorGlyphGraphicVariantOptions isEqual:];
-[CUIVectorGlyphGraphicVariantOptions fillColors];
-[CUIVectorGlyphGraphicVariantOptions borderColor];
-[CUIVectorGlyphGraphicVariantOptions fill];
-[CUIVectorGlyphGraphicVariantOptions imageAlignment];
-[CUIVectorGlyphGraphicVariantOptions setImageAlignment:];
-[CUIVectorGlyphGraphicVariantOptions setImageOffset:];
-[CUIVectorGlyphGraphicVariantOptions imageOffset];
-[CUIVectorGlyphGraphicVariantOptions roundedRectCornerRadius];
-[CUIVectorGlyphGraphicVariantOptions setShapeEffect:];
-[CUIVectorGlyphGraphicVariantOptions _areValid];
-[CUIVectorGlyphGraphicVariantOptions contentEffect];
-[CUIVectorGlyphGraphicVariantOptions imageCentering];
-[CUIVectorGlyphGraphicVariantOptions monochromeForegroundColor];
-[CUIVectorGlyphGraphicVariantOptions prefersAutomaticCentering];
-[CUIVectorGlyphGraphicVariantOptions setContentEffect:];
-[CUIVectorGlyphGraphicVariantOptions setFill:];
-[CUIVectorGlyphGraphicVariantOptions setImageCentering:];
-[CUIVectorGlyphGraphicVariantOptions setMonochromeForegroundColor:];
-[CUIVectorGlyphGraphicVariantOptions setRoundedRectCornerRadius:];
-[CUIVectorGlyphGraphicVariantOptions shapeEffect];
```
