# `UIKeyboardVisualModeManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 20 instance methods, 4 class methods

## Instance variables

```
i _lastVisualMode;
@"<UIKeyboardVisualModeManagerDelegate>" _delegate;
```

## Properties

```
@property (Ti,N,V_lastVisualMode) lastVisualMode;
@property (T@"<UIKeyboardVisualModeManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UIKeyboardVisualModeManager softwareKeyboardAllowedForActiveKeyboardSceneDelegate];
+[UIKeyboardVisualModeManager visualModeLog];
+[UIKeyboardVisualModeManager softwareKeyboardAllowedOnExternalScreen];
+[UIKeyboardVisualModeManager windowingSoftwareKeyboardAllowed];
```

## Instance methods

```
-[UIKeyboardVisualModeManager expectedInputModeIsSpecialized];
-[UIKeyboardVisualModeManager textEntryFocusOnExternalDisplay];
-[UIKeyboardVisualModeManager windowingModeEnabled];
-[UIKeyboardVisualModeManager hardwareKeyboardAttached];
-[UIKeyboardVisualModeManager isCustomInputViewSet];
-[UIKeyboardVisualModeManager keyboardSubstitutePresentedOrPresenting];
-[UIKeyboardVisualModeManager init];
-[UIKeyboardVisualModeManager visualMode];
-[UIKeyboardVisualModeManager setDelegate:];
-[UIKeyboardVisualModeManager setLastVisualMode:];
-[UIKeyboardVisualModeManager delegate];
-[UIKeyboardVisualModeManager keyboardCameraPresentedOrPresenting];
-[UIKeyboardVisualModeManager enhancedWindowingModeDidChange:];
-[UIKeyboardVisualModeManager useVisualModeWindowed];
-[UIKeyboardVisualModeManager softwareKeyboardMinimized];
-[UIKeyboardVisualModeManager keyboardCameraNotification:];
-[UIKeyboardVisualModeManager keyboardHasBeenInitialized];
-[UIKeyboardVisualModeManager shouldShowWithinAppWindow];
-[UIKeyboardVisualModeManager isWantsAssistantWhileSuppressingKeyboard];
-[UIKeyboardVisualModeManager lastVisualMode];
```
