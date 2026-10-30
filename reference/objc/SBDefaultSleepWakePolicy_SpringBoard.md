# `SBDefaultSleepWakePolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSleepWakePolicyProviding`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@"NSHashTable" _windowScenes;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDefaultSleepWakePolicy actionForBacklightChangeSource:];
-[SBDefaultSleepWakePolicy windowSceneDidDisconnect:];
-[SBDefaultSleepWakePolicy windowSceneDidConnect:];
-[SBDefaultSleepWakePolicy initWithBacklightCoordinator:windowSceneManager:];
-[SBDefaultSleepWakePolicy targetWindowScenesForBacklightAction:];
```
