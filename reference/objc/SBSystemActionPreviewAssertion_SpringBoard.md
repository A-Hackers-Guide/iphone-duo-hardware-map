# `SBSystemActionPreviewAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionPreviewInvalidatable`
- 14 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@? _urgencyInvalidationBlock;
@? _finalInvalidationBlock;
@"SBSystemActionPreviewSettings" _settings;
@"BSContinuousMachTimer" _urgencyInvalidationTimer;
@"BSContinuousMachTimer" _invalidationTimer;
d _performedTime;
@"NSMutableOrderedSet" _expansionInvalidationBlocks;
@"NSMutableOrderedSet" _invalidationBlocks;
B _valid;
B _urgent;
B _expanding;
B _prominent;
@"NSString" _identifier;
@"NSString" _reason;
```

## Properties

```
@property (TB,R,N,GisValid,V_valid) valid;
@property (TB,R,N,GisUrgent,V_urgent) urgent;
@property (TB,R,N,GisExpanding,V_expanding) expanding;
@property (TB,R,N,GisProminent,V_prominent) prominent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemActionPreviewAssertion isUrgent];
-[SBSystemActionPreviewAssertion addInvalidationBlock:];
-[SBSystemActionPreviewAssertion dealloc];
-[SBSystemActionPreviewAssertion isValid];
-[SBSystemActionPreviewAssertion description];
-[SBSystemActionPreviewAssertion isProminent];
-[SBSystemActionPreviewAssertion isExpanding];
-[SBSystemActionPreviewAssertion acquireAssertionForInvalidatingAfterDefaultTimeoutForActionPerformed];
-[SBSystemActionPreviewAssertion addExpansionInvalidationBlock:];
-[SBSystemActionPreviewAssertion invalidateAfterDefaultTimeoutForActionCancelled];
-[SBSystemActionPreviewAssertion invalidateWithResult:];
```
