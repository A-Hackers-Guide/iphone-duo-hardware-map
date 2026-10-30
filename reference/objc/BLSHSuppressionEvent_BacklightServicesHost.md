# `BLSHSuppressionEvent`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _type;
Q _reason;
Q _machContinuousTimestamp;
```

## Properties

```
@property (TQ,R,N,V_type) type;
@property (TQ,R,N,V_reason) reason;
@property (TQ,R,N,V_machContinuousTimestamp) machContinuousTimestamp;
@property (TB,R,N,GwantsSuppression) suppression;
```

## Instance methods

```
-[BLSHSuppressionEvent type];
-[BLSHSuppressionEvent machContinuousTimestamp];
-[BLSHSuppressionEvent description];
-[BLSHSuppressionEvent reason];
-[BLSHSuppressionEvent initWithCoreMotionEvent:timestamp:];
-[BLSHSuppressionEvent initWithType:reason:timestamp:];
-[BLSHSuppressionEvent wantsSuppression];
```
