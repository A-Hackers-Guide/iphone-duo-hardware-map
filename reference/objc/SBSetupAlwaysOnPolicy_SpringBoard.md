# `SBSetupAlwaysOnPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlwaysOnPolicy`
- 3 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"BLSAssertion" _alwaysOnDisabledAssertion;
B _alwaysOnPolicyActive;
B _inSetupMode;
```

## Properties

```
@property (TB,N,G_isInSetupMode,S_setInSetupMode:,V_inSetupMode) inSetupMode;
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
-[SBSetupAlwaysOnPolicy _isInSetupMode];
-[SBSetupAlwaysOnPolicy _setInSetupMode:];
-[SBSetupAlwaysOnPolicy _setupModeStateDidChange:];
-[SBSetupAlwaysOnPolicy _updateSetupModeState];
-[SBSetupAlwaysOnPolicy activateAlwaysOnPolicy];
-[SBSetupAlwaysOnPolicy analyticsPolicyName];
-[SBSetupAlwaysOnPolicy analyticsPolicyValue];
-[SBSetupAlwaysOnPolicy isAlwaysOnPolicyActive];
```
