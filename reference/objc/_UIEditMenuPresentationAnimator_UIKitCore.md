# `_UIEditMenuPresentationAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIEditMenuInteractionAnimating`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _animationBlocks;
@"NSMutableArray" _completionBlocks;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_animationBlocks) animationBlocks;
@property (T@"NSMutableArray",&,N,V_completionBlocks) completionBlocks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIEditMenuPresentationAnimator addAnimations:];
-[_UIEditMenuPresentationAnimator addCompletion:];
-[_UIEditMenuPresentationAnimator completionBlocks];
-[_UIEditMenuPresentationAnimator setCompletionBlocks:];
-[_UIEditMenuPresentationAnimator animationBlocks];
-[_UIEditMenuPresentationAnimator runAnimations];
-[_UIEditMenuPresentationAnimator runCompletions];
-[_UIEditMenuPresentationAnimator setAnimationBlocks:];
```
