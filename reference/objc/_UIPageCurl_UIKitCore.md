# `_UIPageCurl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 36 instance methods, 0 class methods

## Instance variables

```
q _spineLocation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentRect;
@"UIView" _contentView;
@"_UIPageCurlState" _manualPageCurlState;
@"NSMutableArray" _pendingStateQueue;
@"NSMutableArray" _activeStateQueue;
@"NSMutableSet" _completedStates;
d _delayBetweenSuccessiveAnimations;
d _pageDiagonalAngle;
d _pageDiagonalLength;
d _manualPageCurlMaxDAngle;
```

## Properties

```
@property (Tq,R,N,V_spineLocation) _spineLocation;
@property (TB,R,N,G_isManualPageCurlInProgressAndUncommitted) _manualPageCurlInProgressAndUncommitted;
@property (T@"NSNumber",R,N) _wrappedManualPageCurlDirection;
@property (Td,N,S_setManualPageCurlMaxDAngle:,V_manualPageCurlMaxDAngle) _manualPageCurlMaxDAngle;
```

## Instance methods

```
-[_UIPageCurl dealloc];
-[_UIPageCurl _pageViewFrame:];
-[_UIPageCurl _wrappedManualPageCurlDirection];
-[_UIPageCurl _areAnimationsInFlightOrPending];
-[_UIPageCurl _abortManualCurlAtLocation:withSuggestedVelocity:];
-[_UIPageCurl _animationKeyPaths];
-[_UIPageCurl _baseAngleOffsetForState:];
-[_UIPageCurl _beginCurlWithState:previousState:];
-[_UIPageCurl _cancelAllActiveTransitionsAndAbandonCallbacks:];
-[_UIPageCurl _cancelTransitionWithState:invalidatingPageCurl:];
-[_UIPageCurl _cleanupState:];
-[_UIPageCurl _completeManualCurlAtLocation:withSuggestedVelocity:];
-[_UIPageCurl _distanceToTravelWithCurrentSpineLocation];
-[_UIPageCurl _durationForManualCurlEndAnimationWithSuggestedVelocity:shouldComplete:];
-[_UIPageCurl _endManualCurlAtLocation:withSuggestedVelocity:shouldComplete:];
-[_UIPageCurl _enqueueCurlOfType:fromLocation:inDirection:withView:revealingView:completion:finally:];
-[_UIPageCurl _ensureCurlFilterOnLayer:];
-[_UIPageCurl _forceCleanupState:finished:completed:];
-[_UIPageCurl _fromValue:toValue:fromState:forAnimationWithKeyPath:];
-[_UIPageCurl _inputTimeForProgress:distanceToTravel:radius:minRadius:angle:dAngle:touchLocation:state:];
-[_UIPageCurl _isManualPageCurlInProgressAndUncommitted];
-[_UIPageCurl _isPreviousCurlCompatibleWithCurlOfType:inDirection:];
-[_UIPageCurl _manualPageCurlMaxDAngle];
-[_UIPageCurl _newAnimationForState:withKeyPath:duration:fromValue:];
-[_UIPageCurl _newCurlFilter];
-[_UIPageCurl _pageCurlAnimationDidStop:withState:];
-[_UIPageCurl _populateFromValue:toValue:fromState:forAnimationWithKeyPath:];
-[_UIPageCurl _referenceLocationForInitialLocation:direction:];
-[_UIPageCurl _setContentRect:];
-[_UIPageCurl _setManualPageCurlMaxDAngle:];
-[_UIPageCurl _spineLocation];
-[_UIPageCurl _updateCurlFromState:withTime:radius:angle:addingAnimations:];
-[_UIPageCurl _updateManualCurlToLocation:];
-[_UIPageCurl _updatedInputsFromState:forLocation:time:radius:angle:];
-[_UIPageCurl _validatedPageCurlTypeForPageCurlType:inDirection:];
-[_UIPageCurl initWithSpineLocation:andContentRect:inContentView:];
```
