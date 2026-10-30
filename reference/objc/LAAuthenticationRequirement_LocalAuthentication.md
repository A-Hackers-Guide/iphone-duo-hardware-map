# `LAAuthenticationRequirement`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAACLSerializable`
- 2 instance variables, 0 properties, 5 instance methods, 6 class methods

## Instance variables

```
q _authType;
@"NSMutableSet" _subrequirements;
```

## Class methods

```
+[LAAuthenticationRequirement biometryCurrentSetRequirement];
+[LAAuthenticationRequirement biometryCurrentSetRequirementWithFallback:];
+[LAAuthenticationRequirement biometryRefreshableSetRequirementWithFallback:];
+[LAAuthenticationRequirement biometryRequirement];
+[LAAuthenticationRequirement biometryRequirementWithFallback:];
+[LAAuthenticationRequirement defaultRequirement];
```

## Instance methods

```
-[LAAuthenticationRequirement init];
-[LAAuthenticationRequirement isEqual:];
-[LAAuthenticationRequirement key];
-[LAAuthenticationRequirement encodeWithACLCoder:];
-[LAAuthenticationRequirement requirementByAddingExtendedRequirement:];
```
