# `SBFAlwaysOnDisplayPolicyAttribute`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAttribute`
- 1 instance variables, 1 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSSet" _policiesToSuspend;
```

## Properties

```
@property (T@"NSSet",R,C,N,V_policiesToSuspend) policiesToSuspend;
```

## Class methods

```
+[SBFAlwaysOnDisplayPolicyAttribute supportsSecureCoding];
+[SBFAlwaysOnDisplayPolicyAttribute suspendAlwaysOnDisplayPolicies:];
+[SBFAlwaysOnDisplayPolicyAttribute suspendAllAlwaysOnDisplayPolicies];
```

## Instance methods

```
-[SBFAlwaysOnDisplayPolicyAttribute initWithXPCDictionary:];
-[SBFAlwaysOnDisplayPolicyAttribute encodeWithXPCDictionary:];
-[SBFAlwaysOnDisplayPolicyAttribute encodeWithCoder:];
-[SBFAlwaysOnDisplayPolicyAttribute hash];
-[SBFAlwaysOnDisplayPolicyAttribute description];
-[SBFAlwaysOnDisplayPolicyAttribute initWithCoder:];
-[SBFAlwaysOnDisplayPolicyAttribute copyWithZone:];
-[SBFAlwaysOnDisplayPolicyAttribute isEqual:];
-[SBFAlwaysOnDisplayPolicyAttribute checkEntitlementSourceForRequiredEntitlements:error:];
-[SBFAlwaysOnDisplayPolicyAttribute initWithAlwaysOnDisplayPolicies:];
-[SBFAlwaysOnDisplayPolicyAttribute policiesToSuspend];
```
