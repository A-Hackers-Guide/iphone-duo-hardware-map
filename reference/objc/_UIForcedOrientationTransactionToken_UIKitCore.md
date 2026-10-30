# `_UIForcedOrientationTransactionToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `_UIOrientationDebugDescriptionProviding`
- 6 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _disablesInterfaceAutorotation;
q _originalInterfaceOrientation;
Q _state;
@"NSString" _transactionReason;
@? _commitCompletionBlock;
@"<_UIForcedOrientationTransactionHandler>" _transactionHandler;
```

## Properties

```
@property (T@?,C,N,V_commitCompletionBlock) commitCompletionBlock;
@property (T@"<_UIForcedOrientationTransactionHandler>",W,N,V_transactionHandler) transactionHandler;
@property (TB,R,N,V_disablesInterfaceAutorotation) disablesInterfaceAutorotation;
@property (Tq,R,N,V_originalInterfaceOrientation) originalInterfaceOrientation;
@property (TQ,R,N,V_state) state;
@property (T@"NSString",R,N,V_transactionReason) transactionReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIForcedOrientationTransactionToken _orientationDebugDescription];
-[_UIForcedOrientationTransactionToken debugDescription];
-[_UIForcedOrientationTransactionToken succinctDescriptionBuilder];
-[_UIForcedOrientationTransactionToken commitAnimated:completionBlock:];
-[_UIForcedOrientationTransactionToken dealloc];
-[_UIForcedOrientationTransactionToken setCommitCompletionBlock:];
-[_UIForcedOrientationTransactionToken transactionHandler];
-[_UIForcedOrientationTransactionToken didCommitOrientation];
-[_UIForcedOrientationTransactionToken descriptionWithMultilinePrefix:];
-[_UIForcedOrientationTransactionToken _orientationDebugDescriptionWithMultilinePrefix:];
-[_UIForcedOrientationTransactionToken succinctDescription];
-[_UIForcedOrientationTransactionToken originalInterfaceOrientation];
-[_UIForcedOrientationTransactionToken disablesInterfaceAutorotation];
-[_UIForcedOrientationTransactionToken debugDescriptionWithMultilinePrefix:];
-[_UIForcedOrientationTransactionToken initWithOriginalOrientation:handler:reason:disablingInterfaceAutorotation:];
-[_UIForcedOrientationTransactionToken transactionReason];
-[_UIForcedOrientationTransactionToken description];
-[_UIForcedOrientationTransactionToken setTransactionHandler:];
-[_UIForcedOrientationTransactionToken _orientationDebugDescriptionBuilderWithMultilinePrefix:];
-[_UIForcedOrientationTransactionToken initWithOriginalOrientation:handler:reason:];
-[_UIForcedOrientationTransactionToken cancel];
-[_UIForcedOrientationTransactionToken commitCompletionBlock];
-[_UIForcedOrientationTransactionToken state];
-[_UIForcedOrientationTransactionToken descriptionBuilderWithMultilinePrefix:];
```
