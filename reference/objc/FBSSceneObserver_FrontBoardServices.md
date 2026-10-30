# `FBSSceneObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneObserver_Internal`, `FBSSceneObserverConfiguring`, `BSInvalidatable`
- 18 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<FBSSceneObserver>" _observer;
@"<FBSSceneComponent>" _component;
Q _observerAddress;
# _extension;
@"NSSet" _settings;
@"NSSet" _clientSettings;
@"NSSet" _actions;
@? _settingsHandler;
@? _clintSettingsHandler;
@? _actionHandler;
@? _invalidationHandler;
B _respondsToHostHandle;
B _respondsToSettings;
B _respondsToClientSettings;
B _respondsToActions;
B _respondsToInvalidate;
B _componentRespondsToPrivateActions;
B _componentRespondsToInvalidate;
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
-[FBSSceneObserver scene:didUpdateHostHandle:];
-[FBSSceneObserver observer];
-[FBSSceneObserver scene:handlePrivateActions:];
-[FBSSceneObserver actionHandler:];
-[FBSSceneObserver scene:didUpdateSettings:];
-[FBSSceneObserver scene:handleActions:];
-[FBSSceneObserver updateHandler:];
-[FBSSceneObserver actionClasses:];
-[FBSSceneObserver component];
-[FBSSceneObserver settingNames:];
-[FBSSceneObserver clientSettings:];
-[FBSSceneObserver invalidationHandler:];
-[FBSSceneObserver invalidate];
-[FBSSceneObserver actions:];
-[FBSSceneObserver initWithObserver:];
-[FBSSceneObserver hash];
-[FBSSceneObserver extension];
-[FBSSceneObserver isEqual:];
-[FBSSceneObserver sceneWillInvalidate:];
-[FBSSceneObserver settings:];
-[FBSSceneObserver clientUpdateHandler:];
-[FBSSceneObserver scene:didUpdateClientSettings:];
-[FBSSceneObserver clientSettingNames:];
-[FBSSceneObserver initWithComponent:extension:];
```
