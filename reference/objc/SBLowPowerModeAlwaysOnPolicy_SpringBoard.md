# `SBLowPowerModeAlwaysOnPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlwaysOnPolicy`
- 3 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BSCompoundAssertion" _suspensionAssertions;
@"BLSAssertion" _alwaysOnDisabledAssertion;
B _alwaysOnPolicyActive;
```

## Properties

```
@property (TB,R,N,GisAlwaysOnPolicyActive,V_alwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBLowPowerModeAlwaysOnPolicy policyIdentifier];
```

## Instance methods

```
-[SBLowPowerModeAlwaysOnPolicy _updateAssertion];
-[SBLowPowerModeAlwaysOnPolicy _noteLowPowerModeChanged:];
-[SBLowPowerModeAlwaysOnPolicy acquirePolicySuspensionAssertionForReason:];
-[SBLowPowerModeAlwaysOnPolicy activateAlwaysOnPolicy];
-[SBLowPowerModeAlwaysOnPolicy analyticsPolicyName];
-[SBLowPowerModeAlwaysOnPolicy analyticsPolicyValue];
-[SBLowPowerModeAlwaysOnPolicy isAlwaysOnPolicyActive];
```
