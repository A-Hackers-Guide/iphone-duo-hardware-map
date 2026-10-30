# `_SBKeyboardFocusCoalitionPolicyEnforcer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusPolicyEnforcer`
- 6 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeferringPredicate" _predicate;
@"NSString" _deferringRuleReason;
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"NSString" _debugName;
@"BKSHIDEventDeferringTarget" _enforcedTarget;
@"<BSInvalidatable>" _focusRule;
```

## Properties

```
@property (T@"BKSHIDEventDeferringTarget",&,N,V_enforcedTarget) enforcedTarget;
@property (T@"<BSInvalidatable>",&,N,V_focusRule) focusRule;
@property (T@"BKSHIDEventDeferringPredicate",R,N,V_predicate) predicate;
@property (T@"NSString",R,N,V_deferringRuleReason) deferringRuleReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBKeyboardFocusCoalitionPolicyEnforcer invalidate];
-[_SBKeyboardFocusCoalitionPolicyEnforcer predicate];
-[_SBKeyboardFocusCoalitionPolicyEnforcer deferringRuleReason];
-[_SBKeyboardFocusCoalitionPolicyEnforcer deferringTargetForPolicy:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer enforce:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer enforcedTarget];
-[_SBKeyboardFocusCoalitionPolicyEnforcer focusRule];
-[_SBKeyboardFocusCoalitionPolicyEnforcer initWithDeferringRulePredicate:deferringRuleReason:debugName:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer initWithDeferringRulePredicate:deferringRuleReason:debugName:deliveryManager:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer setEnforcedTarget:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer setFocusRule:];
-[_SBKeyboardFocusCoalitionPolicyEnforcer stopEnforcing];
```
