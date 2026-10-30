# `_UIContainerWindowPortalInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `_UIGeometryChangeObserver`, `UIInteraction`
- 6 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _portalViewEnabled;
B _enabled;
B _attemptsToUseAncestorViewContainer;
B _shouldAdjustZPositionToMatchAncestorViewContainer;
@"UIView" _view;
@"_UIContainerWindowPortalView" _portalView;
```

## Properties

```
@property (TB,N,S_setPortalViewEnabled:,V_portalViewEnabled) _portalViewEnabled;
@property (T@"_UIContainerWindowPortalView",&,N,V_portalView) portalView;
@property (T@"UIWindow",R,N) containerWindow;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,V_attemptsToUseAncestorViewContainer) attemptsToUseAncestorViewContainer;
@property (TB,N,V_shouldAdjustZPositionToMatchAncestorViewContainer) shouldAdjustZPositionToMatchAncestorViewContainer;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContainerWindowPortalInteraction containerWindow];
-[_UIContainerWindowPortalInteraction portalView];
-[_UIContainerWindowPortalInteraction setPortalView:];
-[_UIContainerWindowPortalInteraction _visibleViewContainer];
-[_UIContainerWindowPortalInteraction setAttemptsToUseAncestorViewContainer:];
-[_UIContainerWindowPortalInteraction _makePortalView];
-[_UIContainerWindowPortalInteraction _setPortalViewEnabled:];
-[_UIContainerWindowPortalInteraction _isSwiftUI:];
-[_UIContainerWindowPortalInteraction _unionFrameForView:];
-[_UIContainerWindowPortalInteraction attemptsToUseAncestorViewContainer];
-[_UIContainerWindowPortalInteraction shouldAdjustZPositionToMatchAncestorViewContainer];
-[_UIContainerWindowPortalInteraction isEnabled];
-[_UIContainerWindowPortalInteraction view];
-[_UIContainerWindowPortalInteraction setEnabled:];
-[_UIContainerWindowPortalInteraction willMoveToView:];
-[_UIContainerWindowPortalInteraction _calculateCenteredUnionRectForPortal];
-[_UIContainerWindowPortalInteraction setShouldAdjustZPositionToMatchAncestorViewContainer:];
-[_UIContainerWindowPortalInteraction _viewVisibilityDidChange];
-[_UIContainerWindowPortalInteraction _portalViewEnabled];
-[_UIContainerWindowPortalInteraction ensureVisibilityInContainerWindow];
-[_UIContainerWindowPortalInteraction didMoveToView:];
-[_UIContainerWindowPortalInteraction _viewIsVisibleInContainer:];
```
