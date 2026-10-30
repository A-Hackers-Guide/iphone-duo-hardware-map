# `CBLinearSegmentMapping`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBSegmentMapping`
- 2 instance variables, 6 properties, 5 instance methods, 1 class methods

## Instance variables

```
f _slope;
f _offset;
```

## Properties

```
@property (Tf,R,V_slope) slope;
@property (Tf,R,V_offset) offset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBLinearSegmentMapping forSlope:andOffset:];
```

## Instance methods

```
-[CBLinearSegmentMapping description];
-[CBLinearSegmentMapping offset];
-[CBLinearSegmentMapping slope];
-[CBLinearSegmentMapping computeSegmentOutputFor:];
-[CBLinearSegmentMapping initWithSlope:andOffset:];
```
