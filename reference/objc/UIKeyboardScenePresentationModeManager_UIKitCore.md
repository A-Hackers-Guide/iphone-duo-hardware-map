# `UIKeyboardScenePresentationModeManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _enhancedWindowingModeEnabled;
@"<UIKeyboardScenePresentationModeManagerDelegate>" _delegate;
Q _currentPresentationMode;
```

## Properties

```
@property (TB,N,V_enhancedWindowingModeEnabled) enhancedWindowingModeEnabled;
@property (TQ,N,V_currentPresentationMode) currentPresentationMode;
@property (TQ,R,N) presentationMode;
@property (T@"<UIKeyboardScenePresentationModeManagerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[UIKeyboardScenePresentationModeManager presentationMode];
-[UIKeyboardScenePresentationModeManager setEnhancedWindowingModeEnabled:];
-[UIKeyboardScenePresentationModeManager setDelegate:];
-[UIKeyboardScenePresentationModeManager delegate];
-[UIKeyboardScenePresentationModeManager enhancedWindowingModeEnabled];
-[UIKeyboardScenePresentationModeManager determineiPhonePresentationMode];
-[UIKeyboardScenePresentationModeManager _enhancedWindowingModeEnabledDidChange:];
-[UIKeyboardScenePresentationModeManager currentPresentationMode];
-[UIKeyboardScenePresentationModeManager determinePresentationMode];
-[UIKeyboardScenePresentationModeManager determineiPadPresentationMode];
-[UIKeyboardScenePresentationModeManager didChangeToPresentationMode:];
-[UIKeyboardScenePresentationModeManager enhancedWindowingModeEnabledDidChange:];
-[UIKeyboardScenePresentationModeManager setCurrentPresentationMode:];
```
