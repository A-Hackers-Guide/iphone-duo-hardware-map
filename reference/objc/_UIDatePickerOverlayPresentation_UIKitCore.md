# `_UIDatePickerOverlayPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 17 properties, 51 instance methods, 0 class methods

## Instance variables

```
@? _containerPresentCompletion;
B _defersAutomaticKeyboardAvoidanceAdjustments;
B _accessoryViewIgnoresDefaultInsets;
B _presentingContainerViewController;
B _ignoresPassthroughOnSourceView;
q _activeMode;
@"UIDatePicker" _activeDatePicker;
@"UIView" _sourceView;
q _alignment;
q _overlayAnchor;
@"UIView" _accessoryView;
@"_UIDatePickerContainerViewController" _containerViewController;
@"_UIDatePickerOverlayPlatterView" _platterView;
@? _dismissHandler;
@"<_UIDatePickerOverlayPresentationDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T@"_UIDatePickerContainerViewController",&,N,V_containerViewController) containerViewController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) resolvedSourceRect;
@property (TB,N,GisPresentingContainerViewController,V_presentingContainerViewController) presentingContainerViewController;
@property (T@"_UIDatePickerOverlayPlatterView",&,N,V_platterView) platterView;
@property (T@?,C,N,V_dismissHandler) dismissHandler;
@property (T@"<_UIDatePickerOverlayPresentationDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_activeMode) activeMode;
@property (TB,R,N) isPresentingOverlay;
@property (TB,N,V_ignoresPassthroughOnSourceView) ignoresPassthroughOnSourceView;
@property (T@"UIDatePicker",R,W,N,V_activeDatePicker) activeDatePicker;
@property (T@"UIView",R,W,N,V_sourceView) sourceView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
@property (TB,N,V_defersAutomaticKeyboardAvoidanceAdjustments) defersAutomaticKeyboardAvoidanceAdjustments;
@property (Tq,N,V_alignment) alignment;
@property (Tq,N,V_overlayAnchor) overlayAnchor;
@property (T@"UIView",&,N,V_accessoryView) accessoryView;
@property (TB,N,V_accessoryViewIgnoresDefaultInsets) accessoryViewIgnoresDefaultInsets;
```

## Instance methods

```
-[_UIDatePickerOverlayPresentation platterView];
-[_UIDatePickerOverlayPresentation setSourceRect:];
-[_UIDatePickerOverlayPresentation accessoryView];
-[_UIDatePickerOverlayPresentation sourceRect];
-[_UIDatePickerOverlayPresentation setPlatterView:];
-[_UIDatePickerOverlayPresentation initWithSourceView:];
-[_UIDatePickerOverlayPresentation setAccessoryView:];
-[_UIDatePickerOverlayPresentation setContainerViewController:];
-[_UIDatePickerOverlayPresentation setAlignment:];
-[_UIDatePickerOverlayPresentation alignment];
-[_UIDatePickerOverlayPresentation setDelegate:];
-[_UIDatePickerOverlayPresentation containerViewController];
-[_UIDatePickerOverlayPresentation delegate];
-[_UIDatePickerOverlayPresentation sourceView];
-[_UIDatePickerOverlayPresentation _adjustedAnchorPointForFrame:alignment:anchorPoint:];
-[_UIDatePickerOverlayPresentation _adjustedFrameForInputSize:outputFrame:];
-[_UIDatePickerOverlayPresentation _computedLayoutForPlatterView:];
-[_UIDatePickerOverlayPresentation _layoutArbiterAnchorAlignmentOffset];
-[_UIDatePickerOverlayPresentation _normalizedSourcePointForAnchorPoint:menuFrame:];
-[_UIDatePickerOverlayPresentation _overlayAlignment];
-[_UIDatePickerOverlayPresentation _overlayAlignmentEdge];
-[_UIDatePickerOverlayPresentation _prepareDatePickerPresentationWithCompletion:];
-[_UIDatePickerOverlayPresentation _presentNewDatePicker:];
-[_UIDatePickerOverlayPresentation _transitionToDatePicker:];
-[_UIDatePickerOverlayPresentation accessoryViewIgnoresDefaultInsets];
-[_UIDatePickerOverlayPresentation activateEmptyPresentationWithMode:onDismiss:];
-[_UIDatePickerOverlayPresentation activeDatePicker];
-[_UIDatePickerOverlayPresentation activeMode];
-[_UIDatePickerOverlayPresentation animateDismissalWithAnimations:completion:];
-[_UIDatePickerOverlayPresentation animatePresentWithAnimations:completion:];
-[_UIDatePickerOverlayPresentation animateReducedMotionTransitionWithAnimations:completion:];
-[_UIDatePickerOverlayPresentation animateTransitionWithAnimations:completion:];
-[_UIDatePickerOverlayPresentation defersAutomaticKeyboardAvoidanceAdjustments];
-[_UIDatePickerOverlayPresentation dismissHandler];
-[_UIDatePickerOverlayPresentation dismissPresentationAnimated:];
-[_UIDatePickerOverlayPresentation ignoresPassthroughOnSourceView];
-[_UIDatePickerOverlayPresentation isBeingDismissedOrPresented];
-[_UIDatePickerOverlayPresentation isPresentingContainerViewController];
-[_UIDatePickerOverlayPresentation isPresentingOverlay];
-[_UIDatePickerOverlayPresentation overlayAnchor];
-[_UIDatePickerOverlayPresentation presentDatePicker:onDismiss:];
-[_UIDatePickerOverlayPresentation resolvedSourceBounds];
-[_UIDatePickerOverlayPresentation resolvedSourceRect];
-[_UIDatePickerOverlayPresentation retargetCurrentPresentationToSourceView];
-[_UIDatePickerOverlayPresentation setAccessoryViewIgnoresDefaultInsets:];
-[_UIDatePickerOverlayPresentation setActiveMode:];
-[_UIDatePickerOverlayPresentation setDefersAutomaticKeyboardAvoidanceAdjustments:];
-[_UIDatePickerOverlayPresentation setDismissHandler:];
-[_UIDatePickerOverlayPresentation setIgnoresPassthroughOnSourceView:];
-[_UIDatePickerOverlayPresentation setOverlayAnchor:];
-[_UIDatePickerOverlayPresentation setPresentingContainerViewController:];
```
