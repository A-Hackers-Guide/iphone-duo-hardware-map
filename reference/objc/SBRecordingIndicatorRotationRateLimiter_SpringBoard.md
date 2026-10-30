# `SBRecordingIndicatorRotationRateLimiter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _rotationTimestamps;
Q _rateLimitNumber;
d _rateLimitPeriod;
```

## Properties

```
@property (TQ,N,V_rateLimitNumber) rateLimitNumber;
@property (Td,N,V_rateLimitPeriod) rateLimitPeriod;
```

## Instance methods

```
-[SBRecordingIndicatorRotationRateLimiter init];
-[SBRecordingIndicatorRotationRateLimiter rateLimitNumber];
-[SBRecordingIndicatorRotationRateLimiter setRateLimitPeriod:];
-[SBRecordingIndicatorRotationRateLimiter setRateLimitNumber:];
-[SBRecordingIndicatorRotationRateLimiter rateLimitPeriod];
-[SBRecordingIndicatorRotationRateLimiter _addTimestampForTime:];
-[SBRecordingIndicatorRotationRateLimiter _removeTimestampsEarlierThan:];
-[SBRecordingIndicatorRotationRateLimiter shouldAllowRotationUnderRateLimits];
```
