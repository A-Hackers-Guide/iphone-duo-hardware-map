# `_UIKeyboardUIInformation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 28 instance variables, 28 properties, 64 instance methods, 2 class methods

## Instance variables

```
B _keyboardOnScreen;
B _assistantBarVisible;
B _requiresHeightForIntegratedAssistantBar;
B _animated;
B _tracking;
B _resizing;
B _isLocal;
B _changedAccessoryOnly;
B _assistantOnScreenOnly;
B _forceNotification;
B _wasCausedRemotely;
B _dueToRotation;
B _startNotification;
@"BKSAnimationFenceHandle" _animationFence;
@"NSString" _currentInputMode;
Q _uiPosition;
Q _keyboardScenePresentationMode;
q _orientation;
@"NSString" _applicationIdentifier;
@"NSString" _bundleIdentifier;
d _duration;
Q _options;
Q _assistantPosition;
Q _notification;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardPosition;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _beginFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _assistantFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_beginFrame) beginFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_endFrame) endFrame;
@property (Td,N,V_duration) duration;
@property (TQ,N,V_options) options;
@property (TB,N,V_changedAccessoryOnly) changedAccessoryOnly;
@property (TB,N,V_assistantOnScreenOnly) assistantOnScreenOnly;
@property (TQ,N,V_assistantPosition) assistantPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_assistantFrame) assistantFrame;
@property (TB,N,V_forceNotification) forceNotification;
@property (TB,N,V_wasCausedRemotely) wasCausedRemotely;
@property (TB,N,V_dueToRotation) dueToRotation;
@property (TB,N,GisStartNotification,V_startNotification) startNotification;
@property (TQ,N,V_notification) notification;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,V_keyboardPosition) keyboardPosition;
@property (T@"BKSAnimationFenceHandle",R,C,V_animationFence) animationFence;
@property (TB,R,V_keyboardOnScreen) keyboardOnScreen;
@property (TB,V_assistantBarVisible) assistantBarVisible;
@property (TB,V_requiresHeightForIntegratedAssistantBar) requiresHeightForIntegratedAssistantBar;
@property (TB,R,V_animated) animated;
@property (TB,R,V_tracking) tracking;
@property (TB,N,V_resizing) resizing;
@property (TB,V_isLocal) isLocal;
@property (T@"NSString",C,N,V_currentInputMode) currentInputMode;
@property (TQ,V_uiPosition) uiPosition;
@property (TQ,V_keyboardScenePresentationMode) keyboardScenePresentationMode;
@property (Tq,R,V_orientation) orientation;
@property (T@"NSString",C,N,V_applicationIdentifier) applicationIdentifier;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
```

## Class methods

```
+[_UIKeyboardUIInformation animationFence];
+[_UIKeyboardUIInformation supportsSecureCoding];
```

## Instance methods

```
-[_UIKeyboardUIInformation assistantBarVisible];
-[_UIKeyboardUIInformation setForceNotification:];
-[_UIKeyboardUIInformation animationFence];
-[_UIKeyboardUIInformation descriptionForLog];
-[_UIKeyboardUIInformation uiPosition];
-[_UIKeyboardUIInformation keyboardPosition];
-[_UIKeyboardUIInformation setBeginFrame:];
-[_UIKeyboardUIInformation assistantPosition];
-[_UIKeyboardUIInformation forceNotification];
-[_UIKeyboardUIInformation notification];
-[_UIKeyboardUIInformation tracking];
-[_UIKeyboardUIInformation dueToRotation];
-[_UIKeyboardUIInformation endFrame];
-[_UIKeyboardUIInformation setAssistantFrame:];
-[_UIKeyboardUIInformation setDueToRotation:];
-[_UIKeyboardUIInformation assistantFrame];
-[_UIKeyboardUIInformation setOptions:];
-[_UIKeyboardUIInformation hasValidNotification];
-[_UIKeyboardUIInformation setWasCausedRemotely:];
-[_UIKeyboardUIInformation beginFrame];
-[_UIKeyboardUIInformation setAssistantOnScreenOnly:];
-[_UIKeyboardUIInformation setResizing:];
-[_UIKeyboardUIInformation changedAccessoryOnly];
-[_UIKeyboardUIInformation setAssistantBarVisible:];
-[_UIKeyboardUIInformation setNotification:];
-[_UIKeyboardUIInformation wasCausedRemotely];
-[_UIKeyboardUIInformation assistantOnScreenOnly];
-[_UIKeyboardUIInformation notificationInfo];
-[_UIKeyboardUIInformation setAssistantPosition:];
-[_UIKeyboardUIInformation animated];
-[_UIKeyboardUIInformation orientation];
-[_UIKeyboardUIInformation setChangedAccessoryOnly:];
-[_UIKeyboardUIInformation setEndFrame:];
-[_UIKeyboardUIInformation setIsLocal:];
-[_UIKeyboardUIInformation bundleIdentifier];
-[_UIKeyboardUIInformation resetAnimationFencing];
-[_UIKeyboardUIInformation currentInputMode];
-[_UIKeyboardUIInformation setUiPosition:];
-[_UIKeyboardUIInformation addNotificationInfo:isStart:];
-[_UIKeyboardUIInformation duration];
-[_UIKeyboardUIInformation setKeyboardScenePresentationMode:];
-[_UIKeyboardUIInformation isLocal];
-[_UIKeyboardUIInformation resizing];
-[_UIKeyboardUIInformation applicationIdentifier];
-[_UIKeyboardUIInformation initWithKeyboardFrame:onScreen:animated:tracking:fence:];
-[_UIKeyboardUIInformation encodeWithCoder:];
-[_UIKeyboardUIInformation keyboardOnScreen];
-[_UIKeyboardUIInformation isStartNotification];
-[_UIKeyboardUIInformation copyWithoutFence];
-[_UIKeyboardUIInformation setApplicationIdentifier:];
-[_UIKeyboardUIInformation description];
-[_UIKeyboardUIInformation initWithCoder:];
-[_UIKeyboardUIInformation options];
-[_UIKeyboardUIInformation initWithKeyboardFrame:onScreen:animated:tracking:wantsFence:];
-[_UIKeyboardUIInformation setRequiresHeightForIntegratedAssistantBar:];
-[_UIKeyboardUIInformation keyboardScenePresentationMode];
-[_UIKeyboardUIInformation setDuration:];
-[_UIKeyboardUIInformation setBundleIdentifier:];
-[_UIKeyboardUIInformation initWithKeyboardFrame:onScreen:animated:tracking:orientation:wantsFence:];
-[_UIKeyboardUIInformation copyWithZone:];
-[_UIKeyboardUIInformation requiresHeightForIntegratedAssistantBar];
-[_UIKeyboardUIInformation initWithKeyboardFrame:onScreen:animated:tracking:orientation:fence:];
-[_UIKeyboardUIInformation setCurrentInputMode:];
-[_UIKeyboardUIInformation setStartNotification:];
```
