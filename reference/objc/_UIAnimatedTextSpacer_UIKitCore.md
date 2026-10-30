# `_UIAnimatedTextSpacer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"UIViewSpringAnimationBehavior" _springBehavior;
d _delay;
d _duration;
d _targetHeight;
@? _synchronizedAnimationUpdater;
@? _completionHandler;
@"UIViewFloatAnimatableProperty" _heightAnimationProperty;
d _height;
@? _layoutInvalidator;
```

## Properties

```
@property (TB,R,D,N) isAnimating;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_heightAnimationProperty) heightAnimationProperty;
@property (Td,R,N,V_height) height;
@property (T@?,C,N,V_layoutInvalidator) layoutInvalidator;
@property (T@?,C,N,V_synchronizedAnimationUpdater) synchronizedAnimationUpdater;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Class methods

```
+[_UIAnimatedTextSpacer worksWithTextView:];
```

## Instance methods

```
-[_UIAnimatedTextSpacer _clearAnimationState];
-[_UIAnimatedTextSpacer setCompletionHandler:];
-[_UIAnimatedTextSpacer completionHandler];
-[_UIAnimatedTextSpacer init];
-[_UIAnimatedTextSpacer dealloc];
-[_UIAnimatedTextSpacer _startAnimation];
-[_UIAnimatedTextSpacer copyWithZone:];
-[_UIAnimatedTextSpacer isAnimating];
-[_UIAnimatedTextSpacer height];
-[_UIAnimatedTextSpacer _finalizeAnimation];
-[_UIAnimatedTextSpacer _updateAnimationWithPresentationValue:];
-[_UIAnimatedTextSpacer animateHeightFromSource:destination:];
-[_UIAnimatedTextSpacer beginExplicitHeightAnimationFromSource:toDestination:];
-[_UIAnimatedTextSpacer heightAnimationProperty];
-[_UIAnimatedTextSpacer initWithSpringBehavior:delay:duration:];
-[_UIAnimatedTextSpacer layoutInvalidator];
-[_UIAnimatedTextSpacer presentationFrameForTextLayoutFragmentFrame:];
-[_UIAnimatedTextSpacer setHeightAnimationProperty:];
-[_UIAnimatedTextSpacer setLayoutInvalidator:];
-[_UIAnimatedTextSpacer setSynchronizedAnimationUpdater:];
-[_UIAnimatedTextSpacer synchronizedAnimationUpdater];
-[_UIAnimatedTextSpacer verticalOffsetForSucceedingLayout];
```
