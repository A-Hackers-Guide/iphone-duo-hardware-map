# `SBAdditionalEnvironmentDeferralsPolicyEnforcer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusPolicyEnforcer`
- 4 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"NSString" _debugName;
@"<SBAdditionalEnvironmentDeferralsPolicyEnforcerDelegate>" _delegate;
@"NSMutableArray" _rules;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_rules) rules;
@property (T@"<SBAdditionalEnvironmentDeferralsPolicyEnforcerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer rules];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer init];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer setRules:];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer invalidate];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer setDelegate:];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer delegate];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer enforce:];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer initWithDebugName:deliveryManager:];
-[SBAdditionalEnvironmentDeferralsPolicyEnforcer stopEnforcing];
```
