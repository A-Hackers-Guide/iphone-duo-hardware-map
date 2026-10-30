# `SBTouchHistory`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBGestureRecognizerTouchHistoryProviding`
- 6 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _depth;
Q _count;
Q _start;
^{TouchHistory={CGPoint=dd}d} _history;
d _peakSpeed;
d _lastTouchLatency;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTouchHistory averageTouchPathAngleOverTimeDuration:];
-[SBTouchHistory conformsToSBGestureRecognizerTouchHistoryProviding];
-[SBTouchHistory peakSpeed];
-[SBTouchHistory timeWithinRadius:];
-[SBTouchHistory init];
-[SBTouchHistory dealloc];
-[SBTouchHistory reset];
-[SBTouchHistory averageTouchVelocityOverTimeDuration:];
-[SBTouchHistory initWithDepth:];
-[SBTouchHistory touchHistoryDepthForTimeDuration:forComputingDerivative:];
-[SBTouchHistory updateWithLocation:timestamp:];
-[SBTouchHistory updateWithLocation:timestamp:touchLatency:];
```
