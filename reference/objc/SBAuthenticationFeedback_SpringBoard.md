# `SBAuthenticationFeedback`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q result;
B _vibrate;
B _showPasscode;
B _jiggleLock;
B _driven;
Q _result;
```

## Properties

```
@property (TQ,R,N,V_result) result;
@property (TB,R,N,V_driven) driven;
@property (TB,R,N,V_showPasscode) showPasscode;
@property (TB,R,N) hintFailureText;
@property (TB,R,N,V_vibrate) vibrate;
@property (TB,R,N,V_jiggleLock) jiggleLock;
```

## Instance methods

```
-[SBAuthenticationFeedback result];
-[SBAuthenticationFeedback hash];
-[SBAuthenticationFeedback description];
-[SBAuthenticationFeedback showPasscode];
-[SBAuthenticationFeedback isEqual:];
-[SBAuthenticationFeedback vibrate];
-[SBAuthenticationFeedback jiggleLock];
-[SBAuthenticationFeedback hintFailureText];
-[SBAuthenticationFeedback driven];
-[SBAuthenticationFeedback initForDrivenUIUnlock];
-[SBAuthenticationFeedback initForFailureShowingPasscode:];
-[SBAuthenticationFeedback initForFailureWithFailureSettings:];
-[SBAuthenticationFeedback initForSuccess];
```
