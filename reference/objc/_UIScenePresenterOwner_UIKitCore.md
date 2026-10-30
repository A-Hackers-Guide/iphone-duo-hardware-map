# `_UIScenePresenterOwner`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 8 instance variables, 7 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UIScenePresentationManager" _scenePresentationManager;
@"<UISceneLayerTarget>" _layerTarget;
@"_UISceneLayerHostContainerView" _realSceneHostViewsContainer;
@"NSMutableOrderedSet" _activePresentersByPriority;
@"NSMutableSet" _inactivePresentersByPriority;
@"_UIScenePresenter" _prioritizedPresenter;
B _invalidated;
@"<_UIScenePresenterOwnerDelegate>" _delegate;
```

## Properties

```
@property (T@"<UISceneLayerTarget>",R,N,V_layerTarget) layerTarget;
@property (T@"<_UIScenePresenterOwnerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIScenePresentationContext",R,C,N) defaultPresentationContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIScenePresenterOwner addPresenter:];
-[_UIScenePresenterOwner layerTarget];
-[_UIScenePresenterOwner defaultPresentationContext];
-[_UIScenePresenterOwner succinctDescriptionBuilder];
-[_UIScenePresenterOwner dealloc];
-[_UIScenePresenterOwner _activatePresenter:];
-[_UIScenePresenterOwner _setActivePrioritizedPresenter:];
-[_UIScenePresenterOwner descriptionWithMultilinePrefix:];
-[_UIScenePresenterOwner _deactivatePresenter:];
-[_UIScenePresenterOwner succinctDescription];
-[_UIScenePresenterOwner invalidate];
-[_UIScenePresenterOwner setDelegate:];
-[_UIScenePresenterOwner presenterWithIdentifier:];
-[_UIScenePresenterOwner activePrioritizedPresenter];
-[_UIScenePresenterOwner delegate];
-[_UIScenePresenterOwner description];
-[_UIScenePresenterOwner _updateHostingStateForScenePresentersIfNecessary];
-[_UIScenePresenterOwner enumeratePresentersUsingBlock:];
-[_UIScenePresenterOwner _isPresenterActive:];
-[_UIScenePresenterOwner initWithScenePresentationManager:layerTarget:];
-[_UIScenePresenterOwner _updateActivePrioritizedPresenterIfNecessary];
-[_UIScenePresenterOwner _isPresenterHosting:];
-[_UIScenePresenterOwner descriptionBuilderWithMultilinePrefix:];
-[_UIScenePresenterOwner _invalidatePresenter:];
```
