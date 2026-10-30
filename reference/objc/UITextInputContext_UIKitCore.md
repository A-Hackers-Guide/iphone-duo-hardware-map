# `UITextInputContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 3 properties, 8 instance methods, 2 class methods

## Properties

```
@property (TB,N,GisPencilInputExpected) pencilInputExpected;
@property (TB,N,GisDictationInputExpected) dictationInputExpected;
@property (TB,N,GisHardwareKeyboardInputExpected) hardwareKeyboardInputExpected;
```

## Class methods

```
+[UITextInputContext new];
+[UITextInputContext current];
```

## Instance methods

```
-[UITextInputContext isPencilInputExpected];
-[UITextInputContext isHardwareKeyboardInputExpected];
-[UITextInputContext isDictationInputExpected];
-[UITextInputContext isPasswordFieldInSignupForm];
-[UITextInputContext setDictationInputExpected:];
-[UITextInputContext setHardwareKeyboardInputExpected:];
-[UITextInputContext setPencilInputExpected:];
-[UITextInputContext updateInputSource:toUpdate:];
```
