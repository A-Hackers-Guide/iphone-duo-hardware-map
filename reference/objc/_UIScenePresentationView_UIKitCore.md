# `_UIScenePresentationView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIVisibilityPropagationView`
- Protocols: `FBSceneObserver`, `_UISceneLayerHostContainerViewDataSource`, `BSDescriptionProviding`, `UIScenePresentation`, `BSInvalidatable`
- 9 instance variables, 9 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"_UIScenePresenter" _presenter;
@"FBScene" _scene;
@"FBSSceneSettings" _effectiveSettings;
@"UIScenePresentationContext" _currentPresentationContext;
@"_UISceneLayerHostContainerView" _hostContainerView;
@"UIView" _backgroundView;
@"FBSSceneSettingsDiffInspector" _geometrySettingsDiffInspector;
@"NSHashTable" _observers;
B _invalidated;
```

## Properties

```
@property (T#,N,R) _intelligenceBaseClass;
@property (T@"UIScenePresentationContext",&,N,V_currentPresentationContext) currentPresentationContext;
@property (T@"_UISceneLayerHostContainerView",&,N,V_hostContainerView) hostContainerView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIScenePresenter>",R,W,N) presenter;
@property (T@"UIView",&,N) backgroundView;
```

## Instance methods

```
-[_UIScenePresentationView presentationContextForSceneLayerHostContainerView];
-[_UIScenePresentationView didMoveToWindow];
-[_UIScenePresentationView presenter];
-[_UIScenePresentationView scene:clientDidConnect:];
-[_UIScenePresentationView sceneWillDeactivate:withContext:];
-[_UIScenePresentationView debugDescription];
-[_UIScenePresentationView scene:didPrepareUpdateWithContext:];
-[_UIScenePresentationView identifier];
-[_UIScenePresentationView succinctDescriptionBuilder];
-[_UIScenePresentationView removeObserver:];
-[_UIScenePresentationView sceneDidActivate:];
-[_UIScenePresentationView _intelligenceCollectContentIn:collector:];
-[_UIScenePresentationView _updateFrameAndTransform];
-[_UIScenePresentationView dealloc];
-[_UIScenePresentationView descriptionWithMultilinePrefix:];
-[_UIScenePresentationView succinctDescription];
-[_UIScenePresentationView addObserver:];
-[_UIScenePresentationView invalidate];
-[_UIScenePresentationView initWithPresenter:];
-[_UIScenePresentationView _geometryDidUpdateWithTransitionContext:];
-[_UIScenePresentationView currentPresentationContext];
-[_UIScenePresentationView backgroundView];
-[_UIScenePresentationView description];
-[_UIScenePresentationView _hitTest:withEvent:windowServerHitTestWindow:];
-[_UIScenePresentationView _intelligenceBaseClass];
-[_UIScenePresentationView setCurrentPresentationContext:];
-[_UIScenePresentationView setHostContainerView:];
-[_UIScenePresentationView _updatePresentationContextFrom:toContext:];
-[_UIScenePresentationView _updateBackgroundColor];
-[_UIScenePresentationView _intelligenceCollectRemoteContentIn:remoteContextWrapper:];
-[_UIScenePresentationView hostContainerView];
-[_UIScenePresentationView setBackgroundView:];
-[_UIScenePresentationView descriptionBuilderWithMultilinePrefix:];
```
