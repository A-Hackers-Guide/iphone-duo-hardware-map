# `_UISceneHostingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIScrollToTopView`, `_UIGeometryChangeObserver`, `BSDescriptionStreaming`, `_UISceneHostingHierarchyInteractionDelegate`, `BSInvalidatable`
- 5 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<UIScenePresenter>" _scenePresenter;
B _invalidated;
@"UILabel" _debugLabel;
@"_UISceneHostingController" _sceneHostingController;
@"_UISceneHostingHierarchyInteraction" _interaction;
```

## Properties

```
@property (T@"_UISceneHostingController",R,W,N,V_sceneHostingController) _sceneHostingController;
@property (T@"_UISceneHostingHierarchyInteraction",R,N,V_interaction) _interaction;
@property (TB,N) inheritsSecurity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneHostingView updateScene:];
-[_UISceneHostingView debugDescription];
-[_UISceneHostingView isScrollEnabled];
-[_UISceneHostingView layoutSubviews];
-[_UISceneHostingView succinctDescription];
-[_UISceneHostingView invalidate];
-[_UISceneHostingView _scrollToTopFromTouchAtScreenLocation:resultHandler:];
-[_UISceneHostingView willMoveToWindow:];
-[_UISceneHostingView setInheritsSecurity:];
-[_UISceneHostingView inheritsSecurity];
-[_UISceneHostingView description];
-[_UISceneHostingView traitCollectionDidChange:];
-[_UISceneHostingView appendDescriptionToStream:];
-[_UISceneHostingView _hitTest:withEvent:windowServerHitTestWindow:];
-[_UISceneHostingView canBecomeFirstResponder];
-[_UISceneHostingView initWithSceneHostingController:];
-[_UISceneHostingView _interaction];
-[_UISceneHostingView _isHostingRemoteContent];
-[_UISceneHostingView _sceneHostingController];
-[_UISceneHostingView _sceneSafeAreaAlignedEdgesDidChange];
-[_UISceneHostingView interactionRequestsUpdate:prefersFence:];
```
