# `_UIKeyboardArbiterClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UITextInputSourceCacheProtocol`
- 0 instance variables, 8 properties, 48 instance methods, 0 class methods

## Properties

```
@property (TB,R) keyboardVisible;
@property (TB,R) keyboardActive;
@property (TB,R) updatingHeight;
@property (TB,R) remoteKeyboardUndocked;
@property (Td,R,N) heightForRemoteIAVPlaceholderIfNecessary;
@property (TB,R,N) handlingRemoteEvent;
@property (TB,N) shouldFence;
@property (TB,N) snapshotting;
```

## Instance methods

```
-[_UIKeyboardArbiterClient vendKeyboardSuppressionAssertionForReason:];
-[_UIKeyboardArbiterClient hasActiveKeyboardSuppressionAssertionsForReason:];
-[_UIKeyboardArbiterClient prepareForHostedWindowWithScene:];
-[_UIKeyboardArbiterClient keyboardVisible];
-[_UIKeyboardArbiterClient peekApplicationEvent:];
-[_UIKeyboardArbiterClient restorePreservedInputViewsIfNecessary];
-[_UIKeyboardArbiterClient setKeyboardSceneIdentifierEnteringForegroundForScene:];
-[_UIKeyboardArbiterClient performOnControllers:];
-[_UIKeyboardArbiterClient heightForRemoteIAVPlaceholderIfNecessary];
-[_UIKeyboardArbiterClient shouldAllowInputViewsRestoredForId:];
-[_UIKeyboardArbiterClient remoteKeyboardUndocked:];
-[_UIKeyboardArbiterClient hasWindowHostingCallerID:];
-[_UIKeyboardArbiterClient checkState];
-[_UIKeyboardArbiterClient addIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClient keyboardActive];
-[_UIKeyboardArbiterClient performOnDistributedControllers:];
-[_UIKeyboardArbiterClient performOnLocalDistributedControllers:];
-[_UIKeyboardArbiterClient removeIgnoredSceneIdentityTokenString:];
-[_UIKeyboardArbiterClient ignoreLayoutNotifications:];
-[_UIKeyboardArbiterClient verifyPlacement];
-[_UIKeyboardArbiterClient finishWithHostedWindow];
-[_UIKeyboardArbiterClient registerController:];
-[_UIKeyboardArbiterClient handlingRemoteEvent];
-[_UIKeyboardArbiterClient isWritingToolsHostingViewService];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:updatePlacement:wantsAssistant:];
-[_UIKeyboardArbiterClient _isArbiterClientReadyForWritingToolsToHandleKeyboardTracking];
-[_UIKeyboardArbiterClient setShouldFence:];
-[_UIKeyboardArbiterClient allowedToEnableKeyboardWindow];
-[_UIKeyboardArbiterClient remoteKeyboardUndocked];
-[_UIKeyboardArbiterClient performRequiredSceneUpdateIfPermittedForChildSceneHostWindow:];
-[_UIKeyboardArbiterClient shouldFence];
-[_UIKeyboardArbiterClient inputWindowRootViewController];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:];
-[_UIKeyboardArbiterClient sceneUpdated];
-[_UIKeyboardArbiterClient vendKeyboardSuppressionAssertionForReason:type:];
-[_UIKeyboardArbiterClient setSnapshotting:];
-[_UIKeyboardArbiterClient snapshotting];
-[_UIKeyboardArbiterClient updatingHeight];
-[_UIKeyboardArbiterClient hasAnyHostedViews];
-[_UIKeyboardArbiterClient unregisterController:];
-[_UIKeyboardArbiterClient setSuppressingKeyboard:forScene:];
-[_UIKeyboardArbiterClient vendEmojiKeyboardPrewarmingAssertionForReason:];
-[_UIKeyboardArbiterClient setDisableBecomeFirstResponder:forSuppressionAssertion:updatePlacement:];
-[_UIKeyboardArbiterClient addWindowHostingPID:callerID:];
-[_UIKeyboardArbiterClient existingInputWindowRootViewController];
-[_UIKeyboardArbiterClient hasWindowHostingPID:];
-[_UIKeyboardArbiterClient performOnExistingControllers:];
-[_UIKeyboardArbiterClient removeWindowHostingPID:callerID:];
```
