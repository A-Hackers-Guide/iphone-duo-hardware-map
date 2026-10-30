# `_UICompanionContainerSceneClientSettingsApplicator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `BSDescriptionStreaming`, `BSInvalidatable`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"FBSScene" _clientScene;
B _isSourceSceneExternalNonInteractive;
@"FBScene" _sourceScene;
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
-[_UICompanionContainerSceneClientSettingsApplicator debugDescription];
-[_UICompanionContainerSceneClientSettingsApplicator init];
-[_UICompanionContainerSceneClientSettingsApplicator sceneDidActivate:];
-[_UICompanionContainerSceneClientSettingsApplicator dealloc];
-[_UICompanionContainerSceneClientSettingsApplicator succinctDescription];
-[_UICompanionContainerSceneClientSettingsApplicator invalidate];
-[_UICompanionContainerSceneClientSettingsApplicator description];
-[_UICompanionContainerSceneClientSettingsApplicator appendDescriptionToStream:];
-[_UICompanionContainerSceneClientSettingsApplicator scene:didUpdateClientSettings:];
```
