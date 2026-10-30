# `_UIPointerContentEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewSubtreeMonitor`, `_UIContentEffect`
- 20 instance variables, 23 properties, 62 instance methods, 0 class methods

## Instance variables

```
{?="isRearrangingEffectViews"B"stopViewOrderPreservation"B} _flags;
B _pressed;
@"UIPointerRegion" _region;
@"UIPointerStyle" _style;
@"UIPointerInteractionAnimator" _entranceAnimator;
@"UIPointerInteractionAnimator" _exitAnimator;
d _liftProgress;
@"_UIPointerEffectPlatterView" _platterView;
@"UIView" _lumaSamplingBackdrop;
@"UIView" _pointerPortal;
@"NSMutableArray" _completions;
q _state;
Q _animationCount;
@"UIView" _positionReferenceView;
@"UIWindow" _subtreeMonitoredWindow;
@"UIView" _sublayerObservationView;
@"UIView" _boundsObservationView;
@"UIViewFloatAnimatableProperty" _liftProgressProperty;
{CGPoint="x"d"y"d} _hoverLocation;
{CGPoint="x"d"y"d} _initialEffectPlatterPosition;
```

## Properties

```
@property (T@"_UIPointerEffectPlatterView",&,N,V_platterView) platterView;
@property (T@"UIView",W,N,V_lumaSamplingBackdrop) lumaSamplingBackdrop;
@property (T@"UIView",W,N,V_pointerPortal) pointerPortal;
@property (T@"UIPointerStyle",&,N,V_style) style;
@property (T@"UIPointerRegion",C,N,V_region) region;
@property (T@"NSMutableArray",R,N,V_completions) completions;
@property (Tq,N,V_state) state;
@property (TQ,N,V_animationCount) animationCount;
@property (T@"UIView",W,N,V_positionReferenceView) positionReferenceView;
@property (T@"UIWindow",W,N,V_subtreeMonitoredWindow) subtreeMonitoredWindow;
@property (T@"UIView",W,N,V_sublayerObservationView) sublayerObservationView;
@property (T@"UIView",W,N,V_boundsObservationView) boundsObservationView;
@property (T{CGPoint=dd},N,V_initialEffectPlatterPosition) initialEffectPlatterPosition;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_liftProgressProperty) liftProgressProperty;
@property (T@"UIPointerInteractionAnimator",&,N,V_entranceAnimator) entranceAnimator;
@property (T@"UIPointerInteractionAnimator",&,N,V_exitAnimator) exitAnimator;
@property (Td,N,V_liftProgress) liftProgress;
@property (T{CGPoint=dd},N,V_hoverLocation) hoverLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIContentEffectDescriptor>",R,N) descriptor;
```

## Instance methods

```
-[_UIPointerContentEffect setRegion:];
-[_UIPointerContentEffect platterView];
-[_UIPointerContentEffect animationCount];
-[_UIPointerContentEffect addCompletion:];
-[_UIPointerContentEffect setDescriptor:andKey:];
-[_UIPointerContentEffect previewForContinuingToEffectWithPreview:];
-[_UIPointerContentEffect region];
-[_UIPointerContentEffect setState:];
-[_UIPointerContentEffect setPlatterView:];
-[_UIPointerContentEffect descriptor];
-[_UIPointerContentEffect observeValueForKeyPath:ofObject:change:context:];
-[_UIPointerContentEffect begin];
-[_UIPointerContentEffect dealloc];
-[_UIPointerContentEffect completions];
-[_UIPointerContentEffect style];
-[_UIPointerContentEffect _monitoredView:didMoveFromSuperview:toSuperview:];
-[_UIPointerContentEffect setStyle:];
-[_UIPointerContentEffect _monitoredView:willMoveFromSuperview:toSuperview:];
-[_UIPointerContentEffect setAnimationCount:];
-[_UIPointerContentEffect liftProgress];
-[_UIPointerContentEffect setLiftProgress:];
-[_UIPointerContentEffect _monitorsView:];
-[_UIPointerContentEffect hash];
-[_UIPointerContentEffect isEqual:];
-[_UIPointerContentEffect state];
-[_UIPointerContentEffect _anchorPlatterView:toPreview:updateBounds:];
-[_UIPointerContentEffect _cleanUpObservation];
-[_UIPointerContentEffect _commitPointerStyleToArbiterWithCompletion:];
-[_UIPointerContentEffect _createAndInstallPlatterView];
-[_UIPointerContentEffect _currentAnimatedLiftProgress];
-[_UIPointerContentEffect _ensureRelativeEffectViewOrderInContainer];
-[_UIPointerContentEffect _modifyEffectContainerViewHierarchy:waitForCACommit:];
-[_UIPointerContentEffect _positionReferenceViewForPreview:];
-[_UIPointerContentEffect _setStyle:andRegion:];
-[_UIPointerContentEffect _tearDownPlatterView];
-[_UIPointerContentEffect _updateFromState:toState:];
-[_UIPointerContentEffect _updatePlatterView:forStyle:];
-[_UIPointerContentEffect boundsObservationView];
-[_UIPointerContentEffect end:];
-[_UIPointerContentEffect entranceAnimator];
-[_UIPointerContentEffect exitAnimator];
-[_UIPointerContentEffect hoverLocation];
-[_UIPointerContentEffect initWithStyle:region:];
-[_UIPointerContentEffect initialEffectPlatterPosition];
-[_UIPointerContentEffect liftProgressProperty];
-[_UIPointerContentEffect lumaSamplingBackdrop];
-[_UIPointerContentEffect pointerPortal];
-[_UIPointerContentEffect positionReferenceView];
-[_UIPointerContentEffect setBoundsObservationView:];
-[_UIPointerContentEffect setEntranceAnimator:];
-[_UIPointerContentEffect setExitAnimator:];
-[_UIPointerContentEffect setHoverLocation:];
-[_UIPointerContentEffect setInitialEffectPlatterPosition:];
-[_UIPointerContentEffect setLiftProgressProperty:];
-[_UIPointerContentEffect setLumaSamplingBackdrop:];
-[_UIPointerContentEffect setPointerPortal:];
-[_UIPointerContentEffect setPositionReferenceView:];
-[_UIPointerContentEffect setPressed:animated:];
-[_UIPointerContentEffect setSublayerObservationView:];
-[_UIPointerContentEffect setSubtreeMonitoredWindow:];
-[_UIPointerContentEffect sublayerObservationView];
-[_UIPointerContentEffect subtreeMonitoredWindow];
```
