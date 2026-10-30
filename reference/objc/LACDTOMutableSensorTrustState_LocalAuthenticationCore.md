# `LACDTOMutableSensorTrustState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOSensorTrustState`
- 2 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSData" _installedSensorID;
@"NSData" _trustedSensorID;
```

## Properties

```
@property (T@"NSData",&,N,V_installedSensorID) installedSensorID;
@property (T@"NSData",&,N,V_trustedSensorID) trustedSensorID;
@property (TB,R,N) isDisapproved;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOMutableSensorTrustState nullInstance];
```

## Instance methods

```
-[LACDTOMutableSensorTrustState description];
-[LACDTOMutableSensorTrustState isEqual:];
-[LACDTOMutableSensorTrustState trustedSensorID];
-[LACDTOMutableSensorTrustState _containsDisapprovedSensorIDFlag:];
-[LACDTOMutableSensorTrustState _disapprovedSensorIDFlag];
-[LACDTOMutableSensorTrustState disapprove];
-[LACDTOMutableSensorTrustState initWithTrustState:];
-[LACDTOMutableSensorTrustState installedSensorID];
-[LACDTOMutableSensorTrustState isDisapproved];
-[LACDTOMutableSensorTrustState setInstalledSensorID:];
-[LACDTOMutableSensorTrustState setTrustedSensorID:];
```
