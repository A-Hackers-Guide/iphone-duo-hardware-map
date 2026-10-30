# `_UIKeyboardArbiterClient`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIRemoteKeyboardDistributedViewSource`, `_UIAssertionControllerSubject`, `_UIKBArbiterDelegateProtocol`, `_UIRemoteKeyboardControllerDelegate`, `_UIRemoteKeyboardsEventObserverDelegate`, `_UIKeyboardArbiterClient`
- 35 instance variables, 41 properties, 155 instance methods, 4 class methods

## Instance variables

```
i _ignoreLayoutSubviews;
i _externalSuppression;
@"NSHashTable" _windowControllers;
i _recursionCheck;
@"_UIAssertionController" _assertionController;
B _shouldFence;
B _snapshotting;
B _handlingRemoteEvent;
B _disableBecomeFirstResponder;
B _expectingInitialState;
B _avoidDisableKeyboard;
B _currentInputDestination;
B _keyboardUIHost;
B _expectedSuppression;
B _enqueuedWillEnterForegroundActions;
B _windowEnabled;
B _updatingHeight;
B _didSignalKeyboardChangedForCurrentKeyboard;
B _deactivatedByControlCenter;
B _deactivatedBySystemGesture;
B _handlingKeyboardTransition;
@"_UIKeyboardChangedInformation" _currentClientState;
@"_UIKeyboardUIInformation" _currentUIState;
@"<_UIKeyboardUIStateDelegate>" _kbUIStateDelegate;
@"UIInputWindowController" _inputWindowRootViewController;
q _lastEventSource;
@"<_UIKBArbiterClientKeyboardChangeDelegate>" _changeInfoDelegate;
@"NSXPCConnection" _connection;
@"UIView" _keyboardSnapshot;
@"_UIKeyboardChangedInformation" _backupState;
q _keyboardSource;
Q _hostedCount;
@"_UIRemoteKeyboardsEventObserver" _eventObserver;
@"FBSScene" _requiredScene;
d _heightForRemoteIAVPlaceholderIfNecessary;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,V_expectingInitialState) expectingInitialState;
@property (TB,V_avoidDisableKeyboard) avoidDisableKeyboard;
@property (TB,N,V_currentInputDestination) currentInputDestination;
@property (TB,N,V_keyboardUIHost) keyboardUIHost;
@property (TB,N,V_expectedSuppression) expectedSuppression;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (TB,N,V_enqueuedWillEnterForegroundActions) enqueuedWillEnterForegroundActions;
@property (T@"UIView",&,N,V_keyboardSnapshot) keyboardSnapshot;
@property (TB,N,V_windowEnabled) windowEnabled;
@property (TB,V_updatingHeight) updatingHeight;
@property (TB,N,V_didSignalKeyboardChangedForCurrentKeyboard) didSignalKeyboardChangedForCurrentKeyboard;
@property (T@"_UIKeyboardChangedInformation",&,N,V_backupState) backupState;
@property (Tq,N,V_keyboardSource) keyboardSource;
@property (TQ,N,V_hostedCount) hostedCount;
@property (T@"_UIRemoteKeyboardsEventObserver",&,N,V_eventObserver) eventObserver;
@property (TB,N,V_deactivatedByControlCenter) deactivatedByControlCenter;
@property (TB,N,V_deactivatedBySystemGesture) deactivatedBySystemGesture;
@property (T@"FBSScene",&,N,V_requiredScene) requiredScene;
@property (Tq,N,V_lastEventSource) lastEventSource;
@property (TB,N,V_handlingKeyboardTransition) handlingKeyboardTransition;
@property (Td,N,V_heightForRemoteIAVPlaceholderIfNecessary) heightForRemoteIAVPlaceholderIfNecessary;
@property (T@"_UIKeyboardChangedInformation",&,N,V_currentClientState) currentClientState;
@property (T@"_UIKeyboardUIInformation",&,N,V_currentUIState) currentUIState;
@property (TB,N,V_shouldFence) shouldFence;
@property (T@"<_UIKeyboardUIStateDelegate>",W,N,V_kbUIStateDelegate) kbUIStateDelegate;
@property (T@"UIInputWindowController",&,N,V_inputWindowRootViewController) inputWindowRootViewController;
@property (TB,N,V_snapshotting) snapshotting;
@property (TB,N,V_handlingRemoteEvent) handlingRemoteEvent;
@property (T@"<_UIKBArbiterClientKeyboardChangeDelegate>",W,N,V_changeInfoDelegate) changeInfoDelegate;
@property (TB,N,V_disableBecomeFirstResponder) disableBecomeFirstResponder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R) keyboardVisible;
@property (TB,R) keyboardActive;
@property (TB,R) remoteKeyboardUndocked;
```

## Class methods

```
+[_UIKeyboardArbiterClient enabled];
+[_UIKeyboardArbiterClient mainBundleIdentifier];
+[_UIKeyboardArbiterClient automaticSharedArbiterClient];
+[_UIKeyboardArbiterClient keyboardClientFBSSceneIdentityStringOrIdentifierFromScene:];
```

## Instance methods

```
-[_UIKeyboardArbiterClient completeTransition:withInfo:];
-[_UIKeyboardArbiterClient startTransition:withInfo:];
-[_UIKeyboardArbiterClient vendKeyboardSuppressionAssertionForReason:];
-[_UIKeyboardArbiterClient updateTransition:withInfo:];
-[_UIKeyboardArbiterClient setRequiredScene:];
-[_UIKeyboardArbiterClient setPlacement:quietly:animated:generateSplitNotification:];
-[_UIKeyboardArbiterClient queue_keyboardUIDidChange:onComplete:];
-[_UIKeyboardArbiterClient willResume:];
-[_UIKeyboardArbiterClient assertionActivationStateForType:];
-[_UIKeyboardArbiterClient isOnScreenRotating];
-[_UIKeyboardArbiterClient hasActiveKeyboardSuppressionAssertionsForReason:];
-[_UIKeyboardArbiterClient prepareForHostedWindowWithScene:];
-[_UIKeyboardArbiterClient keyboardVisible];
-[_UIKeyboardArbiterClient queue_getDebugInfoWithCompletion:];
-[_UIKeyboardArbiterClient allowedToShowKeyboard];
-[_UIKeyboardArbiterClient peekApplicationEvent:];
-[_UIKeyboardArbiterClient restorePreservedInputViewsIfNecessary];
-[_UIKeyboardArbiterClient didSuspend:];
-[_UIKeyboardArbiterClient queue_keyboardSuppressed:withCompletion:];
-[_UIKeyboardArbiterClient init];
-[_UIKeyboardArbiterClient keyboardChangedCompleted];
-[_UIKeyboardArbiterClient lastEventSource];
-[_UIKeyboardArbiterClient updateEventSource:options:];
-[_UIKeyboardArbiterClient backupState];
-[_UIKeyboardArbiterClient requiredScene];
-[_UIKeyboardArbiterClient queue_keyboardTransition:event:withInfo:onComplete:];
-[_UIKeyboardArbiterClient performOnControllers:];
-[_UIKeyboardArbiterClient signalToProxyKeyboardChanged:onCompletion:];
-[_UIKeyboardArbiterClient resetSnapshotWithWindowCheck:];
-[_UIKeyboardArbiterClient dealloc];
-[_UIKeyboardArbiterClient heightForRemoteIAVPlaceholderIfNecessary];
-[_UIKeyboardArbiterClient didSignalKeyboardChangedForCurrentKeyboard];
-[_UIKeyboardArbiterClient disableBecomeFirstResponder];
-[_UIKeyboardArbiterClient configureArbiterCommunication:];
-[_UIKeyboardArbiterClient arbiterProxy];
-[_UIKeyboardArbiterClient stopConnection];
-[_UIKeyboardArbiterClient shouldSnapshot];
-[_UIKeyboardArbiterClient shouldAllowInputViewsRestoredForId:];
-[_UIKeyboardArbiterClient currentHostedPIDs];
-[_UIKeyboardArbiterClient setBackupState:];
-[_UIKeyboardArbiterClient remoteKeyboardUndocked:];
-[_UIKeyboardArbiterClient hasWindowHostingCallerID:];
-[_UIKeyboardArbiterClient checkState];
-[_UIKeyboardArbiterClient reloadForSnapshotting];
-[_UIKeyboardArbiterClient addIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClient _layoutKeyboardViews:];
-[_UIKeyboardArbiterClient keyboardActive];
-[_UIKeyboardArbiterClient performOnDistributedControllers:];
-[_UIKeyboardArbiterClient setWindowEnabled:];
-[_UIKeyboardArbiterClient setHandlingRemoteEvent:];
-[_UIKeyboardArbiterClient performOnLocalDistributedControllers:];
-[_UIKeyboardArbiterClient removeIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClient queue_keyboardIAVChanged:onComplete:];
-[_UIKeyboardArbiterClient ignoreLayoutNotifications:];
-[_UIKeyboardArbiterClient verifyPlacement];
-[_UIKeyboardArbiterClient finishWithHostedWindow];
-[_UIKeyboardArbiterClient queue_endInputSessionWithCompletion:];
-[_UIKeyboardArbiterClient queue_keyboardChanged:onComplete:];
-[_UIKeyboardArbiterClient registerController:];
-[_UIKeyboardArbiterClient handlingRemoteEvent];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:updatePlacement:wantsAssistant:];
-[_UIKeyboardArbiterClient updateEventSource:options:responder:];
-[_UIKeyboardArbiterClient connection];
-[_UIKeyboardArbiterClient _isArbiterClientReadyForWritingToolsToHandleKeyboardTracking];
-[_UIKeyboardArbiterClient _updateEventSource:options:];
-[_UIKeyboardArbiterClient _performOnDistributedControllersExceptSelf:];
-[_UIKeyboardArbiterClient setShouldFence:];
-[_UIKeyboardArbiterClient queue_failedConnection:];
-[_UIKeyboardArbiterClient setConnection:];
-[_UIKeyboardArbiterClient remoteKeyboardUndocked];
-[_UIKeyboardArbiterClient isSpotlight:];
-[_UIKeyboardArbiterClient assertionActivationStateChangedToState:forType:];
-[_UIKeyboardArbiterClient performRequiredSceneUpdateIfPermittedForChildSceneHostWindow:];
-[_UIKeyboardArbiterClient checkConnection];
-[_UIKeyboardArbiterClient shouldFence];
-[_UIKeyboardArbiterClient queue_sceneBecameFocused:withCompletion:];
-[_UIKeyboardArbiterClient _updateEventSource:options:responder:];
-[_UIKeyboardArbiterClient eventObserver];
-[_UIKeyboardArbiterClient localSceneCount];
-[_UIKeyboardArbiterClient inputWindowRootViewController];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:];
-[_UIKeyboardArbiterClient sceneUpdated];
-[_UIKeyboardArbiterClient setLastEventSource:];
-[_UIKeyboardArbiterClient vendKeyboardSuppressionAssertionForReason:type:];
-[_UIKeyboardArbiterClient _postInputSourceDidChangeNotificationForResponder:];
-[_UIKeyboardArbiterClient setSnapshotting:];
-[_UIKeyboardArbiterClient setDidSignalKeyboardChangedForCurrentKeyboard:];
-[_UIKeyboardArbiterClient snapshotting];
-[_UIKeyboardArbiterClient updatingHeight];
-[_UIKeyboardArbiterClient hasAnyHostedViews];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:];
-[_UIKeyboardArbiterClient setCurrentUIState:];
-[_UIKeyboardArbiterClient unregisterController:];
-[_UIKeyboardArbiterClient controllerDidLayoutSubviews:];
-[_UIKeyboardArbiterClient setSuppressingKeyboard:forScene:];
-[_UIKeyboardArbiterClient vendEmojiKeyboardPrewarmingAssertionForReason:];
-[_UIKeyboardArbiterClient queue_setLastEventSource:withCompletion:];
-[_UIKeyboardArbiterClient setEventObserver:];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:updatePlacement:];
-[_UIKeyboardArbiterClient startConnection];
-[_UIKeyboardArbiterClient cleanSuppression];
-[_UIKeyboardArbiterClient queue_keyboardChangedWithCompletion:];
-[_UIKeyboardArbiterClient snapsShotKeyboard];
-[_UIKeyboardArbiterClient setHostedCount:];
-[_UIKeyboardArbiterClient _didHandleKeyboardClientChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:];
-[_UIKeyboardArbiterClient _handleKeyboardChanged:isLocal:onComplete:];
-[_UIKeyboardArbiterClient _preserveInputViewsForClientChange:clientInfo:snapshotIfNecessary:];
-[_UIKeyboardArbiterClient addWindowHostingPID:callerID:];
-[_UIKeyboardArbiterClient applicationResume:];
-[_UIKeyboardArbiterClient arbiterConnection];
-[_UIKeyboardArbiterClient avoidDisableKeyboard];
-[_UIKeyboardArbiterClient changeInfoDelegate];
-[_UIKeyboardArbiterClient currentClientState];
-[_UIKeyboardArbiterClient currentInputDestination];
-[_UIKeyboardArbiterClient currentUIState];
-[_UIKeyboardArbiterClient deactivatedByControlCenter];
-[_UIKeyboardArbiterClient deactivatedBySystemGesture];
-[_UIKeyboardArbiterClient didFailArbiterConnection];
-[_UIKeyboardArbiterClient enqueuedWillEnterForegroundActions];
-[_UIKeyboardArbiterClient existingInputWindowRootViewController];
-[_UIKeyboardArbiterClient expectedSuppression];
-[_UIKeyboardArbiterClient expectingInitialState];
-[_UIKeyboardArbiterClient handlingKeyboardTransition];
-[_UIKeyboardArbiterClient hasWindowHostingPID:];
-[_UIKeyboardArbiterClient hostedCount];
-[_UIKeyboardArbiterClient initWithShouldConnect:];
-[_UIKeyboardArbiterClient isHostedInAnotherProcess];
-[_UIKeyboardArbiterClient kbUIStateDelegate];
-[_UIKeyboardArbiterClient keyboardClientDidChange:];
-[_UIKeyboardArbiterClient keyboardSnapshot];
-[_UIKeyboardArbiterClient keyboardSource];
-[_UIKeyboardArbiterClient keyboardUIHost];
-[_UIKeyboardArbiterClient performOnExistingControllers:];
-[_UIKeyboardArbiterClient removeWindowHostingPID:callerID:];
-[_UIKeyboardArbiterClient resignFirstResponderIfNeeded];
-[_UIKeyboardArbiterClient setAvoidDisableKeyboard:];
-[_UIKeyboardArbiterClient setChangeInfoDelegate:];
-[_UIKeyboardArbiterClient setCurrentClientState:];
-[_UIKeyboardArbiterClient setCurrentInputDestination:];
-[_UIKeyboardArbiterClient setDeactivatedByControlCenter:];
-[_UIKeyboardArbiterClient setDeactivatedBySystemGesture:];
-[_UIKeyboardArbiterClient setEnqueuedWillEnterForegroundActions:];
-[_UIKeyboardArbiterClient setExpectedSuppression:];
-[_UIKeyboardArbiterClient setExpectingInitialState:];
-[_UIKeyboardArbiterClient setHandlingKeyboardTransition:];
-[_UIKeyboardArbiterClient setHeightForRemoteIAVPlaceholderIfNecessary:];
-[_UIKeyboardArbiterClient setInputWindowRootViewController:];
-[_UIKeyboardArbiterClient setKbUIStateDelegate:];
-[_UIKeyboardArbiterClient setKeyboardSnapshot:];
-[_UIKeyboardArbiterClient setKeyboardSource:];
-[_UIKeyboardArbiterClient setKeyboardUIHost:];
-[_UIKeyboardArbiterClient setUpdatingHeight:];
-[_UIKeyboardArbiterClient startConnectionWithCompletion:];
-[_UIKeyboardArbiterClient syncKeyboardUIChangeInfo:];
-[_UIKeyboardArbiterClient windowEnabled];
```
