# `_UIContextMenuContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIPassthroughScrollInteractionDelegate`, `_UIScrollToTopView`
- 11 instance variables, 11 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _lastHitTestWasPassedThroughToInteraction;
B _inPassthroughViewHitTest;
B _didDismiss;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
B _passesBackgroundViewTouchesThrough;
B _allowsDragEventsToPassthrough;
@"UIView" _contentWrapperView;
@? _dismissalHandler;
@? _subtreeTraitPropagationHandler;
@? _sizeChangeHandler;
@? _layoutRegionChangeHandler;
```

## Properties

```
@property (T@"UIView",W,N,V_contentWrapperView) contentWrapperView;
@property (T@?,C,N,V_dismissalHandler) dismissalHandler;
@property (T@?,C,N,V_subtreeTraitPropagationHandler) subtreeTraitPropagationHandler;
@property (T@?,C,N,V_sizeChangeHandler) sizeChangeHandler;
@property (T@?,C,N,V_layoutRegionChangeHandler) layoutRegionChangeHandler;
@property (TB,N,V_passesBackgroundViewTouchesThrough) passesBackgroundViewTouchesThrough;
@property (TB,N,V_allowsDragEventsToPassthrough) allowsDragEventsToPassthrough;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuContainerView setUserInteractionEnabled:];
-[_UIContextMenuContainerView didMoveToWindow];
-[_UIContextMenuContainerView isScrollEnabled];
-[_UIContextMenuContainerView dealloc];
-[_UIContextMenuContainerView hitTest:withEvent:];
-[_UIContextMenuContainerView _didMoveFromWindow:toWindow:];
-[_UIContextMenuContainerView setBounds:];
-[_UIContextMenuContainerView passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIContextMenuContainerView passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIContextMenuContainerView _scrollToTopFromTouchAtScreenLocation:resultHandler:];
-[_UIContextMenuContainerView willMoveToWindow:];
-[_UIContextMenuContainerView setFrame:];
-[_UIContextMenuContainerView isTransparentFocusItem];
-[_UIContextMenuContainerView _sceneRegionsDidChange];
-[_UIContextMenuContainerView _attemptDismiss:];
-[_UIContextMenuContainerView _initSwift];
-[_UIContextMenuContainerView _sceneGeometryWillUpdate:];
-[_UIContextMenuContainerView _traitCollectionDidChangeOnSubtreeInternal:];
-[_UIContextMenuContainerView allowsDragEventsToPassthrough];
-[_UIContextMenuContainerView contentWrapperView];
-[_UIContextMenuContainerView dismissalHandler];
-[_UIContextMenuContainerView initWithFrame:allowsBackgroundInteractionAcrossProccesses:];
-[_UIContextMenuContainerView layoutRegionChangeHandler];
-[_UIContextMenuContainerView passesBackgroundViewTouchesThrough];
-[_UIContextMenuContainerView setAllowsDragEventsToPassthrough:];
-[_UIContextMenuContainerView setContentWrapperView:];
-[_UIContextMenuContainerView setDismissalHandler:];
-[_UIContextMenuContainerView setLayoutRegionChangeHandler:];
-[_UIContextMenuContainerView setPassesBackgroundViewTouchesThrough:];
-[_UIContextMenuContainerView setSizeChangeHandler:];
-[_UIContextMenuContainerView setSubtreeTraitPropagationHandler:];
-[_UIContextMenuContainerView sizeChangeHandler];
-[_UIContextMenuContainerView subtreeTraitPropagationHandler];
```
