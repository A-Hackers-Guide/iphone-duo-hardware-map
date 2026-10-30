# `LACEnvironmentMechanism`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSError" _availabilityError;
@"NSString" _localizedName;
@"NSString" _iconSystemName;
```

## Properties

```
@property (T@"NSError",R,N,V_availabilityError) availabilityError;
@property (T@"NSString",R,N,V_localizedName) localizedName;
@property (T@"NSString",R,N,V_iconSystemName) iconSystemName;
```

## Class methods

```
+[LACEnvironmentMechanism supportsSecureCoding];
+[LACEnvironmentMechanism environmentMechanismForUser:auditToken:dependencies:error:];
```

## Instance methods

```
-[LACEnvironmentMechanism localizedName];
-[LACEnvironmentMechanism availabilityError];
-[LACEnvironmentMechanism encodeWithCoder:];
-[LACEnvironmentMechanism descriptionDetails];
-[LACEnvironmentMechanism description];
-[LACEnvironmentMechanism initWithCoder:];
-[LACEnvironmentMechanism isEqual:];
-[LACEnvironmentMechanism iconSystemName];
-[LACEnvironmentMechanism initWithAvailabilityError:localizedName:iconSystemName:];
```
