# `LACEnvironmentMechanismCompanion`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACEnvironmentMechanism`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
q _companionType;
@"NSData" _stateHash;
```

## Properties

```
@property (Tq,R,N,V_companionType) companionType;
@property (T@"NSData",R,N,V_stateHash) stateHash;
```

## Class methods

```
+[LACEnvironmentMechanismCompanion supportsSecureCoding];
+[LACEnvironmentMechanismCompanion companionForUser:type:error:];
```

## Instance methods

```
-[LACEnvironmentMechanismCompanion stateHash];
-[LACEnvironmentMechanismCompanion encodeWithCoder:];
-[LACEnvironmentMechanismCompanion descriptionDetails];
-[LACEnvironmentMechanismCompanion initWithCoder:];
-[LACEnvironmentMechanismCompanion isEqual:];
-[LACEnvironmentMechanismCompanion companionType];
-[LACEnvironmentMechanismCompanion initWithAvailabilityError:companionType:stateHash:];
```
