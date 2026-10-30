# `_UICampoLightweightController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SGAssistantActionModalBuilderDelegate`, `_UICampoServiceSessionDelegate`, `_UICampoPresentedViewControllerDelegate`
- 23 instance variables, 31 properties, 87 instance methods, 0 class methods

## Instance variables

```
B _isTrackingHover;
B _isHoveringOverPopover;
B _isPointerInPresentationRegion;
B _isPointerOnExposedSelection;
B _isPointerInAffordanceRegion;
B _requiresPointerExitBeforePresentation;
@"UIViewController" _presentingViewController;
q _state;
@"_UICampoLightweightConfiguration" _configuration;
@"_UIIntelligentAssistantTextSelectionContext" _textSelectionContext;
@"_UIIntelligentAssistantImageSelectionContext" _imageSelectionContext;
@"<_UICampoLightweightControllerDelegate>" _delegate;
@"_UICampoActionConfiguration" _campoActionConfiguration;
@"UIViewController" _campoViewController;
@"UIPopoverPresentationController" _popoverPresentationController;
@"UIHoverGestureRecognizer" _sourceHoverRecognizer;
@"UIHoverGestureRecognizer" _popoverHoverRecognizer;
@"UIDelayedAction" _pointerExitDismissalAction;
@"UIDelayedAction" _delayedAction;
@"NSArray" _pendingPassthroughViews;
Q _presentationPermissionGeneration;
@"_UICampoLightweightDebugHighlighter" _debugHighlighter;
@ _modalBuilder;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UICampoActionConfiguration",&,N,V_campoActionConfiguration) campoActionConfiguration;
@property (T@"UIViewController",W,N,V_campoViewController) campoViewController;
@property (T@"UIPopoverPresentationController",W,N,V_popoverPresentationController) popoverPresentationController;
@property (Tq,N,V_state) state;
@property (TB,N,V_isTrackingHover) isTrackingHover;
@property (T@"_UICampoLightweightConfiguration",&,N,V_configuration) configuration;
@property (T@"_UIIntelligentAssistantImageSelectionContext",&,N,V_imageSelectionContext) imageSelectionContext;
@property (T@"UIHoverGestureRecognizer",&,N,V_sourceHoverRecognizer) sourceHoverRecognizer;
@property (T@"UIHoverGestureRecognizer",&,N,V_popoverHoverRecognizer) popoverHoverRecognizer;
@property (T@"UIDelayedAction",&,N,V_pointerExitDismissalAction) pointerExitDismissalAction;
@property (TB,N,V_isPointerInPresentationRegion) isPointerInPresentationRegion;
@property (TB,N,V_isPointerOnExposedSelection) isPointerOnExposedSelection;
@property (TB,N,V_isPointerInAffordanceRegion) isPointerInAffordanceRegion;
@property (TB,N,V_requiresPointerExitBeforePresentation) requiresPointerExitBeforePresentation;
@property (T@"UIDelayedAction",&,N,V_delayedAction) delayedAction;
@property (T@"NSArray",C,N,V_pendingPassthroughViews) pendingPassthroughViews;
@property (TQ,N,V_presentationPermissionGeneration) presentationPermissionGeneration;
@property (T@"_UICampoLightweightDebugHighlighter",&,N,V_debugHighlighter) debugHighlighter;
@property (T@,&,N,V_modalBuilder) modalBuilder;
@property (T@"UIViewController",R,W,N,V_presentingViewController) presentingViewController;
@property (TB,R,N,V_isHoveringOverPopover) isHoveringOverPopover;
@property (T@"_UIIntelligentAssistantTextSelectionContext",&,N,V_textSelectionContext) textSelectionContext;
@property (T@"<_UICampoLightweightControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICampoLightweightController dismissAnimated:];
-[_UICampoLightweightController setState:];
-[_UICampoLightweightController _campoServiceSession:willShowPopoverPresentation:];
-[_UICampoLightweightController setConfiguration:];
-[_UICampoLightweightController isBeingDismissed];
-[_UICampoLightweightController popoverPresentationController];
-[_UICampoLightweightController setPopoverPresentationController:];
-[_UICampoLightweightController dismissViewController:];
-[_UICampoLightweightController presentingViewController];
-[_UICampoLightweightController setDelegate:];
-[_UICampoLightweightController configuration];
-[_UICampoLightweightController initWithPresentingViewController:];
-[_UICampoLightweightController delegate];
-[_UICampoLightweightController _campoServiceSession:didShowPopoverPresentation:];
-[_UICampoLightweightController setDelayedAction:];
-[_UICampoLightweightController delayedAction];
-[_UICampoLightweightController state];
-[_UICampoLightweightController isTrackingHover];
-[_UICampoLightweightController presentCampoAfterDelayAnimated:];
-[_UICampoLightweightController setIsPointerOnExposedSelection:];
-[_UICampoLightweightController setIsPointerInAffordanceRegion:];
-[_UICampoLightweightController _affordanceRegion];
-[_UICampoLightweightController _anchorRect];
-[_UICampoLightweightController _attachPopoverHoverRecognizer];
-[_UICampoLightweightController _campoServiceSession:didDismissPopoverPresentation:];
-[_UICampoLightweightController _canPresentCampo];
-[_UICampoLightweightController _detachPopoverHoverRecognizer];
-[_UICampoLightweightController _dismissAfterPointerExitDelay];
-[_UICampoLightweightController _effectiveAnchorRect];
-[_UICampoLightweightController _launchCampo];
-[_UICampoLightweightController _pointIsInSelectionRects:];
-[_UICampoLightweightController _popoverFitsAboveAnchorRect:];
-[_UICampoLightweightController _presentationRegion];
-[_UICampoLightweightController _rawAnchorRect];
-[_UICampoLightweightController _removeDebugHighlights];
-[_UICampoLightweightController _updateDebugHighlights];
-[_UICampoLightweightController _updatePendingDismissal];
-[_UICampoLightweightController _visibleAffordanceRect];
-[_UICampoLightweightController campoActionConfiguration];
-[_UICampoLightweightController campoPresentedViewController:didReceiveModalPresentationRequestWithContextData:];
-[_UICampoLightweightController campoPresentedViewController:didReceiveStateChangedWithState:];
-[_UICampoLightweightController campoViewController];
-[_UICampoLightweightController cancelAndDismissPresentationAnimated:];
-[_UICampoLightweightController configurePopoverPresentationWithPassthroughViews:];
-[_UICampoLightweightController debugHighlighter];
-[_UICampoLightweightController hoveringWithRecognizer:];
-[_UICampoLightweightController imageSelectionContext];
-[_UICampoLightweightController isBeingPresented];
-[_UICampoLightweightController isHoveringOverPopover];
-[_UICampoLightweightController isPointerInAffordanceRegion];
-[_UICampoLightweightController isPointerInPresentationRegion];
-[_UICampoLightweightController isPointerOnExposedSelection];
-[_UICampoLightweightController modalBuilder];
-[_UICampoLightweightController notifyChangeOfState:toState:];
-[_UICampoLightweightController notifyPopoverDidDismiss];
-[_UICampoLightweightController notifyPopoverDidShow];
-[_UICampoLightweightController pendingPassthroughViews];
-[_UICampoLightweightController pointerExitDismissalAction];
-[_UICampoLightweightController popoverHoverRecognizer];
-[_UICampoLightweightController presentCampoAnimated:];
-[_UICampoLightweightController presentationPermissionGeneration];
-[_UICampoLightweightController requirePointerExitBeforeNextPresentation];
-[_UICampoLightweightController requiresPointerExitBeforePresentation];
-[_UICampoLightweightController setCampoActionConfiguration:];
-[_UICampoLightweightController setCampoViewController:];
-[_UICampoLightweightController setDebugHighlighter:];
-[_UICampoLightweightController setImageSelectionContext:];
-[_UICampoLightweightController setIsPointerInPresentationRegion:];
-[_UICampoLightweightController setIsTrackingHover:];
-[_UICampoLightweightController setModalBuilder:];
-[_UICampoLightweightController setPendingPassthroughViews:];
-[_UICampoLightweightController setPointerExitDismissalAction:];
-[_UICampoLightweightController setPopoverHoverRecognizer:];
-[_UICampoLightweightController setPresentationPermissionGeneration:];
-[_UICampoLightweightController setRequiresPointerExitBeforePresentation:];
-[_UICampoLightweightController setSourceHoverRecognizer:];
-[_UICampoLightweightController setTextSelectionContext:];
-[_UICampoLightweightController showWithConfiguration:context:animated:];
-[_UICampoLightweightController showWithConfiguration:imageSelectionContext:animated:];
-[_UICampoLightweightController showWithConfiguration:textSelectionContext:animated:];
-[_UICampoLightweightController showWithConfiguration:textSelectionContext:imageSelectionContext:animated:];
-[_UICampoLightweightController sourceHoverRecognizer];
-[_UICampoLightweightController startTrackHoveringWithConfiguration:context:];
-[_UICampoLightweightController startTrackHoveringWithConfiguration:textSelectionContext:];
-[_UICampoLightweightController stopTrackHovering];
-[_UICampoLightweightController textSelectionContext];
-[_UICampoLightweightController updatePopoverAnchorIfNeeded];
```
