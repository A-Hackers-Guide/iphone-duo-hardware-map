# `UIKeyboardArbiterManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 1 properties, 7 instance methods, 2 class methods

## Properties

```
@property (TB,R) remoteKeyboardUndocked;
```

## Class methods

```
+[UIKeyboardArbiterManager arbiterClient];
+[UIKeyboardArbiterManager sharedArbiterManager];
```

## Instance methods

```
-[UIKeyboardArbiterManager userSelectedProcessIdentifier:withSceneIdentity:onCompletion:];
-[UIKeyboardArbiterManager restoreKeyboardWithId:];
-[UIKeyboardArbiterManager keyboardWindow];
-[UIKeyboardArbiterManager preserveKeyboardWithId:];
-[UIKeyboardArbiterManager userSelectedApp:onCompletion:];
-[UIKeyboardArbiterManager remoteKeyboardUndocked];
-[UIKeyboardArbiterManager forceKeyboardAway];
```
