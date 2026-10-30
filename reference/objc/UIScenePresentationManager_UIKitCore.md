# `UIScenePresentationManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `_UIScenePresenterOwnerDelegate`, `FBSceneObserver`
- 8 instance variables, 9 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"_UISceneKeyboardProxyLayerForwardingPresentationScene" _keyboardProxyPresentationEnvironment;
@"FBScene" _scene;
@"_UIScenePresenterOwner" _scenePresenterOwner;
@"NSMapTable" _mapLayersToPresenterOwners;
@"NSHashTable" _prioritizedPresenterObservers;
@"UIScenePresentationContext" _defaultScenePresentationContext;
@"<UIScenePresentationManagerDelegate>" _delegate;
{?="defaultPriorityBand"B} _delegateFlags;
```

## Properties

```
@property (TB,R,N) _hasPresenters;
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"<UIScenePresentationManagerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisInvalidated) invalidated;
@property (T@"UIScenePresentationContext",R,C,N,V_defaultScenePresentationContext) defaultPresentationContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIScenePresentationManager sceneHostingGraph];
```

## Instance methods

```
-[UIScenePresentationManager _initWithScene:];
-[UIScenePresentationManager defaultPresentationContext];
-[UIScenePresentationManager _defaultPresentationPriority];
-[UIScenePresentationManager captureSnapshotPresentationView];
-[UIScenePresentationManager _addPrioritizedPresenterObserver:];
-[UIScenePresentationManager succinctDescriptionBuilder];
-[UIScenePresentationManager init];
-[UIScenePresentationManager _hasPresenterWithIdentifier:];
-[UIScenePresentationManager modifyDefaultPresentationContext:];
-[UIScenePresentationManager owner:willPrioritizePresenter:deactivatePresenter:];
-[UIScenePresentationManager dealloc];
-[UIScenePresentationManager sceneContentStateDidChange:];
-[UIScenePresentationManager _removePrioritizedPresenterObserver:];
-[UIScenePresentationManager descriptionWithMultilinePrefix:];
-[UIScenePresentationManager isInvalidated];
-[UIScenePresentationManager _presenterWithIdentifier:];
-[UIScenePresentationManager succinctDescription];
-[UIScenePresentationManager createPresenterWithIdentifier:priority:];
-[UIScenePresentationManager createPresenterWithIdentifier:];
-[UIScenePresentationManager setDelegate:];
-[UIScenePresentationManager snapshotPresentationForSnapshot:];
-[UIScenePresentationManager _initWithScene:keyboardProxyLayerManager:keyboardProxyPresentationEnvironment:];
-[UIScenePresentationManager snapshotContext];
-[UIScenePresentationManager scene];
-[UIScenePresentationManager prepareSnapshotPresentationViewWithConfigurator:];
-[UIScenePresentationManager delegate];
-[UIScenePresentationManager description];
-[UIScenePresentationManager createPresenterForLayerTarget:identifier:];
-[UIScenePresentationManager _hasPresenters];
-[UIScenePresentationManager ownerDidInvalidateLastPresenter:];
-[UIScenePresentationManager createPresenterForLayerTarget:identifier:priority:];
-[UIScenePresentationManager descriptionBuilderWithMultilinePrefix:];
```
