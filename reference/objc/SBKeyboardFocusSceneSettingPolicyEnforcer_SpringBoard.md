# `SBKeyboardFocusSceneSettingPolicyEnforcer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusPolicyEnforcer`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBKeyboardFocusSceneProviding>" _sceneProvider;
@"FBScene" _targetSceneForKeyboardFocusDeferring;
@"FBScene" _sbWindowSceneAncestorForTargetScene;
```

## Properties

```
@property (T@"FBScene",W,N,V_targetSceneForKeyboardFocusDeferring) targetSceneForKeyboardFocusDeferring;
@property (T@"FBScene",W,N,V_sbWindowSceneAncestorForTargetScene) sbWindowSceneAncestorForTargetScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBKeyboardFocusSceneSettingPolicyEnforcer invalidate];
-[SBKeyboardFocusSceneSettingPolicyEnforcer _moveKeyboardFocusDeferringEnvironmentSceneSettingFromScene:withSBAncestor:toScene:withSBAncestor:target:activeDisplayChanging:];
-[SBKeyboardFocusSceneSettingPolicyEnforcer enforce:];
-[SBKeyboardFocusSceneSettingPolicyEnforcer initWithSceneProvider:];
-[SBKeyboardFocusSceneSettingPolicyEnforcer sbWindowSceneAncestorForTargetScene];
-[SBKeyboardFocusSceneSettingPolicyEnforcer setSbWindowSceneAncestorForTargetScene:];
-[SBKeyboardFocusSceneSettingPolicyEnforcer setTargetSceneForKeyboardFocusDeferring:];
-[SBKeyboardFocusSceneSettingPolicyEnforcer stopEnforcing];
-[SBKeyboardFocusSceneSettingPolicyEnforcer targetSceneForKeyboardFocusDeferring];
```
