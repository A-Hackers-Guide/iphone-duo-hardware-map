# `_UIApplicationSceneKeyboardHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneHostKeyboardSuppressionController`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
I _keyboardSuppressionAssertionCount;
@"NSHashTable" _observers;
```

## Properties

```
@property (TB,R,N) suppressKeyboardFocusRequests;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIApplicationSceneKeyboardHostComponent setScene:];
-[_UIApplicationSceneKeyboardHostComponent setHardwareKeyboardExclusivityIdentifier:];
-[_UIApplicationSceneKeyboardHostComponent suppressKeyboardFocusRequestsForReason:];
-[_UIApplicationSceneKeyboardHostComponent addKeyboardSuppressionControllerObserver:];
-[_UIApplicationSceneKeyboardHostComponent setMinimumKeyboardPadding:forSettings:];
-[_UIApplicationSceneKeyboardHostComponent evaluateKeyboardSuppressionSettingForActiveAssertions];
-[_UIApplicationSceneKeyboardHostComponent suppressKeyboardFocusRequests];
-[_UIApplicationSceneKeyboardHostComponent setKeyboardDockDisabled:forSettings:];
-[_UIApplicationSceneKeyboardHostComponent removeKeyboardSuppressionControllerObserver:];
```
