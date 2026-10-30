# `SBIconsOccludedAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"<SBIconsOccludedAssertionInvalidating>" _invalidator;
@"NSString" _reason;
```

## Properties

```
@property (T@"<SBIconsOccludedAssertionInvalidating>",R,W,N,V_invalidator) invalidator;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIconsOccludedAssertion succinctDescriptionBuilder];
-[SBIconsOccludedAssertion dealloc];
-[SBIconsOccludedAssertion descriptionWithMultilinePrefix:];
-[SBIconsOccludedAssertion isInvalidated];
-[SBIconsOccludedAssertion setInvalidated:];
-[SBIconsOccludedAssertion succinctDescription];
-[SBIconsOccludedAssertion invalidate];
-[SBIconsOccludedAssertion description];
-[SBIconsOccludedAssertion reason];
-[SBIconsOccludedAssertion descriptionBuilderWithMultilinePrefix:];
-[SBIconsOccludedAssertion initWithInvalidator:reason:];
-[SBIconsOccludedAssertion invalidator];
```
