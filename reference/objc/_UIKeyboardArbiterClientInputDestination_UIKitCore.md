# `_UIKeyboardArbiterClientInputDestination`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKeyboardArbiterClient`
- 15 instance variables, 5 properties, 84 instance methods, 1 class methods

## Instance variables

```
B _deactivatedBySystemAnimation;
B _resignActiveByControlCenter;
B _hadFocusBeforeOverlay;
@"UIWindowScene" _suppressedScene;
i _hostedCount;
@"UIScreen" _lastScreen;
@"NSObject<OS_os_transaction>" _clientChangeResponseTransaction;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientChangeResponseLock;
@"NSMutableSet" _ignoredSceneIdentityTokenStringSet;
@"NSString" _keyboardSceneIdentifierEnteringForeground;
B _updatingKeyWindow;
@"NSString" _focusedSceneIdentityStringOrIdentifier;
@"NSMutableSet" _pendingKeyboardGrabs;
@"NSMutableSet" _activePIDs;
@"NSMutableDictionary" _callerIDs;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_pendingKeyboardGrabs) pendingKeyboardGrabs;
@property (T@"NSMutableSet",&,N,V_activePIDs) activePIDs;
@property (T@"NSMutableDictionary",&,N,V_callerIDs) callerIDs;
@property (TB,N,V_updatingKeyWindow) updatingKeyWindow;
@property (T@"NSString",C,N,V_focusedSceneIdentityStringOrIdentifier) focusedSceneIdentityStringOrIdentifier;
```

## Class methods

```
+[_UIKeyboardArbiterClientInputDestination currentBundleIdentifier];
```

## Instance methods

```
-[_UIKeyboardArbiterClientInputDestination queue_keyboardUIDidChange:onComplete:];
-[_UIKeyboardArbiterClientInputDestination willResume:];
-[_UIKeyboardArbiterClientInputDestination prepareForHostedWindowWithScene:];
-[_UIKeyboardArbiterClientInputDestination setWindowHostingPID:active:];
-[_UIKeyboardArbiterClientInputDestination allowedToShowKeyboard];
-[_UIKeyboardArbiterClientInputDestination applicationKeyWindowDidChange:];
-[_UIKeyboardArbiterClientInputDestination peekApplicationEvent:];
-[_UIKeyboardArbiterClientInputDestination restorePreservedInputViewsIfNecessary];
-[_UIKeyboardArbiterClientInputDestination didSuspend:];
-[_UIKeyboardArbiterClientInputDestination sceneDidDisconnect:];
-[_UIKeyboardArbiterClientInputDestination _sceneFocusUpdatePermittedForWindow:];
-[_UIKeyboardArbiterClientInputDestination setKeyboardSceneIdentifierEnteringForegroundForScene:];
-[_UIKeyboardArbiterClientInputDestination init];
-[_UIKeyboardArbiterClientInputDestination sceneDidActivate:];
-[_UIKeyboardArbiterClientInputDestination sceneDidEnterBackground:];
-[_UIKeyboardArbiterClientInputDestination didBecomeActive:];
-[_UIKeyboardArbiterClientInputDestination signalToProxyKeyboardChanged:onCompletion:];
-[_UIKeyboardArbiterClientInputDestination setUpdatingKeyWindow:];
-[_UIKeyboardArbiterClientInputDestination setWindowEnabled:force:];
-[_UIKeyboardArbiterClientInputDestination queue_activeProcessResignWithCompletion:];
-[_UIKeyboardArbiterClientInputDestination configureArbiterCommunication:];
-[_UIKeyboardArbiterClientInputDestination setFocusedSceneIdentityStringOrIdentifier:];
-[_UIKeyboardArbiterClientInputDestination stopConnection];
-[_UIKeyboardArbiterClientInputDestination shouldSnapshot];
-[_UIKeyboardArbiterClientInputDestination currentHostedPIDs];
-[_UIKeyboardArbiterClientInputDestination willResignActive:];
-[_UIKeyboardArbiterClientInputDestination hasWindowHostingCallerID:];
-[_UIKeyboardArbiterClientInputDestination addIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClientInputDestination _layoutKeyboardViews:];
-[_UIKeyboardArbiterClientInputDestination keyboardFrameIncludingRemoteIAV];
-[_UIKeyboardArbiterClientInputDestination setWindowEnabled:];
-[_UIKeyboardArbiterClientInputDestination removeIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClientInputDestination finishWithHostedWindow];
-[_UIKeyboardArbiterClientInputDestination _activeScreen];
-[_UIKeyboardArbiterClientInputDestination queue_endInputSessionWithCompletion:];
-[_UIKeyboardArbiterClientInputDestination queue_keyboardChanged:onComplete:];
-[_UIKeyboardArbiterClientInputDestination isWritingToolsHostingViewService];
-[_UIKeyboardArbiterClientInputDestination userSelectedApp:onCompletion:];
-[_UIKeyboardArbiterClientInputDestination allowedToEnableKeyboardWindow];
-[_UIKeyboardArbiterClientInputDestination _sceneFocusPermittedForApplication];
-[_UIKeyboardArbiterClientInputDestination queue_setKeyboardDisabled:withCompletion:];
-[_UIKeyboardArbiterClientInputDestination performRequiredSceneUpdateIfPermittedForChildSceneHostWindow:];
-[_UIKeyboardArbiterClientInputDestination focusedSceneIdentityStringOrIdentifier];
-[_UIKeyboardArbiterClientInputDestination queue_sceneBecameFocused:withCompletion:];
-[_UIKeyboardArbiterClientInputDestination sceneWillEnterForeground:];
-[_UIKeyboardArbiterClientInputDestination localSceneCount];
-[_UIKeyboardArbiterClientInputDestination clearKeyboardSceneIdentifierEnteringForeground:];
-[_UIKeyboardArbiterClientInputDestination queue_keyboardArbiterClientHandleChanged:withCompletion:];
-[_UIKeyboardArbiterClientInputDestination setSnapshotting:];
-[_UIKeyboardArbiterClientInputDestination setSuppressingKeyboard:forScene:];
-[_UIKeyboardArbiterClientInputDestination startConnection];
-[_UIKeyboardArbiterClientInputDestination keyboardUIDidChange:onComplete:];
-[_UIKeyboardArbiterClientInputDestination handleKeyboardUITrackingChange:];
-[_UIKeyboardArbiterClientInputDestination _didHandleKeyboardClientChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:];
-[_UIKeyboardArbiterClientInputDestination _preserveInputViewsForClientChange:snapshotIfNecessary:];
-[_UIKeyboardArbiterClientInputDestination activePIDs];
-[_UIKeyboardArbiterClientInputDestination addWindowHostingPID:callerID:];
-[_UIKeyboardArbiterClientInputDestination callerIDs];
-[_UIKeyboardArbiterClientInputDestination completeMoveKeyboard];
-[_UIKeyboardArbiterClientInputDestination didFailArbiterConnection];
-[_UIKeyboardArbiterClientInputDestination didRemoveDeactivationReason:];
-[_UIKeyboardArbiterClientInputDestination handleKeyboardUIDidChange:];
-[_UIKeyboardArbiterClientInputDestination hasWindowHostingPID:];
-[_UIKeyboardArbiterClientInputDestination inputDestinationDidChange:withIAVHeight:isIAVRelevant:notifyRemote:forScene:];
-[_UIKeyboardArbiterClientInputDestination isHostedInAnotherProcess];
-[_UIKeyboardArbiterClientInputDestination needsToShowKeyboard];
-[_UIKeyboardArbiterClientInputDestination needsToShowKeyboardForViewServiceHost];
-[_UIKeyboardArbiterClientInputDestination pendingKeyboardGrabs];
-[_UIKeyboardArbiterClientInputDestination removeWindowHostingPID:callerID:];
-[_UIKeyboardArbiterClientInputDestination resignFirstResponderIfNeeded];
-[_UIKeyboardArbiterClientInputDestination setActivePIDs:];
-[_UIKeyboardArbiterClientInputDestination setCallerIDs:];
-[_UIKeyboardArbiterClientInputDestination setCurrentClientState:];
-[_UIKeyboardArbiterClientInputDestination setPendingKeyboardGrabs:];
-[_UIKeyboardArbiterClientInputDestination shouldIgnoreInputDestinationChange:withIAVHeight:];
-[_UIKeyboardArbiterClientInputDestination signalToProxyKeyboardChanged:reason:onCompletion:];
-[_UIKeyboardArbiterClientInputDestination startConnectionWithCompletion:];
-[_UIKeyboardArbiterClientInputDestination syncKeyboardUIChangeInfo:];
-[_UIKeyboardArbiterClientInputDestination updateWindowState];
-[_UIKeyboardArbiterClientInputDestination updatingKeyWindow];
-[_UIKeyboardArbiterClientInputDestination wantsToShowKeyboard];
-[_UIKeyboardArbiterClientInputDestination wantsToShowKeyboardForViewServiceHost];
-[_UIKeyboardArbiterClientInputDestination willAddDeactivationReason:];
-[_UIKeyboardArbiterClientInputDestination writingToolsAllowsSceneToRequestFocusOnPeekApplicationEvent];
```
