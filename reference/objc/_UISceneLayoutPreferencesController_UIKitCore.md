# `_UISceneLayoutPreferencesController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSSceneObserver`, `_UISceneLayoutPreferencesControlling`
- 3 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"_UISceneLayoutPreferenceBuilder" _builder;
@"_UIWindowSceneTraitOverrideHandle" __traitHandle;
```

## Properties

```
@property (T@"_UIWindowSceneTraitOverrideHandle",&,N,V__traitHandle) _traitHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hostObservesLayoutPreferenceChanges;
@property (TB,R,N) hostSupportsSceneDoubleTap;
```

## Instance methods

```
-[_UISceneLayoutPreferencesController _traitHandle];
-[_UISceneLayoutPreferencesController systemLayoutSizeFittingSize:];
-[_UISceneLayoutPreferencesController removeObserver:];
-[_UISceneLayoutPreferencesController scene:didUpdateSettings:];
-[_UISceneLayoutPreferencesController settings];
-[_UISceneLayoutPreferencesController setScene:];
-[_UISceneLayoutPreferencesController _effectiveUserResizability];
-[_UISceneLayoutPreferencesController set_traitHandle:];
-[_UISceneLayoutPreferencesController hostObservesLayoutPreferenceChanges];
-[_UISceneLayoutPreferencesController hostSupportsSceneDoubleTap];
-[_UISceneLayoutPreferencesController updateClientSettings:];
-[_UISceneLayoutPreferencesController clientSettings];
-[_UISceneLayoutPreferencesController registerObserver:];
-[_UISceneLayoutPreferencesController updateLayoutPreferences:];
-[_UISceneLayoutPreferencesController didRecognizeDoubleTapInDraggableArea];
-[_UISceneLayoutPreferencesController systemLayoutSizeFittingSize3D:];
-[_UISceneLayoutPreferencesController scene:didUpdateClientSettings:];
```
