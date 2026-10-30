# `CUIEncapsulatedVectorGlyph`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
_glyph;
_imageRect;
_imageCenter;
_encapsulatedAlignmentRect;
_coordinateSystem;
contextTransform;
useASG;
canvasSize;
```

## Properties

```
@property (T@"CUINamedVectorGlyph",N,R) glyph;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) imageRect;
@property (T{CGVector=dd},N,R) imageCenter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) encapsulatedAlignmentRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) imagePixelRect;
@property (T{CGVector=dd},N,R) imagePixelCenter;
@property (Tq,N,R) coordinateSystem;
```

## Instance methods

```
-[CUIEncapsulatedVectorGlyph glyph];
-[CUIEncapsulatedVectorGlyph init];
-[CUIEncapsulatedVectorGlyph imageRect];
-[CUIEncapsulatedVectorGlyph coordinateSystem];
-[CUIEncapsulatedVectorGlyph copyWithZone:];
-[CUIEncapsulatedVectorGlyph imageCenter];
-[CUIEncapsulatedVectorGlyph imageCenterForCoordinateSystem:];
-[CUIEncapsulatedVectorGlyph rasterizeImageUsingRenderBlock:];
-[CUIEncapsulatedVectorGlyph createContextFor:width:height:];
-[CUIEncapsulatedVectorGlyph encapsulatedAlignmentRect];
-[CUIEncapsulatedVectorGlyph encapsulatedAlignmentRectForCoordinateSystem:];
-[CUIEncapsulatedVectorGlyph imagePixelCenter];
-[CUIEncapsulatedVectorGlyph imagePixelCenterForCoordinateSystem:];
-[CUIEncapsulatedVectorGlyph imagePixelRect];
-[CUIEncapsulatedVectorGlyph imagePixelRectForCoordinateSystem:];
-[CUIEncapsulatedVectorGlyph imageRectForCoordinateSystem:];
```
