# `LACEnvironmentMechanismUserPassword`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LACEnvironmentMechanism`
- 1 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
B _set;
```

## Properties

```
@property (TB,R,N,V_set) set;
```

## Class methods

```
+[LACEnvironmentMechanismUserPassword supportsSecureCoding];
+[LACEnvironmentMechanismUserPassword environmentMechanismForUser:auditToken:dependencies:error:];
```

## Instance methods

```
-[LACEnvironmentMechanismUserPassword initWithAvailabilityError:set:];
-[LACEnvironmentMechanismUserPassword set];
-[LACEnvironmentMechanismUserPassword encodeWithCoder:];
-[LACEnvironmentMechanismUserPassword descriptionDetails];
-[LACEnvironmentMechanismUserPassword initWithCoder:];
-[LACEnvironmentMechanismUserPassword isEqual:];
```
