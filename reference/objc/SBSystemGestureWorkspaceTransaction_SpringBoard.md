# `SBSystemGestureWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- 3 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" _suppressionReason;
@"UIGestureRecognizer" _gestureRecognizer;
q _completionType;
```

## Properties

```
@property (T@"UIGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (Tq,R,N,V_completionType) completionType;
```

## Instance methods

```
-[SBSystemGestureWorkspaceTransaction _didComplete];
-[SBSystemGestureWorkspaceTransaction _begin];
-[SBSystemGestureWorkspaceTransaction gestureRecognizer];
-[SBSystemGestureWorkspaceTransaction _setupAnimation];
-[SBSystemGestureWorkspaceTransaction setGestureRecognizer:];
-[SBSystemGestureWorkspaceTransaction initWithTransitionRequest:];
-[SBSystemGestureWorkspaceTransaction _beginAnimation];
-[SBSystemGestureWorkspaceTransaction completionType];
-[SBSystemGestureWorkspaceTransaction _finishWithCompletionType:];
-[SBSystemGestureWorkspaceTransaction finishWithCompletionType:];
-[SBSystemGestureWorkspaceTransaction shouldSuppressMedusaKeyboardDuringGesture];
-[SBSystemGestureWorkspaceTransaction systemGestureStateChanged:];
```
