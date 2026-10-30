# `FBSceneUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _lifecycleExternallyManaged;
@"NSString" _sceneID;
Q _transactionID;
@"FBSSceneSettings" _settings;
@"FBSSceneSettingsDiff" _settingsDiff;
@"FBSSceneTransitionContext" _transitionContext;
@"<NSObject><NSCopying>" _clientContext;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sceneID) sceneID;
@property (TQ,R,N,V_transactionID) transactionID;
@property (T@"FBSSceneSettings",R,N,V_settings) settings;
@property (T@"FBSSceneSettingsDiff",R,N,V_settingsDiff) settingsDiff;
@property (T@"FBSSceneTransitionContext",R,W,N,V_transitionContext) transitionContext;
@property (T@"<NSObject><NSCopying>",C,N,V_clientContext) clientContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSceneUpdateContext contextWithSceneID:transactionID:settings:settingsDiff:transitionContext:];
```

## Instance methods

```
-[FBSceneUpdateContext transactionID];
-[FBSceneUpdateContext settingsDiff];
-[FBSceneUpdateContext sceneID];
-[FBSceneUpdateContext debugDescription];
-[FBSceneUpdateContext succinctDescriptionBuilder];
-[FBSceneUpdateContext transitionContext];
-[FBSceneUpdateContext isClientLifecycleExternallyManaged];
-[FBSceneUpdateContext settings];
-[FBSceneUpdateContext descriptionWithMultilinePrefix:];
-[FBSceneUpdateContext succinctDescription];
-[FBSceneUpdateContext description];
-[FBSceneUpdateContext setClientContext:];
-[FBSceneUpdateContext descriptionBuilderWithMultilinePrefix:];
-[FBSceneUpdateContext clientContext];
```
