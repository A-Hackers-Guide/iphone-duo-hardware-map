# `_UIStatusBarCycleAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`, `_UIStatusBarPersistentAnimation`
- 6 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _stopsAfterReversing;
B _visible;
@"NSArray" _layerAnimations;
q _state;
@"NSArray" _stoppingLayerAnimations;
@"NSMutableArray" _completionHandlers;
```

## Properties

```
@property (TB,N,V_visible) visible;
@property (T@"_UIStatusBarCycleLayerAnimation",R,N) mainLayerAnimation;
@property (T@"NSMutableArray",&,N,V_completionHandlers) completionHandlers;
@property (T@"NSArray",R,N,V_layerAnimations) layerAnimations;
@property (Tq,R,N,V_state) state;
@property (TB,N,V_stopsAfterReversing) stopsAfterReversing;
@property (T@"NSArray",&,N,V_stoppingLayerAnimations) stoppingLayerAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarCycleAnimation visible];
-[_UIStatusBarCycleAnimation resumePersistentAnimation];
-[_UIStatusBarCycleAnimation setVisible:];
-[_UIStatusBarCycleAnimation animationDidStop:finished:];
-[_UIStatusBarCycleAnimation completionHandlers];
-[_UIStatusBarCycleAnimation dealloc];
-[_UIStatusBarCycleAnimation stopWithCompletionHandler:];
-[_UIStatusBarCycleAnimation setCompletionHandlers:];
-[_UIStatusBarCycleAnimation start];
-[_UIStatusBarCycleAnimation description];
-[_UIStatusBarCycleAnimation state];
-[_UIStatusBarCycleAnimation _stopAnimations];
-[_UIStatusBarCycleAnimation layerAnimations];
-[_UIStatusBarCycleAnimation _sendCompletionsWithFinished:];
-[_UIStatusBarCycleAnimation _startAnimations];
-[_UIStatusBarCycleAnimation _stopStoppingAnimations];
-[_UIStatusBarCycleAnimation initWithLayerAnimations:];
-[_UIStatusBarCycleAnimation mainLayerAnimation];
-[_UIStatusBarCycleAnimation pausePersistentAnimation];
-[_UIStatusBarCycleAnimation setStoppingLayerAnimations:];
-[_UIStatusBarCycleAnimation setStopsAfterReversing:];
-[_UIStatusBarCycleAnimation stoppingLayerAnimations];
-[_UIStatusBarCycleAnimation stopsAfterReversing];
```
