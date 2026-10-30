# `ANNordicCrashEvent`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
S _truncatedReason;
I _pc;
Q _referenceWallTime;
Q _referenceTicks;
Q _currentTicks;
```

## Properties

```
@property (TI,R,V_pc) pc;
@property (TS,R,V_truncatedReason) truncatedReason;
@property (TQ,R,V_referenceWallTime) referenceWallTime;
@property (TQ,R,V_referenceTicks) referenceTicks;
@property (TQ,R,V_currentTicks) currentTicks;
```

## Instance methods

```
-[ANNordicCrashEvent description];
-[ANNordicCrashEvent initWithData:];
-[ANNordicCrashEvent truncatedReason];
-[ANNordicCrashEvent currentTicks];
-[ANNordicCrashEvent pc];
-[ANNordicCrashEvent referenceTicks];
-[ANNordicCrashEvent referenceWallTime];
```
