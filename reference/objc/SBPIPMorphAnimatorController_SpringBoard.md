# `SBPIPMorphAnimatorController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBViewMorphAnimatorObserver`
- 15 instance variables, 21 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _gestureInitiated;
B _terminated;
i _targetProcessIdentifier;
@"NSString" _scenePersistenceIdentifier;
@"SBViewMorphAnimator" _viewMorphAnimator;
@"<SBViewMorphAnimatorDataSource>" _viewMorphAnimatorDataSource;
@"NSUUID" _uuid;
@"SBAppLayout" _appLayout;
q _layoutRole;
@"SBPIPContainerViewController" _pictureInPictureContainerViewController;
@"<SBPIPMorphAnimatorControllerDelegate>" _delegate;
@? _setupCompletionBlock;
@? _animatorWaitingForExternalAnimationActionBlock;
q _completedTargetAnimations;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _appLayoutBoundingBox;
```

## Properties

```
@property (Tq,N,V_completedTargetAnimations) completedTargetAnimations;
@property (Ti,R,N,V_targetProcessIdentifier) targetProcessIdentifier;
@property (T@"NSString",R,N,V_scenePersistenceIdentifier) scenePersistenceIdentifier;
@property (T@"SBViewMorphAnimator",R,N,V_viewMorphAnimator) viewMorphAnimator;
@property (T@"<SBViewMorphAnimatorDataSource>",R,N,V_viewMorphAnimatorDataSource) viewMorphAnimatorDataSource;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TB,R,N,GisGestureInitiated,V_gestureInitiated) gestureInitiated;
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (Tq,N,V_layoutRole) layoutRole;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_appLayoutBoundingBox) appLayoutBoundingBox;
@property (T@"SBPIPContainerViewController",W,N,V_pictureInPictureContainerViewController) pictureInPictureContainerViewController;
@property (T@"<SBPIPMorphAnimatorControllerDelegate>",R,W,N,V_delegate) delegate;
@property (T@?,C,N,V_setupCompletionBlock) setupCompletionBlock;
@property (T@?,C,N,V_animatorWaitingForExternalAnimationActionBlock) animatorWaitingForExternalAnimationActionBlock;
@property (TB,R,N,GisTerminated,V_terminated) terminated;
@property (TB,R,N) hasCompletedSourceAnimations;
@property (TB,R,N) hasCompletedTargetAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPMorphAnimatorController layoutRole];
-[SBPIPMorphAnimatorController uuid];
-[SBPIPMorphAnimatorController setAppLayout:];
-[SBPIPMorphAnimatorController setLayoutRole:];
-[SBPIPMorphAnimatorController appLayout];
-[SBPIPMorphAnimatorController isGestureInitiated];
-[SBPIPMorphAnimatorController interrupt];
-[SBPIPMorphAnimatorController delegate];
-[SBPIPMorphAnimatorController cancel];
-[SBPIPMorphAnimatorController _terminate];
-[SBPIPMorphAnimatorController _isWaitingForExternalAnimationCompletion];
-[SBPIPMorphAnimatorController _performAnimatorWaitingForExternalAnimationActionBlock];
-[SBPIPMorphAnimatorController animatorWaitingForExternalAnimationActionBlock];
-[SBPIPMorphAnimatorController animatorWasInterrupted:];
-[SBPIPMorphAnimatorController appLayoutBoundingBox];
-[SBPIPMorphAnimatorController completedTargetAnimations];
-[SBPIPMorphAnimatorController didEndSourceAnimations:finished:continueBlock:];
-[SBPIPMorphAnimatorController didEndTargetAnimations:finished:continueBlock:];
-[SBPIPMorphAnimatorController hasCompletedSourceAnimations];
-[SBPIPMorphAnimatorController hasCompletedTargetAnimations];
-[SBPIPMorphAnimatorController initWithTargetProcessIdentifier:scenePersistenceIdentifier:appLayout:layoutRole:appLayoutBoundingBox:windowScene:direction:gestureInitiated:delegate:uuid:];
-[SBPIPMorphAnimatorController initWithTargetProcessIdentifier:scenePersistenceIdentifier:windowScene:direction:gestureInitiated:delegate:uuid:];
-[SBPIPMorphAnimatorController isTerminated];
-[SBPIPMorphAnimatorController pictureInPictureContainerViewController];
-[SBPIPMorphAnimatorController scenePersistenceIdentifier];
-[SBPIPMorphAnimatorController setAnimatorWaitingForExternalAnimationActionBlock:];
-[SBPIPMorphAnimatorController setAppLayoutBoundingBox:];
-[SBPIPMorphAnimatorController setCompletedTargetAnimations:];
-[SBPIPMorphAnimatorController setPictureInPictureContainerViewController:];
-[SBPIPMorphAnimatorController setSetupCompletionBlock:];
-[SBPIPMorphAnimatorController setupCompletionBlock];
-[SBPIPMorphAnimatorController targetProcessIdentifier];
-[SBPIPMorphAnimatorController viewMorphAnimator];
-[SBPIPMorphAnimatorController viewMorphAnimatorDataSource];
-[SBPIPMorphAnimatorController willRemoveTargeMatchMoveAnimationAtFrame:withinSourceFrame:];
-[SBPIPMorphAnimatorController willStartSourceAnimations:];
```
