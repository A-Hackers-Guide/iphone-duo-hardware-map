# `LABiometryFallbackRequirement`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAACLSerializable`
- 2 instance variables, 0 properties, 2 instance methods, 3 class methods

## Instance variables

```
q _authType;
@"NSArray" _subrequirements;
```

## Class methods

```
+[LABiometryFallbackRequirement customPasswordRequirement:];
+[LABiometryFallbackRequirement defaultRequirement];
+[LABiometryFallbackRequirement devicePasscodeRequirement];
```

## Instance methods

```
-[LABiometryFallbackRequirement isEqual:];
-[LABiometryFallbackRequirement encodeWithACLCoder:];
```
