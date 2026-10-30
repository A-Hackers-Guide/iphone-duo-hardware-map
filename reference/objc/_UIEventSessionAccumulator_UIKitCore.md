# `_UIEventSessionAccumulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMutableOrderedSet" _recentActions;
@"NSString" _name;
@? _block;
@"NSDictionary" _allowedActionSourceTypes;
q _sequenceNumber;
{_NSRange="location"Q"length"Q} _depthRange;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (T{_NSRange=QQ},R,N,V_depthRange) depthRange;
@property (T@?,R,N,V_block) block;
@property (T@"NSDictionary",R,N,V_allowedActionSourceTypes) allowedActionSourceTypes;
@property (Tq,N,V_sequenceNumber) sequenceNumber;
```

## Class methods

```
+[_UIEventSessionAccumulator accumulatorWithName:depthRange:block:allowedActionSourceTypes:];
```

## Instance methods

```
-[_UIEventSessionAccumulator depthRange];
-[_UIEventSessionAccumulator block];
-[_UIEventSessionAccumulator setSequenceNumber:];
-[_UIEventSessionAccumulator sequenceNumber];
-[_UIEventSessionAccumulator reset];
-[_UIEventSessionAccumulator enumerateAnalytics:];
-[_UIEventSessionAccumulator name];
-[_UIEventSessionAccumulator allowedActionSourceTypes];
-[_UIEventSessionAccumulator flushAccumulator];
-[_UIEventSessionAccumulator increaseWithAction:];
-[_UIEventSessionAccumulator isActionAllowed:];
-[_UIEventSessionAccumulator performIncreaseWithActions:];
```
