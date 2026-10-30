# `_UIHyperInProcessPointAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperAnimator_Internal`, `_UIHyperAnimator`, `NSSecureCoding`, `NSCopying`
- 9 instance variables, 13 properties, 26 instance methods, 1 class methods

## Instance variables

```
B __generatesFeedbackWhenBoundaryIsCrossed;
B __regionChangedDiscontinuouslyOnChange;
Q __dimensions;
@"_UIHyperInteractor" __interactor;
@"_UISpringParameters" __trackingSpringParameters;
@"_UISpringParameters" __nonTrackingSpringParameters;
@"UIViewSpringAnimationBehavior" __springAnimationBehavior;
@"UISelectionFeedbackGenerator" __feedbackGenerator;
@"UIViewVectorAnimatableProperty" __animatableProperty;
```

## Properties

```
@property (T@"UIViewSpringAnimationBehavior",R,N,V__springAnimationBehavior) _springAnimationBehavior;
@property (T@"UIViewVectorAnimatableProperty",R,N,V__animatableProperty) _animatableProperty;
@property (TB,N,S_setRegionChangedDiscontinuouslyOnChange:,V__regionChangedDiscontinuouslyOnChange) _regionChangedDiscontinuouslyOnChange;
@property (T@"UISelectionFeedbackGenerator",R,N,V__feedbackGenerator) _feedbackGenerator;
@property (T@"_UISpringParameters",C,N,S_setTrackingSpringParameters:,V__trackingSpringParameters) _trackingSpringParameters;
@property (T@"_UISpringParameters",C,N,S_setNonTrackingSpringParameters:,V__nonTrackingSpringParameters) _nonTrackingSpringParameters;
@property (TB,N,S_setGeneratesFeedbackWhenBoundaryIsCrossed:,V__generatesFeedbackWhenBoundaryIsCrossed) _generatesFeedbackWhenBoundaryIsCrossed;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (T@"_UIHyperInteractor",W,N,S_setInteractor:,V__interactor) _interactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperInProcessPointAnimator supportsSecureCoding];
```

## Instance methods

```
-[_UIHyperInProcessPointAnimator _animateWithParameters:animations:];
-[_UIHyperInProcessPointAnimator _interactionEndedMutatingState:];
-[_UIHyperInProcessPointAnimator initWithDimensions:];
-[_UIHyperInProcessPointAnimator _interactionChanged];
-[_UIHyperInProcessPointAnimator encodeWithCoder:];
-[_UIHyperInProcessPointAnimator description];
-[_UIHyperInProcessPointAnimator initWithCoder:];
-[_UIHyperInProcessPointAnimator _interactor];
-[_UIHyperInProcessPointAnimator _dimensions];
-[_UIHyperInProcessPointAnimator copyWithZone:];
-[_UIHyperInProcessPointAnimator _interactionBegan];
-[_UIHyperInProcessPointAnimator isEqual:];
-[_UIHyperInProcessPointAnimator _setInteractor:];
-[_UIHyperInProcessPointAnimator _animateWithPrelude:animations:];
-[_UIHyperInProcessPointAnimator _animatableProperty];
-[_UIHyperInProcessPointAnimator _feedbackGenerator];
-[_UIHyperInProcessPointAnimator _generatesFeedbackWhenBoundaryIsCrossed];
-[_UIHyperInProcessPointAnimator _nonTrackingSpringParameters];
-[_UIHyperInProcessPointAnimator _regionChangedDiscontinuouslyOnChange];
-[_UIHyperInProcessPointAnimator _setGeneratesFeedbackWhenBoundaryIsCrossed:];
-[_UIHyperInProcessPointAnimator _setNonTrackingSpringParameters:];
-[_UIHyperInProcessPointAnimator _setRegionChangedDiscontinuouslyOnChange:];
-[_UIHyperInProcessPointAnimator _setTrackingSpringParameters:];
-[_UIHyperInProcessPointAnimator _springAnimationBehavior];
-[_UIHyperInProcessPointAnimator _trackingSpringParameters];
-[_UIHyperInProcessPointAnimator _updateAnimatablePropertyValuesToConstrainedPoint];
```
