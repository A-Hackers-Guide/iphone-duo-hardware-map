# `LACDTOMutableTimerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOTimerConfiguration`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _coolOff;
@"NSNumber" _waitingForSecondAuth;
@"NSNumber" _ready;
@"NSNumber" _dtoFallback;
@"NSNumber" _dtoShortFallback;
@"NSNumber" _lostMode;
@"NSNumber" _gracePeriod;
```

## Properties

```
@property (T@"NSNumber",&,N,V_coolOff) coolOff;
@property (T@"NSNumber",&,N,V_waitingForSecondAuth) waitingForSecondAuth;
@property (T@"NSNumber",&,N,V_ready) ready;
@property (T@"NSNumber",&,N,V_dtoFallback) dtoFallback;
@property (T@"NSNumber",&,N,V_dtoShortFallback) dtoShortFallback;
@property (T@"NSNumber",&,N,V_lostMode) lostMode;
@property (T@"NSNumber",&,N,V_gracePeriod) gracePeriod;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOMutableTimerConfiguration gracePeriod];
-[LACDTOMutableTimerConfiguration init];
-[LACDTOMutableTimerConfiguration initWithConfiguration:];
-[LACDTOMutableTimerConfiguration description];
-[LACDTOMutableTimerConfiguration ready];
-[LACDTOMutableTimerConfiguration isEqual:];
-[LACDTOMutableTimerConfiguration setReady:];
-[LACDTOMutableTimerConfiguration setGracePeriod:];
-[LACDTOMutableTimerConfiguration coolOff];
-[LACDTOMutableTimerConfiguration setDtoFallback:];
-[LACDTOMutableTimerConfiguration dtoFallback];
-[LACDTOMutableTimerConfiguration dtoShortFallback];
-[LACDTOMutableTimerConfiguration lostMode];
-[LACDTOMutableTimerConfiguration setCoolOff:];
-[LACDTOMutableTimerConfiguration setDtoShortFallback:];
-[LACDTOMutableTimerConfiguration setLostMode:];
-[LACDTOMutableTimerConfiguration setValue:forTimer:];
-[LACDTOMutableTimerConfiguration setWaitingForSecondAuth:];
-[LACDTOMutableTimerConfiguration waitingForSecondAuth];
```
