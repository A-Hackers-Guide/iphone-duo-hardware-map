# `UIApplicationSceneDeactivationAssertion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
q _reason;
@? _predicate;
@"UIApplicationSceneDeactivationManager" _manager;
B _acquired;
```

## Properties

```
@property (T@"UIApplicationSceneDeactivationManager",R,W,N,V_manager) manager;
@property (Tq,R,N,V_reason) reason;
@property (T@?,R,C,N,V_predicate) predicate;
@property (TB,R,N,GisAcquired,V_acquired) acquired;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIApplicationSceneDeactivationAssertion acquire];
-[UIApplicationSceneDeactivationAssertion succinctDescriptionBuilder];
-[UIApplicationSceneDeactivationAssertion dealloc];
-[UIApplicationSceneDeactivationAssertion manager];
-[UIApplicationSceneDeactivationAssertion descriptionWithMultilinePrefix:];
-[UIApplicationSceneDeactivationAssertion succinctDescription];
-[UIApplicationSceneDeactivationAssertion relinquish];
-[UIApplicationSceneDeactivationAssertion description];
-[UIApplicationSceneDeactivationAssertion isAcquired];
-[UIApplicationSceneDeactivationAssertion predicate];
-[UIApplicationSceneDeactivationAssertion reason];
-[UIApplicationSceneDeactivationAssertion descriptionBuilderWithMultilinePrefix:];
-[UIApplicationSceneDeactivationAssertion acquireWithPredicate:transitionContext:];
-[UIApplicationSceneDeactivationAssertion initWithReason:manager:];
```
