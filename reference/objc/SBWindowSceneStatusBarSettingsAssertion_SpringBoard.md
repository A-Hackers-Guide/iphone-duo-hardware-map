# `SBWindowSceneStatusBarSettingsAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBWindowSceneStatusBarAssertion`
- 5 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBStatusBarSettings" _settings;
Q _level;
@"NSString" _reason;
@"SBWindowSceneStatusBarAssertionManager" _assertionManager;
@"NSDate" _timestamp;
```

## Properties

```
@property (T@"SBWindowSceneStatusBarAssertionManager",R,W,N,V_assertionManager) assertionManager;
@property (TQ,R,N,V_level) level;
@property (T@"SBStatusBarSettings",R,C,N,V_settings) settings;
@property (T@"NSDate",R,C,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_reason) reason;
```

## Instance methods

```
-[SBWindowSceneStatusBarSettingsAssertion acquire];
-[SBWindowSceneStatusBarSettingsAssertion invalidateWithAnimationParameters:];
-[SBWindowSceneStatusBarSettingsAssertion assertionManager];
-[SBWindowSceneStatusBarSettingsAssertion succinctDescriptionBuilder];
-[SBWindowSceneStatusBarSettingsAssertion init];
-[SBWindowSceneStatusBarSettingsAssertion _initWithWindowSceneStatusBarAssertionManager:settings:atLevel:reason:];
-[SBWindowSceneStatusBarSettingsAssertion settings];
-[SBWindowSceneStatusBarSettingsAssertion dealloc];
-[SBWindowSceneStatusBarSettingsAssertion timestamp];
-[SBWindowSceneStatusBarSettingsAssertion level];
-[SBWindowSceneStatusBarSettingsAssertion modifySettingsWithBlock:];
-[SBWindowSceneStatusBarSettingsAssertion descriptionWithMultilinePrefix:];
-[SBWindowSceneStatusBarSettingsAssertion succinctDescription];
-[SBWindowSceneStatusBarSettingsAssertion invalidate];
-[SBWindowSceneStatusBarSettingsAssertion description];
-[SBWindowSceneStatusBarSettingsAssertion acquireWithAnimationParameters:];
-[SBWindowSceneStatusBarSettingsAssertion reason];
-[SBWindowSceneStatusBarSettingsAssertion _initWithWindowSceneStatusBarAssertionManager:statusBarHidden:atLevel:reason:];
-[SBWindowSceneStatusBarSettingsAssertion modifySettingsWithBlock:animationParameters:];
-[SBWindowSceneStatusBarSettingsAssertion descriptionBuilderWithMultilinePrefix:];
```
