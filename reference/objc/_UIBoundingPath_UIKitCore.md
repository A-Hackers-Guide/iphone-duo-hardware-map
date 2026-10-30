# `_UIBoundingPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 2 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"<UICoordinateSpace>" _coordinateSpace;
```

## Properties

```
@property (T@"<UICoordinateSpace>",W,N,V_coordinateSpace) coordinateSpace;
@property (TB,R,N) isNonRectangular;
```

## Class methods

```
+[_UIBoundingPath supportsSecureCoding];
```

## Instance methods

```
-[_UIBoundingPath setCoordinateSpace:];
-[_UIBoundingPath coordinateSpace];
-[_UIBoundingPath _rectTuckedInCorner:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIBoundingPath debugQuickLookObject];
-[_UIBoundingPath _rectTuckedInCorner:ofBoundingRect:withSize:minimumPadding:];
-[_UIBoundingPath boundingPathForCoordinateSpace:withCornerRadii:orientation:scale:];
-[_UIBoundingPath isNonRectangular];
-[_UIBoundingPath initWithCoordinateSpace:];
-[_UIBoundingPath validateForCoordinateSpace];
-[_UIBoundingPath _inscribedRectInBoundingRect:byInsettingRect:onEdges:];
-[_UIBoundingPath _largestInscribedRectInBoundingRect:withCenter:aspectRatio:];
-[_UIBoundingPath encodeWithCoder:];
-[_UIBoundingPath _inscribedRectInBoundingPathAndRect:byInsettingRect:onEdges:withOptions:];
-[_UIBoundingPath _rectTuckedAgainstEdge:ofBoundingPathAndRect:withSize:cornerRadii:minimumPadding:];
-[_UIBoundingPath _largestInscribedRectInBoundingPathAndRect:withCenter:aspectRatio:];
-[_UIBoundingPath _imageRepresentation];
-[_UIBoundingPath boundingPathForCoordinateSpace:];
-[_UIBoundingPath initWithCoder:];
-[_UIBoundingPath _rectTuckedAgainstEdge:ofBoundingRect:withSize:minimumPadding:];
-[_UIBoundingPath _centerEdgeInsetsOfBoundingPathAndRect:];
```
