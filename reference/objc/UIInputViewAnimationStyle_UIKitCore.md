# `UIInputViewAnimationStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 14 properties, 36 instance methods, 3 class methods

## Instance variables

```
B animated;
d duration;
Q extraOptions;
B interactivelyCancelled;
B _isLegacy;
B force;
B _dontMerge;
B _forAssertion;
@"NSMutableArray" _propertyAnimators;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_propertyAnimators) propertyAnimators;
@property (TB,N,V_forAssertion) forAssertion;
@property (TB,N,Vforce) force;
@property (TB,N,Vanimated) animated;
@property (TB,N,V_dontMerge) dontMerge;
@property (Td,N,Vduration) duration;
@property (TQ,N,VextraOptions) extraOptions;
@property (TB,N,VinteractivelyCancelled) interactivelyCancelled;
@property (TB,R,N) isAnimationCompleted;
@property (TB,R,N) canDismissWithScrollView;
@property (TB,R,N) canTakeSnapshot;
@property (Tq,R,N) animationType;
@property (Td,R,N) finalAlpha;
@property (T{CGAffineTransform=dddddd},R,N) finalTransform;
```

## Class methods

```
+[UIInputViewAnimationStyle animationStyleAnimated:duration:];
+[UIInputViewAnimationStyle animationStyleDefault];
+[UIInputViewAnimationStyle animationStyleImmediate];
```

## Instance methods

```
-[UIInputViewAnimationStyle finalTransform];
-[UIInputViewAnimationStyle dontMerge];
-[UIInputViewAnimationStyle setDontMerge:];
-[UIInputViewAnimationStyle endPlacementForInputViewSet:windowScene:];
-[UIInputViewAnimationStyle extraOptions];
-[UIInputViewAnimationStyle canTakeSnapshot];
-[UIInputViewAnimationStyle forAssertion];
-[UIInputViewAnimationStyle canDismissWithScrollView];
-[UIInputViewAnimationStyle addAnimationToCurrentAnimations:];
-[UIInputViewAnimationStyle animationType];
-[UIInputViewAnimationStyle animated];
-[UIInputViewAnimationStyle setExtraOptions:];
-[UIInputViewAnimationStyle launchAnimation:afterStarted:completion:forHost:fromCurrentPosition:];
-[UIInputViewAnimationStyle controllerForStartPlacement:endPlacement:];
-[UIInputViewAnimationStyle setAnimationType:];
-[UIInputViewAnimationStyle removePropertyAnimators];
-[UIInputViewAnimationStyle setAnimated:];
-[UIInputViewAnimationStyle duration];
-[UIInputViewAnimationStyle startPlacementForInputViewSet:currentPlacement:windowScene:];
-[UIInputViewAnimationStyle legacyAnimationCopy];
-[UIInputViewAnimationStyle cancelInterruptibleAnimations];
-[UIInputViewAnimationStyle isAnimationCompleted];
-[UIInputViewAnimationStyle finalAlpha];
-[UIInputViewAnimationStyle setForAssertion:];
-[UIInputViewAnimationStyle description];
-[UIInputViewAnimationStyle startPlacementForInputViewSet:currentPlacement:];
-[UIInputViewAnimationStyle setPropertyAnimators:];
-[UIInputViewAnimationStyle force];
-[UIInputViewAnimationStyle setDuration:];
-[UIInputViewAnimationStyle copyWithZone:];
-[UIInputViewAnimationStyle setInteractivelyCancelled:];
-[UIInputViewAnimationStyle setForce:];
-[UIInputViewAnimationStyle isEqual:];
-[UIInputViewAnimationStyle propertyAnimators];
-[UIInputViewAnimationStyle endPlacementForInputViewSet:];
-[UIInputViewAnimationStyle interactivelyCancelled];
```
