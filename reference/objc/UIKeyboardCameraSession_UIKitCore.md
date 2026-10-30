# `UIKeyboardCameraSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKeyboardCameraViewControllerDelegate`, `UIDimmingViewDelegate`, `UIViewControllerTransitioningDelegate`, `UIAdaptivePresentationControllerDelegate`, `UITextInputSessionActionAnalyticsDelegateSource`
- 18 instance variables, 10 properties, 34 instance methods, 7 class methods

## Instance variables

```
@"UIKeyboardCameraViewController" _keyboardCameraViewController;
@"UIKeyboardCameraBasePresentationController" _presentationController;
@"<UIViewControllerAnimatedTransitioning>" _animationController;
B _didFindText;
@"NSString" _keyboardCameraCandidateString;
@ _sender;
B _presentingOverKeyboard;
B _isTextInputResponder;
B _isWebResponder;
B _isTextFormattingResponder;
B _respondsToKeyboardInputShouldInsertText;
B _isSingleLineDocument;
B _didCleanup;
B _isSecureFieldEditor;
B _shouldSuppressSoftwareKeyboard;
B _shouldResignFirstResponderWhenDone;
@"UITextInputSessionActionAnalytics" _sessionAnalytics;
@"UIResponder<UIKeyInput>" _responder;
```

## Properties

```
@property (T@"UITextInputSessionActionAnalytics",R,V_sessionAnalytics) sessionAnalytics;
@property (TB,N,V_shouldSuppressSoftwareKeyboard) shouldSuppressSoftwareKeyboard;
@property (T@"UIResponder<UIKeyInput>",R,N,V_responder) responder;
@property (TB,R,N) isPresenting;
@property (TB,R,N) isPresented;
@property (TB,R,N) isDismissing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardCameraSession _textContentTypesForDataDetection];
+[UIKeyboardCameraSession sharedSession];
+[UIKeyboardCameraSession shouldShowTextSuggestionForResponder:];
+[UIKeyboardCameraSession updatesGuideDuringRotation];
+[UIKeyboardCameraSession isEnabled];
+[UIKeyboardCameraSession keyboardCameraContentTypeForResponder:];
+[UIKeyboardCameraSession activeSession];
```

## Instance methods

```
-[UIKeyboardCameraSession _firstResponderDidChange:];
-[UIKeyboardCameraSession _addObservers];
-[UIKeyboardCameraSession isPresented];
-[UIKeyboardCameraSession shouldSuppressSoftwareKeyboard];
-[UIKeyboardCameraSession animationControllerForDismissedController:];
-[UIKeyboardCameraSession dimmingViewWasTapped:];
-[UIKeyboardCameraSession presentationControllerDidDismiss:];
-[UIKeyboardCameraSession animationControllerForPresentedController:presentingController:sourceController:];
-[UIKeyboardCameraSession presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[UIKeyboardCameraSession dealloc];
-[UIKeyboardCameraSession responder];
-[UIKeyboardCameraSession _delegateAsResponder];
-[UIKeyboardCameraSession isDismissing];
-[UIKeyboardCameraSession _keyboardAboutToHide:];
-[UIKeyboardCameraSession _didEnterBackground:];
-[UIKeyboardCameraSession sessionAnalytics];
-[UIKeyboardCameraSession _sessionIdentifier];
-[UIKeyboardCameraSession setShouldSuppressSoftwareKeyboard:];
-[UIKeyboardCameraSession isPresenting];
-[UIKeyboardCameraSession _cleanupKeyboardCameraAndShouldInsertText:];
-[UIKeyboardCameraSession _dismissKeyboardCamera];
-[UIKeyboardCameraSession _inputModeDidChange:];
-[UIKeyboardCameraSession _keyboardCameraPreparationDidComplete];
-[UIKeyboardCameraSession _makeResponderEditableIfNecessary];
-[UIKeyboardCameraSession _overrideTextInputSource];
-[UIKeyboardCameraSession _show];
-[UIKeyboardCameraSession _textFormattingResponder];
-[UIKeyboardCameraSession _textInputResponder];
-[UIKeyboardCameraSession _updatePreviewWithString:];
-[UIKeyboardCameraSession endActiveSession];
-[UIKeyboardCameraSession keyboardCameraDidAccept];
-[UIKeyboardCameraSession keyboardCameraDidCancel];
-[UIKeyboardCameraSession keyboardCameraDidUpdateString:];
-[UIKeyboardCameraSession showForResponder:sender:rtiConfiguration:];
```
