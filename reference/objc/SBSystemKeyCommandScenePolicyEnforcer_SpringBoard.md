# `SBSystemKeyCommandScenePolicyEnforcer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusPolicyEnforcer`
- 4 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"NSString" _debugName;
@"<SBKeyboardFocusSceneProviding>" _sceneProvider;
@"<BSInvalidatable>" _spotlightSystemShortcutFocusRule;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V_spotlightSystemShortcutFocusRule) spotlightSystemShortcutFocusRule;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemKeyCommandScenePolicyEnforcer invalidate];
-[SBSystemKeyCommandScenePolicyEnforcer enforce:];
-[SBSystemKeyCommandScenePolicyEnforcer initWithSceneProvider:debugName:deliveryManager:];
-[SBSystemKeyCommandScenePolicyEnforcer setSpotlightSystemShortcutFocusRule:];
-[SBSystemKeyCommandScenePolicyEnforcer spotlightSystemShortcutFocusRule];
-[SBSystemKeyCommandScenePolicyEnforcer stopEnforcing];
```
