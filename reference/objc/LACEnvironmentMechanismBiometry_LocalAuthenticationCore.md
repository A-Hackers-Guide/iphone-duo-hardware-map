# `LACEnvironmentMechanismBiometry`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACEnvironmentMechanism`
- 6 instance variables, 6 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _enrolled;
B _lockedOut;
B _sensorInaccessible;
q _biometryType;
@"NSData" _stateHash;
q _approvalState;
```

## Properties

```
@property (Tq,R,N,V_biometryType) biometryType;
@property (TB,R,N,V_enrolled) enrolled;
@property (TB,R,N,V_lockedOut) lockedOut;
@property (T@"NSData",R,N,V_stateHash) stateHash;
@property (TB,R,N,V_sensorInaccessible) sensorInaccessible;
@property (Tq,R,N,V_approvalState) approvalState;
```

## Class methods

```
+[LACEnvironmentMechanismBiometry supportsSecureCoding];
+[LACEnvironmentMechanismBiometry environmentMechanismForUser:auditToken:dependencies:error:];
```

## Instance methods

```
-[LACEnvironmentMechanismBiometry enrolled];
-[LACEnvironmentMechanismBiometry stateHash];
-[LACEnvironmentMechanismBiometry encodeWithCoder:];
-[LACEnvironmentMechanismBiometry initWithAvailabilityError:biometryType:enrolled:lockedOut:stateHash:sensorInaccessible:approvalState:];
-[LACEnvironmentMechanismBiometry sensorInaccessible];
-[LACEnvironmentMechanismBiometry biometryType];
-[LACEnvironmentMechanismBiometry descriptionDetails];
-[LACEnvironmentMechanismBiometry approvalState];
-[LACEnvironmentMechanismBiometry initWithCoder:];
-[LACEnvironmentMechanismBiometry isEqual:];
-[LACEnvironmentMechanismBiometry lockedOut];
```
