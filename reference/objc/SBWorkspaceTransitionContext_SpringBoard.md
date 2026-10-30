# `SBWorkspaceTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 11 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"SBWorkspaceTransitionRequest" _request;
@"NSMutableDictionary" _entities;
@"NSMutableDictionary" _previousEntities;
B _animationDisabled;
@"BSAnimationSettings" _animationSettings;
@"NSMutableArray" _finalizeBlocks;
B _finalized;
```

## Properties

```
@property (T@"SBWorkspaceTransitionRequest",W,N,V_request) request;
@property (T@"NSDictionary",R,C,N) entitiesByKey;
@property (T@"NSSet",R,C,N) entities;
@property (T@"NSSet",R,C,N) previousEntities;
@property (TB,R,N,GisFinalized,V_finalized) finalized;
@property (TB,N,V_animationDisabled) animationDisabled;
@property (T@"BSAnimationSettings",&,N,V_animationSettings) animationSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWorkspaceTransitionContext context];
```

## Instance methods

```
-[SBWorkspaceTransitionContext finalize];
-[SBWorkspaceTransitionContext setAnimationSettings:];
-[SBWorkspaceTransitionContext entities];
-[SBWorkspaceTransitionContext animationSettings];
-[SBWorkspaceTransitionContext succinctDescriptionBuilder];
-[SBWorkspaceTransitionContext compactDescriptionBuilderWithMultilinePrefix:];
-[SBWorkspaceTransitionContext init];
-[SBWorkspaceTransitionContext descriptionWithMultilinePrefix:];
-[SBWorkspaceTransitionContext request];
-[SBWorkspaceTransitionContext succinctDescription];
-[SBWorkspaceTransitionContext description];
-[SBWorkspaceTransitionContext setRequest:];
-[SBWorkspaceTransitionContext isFinalized];
-[SBWorkspaceTransitionContext descriptionBuilderWithMultilinePrefix:];
-[SBWorkspaceTransitionContext entityForIdentifier:];
-[SBWorkspaceTransitionContext setAnimationDisabled:];
-[SBWorkspaceTransitionContext addFinalizeBlock:];
-[SBWorkspaceTransitionContext animationDisabled];
-[SBWorkspaceTransitionContext entitiesByKey];
-[SBWorkspaceTransitionContext entityForKey:];
-[SBWorkspaceTransitionContext enumerateEntitiesUsingBlock:];
-[SBWorkspaceTransitionContext previousEntities];
-[SBWorkspaceTransitionContext previousEntityForIdentifier:];
-[SBWorkspaceTransitionContext previousEntityForKey:];
-[SBWorkspaceTransitionContext setEntity:forKey:];
-[SBWorkspaceTransitionContext setPreviousEntity:forKey:];
```
