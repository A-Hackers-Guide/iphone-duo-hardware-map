# `AVZoomRange`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
d _minZoomFactor;
d _maxZoomFactor;
```

## Properties

```
@property (Td,R,N,V_minZoomFactor) minZoomFactor;
@property (Td,R,N,V_maxZoomFactor) maxZoomFactor;
```

## Class methods

```
+[AVZoomRange zoomRangeWithMinZoomFactor:maxZoomFactor:];
```

## Instance methods

```
-[AVZoomRange maxZoomFactor];
-[AVZoomRange description];
-[AVZoomRange isEqual:];
-[AVZoomRange containsZoomFactor:];
-[AVZoomRange initWithMinZoomFactor:maxZoomFactor:];
-[AVZoomRange minZoomFactor];
```
