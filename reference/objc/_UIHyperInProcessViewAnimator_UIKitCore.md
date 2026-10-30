# `_UIHyperInProcessViewAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperAnimator_Internal`, `_UIHyperAnimator`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
Q __dimensions;
@"_UIHyperInteractor" __interactor;
@"_UISpringParameters" __trackingSpringParameters;
@"_UISpringParameters" __nonTrackingSpringParameters;
@"UIViewSpringAnimationBehavior" __springAnimationBehavior;
@"<UIViewSpringAnimationBehaviorDescribing>" __overrideSpringAnimationBehavior;
```

## Properties

```
@property (T@"UIViewSpringAnimationBehavior",R,N,V__springAnimationBehavior) _springAnimationBehavior;
@property (T@"<UIViewSpringAnimationBehaviorDescribing>",&,N,S_setOverrideSpringAnimationBehavior:,V__overrideSpringAnimationBehavior) _overrideSpringAnimationBehavior;
@property (T@"_UISpringParameters",C,N,S_setTrackingSpringParameters:,V__trackingSpringParameters) _trackingSpringParameters;
@property (T@"_UISpringParameters",C,N,S_setNonTrackingSpringParameters:,V__nonTrackingSpringParameters) _nonTrackingSpringParameters;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (T@"_UIHyperInteractor",W,N,S_setInteractor:,V__interactor) _interactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperInProcessViewAnimator supportsSecureCoding];
```

## Instance methods

```
-[_UIHyperInProcessViewAnimator _animateWithParameters:animations:];
-[_UIHyperInProcessViewAnimator _interactionEndedMutatingState:];
-[_UIHyperInProcessViewAnimator initWithDimensions:];
-[_UIHyperInProcessViewAnimator _interactionChanged];
-[_UIHyperInProcessViewAnimator encodeWithCoder:];
-[_UIHyperInProcessViewAnimator description];
-[_UIHyperInProcessViewAnimator initWithCoder:];
-[_UIHyperInProcessViewAnimator _interactor];
-[_UIHyperInProcessViewAnimator _dimensions];
-[_UIHyperInProcessViewAnimator copyWithZone:];
-[_UIHyperInProcessViewAnimator _interactionBegan];
-[_UIHyperInProcessViewAnimator isEqual:];
-[_UIHyperInProcessViewAnimator _setInteractor:];
-[_UIHyperInProcessViewAnimator _animateInteractive:animations:];
-[_UIHyperInProcessViewAnimator _nonTrackingSpringParameters];
-[_UIHyperInProcessViewAnimator _overrideSpringAnimationBehavior];
-[_UIHyperInProcessViewAnimator _setNonTrackingSpringParameters:];
-[_UIHyperInProcessViewAnimator _setOverrideSpringAnimationBehavior:];
-[_UIHyperInProcessViewAnimator _setTrackingSpringParameters:];
-[_UIHyperInProcessViewAnimator _springAnimationBehavior];
-[_UIHyperInProcessViewAnimator _trackingSpringParameters];
```
