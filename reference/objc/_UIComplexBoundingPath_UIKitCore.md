# `_UIComplexBoundingPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBoundingPath`
- 3 instance variables, 0 properties, 20 instance methods, 1 class methods

## Instance variables

```
d _scale;
q _orientation;
@"_UIBoundingPathBitmap" _bitmap;
```

## Class methods

```
+[_UIComplexBoundingPath supportsSecureCoding];
```

## Instance methods

```
-[_UIComplexBoundingPath setCoordinateSpace:];
-[_UIComplexBoundingPath _rectTuckedInCorner:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIComplexBoundingPath initWithCoordinateSpace:orientation:scale:boundingPathBitmap:];
-[_UIComplexBoundingPath isNonRectangular];
-[_UIComplexBoundingPath initWithRectangularCoordinateSpace:orientation:scale:];
-[_UIComplexBoundingPath _largestInscribedPortraitPixelRectInBoundingPathWithPortraitPixelRect:portraitAspectRatio:];
-[_UIComplexBoundingPath _portaitPixelRectWithPixelMinimumPaddingFromBoundingPath:againstPortraitEdge:fromPortraitPixelRect:withPortraitPixelCornerRadii:];
-[_UIComplexBoundingPath validateForCoordinateSpace];
-[_UIComplexBoundingPath encodeWithCoder:];
-[_UIComplexBoundingPath _inscribedRectInBoundingPathAndRect:byInsettingRect:onEdges:withOptions:];
-[_UIComplexBoundingPath _rectTuckedAgainstEdge:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIComplexBoundingPath _validateBitmap:withOrientation:scale:forCoordinateSpace:];
-[_UIComplexBoundingPath _largestInscribedRectInBoundingPathAndRect:withCenter:aspectRatio:];
-[_UIComplexBoundingPath _imageRepresentation];
-[_UIComplexBoundingPath description];
-[_UIComplexBoundingPath initWithCoder:];
-[_UIComplexBoundingPath _rectByHorizontallyInsettingPortraitPixelRect:onPortraitEdges:performCompleteTest:];
-[_UIComplexBoundingPath _centerEdgeInsetsOfBoundingPathAndRect:];
-[_UIComplexBoundingPath _rectByVerticallyInsettingPortraitPixelRect:onPortraitEdges:performCompleteTest:];
-[_UIComplexBoundingPath _portaitPixelRectWithPixelMinimumPaddingFromBoundingPath:inPortaitCorner:fromPortraitPixelRect:withPortraitPixelCornerRadii:];
```
