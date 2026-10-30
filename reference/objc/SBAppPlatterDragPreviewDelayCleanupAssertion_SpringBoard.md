# `SBAppPlatterDragPreviewDelayCleanupAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"SBAppPlatterDragPreview" _dragPreview;
@"NSString" _reason;
```

## Properties

```
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"SBAppPlatterDragPreview",R,W,N,V_dragPreview) dragPreview;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppPlatterDragPreviewDelayCleanupAssertion succinctDescriptionBuilder];
-[SBAppPlatterDragPreviewDelayCleanupAssertion dealloc];
-[SBAppPlatterDragPreviewDelayCleanupAssertion descriptionWithMultilinePrefix:];
-[SBAppPlatterDragPreviewDelayCleanupAssertion isInvalidated];
-[SBAppPlatterDragPreviewDelayCleanupAssertion setInvalidated:];
-[SBAppPlatterDragPreviewDelayCleanupAssertion succinctDescription];
-[SBAppPlatterDragPreviewDelayCleanupAssertion invalidate];
-[SBAppPlatterDragPreviewDelayCleanupAssertion description];
-[SBAppPlatterDragPreviewDelayCleanupAssertion reason];
-[SBAppPlatterDragPreviewDelayCleanupAssertion descriptionBuilderWithMultilinePrefix:];
-[SBAppPlatterDragPreviewDelayCleanupAssertion dragPreview];
-[SBAppPlatterDragPreviewDelayCleanupAssertion initWithDragPreview:reason:];
```
