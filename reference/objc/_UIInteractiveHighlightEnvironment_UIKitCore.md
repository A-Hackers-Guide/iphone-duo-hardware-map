# `_UIInteractiveHighlightEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 6 properties, 34 instance methods, 2 class methods

## Instance variables

```
@"UIScreen" _containerScreen;
@"_UIInteractiveHighlightEffectWindow" _containerWindow;
@"UIView" _containerView;
@"UIVisualEffectView" _backgroundEffectView;
@"UIView" _contentView;
@"UIView" _contentClipView;
@"UIView" _contentOverlayView;
@"UIViewPropertyAnimator" _backgroundEffectAnimator;
@"UIViewFloatAnimatableProperty" _backgroundEffectProgress;
@"NSArray" _viewRecords;
@"_UIInteractiveHighlightEnvironment" _parentEnvironment;
@"_UIInteractiveHighlightEnvironment" _childEnvironment;
@"NSUUID" _backgroundAnimationIdentifier;
@"UIView" _customBackgroundEffectView;
@? _backgroundEffectApplyBlock;
```

## Properties

```
@property (TB,N,GisHidden) hidden;
@property (T@"UIView",R,N,V_containerView) containerView;
@property (T@"UIView",R,D,N) contentView;
@property (T@"UIView",R,N) contentClipView;
@property (T@"UIView",&,N,V_customBackgroundEffectView) customBackgroundEffectView;
@property (T@?,C,N,V_backgroundEffectApplyBlock) backgroundEffectApplyBlock;
```

## Class methods

```
+[_UIInteractiveHighlightEnvironment interactiveHighlightEnvironmentForContainerView:];
+[_UIInteractiveHighlightEnvironment requestInteractiveHighlightEnvironmentForView:];
```

## Instance methods

```
-[_UIInteractiveHighlightEnvironment setHidden:];
-[_UIInteractiveHighlightEnvironment dealloc];
-[_UIInteractiveHighlightEnvironment reset];
-[_UIInteractiveHighlightEnvironment containerView];
-[_UIInteractiveHighlightEnvironment isHidden];
-[_UIInteractiveHighlightEnvironment initWithContainerView:];
-[_UIInteractiveHighlightEnvironment contentView];
-[_UIInteractiveHighlightEnvironment contentClipView];
-[_UIInteractiveHighlightEnvironment finalizeContainerWindowIfNeeded];
-[_UIInteractiveHighlightEnvironment applyBackgroundEffectWithMagnitude:interactive:completion:];
-[_UIInteractiveHighlightEnvironment applyContentInsets:];
-[_UIInteractiveHighlightEnvironment backgroundEffectApplyBlock];
-[_UIInteractiveHighlightEnvironment backgroundVisualEffectForProgress:];
-[_UIInteractiveHighlightEnvironment customBackgroundEffectView];
-[_UIInteractiveHighlightEnvironment disableClippingForView:ancestorView:];
-[_UIInteractiveHighlightEnvironment finalizeBackgroundEffect];
-[_UIInteractiveHighlightEnvironment finalizeContentViewIfNeeded];
-[_UIInteractiveHighlightEnvironment finalizeViewRecord:];
-[_UIInteractiveHighlightEnvironment indexOfViewRecordForView:];
-[_UIInteractiveHighlightEnvironment initBackgroundEffectViewIfNeeded];
-[_UIInteractiveHighlightEnvironment initContainerWindowIfNeeded];
-[_UIInteractiveHighlightEnvironment initContentViewIfNeeded];
-[_UIInteractiveHighlightEnvironment initWithContainerScreen:];
-[_UIInteractiveHighlightEnvironment initWithParentEnvironment:];
-[_UIInteractiveHighlightEnvironment interactiveHighlightEffectForView:options:];
-[_UIInteractiveHighlightEnvironment newBackgroundEffectAnimator];
-[_UIInteractiveHighlightEnvironment newViewRecordForView:options:];
-[_UIInteractiveHighlightEnvironment removeAllViewRecords];
-[_UIInteractiveHighlightEnvironment removeInteractiveHighlightEffect:];
-[_UIInteractiveHighlightEnvironment removeViewRecordsIfNeeded];
-[_UIInteractiveHighlightEnvironment setBackgroundEffectApplyBlock:];
-[_UIInteractiveHighlightEnvironment setCustomBackgroundEffectView:];
-[_UIInteractiveHighlightEnvironment setHidden:animated:completion:];
-[_UIInteractiveHighlightEnvironment setUserInteractionOnContainerEnabled:];
```
