# `_UIGravityWellEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentEffect`
- 9 instance variables, 14 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"<_UIContentEffectDescriptor>" _descriptor;
@"UITargetedPreview" _continuationPreview;
@"_UIGravityWellEffectBody" _primaryBody;
@"NSArray" _secondaryBodies;
@"NSMutableArray" _completions;
Q _animationCount;
d _effectProgress;
q _state;
d _baseZOffset;
```

## Properties

```
@property (T@"UITargetedPreview",&,N,V_continuationPreview) continuationPreview;
@property (T@"_UIGravityWellEffectBody",&,N,V_primaryBody) primaryBody;
@property (T@"NSArray",&,N,V_secondaryBodies) secondaryBodies;
@property (T@"NSMutableArray",R,N,V_completions) completions;
@property (TQ,N,V_animationCount) animationCount;
@property (Td,N,V_effectProgress) effectProgress;
@property (Tq,N,V_state) state;
@property (Td,N,V_baseZOffset) baseZOffset;
@property (T@"NSArray",R,N) secondaryBodyPreviews;
@property (T@"<_UIContentEffectDescriptor>",R,N,V_descriptor) descriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIGravityWellEffect effectWithDescriptor:continuationPreview:];
```

## Instance methods

```
-[_UIGravityWellEffect continuationPreview];
-[_UIGravityWellEffect primaryBody];
-[_UIGravityWellEffect setSecondaryBodies:];
-[_UIGravityWellEffect _tearDownEffectViews];
-[_UIGravityWellEffect animationCount];
-[_UIGravityWellEffect _installEffectViews];
-[_UIGravityWellEffect addCompletion:];
-[_UIGravityWellEffect setPrimaryBody:];
-[_UIGravityWellEffect setEffectProgress:];
-[_UIGravityWellEffect setContinuationPreview:];
-[_UIGravityWellEffect _performAllCompletions];
-[_UIGravityWellEffect updateWithProgress:];
-[_UIGravityWellEffect setDescriptor:andKey:];
-[_UIGravityWellEffect _updateToProgress:state:];
-[_UIGravityWellEffect secondaryBodyPreviews];
-[_UIGravityWellEffect previewForContinuingToEffectWithPreview:];
-[_UIGravityWellEffect _effectSpringBehavior];
-[_UIGravityWellEffect _criticallyDampedEffectSpringBehavior];
-[_UIGravityWellEffect setState:];
-[_UIGravityWellEffect descriptor];
-[_UIGravityWellEffect begin];
-[_UIGravityWellEffect setBaseZOffset:];
-[_UIGravityWellEffect completions];
-[_UIGravityWellEffect end];
-[_UIGravityWellEffect setAnimationCount:];
-[_UIGravityWellEffect endForHandOff];
-[_UIGravityWellEffect baseZOffset];
-[_UIGravityWellEffect secondaryBodies];
-[_UIGravityWellEffect effectProgress];
-[_UIGravityWellEffect state];
```
