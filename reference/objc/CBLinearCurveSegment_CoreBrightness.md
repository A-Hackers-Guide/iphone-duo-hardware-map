# `CBLinearCurveSegment`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCurveSegment`
- 2 instance variables, 6 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"CBRange" _range;
@"CBLinearSegmentMapping" _mapping;
```

## Properties

```
@property (T@"CBRange",R,V_range) range;
@property (T@"CBLinearSegmentMapping",R,V_mapping) mapping;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBLinearCurveSegment forStartPoint:andEndPoint:];
```

## Instance methods

```
-[CBLinearCurveSegment range];
-[CBLinearCurveSegment mapping];
-[CBLinearCurveSegment dealloc];
-[CBLinearCurveSegment description];
-[CBLinearCurveSegment initWithStartPoint:andEndPoint:];
-[CBLinearCurveSegment getCurveSegmentOutputFor:];
-[CBLinearCurveSegment valueBelongsToSegment:];
```
