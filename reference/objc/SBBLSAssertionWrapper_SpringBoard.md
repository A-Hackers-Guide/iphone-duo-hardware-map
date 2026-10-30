# `SBBLSAssertionWrapper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionObserving`
- 6 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"BLSAssertion" _wrappedAssertion;
q _state;
@"NSMutableArray" _pendingActivations;
@"NSMutableArray" _pendingDeactivations;
@"NSArray" _attributes;
@"NSString" _explanation;
```

## Properties

```
@property (T@"BLSAssertion",&,N,V_wrappedAssertion) wrappedAssertion;
@property (Tq,N,V_state) state;
@property (T@"NSMutableArray",&,N,V_pendingActivations) pendingActivations;
@property (T@"NSMutableArray",&,N,V_pendingDeactivations) pendingDeactivations;
@property (T@"NSArray",R,C,N,V_attributes) attributes;
@property (T@"NSString",C,N,V_explanation) explanation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBLSAssertionWrapper disableAODAssertionForDisplay:reason:];
```

## Instance methods

```
-[SBBLSAssertionWrapper initWithAttributes:];
-[SBBLSAssertionWrapper setState:];
-[SBBLSAssertionWrapper activateWithCompletion:];
-[SBBLSAssertionWrapper assertion:didCancelWithError:];
-[SBBLSAssertionWrapper setExplanation:];
-[SBBLSAssertionWrapper explanation];
-[SBBLSAssertionWrapper dealloc];
-[SBBLSAssertionWrapper assertion:didFailToAcquireWithError:];
-[SBBLSAssertionWrapper attributes];
-[SBBLSAssertionWrapper state];
-[SBBLSAssertionWrapper assertionWasAcquired:];
-[SBBLSAssertionWrapper _invalidateAssertion];
-[SBBLSAssertionWrapper _invokePendingActivationHandlers];
-[SBBLSAssertionWrapper _invokePendingDeactivationHandlers];
-[SBBLSAssertionWrapper deactivateWithCompletion:];
-[SBBLSAssertionWrapper pendingActivations];
-[SBBLSAssertionWrapper pendingDeactivations];
-[SBBLSAssertionWrapper setPendingActivations:];
-[SBBLSAssertionWrapper setPendingDeactivations:];
-[SBBLSAssertionWrapper setWrappedAssertion:];
-[SBBLSAssertionWrapper wrappedAssertion];
```
