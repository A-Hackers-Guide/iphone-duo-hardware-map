# `_UIKeyboardWorkspaceNamespaceController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIScenePresentationBinderDelegate`, `FBSceneObserver`, `BSDescriptionStreaming`, `BSInvalidatable`, `_UISceneWorkspaceNamespaceDelegate`
- 8 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_UISceneWorkspaceNamespace" _wsNamespace;
@"FBSScene" _rehostingScene;
@"UIScenePresentationBinder" _presentationBinder;
@"UIView" _presentationBinderRootView;
@"<_UIKeyboardNamespaceBehavior>" _behavior;
B _invalidated;
@"NSMutableDictionary" _hostingCompoundAssertions;
@"FBScene" _clientSettingsDriverScene;
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
-[_UIKeyboardWorkspaceNamespaceController scenePresentationBinder:didStartPresentingScene:];
-[_UIKeyboardWorkspaceNamespaceController debugDescription];
-[_UIKeyboardWorkspaceNamespaceController scene:didUpdateSettings:];
-[_UIKeyboardWorkspaceNamespaceController init];
-[_UIKeyboardWorkspaceNamespaceController dealloc];
-[_UIKeyboardWorkspaceNamespaceController sceneDidInvalidate:];
-[_UIKeyboardWorkspaceNamespaceController invalidate];
-[_UIKeyboardWorkspaceNamespaceController scenePresentationBinder:didStopPresentingScene:];
-[_UIKeyboardWorkspaceNamespaceController description];
-[_UIKeyboardWorkspaceNamespaceController appendDescriptionToStream:];
-[_UIKeyboardWorkspaceNamespaceController workspaceNamespace:didAddScene:];
-[_UIKeyboardWorkspaceNamespaceController workspaceNamespace:willRemoveScene:];
-[_UIKeyboardWorkspaceNamespaceController scene:didUpdateClientSettings:];
```
