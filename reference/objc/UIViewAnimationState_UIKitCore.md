# `UIViewAnimationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 52 instance variables, 15 properties, 76 instance methods, 4 class methods

## Instance variables

```
@"UIViewAnimationState" _nextState;
@"NSString" _animationID;
^v _context;
@ _delegate;
d _duration;
d _delay;
d _frameInterval;
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} _preferredFrameRateRange;
I _updateReason;
d _start;
q _curve;
f _repeatCount;
q _transition;
@"UIView" _transitionView;
@"NSDictionary" _transitionOptions;
i _filter;
@"UIView" _filterView;
f _filterValue;
: _willStartSelector;
: _didEndSelector;
i _didEndCount;
b1 _willStartSent;
b1 _useCurrentLayerState;
b1 _cacheTransition;
b1 _autoreverses;
b1 _layoutSubviews;
b1 _hasOuterAnimator;
b1 _hasOuterTrackingAnimator;
b1 _disallowCaptureWithinPropertyAnimator;
b1 _completionCallbacksDisabledOnPop;
@"NSMutableArray" _trackedAnimations;
@"NSUUID" _uuid;
@"<_UIBasicAnimationFactory>" _animationFactory;
@"CAMediaTimingFunction" _customCurve;
B _animationFactoryMakesPerAnimationCustomCurves;
B _disallowAdditiveAnimations;
@? _alongsideAnimations;
@"NSMutableArray" _addedCompletions;
B _flushUpdates;
B _animationDidStopSent;
B _animationDidStopForced;
B _allowUserInteraction;
B _allowUserInteractionToCutOffEndOfAnimation;
B _allowsHitTesting;
B _belongsToTrackingAnimator;
B _disallowInheritance;
B _useBackingOutermostLayerForTransition;
q _finishedPosition;
@"UIViewAnimationState" _retainedSelf;
@"NSMutableArray" _viewsPendingConstraintBasedAnimation;
@"NSMapTable" _viewToDeferredAnimationsMap;
@"UIViewPropertyAnimator" _propertyAnimator;
```

## Properties

```
@property (TB,R,N) _runsAlongsideAnimations;
@property (TB,R,N) _allowsUserInteraction;
@property (T{CAFrameRateRange=fff},N,V_preferredFrameRateRange) preferredFrameRateRange;
@property (TI,N,V_updateReason) updateReason;
@property (T@"UIViewAnimationState",R,N,V_nextState) nextState;
@property (TB,N,V_disallowInheritance) disallowInheritance;
@property (T@,R,N) delegate;
@property (Td,N,V_delay) delay;
@property (Tf,N,V_repeatCount) repeatCount;
@property (TI,N,V_autoreverses) autoreverses;
@property (TB,R,N) isInProcess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIViewAnimationState _addConstraintPendingAnimation:container:];
+[UIViewAnimationState _addViewForConstraintBasedAnimation:];
+[UIViewAnimationState _addSystemPostAnimationAction:];
+[UIViewAnimationState originalAnimationForKeyPath:inLayer:];
```

## Instance methods

```
-[UIViewAnimationState updateReason];
-[UIViewAnimationState pop];
-[UIViewAnimationState nextState];
-[UIViewAnimationState setAutoreverses:];
-[UIViewAnimationState isInProcess];
-[UIViewAnimationState _runAlongsideAnimations];
-[UIViewAnimationState actionForLayer:forKey:];
-[UIViewAnimationState _removeAnimationStateFromTrackingMap:];
-[UIViewAnimationState _isKeyframeAnimation];
-[UIViewAnimationState _shouldAnimateAdditivelyForKey:onLayer:forView:];
-[UIViewAnimationState _removeAnimationStateFromTrackingMap:disableTrackingIfNeeded:];
-[UIViewAnimationState animationDidStart:];
-[UIViewAnimationState setUpdateReason:];
-[UIViewAnimationState _trackedAnimations];
-[UIViewAnimationState disallowInheritance];
-[UIViewAnimationState _elapsedTimeForCanonicallyTrackedAnimation];
-[UIViewAnimationState _isTrackingEnabled];
-[UIViewAnimationState setRepeatCount:];
-[UIViewAnimationState _removeLastCompletion];
-[UIViewAnimationState animationDidStop:finished:];
-[UIViewAnimationState repeatCount];
-[UIViewAnimationState _canonicalTrackedLayerAnimationInLayer:];
-[UIViewAnimationState _deferredAnimationForView:key:ignoringKeyFrames:];
-[UIViewAnimationState _unpacedFractionCompleteForAnimation:inLayer:duration:];
-[UIViewAnimationState _addAnimationStateForTracking:];
-[UIViewAnimationState _hasDeferredAnimationForView:key:];
-[UIViewAnimationState init];
-[UIViewAnimationState _animationDidStopWithNilAnimationFinished:];
-[UIViewAnimationState _trackAnimation:nonAdditiveAnimation:withAnimationKey:forKeyPath:inLayer:];
-[UIViewAnimationState setPreferredFrameRateRange:];
-[UIViewAnimationState _addCompletion:];
-[UIViewAnimationState _runConstraintBasedLayoutAnimations];
-[UIViewAnimationState _setFinishedPosition:];
-[UIViewAnimationState autoreverses];
-[UIViewAnimationState _transferAnimationToTrackingAnimator:];
-[UIViewAnimationState preferredFrameRateRange];
-[UIViewAnimationState _cancelDeferredAnimationForView:key:];
-[UIViewAnimationState _finalizeDeferredAnimations];
-[UIViewAnimationState delay];
-[UIViewAnimationState _createDeferredAnimationForKey:ignoringKeyFrames:];
-[UIViewAnimationState _allowsUserInteractionToCutOffEndOfAnimation];
-[UIViewAnimationState _allowsUserInteraction];
-[UIViewAnimationState _prepareForViewAnimationAfterPush];
-[UIViewAnimationState _setAlongsideAnimations:];
-[UIViewAnimationState configureAnimation:forLayer:forKey:];
-[UIViewAnimationState animationForLayer:forKey:forView:];
-[UIViewAnimationState setDelay:];
-[UIViewAnimationState _trackAnimation:withAnimationKey:forKeyPath:inLayer:];
-[UIViewAnimationState _acceptEarlyAnimationCutoff:];
-[UIViewAnimationState _didEndCount];
-[UIViewAnimationState _allowsHitTesting];
-[UIViewAnimationState _trackObject:withAnimationPropertyName:inLayer:];
-[UIViewAnimationState delegate];
-[UIViewAnimationState _performWithCompletionCallbacksDisabledOnPop:];
-[UIViewAnimationState _untrackAnimationsWithIdentifier:keyPath:inLayer:removeFromLayer:];
-[UIViewAnimationState sendDelegateAnimationDidStop:finished:];
-[UIViewAnimationState _defaultAnimationForKey:];
-[UIViewAnimationState _addCompletionWithPosition:];
-[UIViewAnimationState sendDelegateDidStopManually:];
-[UIViewAnimationState setAnimationAttributes:skipDelegateAssignment:];
-[UIViewAnimationState setAnimationAttributes:];
-[UIViewAnimationState setAnimationAttributes:skipDelegateAssignment:customCurve:];
-[UIViewAnimationState _transformIntoAdditiveAnimationAndNoteOriginal:inLayer:animationKey:];
-[UIViewAnimationState setupWithDuration:delay:view:options:factory:parentState:start:completion:];
-[UIViewAnimationState _incrementDidEndCount];
-[UIViewAnimationState _outerPropertyAnimator:];
-[UIViewAnimationState actionForLayer:forKey:forView:];
-[UIViewAnimationState _runsAlongsideAnimations];
-[UIViewAnimationState setDisallowInheritance:];
-[UIViewAnimationState _decrementDidEndCount];
-[UIViewAnimationState _canonicalTrackedUnpacedFractionComplete];
-[UIViewAnimationState _shouldStartFromCurrentStateForLayer:key:forView:];
-[UIViewAnimationState shouldAnimatePropertyWithKey:];
-[UIViewAnimationState _setCustomCurve:];
-[UIViewAnimationState _updateAnimationFrameWithAnimationProperties:];
-[UIViewAnimationState _animationDidStartWithNilAnimation];
```
