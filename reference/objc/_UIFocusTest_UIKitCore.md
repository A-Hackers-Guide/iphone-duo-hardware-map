# `_UIFocusTest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 18 instance methods, 2 class methods

## Instance variables

```
B _isApplicationTest;
@"NSString" _identifier;
q _state;
@"<_UIFocusTestDelegate>" _delegate;
@? _runCompletionHandler;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@?,C,N,V_runCompletionHandler) runCompletionHandler;
@property (TB,N,G_isApplicationTest,V_isApplicationTest) isApplicationTest;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"<_UIFocusTestDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[_UIFocusTest currentTest];
+[_UIFocusTest _setCurrentTest:];
```

## Instance methods

```
-[_UIFocusTest setState:];
-[_UIFocusTest _start];
-[_UIFocusTest identifier];
-[_UIFocusTest stop];
-[_UIFocusTest main];
-[_UIFocusTest reset];
-[_UIFocusTest setDelegate:];
-[_UIFocusTest delegate];
-[_UIFocusTest prepareWithCompletionHandler:];
-[_UIFocusTest cancel];
-[_UIFocusTest initWithIdentifier:];
-[_UIFocusTest state];
-[_UIFocusTest _finish:];
-[_UIFocusTest _isApplicationTest];
-[_UIFocusTest runCompletionHandler];
-[_UIFocusTest runWithCompletionHandler:];
-[_UIFocusTest setIsApplicationTest:];
-[_UIFocusTest setRunCompletionHandler:];
```
