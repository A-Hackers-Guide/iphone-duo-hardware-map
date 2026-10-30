# `_UIAnimatedTextAttachment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSTextAttachment`
- 5 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@? _invalidationHandler;
d _targetHeight;
@"UIViewFloatAnimatableProperty" _heightAnimationProperty;
@"NSMutableArray" _animateAlongsideHandlers;
@"NSMutableArray" _completionHandlers;
```

## Properties

```
@property (Td,N,V_targetHeight) targetHeight;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_heightAnimationProperty) heightAnimationProperty;
@property (T@"NSMutableArray",&,N,V_animateAlongsideHandlers) animateAlongsideHandlers;
@property (T@"NSMutableArray",&,N,V_completionHandlers) completionHandlers;
@property (T@"NSAttributedString",R,C,N) attachmentString;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[_UIAnimatedTextAttachment addCompletionHandler:];
-[_UIAnimatedTextAttachment completionHandlers];
-[_UIAnimatedTextAttachment setInvalidationHandler:];
-[_UIAnimatedTextAttachment init];
-[_UIAnimatedTextAttachment setCompletionHandlers:];
-[_UIAnimatedTextAttachment setBounds:];
-[_UIAnimatedTextAttachment invalidationHandler];
-[_UIAnimatedTextAttachment _initiateAnimationUsingSpringBehavior:];
-[_UIAnimatedTextAttachment _updatePresentationValues];
-[_UIAnimatedTextAttachment addAlongsideAnimation:];
-[_UIAnimatedTextAttachment animateAlongsideHandlers];
-[_UIAnimatedTextAttachment animateToTargetHeight:delay:usingSpringBehavior:];
-[_UIAnimatedTextAttachment attachmentString];
-[_UIAnimatedTextAttachment heightAnimationProperty];
-[_UIAnimatedTextAttachment setAnimateAlongsideHandlers:];
-[_UIAnimatedTextAttachment setHeightAnimationProperty:];
-[_UIAnimatedTextAttachment setTargetHeight:];
-[_UIAnimatedTextAttachment targetHeight];
```
