# `LACDTOEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 13 properties, 14 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisConfirmed) confirmed;
@property (TB,R,N) isDTOEnabled;
@property (TB,R,N) hasExpiredBiometry;
@property (TB,R,N) allowsGracePeriodUI;
@property (TB,R,N) isGracePeriodActive;
@property (TB,R,N) isStrictModeEnabled;
@property (T@"LACDTOBiometryWatchdogPack",R,N) biometryWatchdogPack;
@property (T@"<LACDTOFeatureState>",R,N) featureState;
@property (T@"LACDTOLocationState",R,N) locationState;
@property (T@"LACDTOLostModeState",R,N) lostModeState;
@property (T@"LACDTORatchetState",R,N) ratchetState;
@property (T@"LACDTOGracePeriodState",R,N) gracePeriodState;
@property (T@"<LACDTOFeatureRequirements>",R,N) featureRequirements;
```

## Instance methods

```
-[LACDTOEnvironment isStrictModeEnabled];
-[LACDTOEnvironment isGracePeriodActive];
-[LACDTOEnvironment lostModeState];
-[LACDTOEnvironment locationState];
-[LACDTOEnvironment allowsGracePeriodUI];
-[LACDTOEnvironment featureState];
-[LACDTOEnvironment gracePeriodState];
-[LACDTOEnvironment hasExpiredBiometry];
-[LACDTOEnvironment isDTOEnabled];
-[LACDTOEnvironment featureRequirements];
-[LACDTOEnvironment allowsAuthenticationFallbacksForOptions:];
-[LACDTOEnvironment ratchetState];
-[LACDTOEnvironment isConfirmed];
-[LACDTOEnvironment biometryWatchdogPack];
```
