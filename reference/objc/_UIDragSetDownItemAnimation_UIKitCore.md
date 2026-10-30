# `_UIDragSetDownItemAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 40 instance variables, 42 properties, 103 instance methods, 0 class methods

## Instance variables

```
B _reachedTarget;
B _done;
B _defaultAnimation;
B _sourceAnimation;
B _hasStartedSpringAnimation;
B _wasVisibleAtStart;
B _midwayToTarget;
B _almostToTarget;
B _reparentingCrossfadeComplete;
B _updatedPreviewWasAdded;
B _didTerminateEarly;
i _animationCount;
@"UIDragItem" _item;
@"_DUIVisibleDroppedItem" _droppedItem;
@"<UIViewSpringAnimationBehaviorDescribing>" _customSpringAnimationBehavior;
@"<_UIDragSetDownItemAnimationDelegate>" _delegate;
@"UIView" _dropContainerView;
@"<_UIDragSetDownAnimationTarget>" _visualTarget;
@"UITargetedDragPreview" _targetedDropPreview;
@"UITargetedDragPreview" _updatedTargetedDropPreview;
d _initialDistanceFromTargetFrame;
d _targetCenterZ;
@"UIViewPropertyAnimator" _propertyAnimator;
@? _completionHandler;
@"UIView" _retargetingContainerView;
@"_UIPortalView" _retargetingContainerPortalView;
@"_UIPlatterView" _appPlatterView;
@"_UIPlatterView" _updatedAppPlatterView;
@"_UIPlatterView" _druidPlatterView;
@"_UIPlatterContainerView" _platterContainerView;
@"_UIPlatterView" _defaultPlatterView;
@? _positionHandler;
@? _morphHandler;
@? _midpointHandler;
@? _nonAnimatedMidpointHandler;
@? _nearCompletionHandler;
{CAPoint3D="x"d"y"d"z"d} _center;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetFrame;
(?=""{?="x"d"y"d"z"d"_padding"d}"vector") _initialVelocity;
(?=""{?="x"d"y"d"z"d"_padding"d}"vector") _initialTargetVelocity;
```

## Properties

```
@property (T@"<_UIDragSetDownItemAnimationDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N,V_dropContainerView) dropContainerView;
@property (T@"<_UIDragSetDownAnimationTarget>",&,N,V_visualTarget) visualTarget;
@property (T@"UITargetedDragPreview",&,N,V_targetedDropPreview) targetedDropPreview;
@property (T@"UITargetedDragPreview",&,N,V_updatedTargetedDropPreview) updatedTargetedDropPreview;
@property (T{CAPoint3D=ddd},N,V_center) center;
@property (Td,N,V_initialDistanceFromTargetFrame) initialDistanceFromTargetFrame;
@property (Td,N,V_targetCenterZ) targetCenterZ;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetFrame) targetFrame;
@property (TB,N,V_defaultAnimation) defaultAnimation;
@property (TB,N,V_sourceAnimation) sourceAnimation;
@property (T@"UIViewPropertyAnimator",&,N,V_propertyAnimator) propertyAnimator;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,N,V_hasStartedSpringAnimation) hasStartedSpringAnimation;
@property (TB,N,V_wasVisibleAtStart) wasVisibleAtStart;
@property (TB,N,V_midwayToTarget) midwayToTarget;
@property (TB,N,V_almostToTarget) almostToTarget;
@property (TB,N,V_reparentingCrossfadeComplete) reparentingCrossfadeComplete;
@property (TB,N,V_updatedPreviewWasAdded) updatedPreviewWasAdded;
@property (TB,N,V_didTerminateEarly) didTerminateEarly;
@property (Ti,N,V_animationCount) animationCount;
@property (Tq,R,N) previewMode;
@property (T(?={?=dddd}),N,V_initialVelocity) initialVelocity;
@property (T(?={?=dddd}),N,V_initialTargetVelocity) initialTargetVelocity;
@property (T@"UIView",&,N,V_retargetingContainerView) retargetingContainerView;
@property (T@"_UIPortalView",&,N,V_retargetingContainerPortalView) retargetingContainerPortalView;
@property (T@"_UIPlatterView",&,N,V_appPlatterView) appPlatterView;
@property (T@"_UIPlatterView",&,N,V_updatedAppPlatterView) updatedAppPlatterView;
@property (T@"_UIPlatterView",&,N,V_druidPlatterView) druidPlatterView;
@property (T@"_UIPlatterContainerView",&,N,V_platterContainerView) platterContainerView;
@property (T@"_UIPlatterView",&,N,V_defaultPlatterView) defaultPlatterView;
@property (T@?,C,N,V_positionHandler) positionHandler;
@property (T@?,C,N,V_morphHandler) morphHandler;
@property (T@?,C,N,V_midpointHandler) midpointHandler;
@property (T@?,C,N,V_nonAnimatedMidpointHandler) nonAnimatedMidpointHandler;
@property (T@?,C,N,V_nearCompletionHandler) nearCompletionHandler;
@property (T@"UIDragItem",R,N,V_item) item;
@property (T@"_DUIVisibleDroppedItem",R,N,V_droppedItem) droppedItem;
@property (TB,R,N,V_reachedTarget) reachedTarget;
@property (TB,R,N,V_done) done;
@property (T@"UIWindow",R,N) targetContainerWindow;
@property (T@"<UIViewSpringAnimationBehaviorDescribing>",&,N,V_customSpringAnimationBehavior) customSpringAnimationBehavior;
```

## Instance methods

```
-[_UIDragSetDownItemAnimation animationCount];
-[_UIDragSetDownItemAnimation setInitialVelocity:];
-[_UIDragSetDownItemAnimation setCompletionHandler:];
-[_UIDragSetDownItemAnimation completionHandler];
-[_UIDragSetDownItemAnimation done];
-[_UIDragSetDownItemAnimation setCenter:];
-[_UIDragSetDownItemAnimation item];
-[_UIDragSetDownItemAnimation setAnimationCount:];
-[_UIDragSetDownItemAnimation initialVelocity];
-[_UIDragSetDownItemAnimation setDelegate:];
-[_UIDragSetDownItemAnimation center];
-[_UIDragSetDownItemAnimation delegate];
-[_UIDragSetDownItemAnimation configureSystemDefaultAnimation];
-[_UIDragSetDownItemAnimation positionHandler];
-[_UIDragSetDownItemAnimation sourceAnimation];
-[_UIDragSetDownItemAnimation midpointHandler];
-[_UIDragSetDownItemAnimation setTargetFrame:];
-[_UIDragSetDownItemAnimation _setCenterAndVelocityFromDroppedItem:];
-[_UIDragSetDownItemAnimation almostToTarget];
-[_UIDragSetDownItemAnimation animationCompleted];
-[_UIDragSetDownItemAnimation animationCompletionHandler];
-[_UIDragSetDownItemAnimation animationReachedTarget];
-[_UIDragSetDownItemAnimation appPlatterView];
-[_UIDragSetDownItemAnimation beginAnimation];
-[_UIDragSetDownItemAnimation configureAnimation];
-[_UIDragSetDownItemAnimation configureCrossfadingAnimationToTargetedPreview];
-[_UIDragSetDownItemAnimation customSpringAnimationBehavior];
-[_UIDragSetDownItemAnimation defaultAnimation];
-[_UIDragSetDownItemAnimation defaultPlatterView];
-[_UIDragSetDownItemAnimation didTerminateEarly];
-[_UIDragSetDownItemAnimation dirtyTargetedDropPreview];
-[_UIDragSetDownItemAnimation dropContainerView];
-[_UIDragSetDownItemAnimation droppedItem];
-[_UIDragSetDownItemAnimation druidPlatterView];
-[_UIDragSetDownItemAnimation effectiveDropPreview];
-[_UIDragSetDownItemAnimation estimatedFractionCompleteOfAnimation];
-[_UIDragSetDownItemAnimation executeCompletionHandler];
-[_UIDragSetDownItemAnimation hasStartedSpringAnimation];
-[_UIDragSetDownItemAnimation initWithDragItem:droppedItem:dropContainerView:defaultAnimation:sourceAnimation:delegate:];
-[_UIDragSetDownItemAnimation initialDistanceFromTargetFrame];
-[_UIDragSetDownItemAnimation initialTargetVelocity];
-[_UIDragSetDownItemAnimation midwayToTarget];
-[_UIDragSetDownItemAnimation morphHandler];
-[_UIDragSetDownItemAnimation nearCompletionHandler];
-[_UIDragSetDownItemAnimation needsReparenting];
-[_UIDragSetDownItemAnimation nonAnimatedMidpointHandler];
-[_UIDragSetDownItemAnimation performSpringAnimations:];
-[_UIDragSetDownItemAnimation performTrackingAnimations:];
-[_UIDragSetDownItemAnimation platterContainerView];
-[_UIDragSetDownItemAnimation prepareAnimationInWindow];
-[_UIDragSetDownItemAnimation prepareToBeginAnimation];
-[_UIDragSetDownItemAnimation previewContainerAnimationDidComplete];
-[_UIDragSetDownItemAnimation previewMode];
-[_UIDragSetDownItemAnimation propertyAnimator];
-[_UIDragSetDownItemAnimation reachedTarget];
-[_UIDragSetDownItemAnimation reparentRetargetingContainerViewInTargetContainer];
-[_UIDragSetDownItemAnimation reparentingCrossfadeComplete];
-[_UIDragSetDownItemAnimation retargetingContainerPortalView];
-[_UIDragSetDownItemAnimation retargetingContainerView];
-[_UIDragSetDownItemAnimation setAlmostToTarget:];
-[_UIDragSetDownItemAnimation setAppPlatterView:];
-[_UIDragSetDownItemAnimation setCustomSpringAnimationBehavior:];
-[_UIDragSetDownItemAnimation setDefaultAnimation:];
-[_UIDragSetDownItemAnimation setDefaultPlatterView:];
-[_UIDragSetDownItemAnimation setDidTerminateEarly:];
-[_UIDragSetDownItemAnimation setDropContainerView:];
-[_UIDragSetDownItemAnimation setDruidPlatterView:];
-[_UIDragSetDownItemAnimation setHasStartedSpringAnimation:];
-[_UIDragSetDownItemAnimation setInitialDistanceFromTargetFrame:];
-[_UIDragSetDownItemAnimation setInitialTargetVelocity:];
-[_UIDragSetDownItemAnimation setMidpointHandler:];
-[_UIDragSetDownItemAnimation setMidwayToTarget:];
-[_UIDragSetDownItemAnimation setMorphHandler:];
-[_UIDragSetDownItemAnimation setNearCompletionHandler:];
-[_UIDragSetDownItemAnimation setNonAnimatedMidpointHandler:];
-[_UIDragSetDownItemAnimation setPlatterContainerView:];
-[_UIDragSetDownItemAnimation setPositionHandler:];
-[_UIDragSetDownItemAnimation setPropertyAnimator:];
-[_UIDragSetDownItemAnimation setReparentingCrossfadeComplete:];
-[_UIDragSetDownItemAnimation setRetargetingContainerPortalView:];
-[_UIDragSetDownItemAnimation setRetargetingContainerView:];
-[_UIDragSetDownItemAnimation setSourceAnimation:];
-[_UIDragSetDownItemAnimation setTargetCenterZ:];
-[_UIDragSetDownItemAnimation setTargetedDropPreview:];
-[_UIDragSetDownItemAnimation setUpdatedAppPlatterView:];
-[_UIDragSetDownItemAnimation setUpdatedPreviewWasAdded:];
-[_UIDragSetDownItemAnimation setUpdatedTargetedDropPreview:];
-[_UIDragSetDownItemAnimation setVisualTarget:];
-[_UIDragSetDownItemAnimation setWasVisibleAtStart:];
-[_UIDragSetDownItemAnimation shouldTerminateEarly];
-[_UIDragSetDownItemAnimation targetCenterZ];
-[_UIDragSetDownItemAnimation targetContainerWindow];
-[_UIDragSetDownItemAnimation targetFrame];
-[_UIDragSetDownItemAnimation targetedDropPreview];
-[_UIDragSetDownItemAnimation updateAnimationTargeting];
-[_UIDragSetDownItemAnimation updateCurrentTargetFrame];
-[_UIDragSetDownItemAnimation updateDroppedItem:];
-[_UIDragSetDownItemAnimation updateTargetedDropPreview:];
-[_UIDragSetDownItemAnimation updatedAppPlatterView];
-[_UIDragSetDownItemAnimation updatedPreviewWasAdded];
-[_UIDragSetDownItemAnimation updatedTargetedDropPreview];
-[_UIDragSetDownItemAnimation visualTarget];
-[_UIDragSetDownItemAnimation wasVisibleAtStart];
```
