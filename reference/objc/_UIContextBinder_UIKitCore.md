# `_UIContextBinder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 6 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSPointerArray" _enrolledBindables;
@"NSPointerArray" _enrolledUnsafeUnretainedBindables;
@"NSPointerArray" _attachedBindables;
@"NSMutableOrderedSet" _contexts;
@"NSHashTable" _observers;
@"<_UIContextBinding>" _substrate;
q _contextManagementPolicy;
@"<_UIContextBinderContextCreationPolicyHolding>" _contextCreationPolicyHolder;
```

## Properties

```
@property (T@"<_UIContextBinding>",R,N,V_substrate) substrate;
@property (Tq,N,V_contextManagementPolicy) contextManagementPolicy;
@property (T@"<_UIContextBinderContextCreationPolicyHolding>",W,N,V_contextCreationPolicyHolder) contextCreationPolicyHolder;
@property (T@"NSArray",R,N) enrolledUnsafeUnretainedBindables;
@property (T@"NSArray",R,N) enrolledBindables;
@property (T@"NSArray",R,N) attachedBindables;
```

## Class methods

```
+[_UIContextBinder createContextForBindable:withSubstrate:];
```

## Instance methods

```
-[_UIContextBinder substrate];
-[_UIContextBinder _notifyForBindableExpelled:];
-[_UIContextBinder zombifyBindable:];
-[_UIContextBinder attachBindable:];
-[_UIContextBinder bindableIsTopmostAttached:];
-[_UIContextBinder removeObserver:];
-[_UIContextBinder _notifyForBindableEnrolled:];
-[_UIContextBinder _enrolledBindablePointersAsCopy:];
-[_UIContextBinder enrolledBindables];
-[_UIContextBinder updateBindable:];
-[_UIContextBinder expellBindable:];
-[_UIContextBinder updateBindableOrderWithTest:];
-[_UIContextBinder recreateContextForBindable:];
-[_UIContextBinder contextCreationPolicyHolder];
-[_UIContextBinder attachedBindables];
-[_UIContextBinder _contextForBindable:];
-[_UIContextBinder addObserver:];
-[_UIContextBinder enrollBindable:];
-[_UIContextBinder initWithSubstrate:];
-[_UIContextBinder createContextsWithTest:creationAction:];
-[_UIContextBinder contextManagementPolicy];
-[_UIContextBinder setContextManagementPolicy:];
-[_UIContextBinder bindableEnrolled:];
-[_UIContextBinder setContextCreationPolicyHolder:];
-[_UIContextBinder permitContextCreationForBindable:];
-[_UIContextBinder purgeContextsWithPurgeAction:afterPurgeAction:];
-[_UIContextBinder detachBindable:];
-[_UIContextBinder _attachedBindablePointersAsCopy:];
-[_UIContextBinder enrolledUnsafeUnretainedBindables];
-[_UIContextBinder updateBindableOrderWithTest:force:];
-[_UIContextBinder purgeContextsWithPurgeAction:];
```
