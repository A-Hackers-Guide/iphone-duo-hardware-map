# `SBTestSecureIndicatorMinimumOnTimeProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSecureIndicatorMinimumOnTimeProvider`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _remainingTimeToSatisfyMinimumOnTime;
@? _minimumOnTimeRequestedHandler;
@"NSError" _error;
```

## Properties

```
@property (Td,N,V_remainingTimeToSatisfyMinimumOnTime) remainingTimeToSatisfyMinimumOnTime;
@property (T@?,C,N,V_minimumOnTimeRequestedHandler) minimumOnTimeRequestedHandler;
@property (T@"NSError",&,N,V_error) error;
```

## Instance methods

```
-[SBTestSecureIndicatorMinimumOnTimeProvider setError:];
-[SBTestSecureIndicatorMinimumOnTimeProvider error];
-[SBTestSecureIndicatorMinimumOnTimeProvider minimumOnTimeRequestedHandler];
-[SBTestSecureIndicatorMinimumOnTimeProvider remainingTimeToSatisfyMinimumOnTime];
-[SBTestSecureIndicatorMinimumOnTimeProvider remainingTimeToSatisfyMinimumOnTimeForIndicators:error:];
-[SBTestSecureIndicatorMinimumOnTimeProvider setMinimumOnTimeRequestedHandler:];
-[SBTestSecureIndicatorMinimumOnTimeProvider setRemainingTimeToSatisfyMinimumOnTime:];
```
