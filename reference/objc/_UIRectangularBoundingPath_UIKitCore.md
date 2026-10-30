# `_UIRectangularBoundingPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBoundingPath`
- 1 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingRect;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingRect) boundingRect;
```

## Class methods

```
+[_UIRectangularBoundingPath supportsSecureCoding];
```

## Instance methods

```
-[_UIRectangularBoundingPath boundingRect];
-[_UIRectangularBoundingPath initWithCoordinateSpace:boundingRect:];
-[_UIRectangularBoundingPath setCoordinateSpace:];
-[_UIRectangularBoundingPath _rectTuckedInCorner:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIRectangularBoundingPath isNonRectangular];
-[_UIRectangularBoundingPath validateForCoordinateSpace];
-[_UIRectangularBoundingPath _validateBoundingRect:forCoordinateSpace:];
-[_UIRectangularBoundingPath encodeWithCoder:];
-[_UIRectangularBoundingPath _inscribedRectInBoundingPathAndRect:byInsettingRect:onEdges:withOptions:];
-[_UIRectangularBoundingPath _rectTuckedAgainstEdge:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIRectangularBoundingPath _largestInscribedRectInBoundingPathAndRect:withCenter:aspectRatio:];
-[_UIRectangularBoundingPath _imageRepresentation];
-[_UIRectangularBoundingPath description];
-[_UIRectangularBoundingPath initWithCoder:];
-[_UIRectangularBoundingPath _centerEdgeInsetsOfBoundingPathAndRect:];
```
