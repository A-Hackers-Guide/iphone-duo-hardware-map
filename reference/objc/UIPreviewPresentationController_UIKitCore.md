# `UIPreviewPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- Protocols: `UIGestureRecognizerDelegate`
- 11 instance variables, 15 properties, 54 instance methods, 3 class methods

## Instance variables

```
B _appliesVisualEffectsToPresentingView;
@"<UIPreviewPresentationControllerDelegate>" _previewPresentationDelegate;
@"UITapGestureRecognizer" _dismissGestureRecognizer;
@"UIVisualEffectView" _presentationContainerEffectView;
@"UIView" _localStatusBar;
@"NSArray" _keyboardSnapshotters;
@"NSHashTable" _keyboardWindows;
@"UIResponder" _currentPinnedResponder;
@"UIWindow" _presentationWindow;
@? _containerViewConfigurationBlock;
@? _dismissalTransitionDidEndBlock;
```

## Properties

```
@property (T@"<UIPreviewPresentationControllerDelegate>",W,N,V_previewPresentationDelegate) previewPresentationDelegate;
@property (T@"UITapGestureRecognizer",&,N,V_dismissGestureRecognizer) dismissGestureRecognizer;
@property (TB,N,V_appliesVisualEffectsToPresentingView) appliesVisualEffectsToPresentingView;
@property (T@"UIVisualEffectView",&,N,V_presentationContainerEffectView) presentationContainerEffectView;
@property (T@"UIView",&,N,V_localStatusBar) localStatusBar;
@property (T@"NSArray",C,N,V_keyboardSnapshotters) keyboardSnapshotters;
@property (T@"NSHashTable",C,N,V_keyboardWindows) keyboardWindows;
@property (T@"UIResponder",W,N,V_currentPinnedResponder) currentPinnedResponder;
@property (T@"UIWindow",W,N,V_presentationWindow) presentationWindow;
@property (T@?,C,N,V_containerViewConfigurationBlock) containerViewConfigurationBlock;
@property (T@?,C,N,V_dismissalTransitionDidEndBlock) dismissalTransitionDidEndBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPreviewPresentationController _backgroundEffectForTraitCollection:interactive:];
+[UIPreviewPresentationController _shouldApplyVisualEffectsToPresentingView];
+[UIPreviewPresentationController _shouldInterdictServiceViewTouches];
```

## Instance methods

```
-[UIPreviewPresentationController presentationTransitionDidEnd:];
-[UIPreviewPresentationController gestureRecognizer:shouldReceiveTouch:];
-[UIPreviewPresentationController dismissGestureRecognizer];
-[UIPreviewPresentationController presentationStyle];
-[UIPreviewPresentationController _shouldKeepCurrentFirstResponder];
-[UIPreviewPresentationController initWithPresentedViewController:presentingViewController:];
-[UIPreviewPresentationController _shouldDisableInteractionDuringTransitions];
-[UIPreviewPresentationController setDismissGestureRecognizer:];
-[UIPreviewPresentationController _presentationPotentiallyUnderlapsStatusBar];
-[UIPreviewPresentationController dismissalTransitionWillBegin];
-[UIPreviewPresentationController dismissalTransitionDidEnd:];
-[UIPreviewPresentationController presentationTransitionWillBegin];
-[UIPreviewPresentationController containerViewConfigurationBlock];
-[UIPreviewPresentationController presentationContainerEffectView];
-[UIPreviewPresentationController setPreviewPresentationDelegate:];
-[UIPreviewPresentationController keyboardWindows];
-[UIPreviewPresentationController _allowsAutorotation];
-[UIPreviewPresentationController _animatePreviewTransitionIfNeeded:];
-[UIPreviewPresentationController _applyVisualEffectsForPresentationPhase:];
-[UIPreviewPresentationController _cancelTransitionDidEnd:];
-[UIPreviewPresentationController _finalizeAfterDismissalTransition];
-[UIPreviewPresentationController _frameForTransitionViewInPresentationSuperview:];
-[UIPreviewPresentationController _handleDismissGestureRecognizer:];
-[UIPreviewPresentationController _interactiveHighlightTransitionDidEnd:];
-[UIPreviewPresentationController _keyboardShouldAnimateAlongsideForInteractiveTransitions];
-[UIPreviewPresentationController _layoutForCancel];
-[UIPreviewPresentationController _layoutForInteractiveHighlight];
-[UIPreviewPresentationController _layoutForPreview];
-[UIPreviewPresentationController _prepareContainerViewForPresentationTransition];
-[UIPreviewPresentationController _prepareDismissAnimationsForTransitionCoordinator:];
-[UIPreviewPresentationController _prepareDismissGestureRecognizersIfNeeded];
-[UIPreviewPresentationController _prepareKeyboardForPresentationTransition];
-[UIPreviewPresentationController _preparePresentationAnimationsForTransitionCoordinator:];
-[UIPreviewPresentationController _prepareStatusBarForPresentationTransition];
-[UIPreviewPresentationController _presentationContainerView];
-[UIPreviewPresentationController _presentationTransitionWillBeginForContainerEffectView:];
-[UIPreviewPresentationController _previewTransitionDidEnd:];
-[UIPreviewPresentationController _shouldSavePresentedViewControllerForStateRestoration];
-[UIPreviewPresentationController appliesVisualEffectsToPresentingView];
-[UIPreviewPresentationController currentPinnedResponder];
-[UIPreviewPresentationController dismissalTransitionDidEndBlock];
-[UIPreviewPresentationController keyboardSnapshotters];
-[UIPreviewPresentationController localStatusBar];
-[UIPreviewPresentationController presentationWindow];
-[UIPreviewPresentationController previewPresentationDelegate];
-[UIPreviewPresentationController setAppliesVisualEffectsToPresentingView:];
-[UIPreviewPresentationController setContainerViewConfigurationBlock:];
-[UIPreviewPresentationController setCurrentPinnedResponder:];
-[UIPreviewPresentationController setDismissalTransitionDidEndBlock:];
-[UIPreviewPresentationController setKeyboardSnapshotters:];
-[UIPreviewPresentationController setKeyboardWindows:];
-[UIPreviewPresentationController setLocalStatusBar:];
-[UIPreviewPresentationController setPresentationContainerEffectView:];
-[UIPreviewPresentationController setPresentationWindow:];
```
