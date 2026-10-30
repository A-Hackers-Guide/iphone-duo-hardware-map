# `SBKeyboardSuppressionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"SBSceneManager" _sceneManager;
@"NSMutableDictionary" _keyboardSuppressionAssertions;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
```

## Class methods

```
+[SBKeyboardSuppressionManager sharedInstance];
```

## Instance methods

```
-[SBKeyboardSuppressionManager dealloc];
-[SBKeyboardSuppressionManager description];
-[SBKeyboardSuppressionManager initWithSceneManager:];
-[SBKeyboardSuppressionManager _setKeyboardSuppressed:forReason:withPredicate:displayIdentity:];
-[SBKeyboardSuppressionManager acquireKeyboardSuppressionAssertionWithReason:predicate:displayIdentity:];
-[SBKeyboardSuppressionManager startSuppressingKeyboardWithReason:predicate:displayIdentity:];
-[SBKeyboardSuppressionManager stopSuppressingKeyboardWithReason:];
```
