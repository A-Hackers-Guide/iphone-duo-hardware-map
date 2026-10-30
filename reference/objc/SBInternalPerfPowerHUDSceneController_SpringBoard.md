# `SBInternalPerfPowerHUDSceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `SBFBacklightEnvironmentSceneProviding`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _registeredBacklightSceneProvider;
@"FBScene" _backlightParticipantScene;
```

## Properties

```
@property (TB,N,V_registeredBacklightSceneProvider) registeredBacklightSceneProvider;
@property (T@"FBScene",W,N,V_backlightParticipantScene) backlightParticipantScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBInternalPerfPowerHUDSceneController _setupInfo];
```

## Instance methods

```
-[SBInternalPerfPowerHUDSceneController scenesForBacklightSession];
-[SBInternalPerfPowerHUDSceneController backlightParticipantScene];
-[SBInternalPerfPowerHUDSceneController setBacklightParticipantScene:];
-[SBInternalPerfPowerHUDSceneController windowSceneDidDisconnect:];
-[SBInternalPerfPowerHUDSceneController setRegisteredBacklightSceneProvider:];
-[SBInternalPerfPowerHUDSceneController _configureBacklightEnvironmentSceneProviderIfNecessary];
-[SBInternalPerfPowerHUDSceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBInternalPerfPowerHUDSceneController windowSceneDidConnect:];
-[SBInternalPerfPowerHUDSceneController registeredBacklightSceneProvider];
```
