# `_UIHyperOutOfProcessViewAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperAnimator_Internal`, `_UIHyperAnimator`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 13 properties, 26 instance methods, 2 class methods

## Instance variables

```
I __updateReason;
Q __dimensions;
@"_UIHyperInteractor" __interactor;
@"_UISpringParameters" __boundaryCrossedSpringParameters;
@"_UISpringParameters" __interactionEndedSpringParameters;
@"NSMutableSet" __propertyAnimators;
@"<_UIHyperOutOfProcessViewAnimatorDelegate>" __delegate;
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} __preferredFrameRateRange;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__propertyAnimators) _propertyAnimators;
@property (T{CAFrameRateRange=fff},N,S_setPreferredFrameRateRange:,V__preferredFrameRateRange) _preferredFrameRateRange;
@property (TI,N,S_setUpdateReason:,V__updateReason) _updateReason;
@property (TB,R,N,G_isAnimating) _animating;
@property (T@"<_UIHyperOutOfProcessViewAnimatorDelegate>",W,N,S_setDelegate:,V__delegate) _delegate;
@property (T@"_UISpringParameters",C,N,S_setBoundaryCrossedSpringParameters:,V__boundaryCrossedSpringParameters) _boundaryCrossedSpringParameters;
@property (T@"_UISpringParameters",C,N,S_setInteractionEndedSpringParameters:,V__interactionEndedSpringParameters) _interactionEndedSpringParameters;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (T@"_UIHyperInteractor",W,N,S_setInteractor:,V__interactor) _interactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperOutOfProcessViewAnimator supportsSecureCoding];
+[_UIHyperOutOfProcessViewAnimator keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperOutOfProcessViewAnimator _setDelegate:];
-[_UIHyperOutOfProcessViewAnimator _isAnimating];
-[_UIHyperOutOfProcessViewAnimator _animateWithParameters:animations:];
-[_UIHyperOutOfProcessViewAnimator _interactionEndedMutatingState:];
-[_UIHyperOutOfProcessViewAnimator _boundaryCrossedSpringParameters];
-[_UIHyperOutOfProcessViewAnimator initWithDimensions:];
-[_UIHyperOutOfProcessViewAnimator _setUpdateReason:];
-[_UIHyperOutOfProcessViewAnimator _setBoundaryCrossedSpringParameters:];
-[_UIHyperOutOfProcessViewAnimator _propertyAnimators];
-[_UIHyperOutOfProcessViewAnimator _delegate];
-[_UIHyperOutOfProcessViewAnimator _setInteractionEndedSpringParameters:];
-[_UIHyperOutOfProcessViewAnimator _animateWithParameters:velocity:animations:];
-[_UIHyperOutOfProcessViewAnimator _interactionChanged];
-[_UIHyperOutOfProcessViewAnimator encodeWithCoder:];
-[_UIHyperOutOfProcessViewAnimator _interactionEndedSpringParameters];
-[_UIHyperOutOfProcessViewAnimator description];
-[_UIHyperOutOfProcessViewAnimator initWithCoder:];
-[_UIHyperOutOfProcessViewAnimator _updateReason];
-[_UIHyperOutOfProcessViewAnimator _interactor];
-[_UIHyperOutOfProcessViewAnimator _dimensions];
-[_UIHyperOutOfProcessViewAnimator _preferredFrameRateRange];
-[_UIHyperOutOfProcessViewAnimator copyWithZone:];
-[_UIHyperOutOfProcessViewAnimator _interactionBegan];
-[_UIHyperOutOfProcessViewAnimator isEqual:];
-[_UIHyperOutOfProcessViewAnimator _setInteractor:];
-[_UIHyperOutOfProcessViewAnimator _setPreferredFrameRateRange:];
```
