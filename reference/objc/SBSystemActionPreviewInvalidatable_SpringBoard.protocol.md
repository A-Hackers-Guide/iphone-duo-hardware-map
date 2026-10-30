# `SBSystemActionPreviewInvalidatable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisValid) valid;
@property (TB,R,N,GisUrgent) urgent;
@property (TB,R,N,GisExpanding) expanding;
@property (TB,R,N,GisProminent) prominent;
```

## Instance methods

```
-[SBSystemActionPreviewInvalidatable isUrgent];
-[SBSystemActionPreviewInvalidatable addInvalidationBlock:];
-[SBSystemActionPreviewInvalidatable isValid];
-[SBSystemActionPreviewInvalidatable isProminent];
-[SBSystemActionPreviewInvalidatable isExpanding];
-[SBSystemActionPreviewInvalidatable acquireAssertionForInvalidatingAfterDefaultTimeoutForActionPerformed];
-[SBSystemActionPreviewInvalidatable addExpansionInvalidationBlock:];
-[SBSystemActionPreviewInvalidatable invalidateAfterDefaultTimeoutForActionCancelled];
-[SBSystemActionPreviewInvalidatable invalidateWithResult:];
```
