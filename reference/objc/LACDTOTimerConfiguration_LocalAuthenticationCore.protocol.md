# `LACDTOTimerConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSNumber",R,N) coolOff;
@property (T@"NSNumber",R,N) waitingForSecondAuth;
@property (T@"NSNumber",R,N) ready;
@property (T@"NSNumber",R,N) dtoFallback;
@property (T@"NSNumber",R,N) dtoShortFallback;
@property (T@"NSNumber",R,N) lostMode;
@property (T@"NSNumber",R,N) gracePeriod;
```

## Instance methods

```
-[LACDTOTimerConfiguration gracePeriod];
-[LACDTOTimerConfiguration ready];
-[LACDTOTimerConfiguration coolOff];
-[LACDTOTimerConfiguration dtoFallback];
-[LACDTOTimerConfiguration dtoShortFallback];
-[LACDTOTimerConfiguration lostMode];
-[LACDTOTimerConfiguration waitingForSecondAuth];
```
