# `_UIViewControllerTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerTransitionCoordinatorInternal`
- 7 instance variables, 23 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"_UIViewControllerTransitionContext" __mainContext;
@"NSMutableArray" __systemAlongsideAnimations;
@"NSMutableArray" __alongsideAnimations;
@"NSMutableArray" __alongsideAnimationViews;
@"NSMutableArray" __alongsideCompletions;
@"NSMutableArray" __interactiveChangeHandlers;
@"NSMutableArray" __invalidationHandlers;
```

## Properties

```
@property (T@"_UIViewControllerTransitionContext",N,S_setMainContext:,V__mainContext) _mainContext;
@property (T@"NSMutableArray",&,N,S_setSystemAlongsideAnimations:,V__systemAlongsideAnimations) _systemAlongsideAnimations;
@property (T@"NSMutableArray",&,N,S_setAlongsideAnimations:,V__alongsideAnimations) _alongsideAnimations;
@property (T@"NSMutableArray",&,N,S_setAlongsideAnimationViews:,V__alongsideAnimationViews) _alongsideAnimationViews;
@property (T@"NSMutableArray",&,N,S_setAlongsideCompletions:,V__alongsideCompletions) _alongsideCompletions;
@property (T@"NSMutableArray",&,N,S_setInteractiveChangeHandlers:,V__interactiveChangeHandlers) _interactiveChangeHandlers;
@property (T@"NSMutableArray",&,N,S_setInvalidationHandlers:,V__invalidationHandlers) _invalidationHandlers;
@property (TB,R,N,GisAnimated) animated;
@property (Tq,R,N) presentationStyle;
@property (TB,R,N) initiallyInteractive;
@property (TB,R,N) isInterruptible;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N,GisCancelled) cancelled;
@property (Td,R,N) transitionDuration;
@property (Td,R,N) percentComplete;
@property (Td,R,N) completionVelocity;
@property (Tq,R,N) completionCurve;
@property (T@"UIView",R,N) containerView;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIViewControllerTransitionCoordinator completionVelocity];
-[_UIViewControllerTransitionCoordinator _setMainContext:];
-[_UIViewControllerTransitionCoordinator percentComplete];
-[_UIViewControllerTransitionCoordinator animateAlongsideTransitionInView:animation:completion:];
-[_UIViewControllerTransitionCoordinator viewControllerForKey:];
-[_UIViewControllerTransitionCoordinator animateAlongsideTransition:completion:];
-[_UIViewControllerTransitionCoordinator viewForKey:];
-[_UIViewControllerTransitionCoordinator isAnimated];
-[_UIViewControllerTransitionCoordinator notifyWhenInteractionEndsUsingBlock:];
-[_UIViewControllerTransitionCoordinator initiallyInteractive];
-[_UIViewControllerTransitionCoordinator _applyVoidBlocks:releaseBlocks:];
-[_UIViewControllerTransitionCoordinator notifyWhenInteractionChangesUsingBlock:];
-[_UIViewControllerTransitionCoordinator isInteractive];
-[_UIViewControllerTransitionCoordinator initWithMainContext:];
-[_UIViewControllerTransitionCoordinator presentationStyle];
-[_UIViewControllerTransitionCoordinator isCancelled];
-[_UIViewControllerTransitionCoordinator _applyBlocks:releaseBlocks:];
-[_UIViewControllerTransitionCoordinator transitionDuration];
-[_UIViewControllerTransitionCoordinator _interactiveChangeHandlers];
-[_UIViewControllerTransitionCoordinator _systemAlongsideAnimations];
-[_UIViewControllerTransitionCoordinator isInterruptible];
-[_UIViewControllerTransitionCoordinator containerView];
-[_UIViewControllerTransitionCoordinator _setAlongsideAnimationViews:];
-[_UIViewControllerTransitionCoordinator targetTransform];
-[_UIViewControllerTransitionCoordinator completionCurve];
-[_UIViewControllerTransitionCoordinator _alongsideAnimationViews];
-[_UIViewControllerTransitionCoordinator _alongsideCompletions:];
-[_UIViewControllerTransitionCoordinator _setSystemAlongsideAnimations:];
-[_UIViewControllerTransitionCoordinator _animateAlongsideTransitionInView:systemAnimation:systemCompletion:animation:completion:];
-[_UIViewControllerTransitionCoordinator _mainContext];
-[_UIViewControllerTransitionCoordinator _interactiveChangeHandlers:];
-[_UIViewControllerTransitionCoordinator _setAlongsideAnimations:];
-[_UIViewControllerTransitionCoordinator isRotating];
-[_UIViewControllerTransitionCoordinator _systemAlongsideAnimations:];
-[_UIViewControllerTransitionCoordinator isCompleting];
-[_UIViewControllerTransitionCoordinator _setInteractiveChangeHandlers:];
-[_UIViewControllerTransitionCoordinator _alongsideCompletions];
-[_UIViewControllerTransitionCoordinator _alongsideAnimations];
-[_UIViewControllerTransitionCoordinator _setAlongsideCompletions:];
-[_UIViewControllerTransitionCoordinator _invalidationHandlers:];
-[_UIViewControllerTransitionCoordinator affineTransform];
-[_UIViewControllerTransitionCoordinator _setInvalidationHandlers:];
-[_UIViewControllerTransitionCoordinator _invalidationHandlers];
-[_UIViewControllerTransitionCoordinator _addInvalidationHandler:];
-[_UIViewControllerTransitionCoordinator _alongsideAnimations:];
```
