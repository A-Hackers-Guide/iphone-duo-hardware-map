# `SBAssistantIslandHomeGestureAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 8 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"<SBAssistantIslandHomeGestureAssertionDelegate>" _delegate;
@"NSString" _acquiredReason;
@"NSString" _relinquishedReason;
```

## Properties

```
@property (T@"NSString",C,N,V_acquiredReason) acquiredReason;
@property (T@"NSString",C,N,V_relinquishedReason) relinquishedReason;
@property (T@"<SBAssistantIslandHomeGestureAssertionDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisAcquired) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAssistantIslandHomeGestureAssertion acquireWithDelegate:reason:];
```

## Instance methods

```
-[SBAssistantIslandHomeGestureAssertion succinctDescriptionBuilder];
-[SBAssistantIslandHomeGestureAssertion dealloc];
-[SBAssistantIslandHomeGestureAssertion descriptionWithMultilinePrefix:];
-[SBAssistantIslandHomeGestureAssertion succinctDescription];
-[SBAssistantIslandHomeGestureAssertion setDelegate:];
-[SBAssistantIslandHomeGestureAssertion delegate];
-[SBAssistantIslandHomeGestureAssertion description];
-[SBAssistantIslandHomeGestureAssertion isAcquired];
-[SBAssistantIslandHomeGestureAssertion _initWithDelegate:];
-[SBAssistantIslandHomeGestureAssertion descriptionBuilderWithMultilinePrefix:];
-[SBAssistantIslandHomeGestureAssertion _acquireWithReason:];
-[SBAssistantIslandHomeGestureAssertion acquiredReason];
-[SBAssistantIslandHomeGestureAssertion relinquishWithReason:];
-[SBAssistantIslandHomeGestureAssertion relinquishedReason];
-[SBAssistantIslandHomeGestureAssertion setAcquiredReason:];
-[SBAssistantIslandHomeGestureAssertion setRelinquishedReason:];
```
