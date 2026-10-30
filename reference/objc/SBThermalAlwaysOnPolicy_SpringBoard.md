# `SBThermalAlwaysOnPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlwaysOnPolicy`
- 4 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BLSAssertion" _alwaysOnDisabledAssertion;
@"<SBFLockOutStatusProvider>" _lockOutStatusProvider;
B _alwaysOnPolicyActive;
B _thermallyBlocked;
```

## Properties

```
@property (TB,N,G_isThermallyBlocked,S_setThermallyBlocked:,V_thermallyBlocked) thermallyBlocked;
@property (TB,R,N,GisAlwaysOnPolicyActive,V_alwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBThermalAlwaysOnPolicy _noteDeviceBlockStateDidChange:];
-[SBThermalAlwaysOnPolicy _isThermallyBlocked];
-[SBThermalAlwaysOnPolicy _noteBootCompleted:];
-[SBThermalAlwaysOnPolicy _setThermallyBlocked:];
-[SBThermalAlwaysOnPolicy _updateThermalState];
-[SBThermalAlwaysOnPolicy activateAlwaysOnPolicy];
-[SBThermalAlwaysOnPolicy analyticsPolicyName];
-[SBThermalAlwaysOnPolicy analyticsPolicyValue];
-[SBThermalAlwaysOnPolicy isAlwaysOnPolicyActive];
```
