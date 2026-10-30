# `SBKeyboardFocusScenePolicyEnforcer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusPolicyEnforcer`
- 6 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"NSString" _debugName;
@"SBKeyboardFocusTarget" _sentKeyboardFocusOutboundTarget;
@"<_UIEventDeferringSystemShellBehaviorDelegate>" _systemShellBehaviorDelegate;
@"<BSInvalidatable>" _localToRemoteKeyboardFocusRule;
@"SBKeyboardFocusPolicy" _enforcedPolicy;
```

## Properties

```
@property (T@"SBKeyboardFocusTarget",&,N,V_sentKeyboardFocusOutboundTarget) sentKeyboardFocusOutboundTarget;
@property (T@"<_UIEventDeferringSystemShellBehaviorDelegate>",&,N,V_systemShellBehaviorDelegate) systemShellBehaviorDelegate;
@property (T@"<BSInvalidatable>",&,N,V_localToRemoteKeyboardFocusRule) localToRemoteKeyboardFocusRule;
@property (T@"SBKeyboardFocusPolicy",&,N,V_enforcedPolicy) enforcedPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBKeyboardFocusScenePolicyEnforcer invalidate];
-[SBKeyboardFocusScenePolicyEnforcer systemShellBehaviorDelegate];
-[SBKeyboardFocusScenePolicyEnforcer setSystemShellBehaviorDelegate:];
-[SBKeyboardFocusScenePolicyEnforcer enforcedPolicy];
-[SBKeyboardFocusScenePolicyEnforcer setEnforcedPolicy:];
-[SBKeyboardFocusScenePolicyEnforcer sentKeyboardFocusOutboundTarget];
-[SBKeyboardFocusScenePolicyEnforcer enforce:];
-[SBKeyboardFocusScenePolicyEnforcer initWithDeliveryManager:debugName:systemShellDelegate:];
-[SBKeyboardFocusScenePolicyEnforcer localToRemoteKeyboardFocusRule];
-[SBKeyboardFocusScenePolicyEnforcer setLocalToRemoteKeyboardFocusRule:];
-[SBKeyboardFocusScenePolicyEnforcer setSentKeyboardFocusOutboundTarget:];
-[SBKeyboardFocusScenePolicyEnforcer stopEnforcing];
```
