# `UIDynamicAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 6 properties, 101 instance methods, 6 class methods

## Instance variables

```
@"PKExtendedPhysicsWorld" _world;
^{_UIUpdateSequenceItemInternal=} _uiUpdateSequenceItem;
d _elapsedTime;
d _realElapsedTime;
d _lastUpdateTime;
d _lastInterval;
q _ticks;
@"UIDynamicsDebug" _dynamicsDebug;
@"NSMutableDictionary" _bodies;
@"NSMutableArray" _topLevelBehaviors;
@"NSMutableSet" _registeredBehaviors;
@"NSMutableSet" _behaviorsToRemove;
@"NSMutableSet" _behaviorsToAdd;
@"NSMutableIndexSet" _availableFieldCategories;
@"NSMutableArray" _postSolverActions;
@"NSMutableArray" _beginContacts;
@"NSMutableArray" _endContacts;
B _isInWorldStepMethod;
B _needsLocalBehaviorReevaluation;
B _stopping;
{_UIUpdateRequest="flags"I"minRate"I"preferredRate"I"maxRate"I"phase"Q"load"Q} _updateRequest;
B _updateRequestIsConfiguredForSettling;
Q _referenceSystemType;
Q _integralization;
{?="delegateImplementsDynamicAnimatorDidPause"b1"delegateImplementsDynamicAnimatorWillResume"b1"physicsKitImplements109159385"b1} _stateFlags;
d _accuracy;
i _registeredCollisionGroups;
i _registeredImplicitBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceSystemBounds;
@"<_UIDynamicReferenceSystem>" _referenceSystem;
i _debugInterval;
B _debugEnabled;
@? _action;
@"<UIDynamicAnimatorDelegate>" _delegate;
B _disableDisplayLink;
d _speed;
@"UIDynamicAnimatorTicker" _ticker;
```

## Properties

```
@property (T@"UIDynamicAnimatorTicker",&,N,V_ticker) ticker;
@property (T@"UIView",R,N) referenceView;
@property (T@"NSArray",R,C,N) behaviors;
@property (TB,R,N,GisRunning) running;
@property (Td,R,N) elapsedTime;
@property (T@"<UIDynamicAnimatorDelegate>",W,N) delegate;
```

## Class methods

```
+[UIDynamicAnimator initialize];
+[UIDynamicAnimator _allDynamicAnimators];
+[UIDynamicAnimator _clearReferenceViewFromAnimators:];
+[UIDynamicAnimator _referenceViewSizeChanged:];
+[UIDynamicAnimator _registerAnimator:];
+[UIDynamicAnimator _unregisterAnimator:];
```

## Instance methods

```
-[UIDynamicAnimator _setDelegate:];
-[UIDynamicAnimator isRunning];
-[UIDynamicAnimator elapsedTime];
-[UIDynamicAnimator _stop];
-[UIDynamicAnimator recursiveDescription];
-[UIDynamicAnimator layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[UIDynamicAnimator setDebugEnabled:];
-[UIDynamicAnimator _start];
-[UIDynamicAnimator init];
-[UIDynamicAnimator layoutAttributesForDecorationViewOfKind:atIndexPath:];
-[UIDynamicAnimator initWithCollectionViewLayout:];
-[UIDynamicAnimator dealloc];
-[UIDynamicAnimator _world];
-[UIDynamicAnimator _delegate];
-[UIDynamicAnimator setDelegate:];
-[UIDynamicAnimator settlingDuration];
-[UIDynamicAnimator setReferenceView:];
-[UIDynamicAnimator delegate];
-[UIDynamicAnimator description];
-[UIDynamicAnimator referenceView];
-[UIDynamicAnimator _speed];
-[UIDynamicAnimator _shouldReevaluateLocalBehaviors];
-[UIDynamicAnimator removeBehavior:];
-[UIDynamicAnimator _checkBehavior:];
-[UIDynamicAnimator _deactivateUIUpdateSequenceItem];
-[UIDynamicAnimator _postSolverStep];
-[UIDynamicAnimator _tickle];
-[UIDynamicAnimator settlingLinearVelocityThreshold];
-[UIDynamicAnimator _activateUIUpdateSequenceItem];
-[UIDynamicAnimator _alwaysDisableDisplayLink];
-[UIDynamicAnimator _animatorIntegralization];
-[UIDynamicAnimator _animatorInterval];
-[UIDynamicAnimator _animatorStep:];
-[UIDynamicAnimator _bodyForItem:];
-[UIDynamicAnimator _clearReferenceView];
-[UIDynamicAnimator _configureUpdateRequestFrameRateForSettling:];
-[UIDynamicAnimator _containsBehavior:];
-[UIDynamicAnimator _debugEnabled];
-[UIDynamicAnimator _debugInterval];
-[UIDynamicAnimator _defaultMapper:position:angle:itemType:];
-[UIDynamicAnimator _evaluateLocalBehaviors];
-[UIDynamicAnimator _invalidateCollectionViewLayout:];
-[UIDynamicAnimator _isWorldActive];
-[UIDynamicAnimator _keyForItem:];
-[UIDynamicAnimator _newBodyForItem:inItemGroup:];
-[UIDynamicAnimator _performAnimationTickForTimestamp:];
-[UIDynamicAnimator _preSolverStep];
-[UIDynamicAnimator _ptmRatio];
-[UIDynamicAnimator _realElapsedTime];
-[UIDynamicAnimator _reevaluateImplicitBounds];
-[UIDynamicAnimator _referenceSystem];
-[UIDynamicAnimator _referenceSystemBounds];
-[UIDynamicAnimator _referenceSystemType];
-[UIDynamicAnimator _registerBehavior:];
-[UIDynamicAnimator _registerBodyForItem:];
-[UIDynamicAnimator _registerCollisionGroup];
-[UIDynamicAnimator _registerFieldCategoryForFieldBehavior:];
-[UIDynamicAnimator _registerImplicitBounds];
-[UIDynamicAnimator _reportBeginContacts];
-[UIDynamicAnimator _reportEndContacts];
-[UIDynamicAnimator _runBlockPostSolverIfNeeded:];
-[UIDynamicAnimator _setAction:];
-[UIDynamicAnimator _setAlwaysDisableDisplayLink:];
-[UIDynamicAnimator _setAnimatorIntegralization:];
-[UIDynamicAnimator _setDebugEnabled:];
-[UIDynamicAnimator _setDebugInterval:];
-[UIDynamicAnimator _setReferenceSystem:];
-[UIDynamicAnimator _setRunning:];
-[UIDynamicAnimator _setSpeed:];
-[UIDynamicAnimator _setupWorld];
-[UIDynamicAnimator _ticks];
-[UIDynamicAnimator _traverseBehaviorHierarchy:];
-[UIDynamicAnimator _unregisterBehavior:];
-[UIDynamicAnimator _unregisterBodyForItem:action:];
-[UIDynamicAnimator _unregisterCollisionGroup];
-[UIDynamicAnimator _unregisterFieldCategoryForFieldBehavior:];
-[UIDynamicAnimator _unregisterImplicitBounds];
-[UIDynamicAnimator _updateRequestedFrameRateIfNeeded];
-[UIDynamicAnimator addBehavior:];
-[UIDynamicAnimator behaviors];
-[UIDynamicAnimator debugAnimationSpeed];
-[UIDynamicAnimator debugFrameInterval];
-[UIDynamicAnimator didBeginContact:];
-[UIDynamicAnimator didEndContact:];
-[UIDynamicAnimator initWithReferenceSystem:];
-[UIDynamicAnimator initWithReferenceView:];
-[UIDynamicAnimator isDebugEnabled];
-[UIDynamicAnimator isSettling];
-[UIDynamicAnimator itemsInRect:];
-[UIDynamicAnimator layoutAttributesForCellAtIndexPath:];
-[UIDynamicAnimator removeAllBehaviors];
-[UIDynamicAnimator setDebugAnimationSpeed:];
-[UIDynamicAnimator setDebugFrameInterval:];
-[UIDynamicAnimator setSettlingAngularVelocityThreshold:];
-[UIDynamicAnimator setSettlingDuration:];
-[UIDynamicAnimator setSettlingLinearVelocityThreshold:];
-[UIDynamicAnimator setTicker:];
-[UIDynamicAnimator settlingAngularVelocityThreshold];
-[UIDynamicAnimator ticker];
-[UIDynamicAnimator updateItemFromCurrentState:];
-[UIDynamicAnimator updateItemUsingCurrentState:];
```
