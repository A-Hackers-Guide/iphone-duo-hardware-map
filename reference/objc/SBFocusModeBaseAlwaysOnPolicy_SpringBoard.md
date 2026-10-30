# `SBFocusModeBaseAlwaysOnPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDoNotDisturbStateMonitorObserver`, `PTSettingsKeyObserver`, `SBAlwaysOnPolicy`
- 5 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BSCompoundAssertion" _suspensionAssertions;
@"SBDoNotDisturbStateMonitor" _dndStateMonitor;
@"SBAlwaysOnPolicySettings" _policySettings;
B _active;
B _alwaysOnPolicyActive;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisAlwaysOnPolicyActive,V_alwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
```

## Class methods

```
+[SBFocusModeBaseAlwaysOnPolicy policyIdentifier];
```

## Instance methods

```
-[SBFocusModeBaseAlwaysOnPolicy settings:changedValueForKey:];
-[SBFocusModeBaseAlwaysOnPolicy doNotDisturbStateMonitor:didUpdateToState:];
-[SBFocusModeBaseAlwaysOnPolicy _didChangeActive:dndState:suspensionState:];
-[SBFocusModeBaseAlwaysOnPolicy _shouldActivateForDNDState:];
-[SBFocusModeBaseAlwaysOnPolicy _updateWithDNDState:];
-[SBFocusModeBaseAlwaysOnPolicy _updateWithSuspensionState:];
-[SBFocusModeBaseAlwaysOnPolicy _updateWithSuspensionState:dndState:];
-[SBFocusModeBaseAlwaysOnPolicy acquirePolicySuspensionAssertionForReason:];
-[SBFocusModeBaseAlwaysOnPolicy activateAlwaysOnPolicy];
-[SBFocusModeBaseAlwaysOnPolicy analyticsPolicyName];
-[SBFocusModeBaseAlwaysOnPolicy analyticsPolicyValue];
-[SBFocusModeBaseAlwaysOnPolicy isAlwaysOnPolicyActive];
```
