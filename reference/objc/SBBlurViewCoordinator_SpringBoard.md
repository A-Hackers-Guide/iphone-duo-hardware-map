# `SBBlurViewCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _elementVCs;
Q _state;
@"NSMutableDictionary" _mapStateToBlocks;
```

## Properties

```
@property (T@"NSArray",R,N,V_elementVCs) viewControllers;
@property (TB,R,N,GisBlurred) blurred;
@property (TQ,R,N,V_state) state;
```

## Instance methods

```
-[SBBlurViewCoordinator _setState:];
-[SBBlurViewCoordinator init];
-[SBBlurViewCoordinator isBlurred];
-[SBBlurViewCoordinator description];
-[SBBlurViewCoordinator viewControllers];
-[SBBlurViewCoordinator state];
-[SBBlurViewCoordinator initWithElementViewControllers:];
-[SBBlurViewCoordinator _fireBlocksForState:];
-[SBBlurViewCoordinator addNotifyBlock:forState:];
-[SBBlurViewCoordinator removeNotifyBlock:forState:];
-[SBBlurViewCoordinator setBlurred:withAnimationFactory:completion:];
```
