# `PKConvertedBezierPoint`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _index;
q _pointCount;
{CGPoint="x"d"y"d} _location;
q _bezierSegmentIndex;
```

## Properties

```
@property (Tq,R,N,V_index) index;
@property (Tq,R,N,V_pointCount) pointCount;
@property (T{CGPoint=dd},R,N,V_location) location;
@property (Tq,R,N,V_bezierSegmentIndex) bezierSegmentIndex;
```

## Instance methods

```
-[PKConvertedBezierPoint pointCount];
-[PKConvertedBezierPoint location];
-[PKConvertedBezierPoint index];
-[PKConvertedBezierPoint bezierSegmentIndex];
-[PKConvertedBezierPoint initWithPointCount:];
-[PKConvertedBezierPoint setIndex:location:bezierSegmentIndex:];
```
