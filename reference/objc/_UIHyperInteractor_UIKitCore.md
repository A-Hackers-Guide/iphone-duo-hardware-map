# `_UIHyperInteractor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 36 instance variables, 35 properties, 78 instance methods, 0 class methods

## Instance variables

```
^d __unconstrainedPoint;
^d __initialTranslation;
^d __translation;
^d __translatedUnconstrainedPoint;
^d __velocity;
^d __effectiveVelocity;
^d __projectedPoint;
^d __closestPoint;
B __rubberBanding;
^d __unconstrainedVector;
^d __extentVector;
d __extent;
^d __unconstrainedExtentVector;
d __unconstrainedExtent;
d __constrainedFraction;
^d __constrainedPoint;
^d __constrainedVelocity;
^d __overridePresentationPoint;
r^d __presentationPoint;
^d __lastConstrainedPoint;
{?="region"b1"extender"b1"unconstrainedPoint"b1"translatedUnconstrainedPoint"b1"effectiveVelocity"b1"projectedPoint"b1"closestPoint"b1"rubberBanding"b1"unconstrainedVector"b1"extentVector"b1"extent"b1"unconstrainedExtentVector"b1"unconstrainedExtent"b1"constrainedFraction"b1"constrainedPoint"b1"constrainedVelocity"b1"presentationPoint"b1} _clean;
B __interactive;
B __overridingPresentationPoint;
@"NSObject<_UIHyperregion>" __region;
@"NSObject<_UIHyperExtender>" __extender;
@"NSObject<_UIHyperAnimator>" __animator;
Q __dimensions;
d __minimumSpeed;
d __decelerationRate;
d __rubberBandCoefficient;
@"<_UIHyperInteractorDelegate>" __delegate;
@? __regionGetter;
@? __extenderGetter;
@? __unconstrainedPointGetter;
@? __presentationPointWasInvalidated;
@"<_UIHyperInteractorBroadcaster>" __broadcaster;
```

## Properties

```
@property (Tr^d,R,N) _effectiveVelocity;
@property (Tr^d,R,N) _unconstrainedVector;
@property (Tr^d,R,N) _unconstrainedExtentVector;
@property (Td,R,N) _constrainedFraction;
@property (Tr^d,R,N,V__initialTranslation) _initialTranslation;
@property (Tr^d,R,N) _extentVector;
@property (Td,R,N) _unconstrainedExtent;
@property (Td,R,N) _extent;
@property (Tr^d,R,N) _overridePresentationPoint;
@property (TB,N,G_isOverridingPresentationPoint,S_setOverridingPresentationPoint:,V__overridingPresentationPoint) _overridingPresentationPoint;
@property (Tr^d,R,N,V__lastConstrainedPoint) _lastConstrainedPoint;
@property (T@?,C,N,S_setRegionGetter:,V__regionGetter) _regionGetter;
@property (T@?,C,N,S_setExtenderGetter:,V__extenderGetter) _extenderGetter;
@property (T@?,C,N,S_setUnconstrainedPointGetter:,V__unconstrainedPointGetter) _unconstrainedPointGetter;
@property (T@?,C,N,S_setPresentationPointWasInvalidated:,V__presentationPointWasInvalidated) _presentationPointWasInvalidated;
@property (T@"<_UIHyperInteractorBroadcaster>",&,N,S_setBroadcaster:,V__broadcaster) _broadcaster;
@property (Tr^d,R,N,V__translation) _translation;
@property (Tr^d,R,N) _velocity;
@property (Tr^d,R,N) _constrainedPoint;
@property (Tr^d,R,N) _constrainedVelocity;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (T@"NSObject<_UIHyperregion>",&,N,S_setRegion:,V__region) _region;
@property (T@"NSObject<_UIHyperExtender>",&,N,S_setExtender:,V__extender) _extender;
@property (T@"NSObject<_UIHyperAnimator>",&,N,S_setAnimator:,V__animator) _animator;
@property (Td,N,S_setMinimumSpeed:,V__minimumSpeed) _minimumSpeed;
@property (Td,N,S_setDecelerationRate:,V__decelerationRate) _decelerationRate;
@property (Td,N,S_setRubberBandCoefficient:,V__rubberBandCoefficient) _rubberBandCoefficient;
@property (Tr^d,R,N) _unconstrainedPoint;
@property (TB,R,N,G_isInteractive,V__interactive) _interactive;
@property (Tr^d,R,N) _translatedUnconstrainedPoint;
@property (Tr^d,R,N) _projectedPoint;
@property (Tr^d,R,N) _closestPoint;
@property (TB,R,N,G_isRubberBanding) _rubberBanding;
@property (Tr^d,R,N) _presentationPoint;
@property (T@"<_UIHyperInteractorDelegate>",W,N,S_setDelegate:,V__delegate) _delegate;
```

## Instance methods

```
-[_UIHyperInteractor _setDelegate:];
-[_UIHyperInteractor _velocity];
-[_UIHyperInteractor _interactionEndedMutatingState:];
-[_UIHyperInteractor observeValueForKeyPath:ofObject:change:context:];
-[_UIHyperInteractor initWithDimensions:];
-[_UIHyperInteractor dealloc];
-[_UIHyperInteractor _animator];
-[_UIHyperInteractor _delegate];
-[_UIHyperInteractor _setAnimator:];
-[_UIHyperInteractor description];
-[_UIHyperInteractor _dimensions];
-[_UIHyperInteractor _interactionBegan];
-[_UIHyperInteractor _copyOverridePresentationPoint:];
-[_UIHyperInteractor _extenderGetter];
-[_UIHyperInteractor _extent];
-[_UIHyperInteractor _projectedPoint];
-[_UIHyperInteractor _region];
-[_UIHyperInteractor _broadcaster];
-[_UIHyperInteractor _closestPoint];
-[_UIHyperInteractor _commitTranslation];
-[_UIHyperInteractor _constrainedFraction];
-[_UIHyperInteractor _constrainedPoint];
-[_UIHyperInteractor _constrainedVelocity];
-[_UIHyperInteractor _copyInitialTranslation:];
-[_UIHyperInteractor _copyTranslation:];
-[_UIHyperInteractor _copyUnconstrainedPoint:];
-[_UIHyperInteractor _copyVelocity:];
-[_UIHyperInteractor _decelerationRate];
-[_UIHyperInteractor _effectiveVelocity];
-[_UIHyperInteractor _extender];
-[_UIHyperInteractor _extentVector];
-[_UIHyperInteractor _getUnconstrainedPoint:forConstrainedPoint:];
-[_UIHyperInteractor _initialTranslation];
-[_UIHyperInteractor _interactionChangedCopyingTranslation:velocity:];
-[_UIHyperInteractor _interactionChangedCopyingTranslation:velocity:mutatingState:];
-[_UIHyperInteractor _interactionChangedMutatingTranslation:velocity:];
-[_UIHyperInteractor _interactionChangedMutatingTranslation:velocity:mutatingState:];
-[_UIHyperInteractor _interactionEnded];
-[_UIHyperInteractor _invalidateExtender];
-[_UIHyperInteractor _invalidateRegion];
-[_UIHyperInteractor _invalidateUnconstrainedPoint];
-[_UIHyperInteractor _isInteractive];
-[_UIHyperInteractor _isOverridingPresentationPoint];
-[_UIHyperInteractor _isRubberBanding];
-[_UIHyperInteractor _lastConstrainedPoint];
-[_UIHyperInteractor _minimumSpeed];
-[_UIHyperInteractor _mutateInitialTranslation:];
-[_UIHyperInteractor _mutateInternalUnconstrainedPoint:];
-[_UIHyperInteractor _mutateOverridePresentationPoint:];
-[_UIHyperInteractor _mutateTranslation:];
-[_UIHyperInteractor _mutateUnconstrainedPoint:];
-[_UIHyperInteractor _mutateVelocity:];
-[_UIHyperInteractor _overridePresentationPoint];
-[_UIHyperInteractor _presentationPoint];
-[_UIHyperInteractor _presentationPointWasInvalidated];
-[_UIHyperInteractor _regionGetter];
-[_UIHyperInteractor _rubberBandCoefficient];
-[_UIHyperInteractor _setBroadcaster:];
-[_UIHyperInteractor _setDecelerationRate:];
-[_UIHyperInteractor _setExtender:];
-[_UIHyperInteractor _setExtenderGetter:];
-[_UIHyperInteractor _setInteractive:];
-[_UIHyperInteractor _setInternalExtender:];
-[_UIHyperInteractor _setInternalRegion:];
-[_UIHyperInteractor _setMinimumSpeed:];
-[_UIHyperInteractor _setOverridingPresentationPoint:];
-[_UIHyperInteractor _setPresentationPointWasInvalidated:];
-[_UIHyperInteractor _setRegion:];
-[_UIHyperInteractor _setRegionGetter:];
-[_UIHyperInteractor _setRubberBandCoefficient:];
-[_UIHyperInteractor _setUnconstrainedPointGetter:];
-[_UIHyperInteractor _translatedUnconstrainedPoint];
-[_UIHyperInteractor _translation];
-[_UIHyperInteractor _unconstrainedExtent];
-[_UIHyperInteractor _unconstrainedExtentVector];
-[_UIHyperInteractor _unconstrainedPoint];
-[_UIHyperInteractor _unconstrainedPointGetter];
-[_UIHyperInteractor _unconstrainedVector];
```
