# `SBSceneSnapshotRequestContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _lastAppearanceChangeTimestamp;
@"<SBSceneSnapshotReferenceFrameProviding>" _sceneDisplayReferenceFrameProvider;
@"SBSwitcherWindowManagementContext" _sceneDisplayWindowManagementContext;
@"SBLayoutStateTransitionContext" _sceneDisplayLayoutStateTransitionContext;
@"<SBDisplayItemLayoutAttributesProviding>" _sceneDisplayLayoutAttributesProvider;
q _sceneDisplaySurfaceType;
@"<SBSceneSnapshotReferenceFrameProviding>" _alternateDisplayReferenceFrameProvider;
```

## Properties

```
@property (T@"NSDate",C,N,V_lastAppearanceChangeTimestamp) lastAppearanceChangeTimestamp;
@property (T@"<SBSceneSnapshotReferenceFrameProviding>",&,N,V_sceneDisplayReferenceFrameProvider) sceneDisplayReferenceFrameProvider;
@property (T@"SBSwitcherWindowManagementContext",&,N,V_sceneDisplayWindowManagementContext) sceneDisplayWindowManagementContext;
@property (T@"SBLayoutStateTransitionContext",&,N,V_sceneDisplayLayoutStateTransitionContext) sceneDisplayLayoutStateTransitionContext;
@property (T@"<SBDisplayItemLayoutAttributesProviding>",&,N,V_sceneDisplayLayoutAttributesProvider) sceneDisplayLayoutAttributesProvider;
@property (Tq,N,V_sceneDisplaySurfaceType) sceneDisplaySurfaceType;
@property (T@"<SBSceneSnapshotReferenceFrameProviding>",&,N,V_alternateDisplayReferenceFrameProvider) alternateDisplayReferenceFrameProvider;
```

## Instance methods

```
-[SBSceneSnapshotRequestContext alternateDisplayReferenceFrameProvider];
-[SBSceneSnapshotRequestContext lastAppearanceChangeTimestamp];
-[SBSceneSnapshotRequestContext sceneDisplayLayoutAttributesProvider];
-[SBSceneSnapshotRequestContext sceneDisplayLayoutStateTransitionContext];
-[SBSceneSnapshotRequestContext sceneDisplayReferenceFrameProvider];
-[SBSceneSnapshotRequestContext sceneDisplaySurfaceType];
-[SBSceneSnapshotRequestContext sceneDisplayWindowManagementContext];
-[SBSceneSnapshotRequestContext setAlternateDisplayReferenceFrameProvider:];
-[SBSceneSnapshotRequestContext setLastAppearanceChangeTimestamp:];
-[SBSceneSnapshotRequestContext setSceneDisplayLayoutAttributesProvider:];
-[SBSceneSnapshotRequestContext setSceneDisplayLayoutStateTransitionContext:];
-[SBSceneSnapshotRequestContext setSceneDisplayReferenceFrameProvider:];
-[SBSceneSnapshotRequestContext setSceneDisplaySurfaceType:];
-[SBSceneSnapshotRequestContext setSceneDisplayWindowManagementContext:];
```
