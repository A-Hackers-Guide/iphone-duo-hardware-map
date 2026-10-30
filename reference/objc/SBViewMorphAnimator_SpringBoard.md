# `SBViewMorphAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBViewMorphAnimatorObserver`
- 38 instance variables, 44 properties, 111 instance methods, 0 class methods

## Instance variables

```
B _automaticallyStartSourceAnimations;
B _automaticallyStartTargetAnimations;
B _invalidated;
B _sourceAllEnded;
B _targetExternalPlaceholderAllEnded;
B _sourceContentFrameWasAltered;
@"NSUUID" _uuid;
@"UIView" _sourceView;
@"UIView" _targetView;
@"UIView" _targetContentView;
@"SBWindowScene" _windowScene;
q _fromOrientation;
q _toOrientation;
@"SBFFluidBehaviorSettings" _sourceClipAnimationSettings;
@"SBFFluidBehaviorSettings" _targetClipAnimationSettings;
@"<SBViewMorphAnimatorDelegate>" _delegate;
@"<SBViewMorphAnimatorDataSource>" _dataSource;
q _direction;
Q _startedSourceAnimations;
Q _startedTargetAnimations;
Q _completedSourceAnimations;
Q _completedTargetAnimations;
d _sourceFinalScale;
d _targetCornerRadius;
@"NSHashTable" _observers;
@? _sourceAllAnimationsCompletionBlock;
@"BSAbsoluteMachTimer" _allAnimationsTimeoutTimer;
@"BSAbsoluteMachTimer" _morphAnimationTimeout;
@"BSAbsoluteMachTimer" _sourceAnimationsCompletionContinueBlockTimeoutTimer;
@"SBViewMorphAnimatorContentBlackCurtainView" _sourceBlackCurtainView;
@"SBViewMorphAnimatorContentClippingView" _targetContentClippingView;
d _sourceCornerRadius;
{CGPoint="x"d"y"d} _sourceFinalCenter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetSourcePinningFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetFinalFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetContentClippingViewInitialFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceContentContainerFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceContentFrame;
```

## Properties

```
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (TQ,N,V_startedSourceAnimations) startedSourceAnimations;
@property (TQ,N,V_startedTargetAnimations) startedTargetAnimations;
@property (TQ,N,V_completedSourceAnimations) completedSourceAnimations;
@property (TQ,N,V_completedTargetAnimations) completedTargetAnimations;
@property (TB,N,V_invalidated) invalidated;
@property (TB,N,V_sourceAllEnded) sourceAllEnded;
@property (TB,N,V_targetExternalPlaceholderAllEnded) targetExternalPlaceholderAllEnded;
@property (TB,N,V_sourceContentFrameWasAltered) sourceContentFrameWasAltered;
@property (T@?,C,N,V_sourceAllAnimationsCompletionBlock) sourceAllAnimationsCompletionBlock;
@property (T@"BSAbsoluteMachTimer",&,N,V_allAnimationsTimeoutTimer) allAnimationsTimeoutTimer;
@property (T@"BSAbsoluteMachTimer",&,N,V_morphAnimationTimeout) morphAnimationTimeout;
@property (T@"BSAbsoluteMachTimer",&,N,V_sourceAnimationsCompletionContinueBlockTimeoutTimer) sourceAnimationsCompletionContinueBlockTimeoutTimer;
@property (T@"SBViewMorphAnimatorContentBlackCurtainView",&,N,V_sourceBlackCurtainView) sourceBlackCurtainView;
@property (T@"SBViewMorphAnimatorContentClippingView",&,N,V_targetContentClippingView) targetContentClippingView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetContentClippingViewInitialFrame) targetContentClippingViewInitialFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceContentContainerFrame) sourceContentContainerFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceContentFrame) sourceContentFrame;
@property (Td,N,V_sourceCornerRadius) sourceCornerRadius;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (T@"UIView",W,N,V_targetView) targetView;
@property (T@"UIView",W,N,V_targetContentView) targetContentView;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (Tq,N,V_fromOrientation) fromOrientation;
@property (Tq,N,V_toOrientation) toOrientation;
@property (T@"SBFFluidBehaviorSettings",&,N,V_sourceClipAnimationSettings) sourceClipAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_targetClipAnimationSettings) targetClipAnimationSettings;
@property (T@"<SBViewMorphAnimatorDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBViewMorphAnimatorDataSource>",W,N,V_dataSource) dataSource;
@property (TB,N,V_automaticallyStartSourceAnimations) automaticallyStartSourceAnimations;
@property (TB,N,V_automaticallyStartTargetAnimations) automaticallyStartTargetAnimations;
@property (Tq,N,V_direction) direction;
@property (T{CGPoint=dd},R,N,V_sourceFinalCenter) sourceFinalCenter;
@property (Td,R,N,V_sourceFinalScale) sourceFinalScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) sourceClippingFrame;
@property (Td,R,N) sourceClippingCornerRadius;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetSourcePinningFrame) targetSourcePinningFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetFinalFrame) targetFinalFrame;
@property (Td,R,N,V_targetCornerRadius) targetCornerRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBViewMorphAnimator targetView];
-[SBViewMorphAnimator _reset];
-[SBViewMorphAnimator invalidated];
-[SBViewMorphAnimator uuid];
-[SBViewMorphAnimator init];
-[SBViewMorphAnimator dealloc];
-[SBViewMorphAnimator setDirection:];
-[SBViewMorphAnimator setDataSource:];
-[SBViewMorphAnimator setInvalidated:];
-[SBViewMorphAnimator addObserver:];
-[SBViewMorphAnimator direction];
-[SBViewMorphAnimator setDelegate:];
-[SBViewMorphAnimator setTargetView:];
-[SBViewMorphAnimator cancel:];
-[SBViewMorphAnimator dataSource];
-[SBViewMorphAnimator setSourceView:];
-[SBViewMorphAnimator delegate];
-[SBViewMorphAnimator _enumerateObserversRespondingToSelector:usingBlock:];
-[SBViewMorphAnimator setObservers:];
-[SBViewMorphAnimator observers];
-[SBViewMorphAnimator windowScene];
-[SBViewMorphAnimator sourceView];
-[SBViewMorphAnimator fromOrientation];
-[SBViewMorphAnimator setFromOrientation:];
-[SBViewMorphAnimator setToOrientation:];
-[SBViewMorphAnimator toOrientation];
-[SBViewMorphAnimator setTargetContentView:];
-[SBViewMorphAnimator targetContentView];
-[SBViewMorphAnimator _removeMatchMoveAnimation];
-[SBViewMorphAnimator setSourceContentFrame:];
-[SBViewMorphAnimator sourceContentFrame];
-[SBViewMorphAnimator _isReversed];
-[SBViewMorphAnimator _updateParameters];
-[SBViewMorphAnimator interrupt:];
-[SBViewMorphAnimator _sourceContentContainerFrameForSourceView:withTargetDataSource:];
-[SBViewMorphAnimator noteWillRemoveTargeMatchMoveAnimationAtFrame:withinSourceFrame:];
-[SBViewMorphAnimator setSourceClipAnimationSettings:];
-[SBViewMorphAnimator setSourceContentContainerFrame:];
-[SBViewMorphAnimator setTargetClipAnimationSettings:];
-[SBViewMorphAnimator _checkAnimationsDependencies:];
-[SBViewMorphAnimator _continueSourceAnimationsCompletionPendingBlock];
-[SBViewMorphAnimator _handleHandoffTimeout];
-[SBViewMorphAnimator _isTargetSourcePinningFrameEquivalentToSourceViewFrame];
-[SBViewMorphAnimator _noteAnimatorWasCanceled];
-[SBViewMorphAnimator _noteAnimatorWasInterrupted];
-[SBViewMorphAnimator _noteDidEndAllAnimations];
-[SBViewMorphAnimator _removeBlackCurtainView];
-[SBViewMorphAnimator _removeTargetClippingView];
-[SBViewMorphAnimator _resetAllAnimations];
-[SBViewMorphAnimator _source:finalCenterWithFinalScale:contentFrame:targetFinalFrame:];
-[SBViewMorphAnimator _sourceFinalScaleWithContentFrame:targetFinalFrame:];
-[SBViewMorphAnimator _startMorphAnimationTimeoutTimer];
-[SBViewMorphAnimator _targetInitialClippingBoundsWithSourceContentFrame:sourceFinalScale:targetViewBounds:];
-[SBViewMorphAnimator _targetSourcePinningFrameWithSourceContentFrame:targetFinalFrame:];
-[SBViewMorphAnimator _validatedSourceContentFrame:withinSourceView:withSourceFinalScale:];
-[SBViewMorphAnimator allAnimationsTimeoutTimer];
-[SBViewMorphAnimator automaticallyStartSourceAnimations];
-[SBViewMorphAnimator automaticallyStartTargetAnimations];
-[SBViewMorphAnimator completedSourceAnimations];
-[SBViewMorphAnimator completedTargetAnimations];
-[SBViewMorphAnimator didEndSourceAnimations:finished:continueBlock:];
-[SBViewMorphAnimator didEndTargetAnimations:finished:continueBlock:];
-[SBViewMorphAnimator initWithUUID:windowScene:direction:];
-[SBViewMorphAnimator morphAnimationTimeout];
-[SBViewMorphAnimator noteSourceAnimationsDidEnd:finished:continueBlock:];
-[SBViewMorphAnimator noteSourceAnimationsWillStart:];
-[SBViewMorphAnimator noteTargetAnimationsDidEnd:finished:continueBlock:];
-[SBViewMorphAnimator noteTargetAnimationsWillStart:];
-[SBViewMorphAnimator preflightCheck];
-[SBViewMorphAnimator setAllAnimationsTimeoutTimer:];
-[SBViewMorphAnimator setAutomaticallyStartSourceAnimations:];
-[SBViewMorphAnimator setAutomaticallyStartTargetAnimations:];
-[SBViewMorphAnimator setCompletedSourceAnimations:];
-[SBViewMorphAnimator setCompletedTargetAnimations:];
-[SBViewMorphAnimator setMorphAnimationTimeout:];
-[SBViewMorphAnimator setSourceAllAnimationsCompletionBlock:];
-[SBViewMorphAnimator setSourceAllEnded:];
-[SBViewMorphAnimator setSourceAnimationsCompletionContinueBlockTimeoutTimer:];
-[SBViewMorphAnimator setSourceBlackCurtainView:];
-[SBViewMorphAnimator setSourceContentFrameWasAltered:];
-[SBViewMorphAnimator setSourceCornerRadius:];
-[SBViewMorphAnimator setStartedSourceAnimations:];
-[SBViewMorphAnimator setStartedTargetAnimations:];
-[SBViewMorphAnimator setTargetContentClippingView:];
-[SBViewMorphAnimator setTargetContentClippingViewInitialFrame:];
-[SBViewMorphAnimator setTargetExternalPlaceholderAllEnded:];
-[SBViewMorphAnimator sourceAllAnimationsCompletionBlock];
-[SBViewMorphAnimator sourceAllEnded];
-[SBViewMorphAnimator sourceAnimationsCompletionContinueBlockTimeoutTimer];
-[SBViewMorphAnimator sourceBlackCurtainView];
-[SBViewMorphAnimator sourceClipAnimationSettings];
-[SBViewMorphAnimator sourceClippingCornerRadius];
-[SBViewMorphAnimator sourceClippingFrame];
-[SBViewMorphAnimator sourceContentContainerFrame];
-[SBViewMorphAnimator sourceContentFrameWasAltered];
-[SBViewMorphAnimator sourceCornerRadius];
-[SBViewMorphAnimator sourceFinalCenter];
-[SBViewMorphAnimator sourceFinalScale];
-[SBViewMorphAnimator startSourceAnimations:];
-[SBViewMorphAnimator startTargetAnimations:];
-[SBViewMorphAnimator startedSourceAnimations];
-[SBViewMorphAnimator startedTargetAnimations];
-[SBViewMorphAnimator targetClipAnimationSettings];
-[SBViewMorphAnimator targetContentClippingView];
-[SBViewMorphAnimator targetContentClippingViewInitialFrame];
-[SBViewMorphAnimator targetCornerRadius];
-[SBViewMorphAnimator targetExternalPlaceholderAllEnded];
-[SBViewMorphAnimator targetFinalFrame];
-[SBViewMorphAnimator targetSourcePinningFrame];
-[SBViewMorphAnimator willStartSourceAnimations:];
-[SBViewMorphAnimator willStartTargetAnimations:];
```
