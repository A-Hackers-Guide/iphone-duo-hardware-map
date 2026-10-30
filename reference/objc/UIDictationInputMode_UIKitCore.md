# `UIDictationInputMode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISpecializedInputMode`
- 5 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _cachedIcons;
B _usingTypeAndTalk;
B _isCurrentDictationLanguageOnDevice;
@"UITouch" _triggeringTouch;
@"UIKeyboardInputMode" _currentInputModeForDictation;
```

## Properties

```
@property (T@"UITouch",&,N,V_triggeringTouch) triggeringTouch;
@property (T@"UIKeyboardInputMode",&,N,V_currentInputModeForDictation) currentInputModeForDictation;
@property (TB,N,V_usingTypeAndTalk) usingTypeAndTalk;
@property (TB,N,V_isCurrentDictationLanguageOnDevice) isCurrentDictationLanguageOnDevice;
```

## Class methods

```
+[UIDictationInputMode currentInputModeSupportsDictation];
```

## Instance methods

```
-[UIDictationInputMode setUsingTypeAndTalk:];
-[UIDictationInputMode indicatorIconForDictationLanguage:scaleFactor:];
-[UIDictationInputMode includeBarHeight];
-[UIDictationInputMode usingTypeAndTalk];
-[UIDictationInputMode showSWLayoutWithHWKeyboard];
-[UIDictationInputMode isCurrentDictationLanguageOnDevice];
-[UIDictationInputMode setTriggeringTouch:];
-[UIDictationInputMode setCurrentInputModeForDictation:];
-[UIDictationInputMode setIsCurrentDictationLanguageOnDevice:];
-[UIDictationInputMode currentInputModeForDictation];
-[UIDictationInputMode viewControllerClass];
-[UIDictationInputMode triggeringTouch];
```
