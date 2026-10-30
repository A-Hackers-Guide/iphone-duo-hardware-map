# `_UIViewServiceTextEffectsOperator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHostedWindowDelegate`, `_UIViewServiceSessionActivityProviding`, `_UIViewServiceTextEffectsOperator_RemoteViewControllerInterface`, `_UIViewServiceDeputy`, `_UIViewServiceDeputyRotationDelegate`
- 17 instance variables, 6 properties, 44 instance methods, 4 class methods

## Instance variables

```
@ _remoteViewControllerProxy;
@"NSUUID" _sessionIdentifier;
B _wasInvalidated;
@"_UIAsyncInvocation" _prepareForDisconnectionInvocation;
@"_UIAsyncInvocation" _invalidationInvocation;
@"_UIHostedWindow" _hostedWindow;
{CGPoint="x"d"y"d} _windowOrigin;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _safeAreaInsets;
{CGSize="width"d"height"d} _hostedViewSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hostedViewReference;
B _canRestoreInputViews;
B _isRestoringInputViews;
B _didResignForDisappear;
B _localVCDisablesAutomaticBehaviors;
@"_UIViewServiceSessionActivityRecord" _sessionActivityRecord;
@"_UITouchesBeganObserverGestureRecognizer" _hostedTEWActivityObserverGesture;
@"_UITouchesBeganObserverGestureRecognizer" _hostedRemoteKeyboardWindowActivityObserverGesture;
```

## Properties

```
@property (TQ,R,N) _providerType;
@property (T@"NSUUID",R,N) _sessionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewServiceTextEffectsOperator initialize];
+[_UIViewServiceTextEffectsOperator XPCInterface];
+[_UIViewServiceTextEffectsOperator _shouldAddServiceOperator];
+[_UIViewServiceTextEffectsOperator operatorWithRemoteViewControllerProxy:hostPID:sessionIdentifier:];
```

## Instance methods

```
-[_UIViewServiceTextEffectsOperator willRotateToInterfaceOrientation:duration:];
-[_UIViewServiceTextEffectsOperator _objc_initiateDealloc];
-[_UIViewServiceTextEffectsOperator dealloc];
-[_UIViewServiceTextEffectsOperator invalidate];
-[_UIViewServiceTextEffectsOperator _queue];
-[_UIViewServiceTextEffectsOperator rotateToInterfaceOrientation:duration:];
-[_UIViewServiceTextEffectsOperator _sessionIdentifier];
-[_UIViewServiceTextEffectsOperator _associateHostedTextEffectsWindowWithViewServiceSessionIfNeeded];
-[_UIViewServiceTextEffectsOperator _disassociateHostedKeyboardWindowFromViewServiceSessionIfNeeded];
-[_UIViewServiceTextEffectsOperator __setRemoteTextEffectsWindowMatchesLayerWithContextId:renderId:];
-[_UIViewServiceTextEffectsOperator _invalidateUnconditionallyThen:];
-[_UIViewServiceTextEffectsOperator _windowDidBecomeApplicationKey:];
-[_UIViewServiceTextEffectsOperator forceSyncToStatusBarOrientation];
-[_UIViewServiceTextEffectsOperator __createHostedTextEffectsWithReplyHandler:];
-[_UIViewServiceTextEffectsOperator __hostDidEnterBackground];
-[_UIViewServiceTextEffectsOperator __hostDidReceiveGestureDirection:authenticationMessage:];
-[_UIViewServiceTextEffectsOperator __hostViewDidMoveToScreenWithNewHostingHandleReplyHandler:];
-[_UIViewServiceTextEffectsOperator __hostViewWillAppear:];
-[_UIViewServiceTextEffectsOperator __hostViewWillDisappear:];
-[_UIViewServiceTextEffectsOperator __hostWillEnterForeground];
-[_UIViewServiceTextEffectsOperator __prepareForDisconnectionWithCompletionHandler:];
-[_UIViewServiceTextEffectsOperator __setHostedViewReference:];
-[_UIViewServiceTextEffectsOperator __setHostedViewSize:];
-[_UIViewServiceTextEffectsOperator __setNextAutomaticOrderOutDirection:duration:];
-[_UIViewServiceTextEffectsOperator __setSafeAreaInsets:];
-[_UIViewServiceTextEffectsOperator __setWindowOffset:];
-[_UIViewServiceTextEffectsOperator _associateHostedKeyboardWindowWithViewServiceSessionIfNeeded];
-[_UIViewServiceTextEffectsOperator _disassociateTextEffectsWindowFromViewServiceSessionIfNeeded];
-[_UIViewServiceTextEffectsOperator _handleRemoteKeyboardActivityObserverGesture:];
-[_UIViewServiceTextEffectsOperator _handleTEWActivityObserverGesture:];
-[_UIViewServiceTextEffectsOperator _inputResponderReloaded:];
-[_UIViewServiceTextEffectsOperator _prepareForDisconnectionUnconditionallyThen:];
-[_UIViewServiceTextEffectsOperator _providerType];
-[_UIViewServiceTextEffectsOperator _reloadSafeInsets];
-[_UIViewServiceTextEffectsOperator _removeTextEffectsWindowMatchAnimations];
-[_UIViewServiceTextEffectsOperator _resetHostedViewSize];
-[_UIViewServiceTextEffectsOperator _restoreInputViews];
-[_UIViewServiceTextEffectsOperator _screenInterfaceOrientationDidChange:];
-[_UIViewServiceTextEffectsOperator _viewServiceHostWillEnterForeground:];
-[_UIViewServiceTextEffectsOperator finishRotationFromInterfaceOrientation:];
-[_UIViewServiceTextEffectsOperator hostedWindow:didSetFirstResponder:];
-[_UIViewServiceTextEffectsOperator makeHostWindowKey];
-[_UIViewServiceTextEffectsOperator performOnRelevantWindows:];
-[_UIViewServiceTextEffectsOperator setHostedWindow:disableAutomaticBehaviors:];
```
