# `SBApplicationSceneEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceEntity`
- Protocols: `SBProcessSettings`
- 4 instance variables, 9 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationSceneHandle" _sceneHandle;
@"NSMutableSet" _actions;
@"SBProcessSettings" _processSettings;
B _frozen;
```

## Properties

```
@property (T@"SBProcessSettings",R,N,V_processSettings) processSettings;
@property (T@"SBApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (T@"SBApplication",R,N) application;
@property (T@"NSSet",R,C,N,V_actions) actions;
@property (TB,N,GisFrozen,V_frozen) frozen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationSceneEntity isFrozen];
-[SBApplicationSceneEntity setFrozen:];
-[SBApplicationSceneEntity sceneHandle];
-[SBApplicationSceneEntity application];
-[SBApplicationSceneEntity applicationSceneEntity];
-[SBApplicationSceneEntity removeAllActions];
-[SBApplicationSceneEntity actions];
-[SBApplicationSceneEntity _initWithSceneHandle:];
-[SBApplicationSceneEntity supportedLayoutRoles];
-[SBApplicationSceneEntity hash];
-[SBApplicationSceneEntity entityGenerator];
-[SBApplicationSceneEntity copyWithZone:];
-[SBApplicationSceneEntity isEqual:];
-[SBApplicationSceneEntity descriptionBuilderWithMultilinePrefix:];
-[SBApplicationSceneEntity addActions:];
-[SBApplicationSceneEntity removeActions:];
-[SBApplicationSceneEntity processSettings];
-[SBApplicationSceneEntity _initializeWithSceneHandle:];
-[SBApplicationSceneEntity applyProcessSettings:];
-[SBApplicationSceneEntity boolForProcessSetting:];
-[SBApplicationSceneEntity clearProcessSettings];
-[SBApplicationSceneEntity copyProcessSettings];
-[SBApplicationSceneEntity flagForProcessSetting:];
-[SBApplicationSceneEntity isApplicationSceneEntity];
-[SBApplicationSceneEntity objectForProcessSetting:];
-[SBApplicationSceneEntity setFlag:forProcessSetting:];
-[SBApplicationSceneEntity setObject:forProcessSetting:];
-[SBApplicationSceneEntity translateActivationSettingsToActions];
```
