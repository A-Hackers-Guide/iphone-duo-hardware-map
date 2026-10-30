# `LACDTOMutableEnvironment`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOEnvironment`
- 8 instance variables, 17 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _confirmed;
@"LACDTOBiometryWatchdogPack" _biometryWatchdogPack;
@"<LACDTOFeatureState>" _featureState;
@"LACDTOLocationState" _locationState;
@"LACDTOLostModeState" _lostModeState;
@"LACDTORatchetState" _ratchetState;
@"LACDTOGracePeriodState" _gracePeriodState;
@"<LACDTOFeatureRequirements>" _featureRequirements;
```

## Properties

```
@property (TB,N,GisConfirmed,V_confirmed) confirmed;
@property (T@"LACDTOBiometryWatchdogPack",&,N,V_biometryWatchdogPack) biometryWatchdogPack;
@property (T@"<LACDTOFeatureState>",&,N,V_featureState) featureState;
@property (T@"LACDTOLocationState",&,N,V_locationState) locationState;
@property (T@"LACDTOLostModeState",&,N,V_lostModeState) lostModeState;
@property (T@"LACDTORatchetState",&,N,V_ratchetState) ratchetState;
@property (T@"LACDTOGracePeriodState",&,N,V_gracePeriodState) gracePeriodState;
@property (T@"<LACDTOFeatureRequirements>",&,N,V_featureRequirements) featureRequirements;
@property (TB,R,N) isDTOEnabled;
@property (TB,R,N) hasExpiredBiometry;
@property (TB,R,N) allowsGracePeriodUI;
@property (TB,R,N) isGracePeriodActive;
@property (TB,R,N) isStrictModeEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOMutableEnvironment nullInstance];
```

## Instance methods

```
-[LACDTOMutableEnvironment _isBiometryUsable];
-[LACDTOMutableEnvironment setLostModeState:];
-[LACDTOMutableEnvironment isStrictModeEnabled];
-[LACDTOMutableEnvironment isGracePeriodActive];
-[LACDTOMutableEnvironment setConfirmed:];
-[LACDTOMutableEnvironment setLocationState:];
-[LACDTOMutableEnvironment lostModeState];
-[LACDTOMutableEnvironment locationState];
-[LACDTOMutableEnvironment allowsGracePeriodUI];
-[LACDTOMutableEnvironment isDTOActive];
-[LACDTOMutableEnvironment featureState];
-[LACDTOMutableEnvironment setGracePeriodState:];
-[LACDTOMutableEnvironment gracePeriodState];
-[LACDTOMutableEnvironment setFeatureState:];
-[LACDTOMutableEnvironment hasExpiredBiometry];
-[LACDTOMutableEnvironment setRatchetState:];
-[LACDTOMutableEnvironment setBiometryWatchdogPack:];
-[LACDTOMutableEnvironment description];
-[LACDTOMutableEnvironment isDTOEnabled];
-[LACDTOMutableEnvironment featureRequirements];
-[LACDTOMutableEnvironment allowsAuthenticationFallbacksForOptions:];
-[LACDTOMutableEnvironment ratchetState];
-[LACDTOMutableEnvironment isConfirmed];
-[LACDTOMutableEnvironment isEqual:];
-[LACDTOMutableEnvironment setFeatureRequirements:];
-[LACDTOMutableEnvironment biometryWatchdogPack];
```
