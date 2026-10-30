# `SBPPTBlockOperation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPPTOperation`
- 5 instance variables, 4 properties, 19 instance methods, 4 class methods

## Instance variables

```
B _cancelled;
d _timeoutInterval;
@? _timeoutBlock;
Q _state;
@? _block;
```

## Properties

```
@property (T@?,W,N,V_timeoutBlock) timeoutBlock;
@property (TQ,N,V_state) state;
@property (T@?,R,C,N,V_block) block;
@property (Td,N,V_timeoutInterval) timeoutInterval;
```

## Class methods

```
+[SBPPTBlockOperation keyPathsForValuesAffectingIsExecuting];
+[SBPPTBlockOperation keyPathsForValuesAffectingIsFinished];
+[SBPPTBlockOperation operationWithBlock:];
+[SBPPTBlockOperation operationWithName:block:];
```

## Instance methods

```
-[SBPPTBlockOperation isFinished];
-[SBPPTBlockOperation setState:];
-[SBPPTBlockOperation block];
-[SBPPTBlockOperation init];
-[SBPPTBlockOperation finish];
-[SBPPTBlockOperation isAsynchronous];
-[SBPPTBlockOperation start];
-[SBPPTBlockOperation main];
-[SBPPTBlockOperation setTimeoutInterval:];
-[SBPPTBlockOperation setTimeoutBlock:];
-[SBPPTBlockOperation description];
-[SBPPTBlockOperation isExecuting];
-[SBPPTBlockOperation timeoutBlock];
-[SBPPTBlockOperation initWithBlock:];
-[SBPPTBlockOperation timeoutInterval];
-[SBPPTBlockOperation cancel];
-[SBPPTBlockOperation state];
-[SBPPTBlockOperation initWithName:block:];
-[SBPPTBlockOperation cancelAndFailTestWithReason:];
```
