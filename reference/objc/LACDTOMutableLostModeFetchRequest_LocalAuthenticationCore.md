# `LACDTOMutableLostModeFetchRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLostModeFetchRequest`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isDTOEnabled;
q _policy;
@"NSDictionary" _options;
@"LACDTORatchetState" _ratchetState;
@"LACDTOBiometryWatchdogPack" _biometryWatchdogPack;
```

## Properties

```
@property (Tq,N,V_policy) policy;
@property (T@"NSDictionary",&,N,V_options) options;
@property (TB,N,V_isDTOEnabled) isDTOEnabled;
@property (T@"LACDTORatchetState",&,N,V_ratchetState) ratchetState;
@property (T@"LACDTOBiometryWatchdogPack",&,N,V_biometryWatchdogPack) biometryWatchdogPack;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOMutableLostModeFetchRequest setOptions:];
-[LACDTOMutableLostModeFetchRequest setRatchetState:];
-[LACDTOMutableLostModeFetchRequest setBiometryWatchdogPack:];
-[LACDTOMutableLostModeFetchRequest description];
-[LACDTOMutableLostModeFetchRequest isDTOEnabled];
-[LACDTOMutableLostModeFetchRequest options];
-[LACDTOMutableLostModeFetchRequest ratchetState];
-[LACDTOMutableLostModeFetchRequest isEqual:];
-[LACDTOMutableLostModeFetchRequest setPolicy:];
-[LACDTOMutableLostModeFetchRequest biometryWatchdogPack];
-[LACDTOMutableLostModeFetchRequest policy];
-[LACDTOMutableLostModeFetchRequest setIsDTOEnabled:];
```
