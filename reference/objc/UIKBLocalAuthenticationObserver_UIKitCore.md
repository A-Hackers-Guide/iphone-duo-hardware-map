# `UIKBLocalAuthenticationObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _isListeningForLAUINotifications;
B _localAuthenticationPresented;
B _isRestoringPreLocalAuthenticationDelegate;
B _inputUIResuming;
B _isRestoringInputViews;
@"<UIKeyInput>" _delegateResignedDuringLocalAuthentication;
@"NSUUID" _uuidOfDelegateResignedDuringLocalAuthentication;
@"NSUUID" _uuidOfSessionEndedDuringLocalAuthentication;
```

## Properties

```
@property (TB,V_localAuthenticationPresented) localAuthenticationPresented;
@property (T@"<UIKeyInput>",W,N,V_delegateResignedDuringLocalAuthentication) delegateResignedDuringLocalAuthentication;
@property (T@"NSUUID",&,N,V_uuidOfDelegateResignedDuringLocalAuthentication) uuidOfDelegateResignedDuringLocalAuthentication;
@property (T@"NSUUID",&,N,V_uuidOfSessionEndedDuringLocalAuthentication) uuidOfSessionEndedDuringLocalAuthentication;
@property (TB,N,V_isRestoringPreLocalAuthenticationDelegate) isRestoringPreLocalAuthenticationDelegate;
@property (TB,N,V_inputUIResuming) inputUIResuming;
@property (TB,N,V_isRestoringInputViews) isRestoringInputViews;
```

## Instance methods

```
-[UIKBLocalAuthenticationObserver _localAuthenticationPresented];
-[UIKBLocalAuthenticationObserver localAuthenticationPresentedOrBeingRecoveredFrom];
-[UIKBLocalAuthenticationObserver _startListeningForLAUINotificationsIfNeeded];
-[UIKBLocalAuthenticationObserver setUuidOfDelegateResignedDuringLocalAuthentication:];
-[UIKBLocalAuthenticationObserver isRestoringPreLocalAuthenticationDelegate];
-[UIKBLocalAuthenticationObserver init];
-[UIKBLocalAuthenticationObserver sessionIDForInputDelegate:];
-[UIKBLocalAuthenticationObserver _localAuthenticationDismissed];
-[UIKBLocalAuthenticationObserver inputUIResuming];
-[UIKBLocalAuthenticationObserver _stopListeningForLAUINotifications];
-[UIKBLocalAuthenticationObserver setIsRestoringInputViews:];
-[UIKBLocalAuthenticationObserver localAuthenticationPresented];
-[UIKBLocalAuthenticationObserver dealloc];
-[UIKBLocalAuthenticationObserver setIsRestoringPreLocalAuthenticationDelegate:];
-[UIKBLocalAuthenticationObserver setUuidOfSessionEndedDuringLocalAuthentication:];
-[UIKBLocalAuthenticationObserver setInputUIResuming:];
-[UIKBLocalAuthenticationObserver uuidOfSessionEndedDuringLocalAuthentication];
-[UIKBLocalAuthenticationObserver setDelegateResignedDuringLocalAuthentication:];
-[UIKBLocalAuthenticationObserver _applicationResumed:];
-[UIKBLocalAuthenticationObserver didTryToBecomeFirstResponder:];
-[UIKBLocalAuthenticationObserver setLocalAuthenticationPresented:];
-[UIKBLocalAuthenticationObserver delegateResignedDuringLocalAuthentication];
-[UIKBLocalAuthenticationObserver willTryToBecomeFirstResponder:];
-[UIKBLocalAuthenticationObserver inputDelegateWillTeardown:sessionUUID:];
-[UIKBLocalAuthenticationObserver uuidOfDelegateResignedDuringLocalAuthentication];
-[UIKBLocalAuthenticationObserver isRestoringInputViews];
-[UIKBLocalAuthenticationObserver _applicationStateIsActive];
```
