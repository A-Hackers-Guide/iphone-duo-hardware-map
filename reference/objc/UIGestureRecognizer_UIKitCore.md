# `UIGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIForceLevelClassifierDelegate`, `_UIGestureRecognizerDriverDelegate`, `GFGestureNodeDelegate`, `GFGestureNodeContainer`, `_UIExcludable`, `NSSecureCoding`, `_UITouchesEventRespondable`, `_UIPressesEventRespondable`, `_UIEventRespondable`
- 34 instance variables, 36 properties, 149 instance methods, 6 class methods

## Instance variables

```
{?="delegateShouldBegin"b1"delegateCanPrevent"b1"delegateCanBePrevented"b1"delegateShouldRecognizeSimultaneously"b1"delegateShouldReceiveEvent"b1"delegateShouldReceiveTouch"b1"delegateShouldReceivePress"b1"delegateShouldRequireFailure"b1"delegateShouldBeRequiredToFail"b1"delegateFailed"b1"privateDelegateShouldBegin"b1"privateDelegateCanPrevent"b1"privateDelegateCanBePrevented"b1"privateDelegateShouldRecognizeSimultaneously"b1"privateDelegateShouldReceiveEvent"b1"privateDelegateShouldReceiveTouch"b1"privateDelegateShouldReceivePress"b1"privateDelegateShouldRequireFailure"b1"privateDelegateShouldBeRequiredToFail"b1"privateDelegateCanCancel"b1"privateDelegateCanBeCancelled"b1"privateDelegateAcceptsBeingFailureRequirement"b1"privateDelegateAcceptsBeingFailureDependent"b1"frontBoardDelegateShouldReceiveDynamicButton"b1"subclassShouldRequireFailure"b1"subclassShouldBeRequiredToFail"b1"hasSubclassDynamicFailureRequirements"b1"hasDelegateDynamicFailureRequirements"b1"subclassTouchesEstimatedPropertiesUpdated"b1"subclassShouldReceiveTouchForEventRecognizerView"b1"queriedFailureRequirements"b1"cancelsTouchesInView"b1"delaysTouchesBegan"b1"delaysTouchesEnded"b1"disabled_DO_NOT_USE_DIRECTLY"b1"dirty"b1"delivered"b1"deliveredEndedOrCancelled"b1"continuous"b1"requiresDelayedBegan"b1"willBeginAfterSatisfyingFailureRequirements"b1"requiresSystemGesturesToFail"b1"requiresExclusiveTouchType"b1"initialTouchTypeIsValid"b1"forceRequirementSatisfied"b1"wantsDragEvents"b1"conformsToDragEventRespondable"b1"isDynamicGesture"b1"canExcludeWithActiveRequirements_DO_NOT_USE_DIRECTLY"b1"isObservingGesture"b1"didCheckForcePressShouldBegin"b1"canSendForcePressAction"b1"queriedShouldReceiveTouchesEvent"b1"shouldReceiveTouchesEvent"b1"queriedDelegateShouldReceiveTouchesEvent"b1"delegateShouldReceiveTouchesEvent"b1"queriedShouldReceivePressesEvent"b1"shouldReceivePressesEvent"b1"queriedDelegateShouldReceivePressesEvent"b1"delegateShouldReceivePressesEvent"b1"conformsToHoverEventRespondable"b1"conformsToScrollEventRespondable"b1"conformsToTransformEventRespondable"b1"conformsToDynamicButtonEventRespondable"b1"queriedShouldReceiveDynamicButtonEvent"b1"shouldReceiveDynamicButtonEvent"b1"queriedDelegateShouldReceiveDynamicButtonEvent"b1"delegateShouldReceiveDynamicButtonEvent"b1"canBeCancelledByAffectedViews"b1"enqueuedForReset"b1"sendUpdateOnEventChange"b1"hasDriver"b1"skipUpdatingContainerInSetView"b1"insideSetState"b1"subclassCanPrevent"b1} _gestureFlags;
@"NSMutableArray" _targets;
@"NSMutableArray" _delayedTouches;
@"NSMutableArray" _delayedPresses;
@"<_UIGestureRecognizerContainer>" _container;
d _lastTouchTimestamp;
d _firstEventTimestamp;
q _state_DO_NOT_USE_DIRECTLY;
q _allowedTouchTypes;
q _initialTouchType;
@"NSMutableSet" _internalActiveTouches;
@"NSString" _name_DO_NOT_USE_DIRECTLY;
@"_UIForceLevelClassifier" _forceClassifier;
q _requiredPreviewForceState;
@"_UITouchForceObservable" _touchForceObservable;
@"NSObservation" _touchForceObservableAndClassifierObservation;
@"NSMutableArray" _forceTargets;
Q _forcePressCount;
@"NSObservationSource" _beganObservable;
@"NSMutableSet" _failureRequirements;
@"NSMutableSet" _failureDependents;
@"NSMutableSet" _activeEvents;
Q _inputPrecision;
q _buttonMask;
q _modifierFlags;
Q _machTimeEnqueuedForReset;
B _keepTouchesOnContinuation;
B _wantsGESEvents;
@"<GFGestureNode>" _node;
@ _componentController;
@"<UIGestureRecognizerDelegate>" _delegate;
@"NSArray" _allowedPressTypes;
@"UIGestureEnvironment" _gestureEnvironment;
@"UIGestureDelayedEventComponentDispatcher" _delayedEventComponentDispatcher;
```

## Properties

```
@property (TB,N) globallyScoped;
@property (TB,R,N) _isTouchGestureRecognizer;
@property (Tq,N,S_setRecognitionEvent:) _recognitionEvent;
@property (T@"NSMutableSet",R,N) _pairedGestureIdentifiers;
@property (TB,R,N,G_isPaused) _paused;
@property (Tq,R,N) _defaultAllowedMouseButtons;
@property (TB,R,N) _wantsPartialTouchSequences;
@property (T@"_UIGestureRecognizerDriver",R,N) _driver;
@property (T@"UIView",&,N) view;
@property (T@"NSString",R,N) _briefDescription;
@property (T@"NSSet",R,N) _allActiveTouches;
@property (TB,R,N) _isAllowedToReceiveGESEvents;
@property (TB,N,G_canExcludeWithActiveRequirements,S_setCanExcludeWithActiveRequirements:) canExcludeWithActiveRequirements;
@property (TB,N,G_wantsGESEvents,S_wantsGESEvents:,V_wantsGESEvents) wantsGESEvents;
@property (TB,N,G_requiresSystemGesturesToFail,S_setRequiresSystemGesturesToFail:) requiresSystemGesturesToFail;
@property (Td,R,N) lastTouchTimestamp;
@property (TB,N,S_setKeepTouchesOnContinuation:,V_keepTouchesOnContinuation) _keepTouchesOnContinuation;
@property (TB,R,N) _hasUnmetFailureRequirements;
@property (T@"<_UIGestureRecognizerContainer>",W,N) container;
@property (Tq,R,N) state;
@property (T@"<UIGestureRecognizerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled) enabled;
@property (TB,N) cancelsTouchesInView;
@property (TB,N) delaysTouchesBegan;
@property (TB,N) delaysTouchesEnded;
@property (T@"NSArray",C,N) allowedTouchTypes;
@property (T@"NSArray",C,N,V_allowedPressTypes) allowedPressTypes;
@property (TB,N) requiresExclusiveTouchType;
@property (TQ,R,N) numberOfTouches;
@property (T@"NSString",C,N) name;
@property (Tq,R,N) modifierFlags;
@property (Tq,R,N) buttonMask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIGestureRecognizer supportsSecureCoding];
+[UIGestureRecognizer _supportsDefaultTouchTypes];
+[UIGestureRecognizer _supportsDefaultPressTypes];
+[UIGestureRecognizer _supportsTouchContinuation];
+[UIGestureRecognizer _shouldUseLinearForceLevelClassifier];
+[UIGestureRecognizer _supportsStylusTouches];
```

## Instance methods

```
-[UIGestureRecognizer _isAllowedToReceiveGESEvents];
-[UIGestureRecognizer canPreventGestureRecognizer:];
-[UIGestureRecognizer _shouldReceivePress:];
-[UIGestureRecognizer allowedTouchTypes];
-[UIGestureRecognizer setCancelsTouchesInView:];
-[UIGestureRecognizer _shouldBegin];
-[UIGestureRecognizer touchesEnded:withEvent:];
-[UIGestureRecognizer shouldReceiveEvent:];
-[UIGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[UIGestureRecognizer setAllowedTouchTypes:];
-[UIGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[UIGestureRecognizer _resetGestureRecognizer];
-[UIGestureRecognizer _shouldReceiveTouch:withEvent:];
-[UIGestureRecognizer _canCancelGestureRecognizer:];
-[UIGestureRecognizer setState:];
-[UIGestureRecognizer touchesCancelled:withEvent:];
-[UIGestureRecognizer _convertPoint:toSceneReferenceCoordinatesFromView:];
-[UIGestureRecognizer _shouldReceiveDynamicButton:];
-[UIGestureRecognizer cancelsTouchesInView];
-[UIGestureRecognizer init];
-[UIGestureRecognizer _gestureRecognizerDriver:didUpdateState:previousState:];
-[UIGestureRecognizer setAllowedPressTypes:];
-[UIGestureRecognizer pressesCancelled:withEvent:];
-[UIGestureRecognizer pressesEnded:withEvent:];
-[UIGestureRecognizer _driver];
-[UIGestureRecognizer _isGestureType:];
-[UIGestureRecognizer dealloc];
-[UIGestureRecognizer setDelaysTouchesEnded:];
-[UIGestureRecognizer setContainer:];
-[UIGestureRecognizer modifierFlags];
-[UIGestureRecognizer numberOfTouches];
-[UIGestureRecognizer reset];
-[UIGestureRecognizer _modifierFlags];
-[UIGestureRecognizer setView:];
-[UIGestureRecognizer requireGestureRecognizerToFail:];
-[UIGestureRecognizer _convertPoint:fromSceneReferenceCoordinatesToView:];
-[UIGestureRecognizer touchesBegan:withEvent:];
-[UIGestureRecognizer touchesMoved:withEvent:];
-[UIGestureRecognizer _needsDynamicDependentRequirementForGestureRecognizer:];
-[UIGestureRecognizer initWithTarget:action:];
-[UIGestureRecognizer locationInView:];
-[UIGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[UIGestureRecognizer isEnabled];
-[UIGestureRecognizer pressesBegan:withEvent:];
-[UIGestureRecognizer pressesChanged:withEvent:];
-[UIGestureRecognizer view];
-[UIGestureRecognizer setDelegate:];
-[UIGestureRecognizer setEnabled:];
-[UIGestureRecognizer delaysTouchesBegan];
-[UIGestureRecognizer encodeWithCoder:];
-[UIGestureRecognizer delegate];
-[UIGestureRecognizer shouldRequireFailureOfGestureRecognizer:];
-[UIGestureRecognizer description];
-[UIGestureRecognizer _shouldReceiveEvent:];
-[UIGestureRecognizer setName:];
-[UIGestureRecognizer initWithCoder:];
-[UIGestureRecognizer _stateUpdatedForDriver:previousState:];
-[UIGestureRecognizer removeTarget:action:];
-[UIGestureRecognizer _canBeCancelledByGestureRecognizer:];
-[UIGestureRecognizer _activeTouchesForEvent:];
-[UIGestureRecognizer _defaultAllowedMouseButtons];
-[UIGestureRecognizer _appendSubclassDescription:];
-[UIGestureRecognizer locationOfTouch:inView:];
-[UIGestureRecognizer setDelaysTouchesBegan:];
-[UIGestureRecognizer name];
-[UIGestureRecognizer _shouldReceiveTouch:forEvent:recognizerView:];
-[UIGestureRecognizer _updateGestureTraits];
-[UIGestureRecognizer state];
-[UIGestureRecognizer touchesEstimatedPropertiesUpdated:];
-[UIGestureRecognizer container];
-[UIGestureRecognizer _componentsCancelled:withEvent:];
-[UIGestureRecognizer _wantsGESEvents];
-[UIGestureRecognizer __canPreventGestureRecognizer:];
-[UIGestureRecognizer __requiresGestureRecognizerToFail:];
-[UIGestureRecognizer _activeEventOfType:];
-[UIGestureRecognizer _activeEvents];
-[UIGestureRecognizer _addTouch:forEvent:];
-[UIGestureRecognizer _affectedByGesture:];
-[UIGestureRecognizer _allActiveTouches];
-[UIGestureRecognizer _briefDescription];
-[UIGestureRecognizer _buttonMask];
-[UIGestureRecognizer _canExcludeOtherExcludables];
-[UIGestureRecognizer _canExcludeWithActiveRequirements];
-[UIGestureRecognizer _centroidOfTouches:excludingEnded:];
-[UIGestureRecognizer _componentControllerShouldReceiveScrollEvent:];
-[UIGestureRecognizer _componentControllerShouldReceiveTouch:buttonMask:];
-[UIGestureRecognizer _componentControllerShouldReceiveTransformEvent:];
-[UIGestureRecognizer _componentsBegan:withEvent:];
-[UIGestureRecognizer _componentsChanged:withEvent:];
-[UIGestureRecognizer _componentsEnded:withEvent:];
-[UIGestureRecognizer _connectInterfaceBuilderEventConnection:];
-[UIGestureRecognizer _createNode];
-[UIGestureRecognizer _currentForceLevel];
-[UIGestureRecognizer _depthFirstCompare:];
-[UIGestureRecognizer _excludableDescription];
-[UIGestureRecognizer _exclude];
-[UIGestureRecognizer _failWithReason:];
-[UIGestureRecognizer _forceLevelClassifier];
-[UIGestureRecognizer _forceLevelClassifier:currentForceLevelDidChange:];
-[UIGestureRecognizer _hasUnmetFailureRequirements];
-[UIGestureRecognizer _isExcludedByExcludable:];
-[UIGestureRecognizer _isPaused];
-[UIGestureRecognizer _isTouchGestureRecognizer];
-[UIGestureRecognizer _keepTouchesOnContinuation];
-[UIGestureRecognizer _needsDynamicFailureRequirementForGestureRecognizer:];
-[UIGestureRecognizer _pairedGestureIdentifiers];
-[UIGestureRecognizer _pairedGestureIdentifiersAndCreate:];
-[UIGestureRecognizer _recognitionEvent];
-[UIGestureRecognizer _removeTouch:forEvent:];
-[UIGestureRecognizer _requiresSystemGesturesToFail];
-[UIGestureRecognizer _resetComponentController];
-[UIGestureRecognizer _sendScrollEventToComponentController:];
-[UIGestureRecognizer _sendTouchesToComponentController:buttonMask:];
-[UIGestureRecognizer _sendTransformEventToComponentController:];
-[UIGestureRecognizer _setCanExcludeWithActiveRequirements:];
-[UIGestureRecognizer _setForceLevelClassifier:];
-[UIGestureRecognizer _setKeepTouchesOnContinuation:];
-[UIGestureRecognizer _setRecognitionEvent:];
-[UIGestureRecognizer _setRequiresSystemGesturesToFail:];
-[UIGestureRecognizer _shouldDelayUntilForceLevelRequirementIsMet];
-[UIGestureRecognizer _touchForceObservable];
-[UIGestureRecognizer _wantsGESEvents:];
-[UIGestureRecognizer _wantsHoverEventsWhilePointerIsLocked];
-[UIGestureRecognizer _wantsPartialTouchSequences];
-[UIGestureRecognizer _willBeginAfterSatisfyingFailureRequirements];
-[UIGestureRecognizer addTarget:action:];
-[UIGestureRecognizer allowedPressTypes];
-[UIGestureRecognizer buttonMask];
-[UIGestureRecognizer currentPreviewForceState];
-[UIGestureRecognizer delaysTouchesEnded];
-[UIGestureRecognizer gestureNode:didEnqueuePhase:];
-[UIGestureRecognizer gestureNode:didUpdatePhase:];
-[UIGestureRecognizer gestureNode:roleForRelationType:relatedNode:];
-[UIGestureRecognizer gestureNodeShouldActivate:];
-[UIGestureRecognizer gestureNodeWillUnblock:];
-[UIGestureRecognizer globallyScoped];
-[UIGestureRecognizer ignorePress:forEvent:];
-[UIGestureRecognizer ignoreTouch:forEvent:];
-[UIGestureRecognizer indexOfGestureNode:];
-[UIGestureRecognizer isDeeperThanContainer:referenceNode:];
-[UIGestureRecognizer isDescendantOfContainer:referenceNode:];
-[UIGestureRecognizer lastTouchTimestamp];
-[UIGestureRecognizer removeFailureRequirement:];
-[UIGestureRecognizer requiredPreviewForceState];
-[UIGestureRecognizer requiresExclusiveTouchType];
-[UIGestureRecognizer setGloballyScoped:];
-[UIGestureRecognizer setRequiredPreviewForceState:];
-[UIGestureRecognizer setRequiresExclusiveTouchType:];
```
