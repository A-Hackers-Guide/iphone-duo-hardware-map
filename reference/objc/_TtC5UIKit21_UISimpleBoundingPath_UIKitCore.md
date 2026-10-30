# `_TtC5UIKit21_UISimpleBoundingPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBoundingPath`
- 15 instance variables, 1 properties, 11 instance methods, 1 class methods

## Instance variables

```
__C.CGRect pathRect;
__C.UIRectCornerRadii cornerRadii;
__C.CGRect intrusionRect;
_$sSS kEncodingKeyPathRectOriginX;
_$sSS kEncodingKeyPathRectOriginY;
_$sSS kEncodingKeyPathRectSizeWidth;
_$sSS kEncodingKeyPathRectSizeHeight;
_$sSS kEncodingKeyCornerRadiiTopLeft;
_$sSS kEncodingKeyCornerRadiiBottomLeft;
_$sSS kEncodingKeyCornerRadiiBottomRight;
_$sSS kEncodingKeyCornerRadiiTopRight;
_$sSS kEncodingKeyIntrusionRectOriginX;
_$sSS kEncodingKeyIntrusionRectOriginY;
_$sSS kEncodingKeyIntrusionRectSizeWidth;
_$sSS kEncodingKeyIntrusionRectSizeHeight;
```

## Properties

```
@property (TB,N,R) isNonRectangular;
```

## Class methods

```
+[_TtC5UIKit21_UISimpleBoundingPath supportsSecureCoding];
```

## Instance methods

```
-[_TtC5UIKit21_UISimpleBoundingPath _rectTuckedInCorner:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_TtC5UIKit21_UISimpleBoundingPath isNonRectangular];
-[_TtC5UIKit21_UISimpleBoundingPath initWithCoordinateSpace:];
-[_TtC5UIKit21_UISimpleBoundingPath validateForCoordinateSpace];
-[_TtC5UIKit21_UISimpleBoundingPath encodeWithCoder:];
-[_TtC5UIKit21_UISimpleBoundingPath _inscribedRectInBoundingPathAndRect:byInsettingRect:onEdges:withOptions:];
-[_TtC5UIKit21_UISimpleBoundingPath _rectTuckedAgainstEdge:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_TtC5UIKit21_UISimpleBoundingPath _largestInscribedRectInBoundingPathAndRect:withCenter:aspectRatio:];
-[_TtC5UIKit21_UISimpleBoundingPath _imageRepresentation];
-[_TtC5UIKit21_UISimpleBoundingPath initWithCoder:];
-[_TtC5UIKit21_UISimpleBoundingPath _centerEdgeInsetsOfBoundingPathAndRect:];
```
