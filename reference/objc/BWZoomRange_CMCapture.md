# `BWZoomRange`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 4 properties, 12 instance methods, 2 class methods

## Instance variables

```
f _lowerBound;
f _upperBound;
f _fudgedLowerBound;
f _fudgedUpperBound;
Q _hash;
```

## Properties

```
@property (Tf,R,N,V_lowerBound) lowerBound;
@property (Tf,R,N,V_upperBound) upperBound;
@property (Tf,R,N,V_fudgedLowerBound) fudgedLowerBound;
@property (Tf,R,N,V_fudgedUpperBound) fudgedUpperBound;
```

## Class methods

```
+[BWZoomRange fudgedZoomRangeWithLower:upperBound:fudgedLowerBound:fudgedUpperBound:];
+[BWZoomRange zoomRangeWithLower:upperBound:];
```

## Instance methods

```
-[BWZoomRange removeFudgeFromZoomFactor:];
-[BWZoomRange hash];
-[BWZoomRange applyFudgeToZoomFactor:];
-[BWZoomRange description];
-[BWZoomRange copyWithZone:];
-[BWZoomRange isEqual:];
-[BWZoomRange lowerBound];
-[BWZoomRange upperBound];
-[BWZoomRange fudgedLowerBound];
-[BWZoomRange fudgedUpperBound];
-[BWZoomRange initWithLowerBound:upperBound:];
-[BWZoomRange initWithLowerBound:upperBound:fudgedLowerBound:fudgedUpperBound:];
```
