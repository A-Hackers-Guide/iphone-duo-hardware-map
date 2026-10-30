# `SBPosterEditingTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `PRUISModalRemoteViewControllerDelegate`
- 7 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"<PRUISExternallyHostedPosterEditingRequest>" _editingRequest;
@"PRUISModalRemoteViewController" _remoteViewController;
@"SBKeyboardFocusTarget" _keyboardFocusTarget;
b1 _hasNotifiedDelegateOfWillDismiss;
b1 _hasNotifiedDelegateOfDidDismiss;
B _synthesizeDelegateCallbacksFromAppearanceTransitions;
@"<SBPosterEditingTransientOverlayViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBPosterEditingTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<PRUISExternallyHostedPosterEditingRequest>",R,C,N,V_editingRequest) editingRequest;
@property (TB,N,V_synthesizeDelegateCallbacksFromAppearanceTransitions) synthesizeDelegateCallbacksFromAppearanceTransitions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPosterEditingTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBPosterEditingTransientOverlayViewController modalRemoteViewController:willDismissWithResponse:];
-[SBPosterEditingTransientOverlayViewController handleGestureDismissal];
-[SBPosterEditingTransientOverlayViewController viewWillDisappear:];
-[SBPosterEditingTransientOverlayViewController getRotationContentSettings:forWindow:];
-[SBPosterEditingTransientOverlayViewController noteDidMoveToWindowScene:];
-[SBPosterEditingTransientOverlayViewController viewDidLoad];
-[SBPosterEditingTransientOverlayViewController movesAutomaticallyToPrimaryWindowScene];
-[SBPosterEditingTransientOverlayViewController sendRequestDismissalAction];
-[SBPosterEditingTransientOverlayViewController keyboardFocusTarget];
-[SBPosterEditingTransientOverlayViewController shouldUseSceneBasedKeyboardFocus];
-[SBPosterEditingTransientOverlayViewController modalRemoteViewController:didDismissWithResponse:];
-[SBPosterEditingTransientOverlayViewController setDelegate:];
-[SBPosterEditingTransientOverlayViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBPosterEditingTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBPosterEditingTransientOverlayViewController delegate];
-[SBPosterEditingTransientOverlayViewController viewDidDisappear:];
-[SBPosterEditingTransientOverlayViewController allowsStackingOverlayContentAbove];
-[SBPosterEditingTransientOverlayViewController prefersStatusBarHidden];
-[SBPosterEditingTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBPosterEditingTransientOverlayViewController handleHomeButtonPress];
-[SBPosterEditingTransientOverlayViewController _notifyDelegateOfDidDismissWithResponse:];
-[SBPosterEditingTransientOverlayViewController _notifyDelegateOfWillDismissWithResponse:];
-[SBPosterEditingTransientOverlayViewController editingRequest];
-[SBPosterEditingTransientOverlayViewController initWithEditingRequest:];
-[SBPosterEditingTransientOverlayViewController setSynthesizeDelegateCallbacksFromAppearanceTransitions:];
-[SBPosterEditingTransientOverlayViewController synthesizeDelegateCallbacksFromAppearanceTransitions];
```
