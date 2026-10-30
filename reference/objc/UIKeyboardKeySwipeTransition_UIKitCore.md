# `UIKeyboardKeySwipeTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardKeyplaneTransition`
- Protocols: `CAAnimationDelegate`
- 7 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _disableMeshOptimization;
@"NSArray" _startKeysOrdered;
@"NSArray" _endKeysOrdered;
@"NSArray" _startGeometries;
@"NSArray" _transitionKeys;
@"NSArray" _keyInfos;
d _previousProgress;
```

## Properties

```
@property (T@"NSArray",&,N,V_startKeysOrdered) startKeysOrdered;
@property (T@"NSArray",&,N,V_endKeysOrdered) endKeysOrdered;
@property (T@"NSArray",&,N,V_startGeometries) startGeometries;
@property (T@"NSArray",&,N,V_transitionKeys) transitionKeys;
@property (T@"NSArray",&,N,V_keyInfos) keyInfos;
@property (Td,N,V_previousProgress) previousProgress;
@property (TB,N,V_disableMeshOptimization) disableMeshOptimization;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardKeySwipeTransition updateWithProgress:];
-[UIKeyboardKeySwipeTransition animationDidStop:finished:];
-[UIKeyboardKeySwipeTransition removeAllAnimations];
-[UIKeyboardKeySwipeTransition startGeometries];
-[UIKeyboardKeySwipeTransition _runOpacityAnimation];
-[UIKeyboardKeySwipeTransition _runTransformAnimation];
-[UIKeyboardKeySwipeTransition commitTransitionRebuild];
-[UIKeyboardKeySwipeTransition disableMeshOptimization];
-[UIKeyboardKeySwipeTransition endKeysOrdered];
-[UIKeyboardKeySwipeTransition gatherTransitionKeys];
-[UIKeyboardKeySwipeTransition keyInfos];
-[UIKeyboardKeySwipeTransition keyRectForFrame:normalizedSubRect:];
-[UIKeyboardKeySwipeTransition meshTransformForKeyplane:forward:initial:];
-[UIKeyboardKeySwipeTransition nonInteractiveDuration];
-[UIKeyboardKeySwipeTransition previousProgress];
-[UIKeyboardKeySwipeTransition rebuildWithStartKeyplane:startView:endKeyplane:endView:];
-[UIKeyboardKeySwipeTransition runNonInteractivelyWithCompletion:];
-[UIKeyboardKeySwipeTransition setDisableMeshOptimization:];
-[UIKeyboardKeySwipeTransition setEndKeysOrdered:];
-[UIKeyboardKeySwipeTransition setKeyInfos:];
-[UIKeyboardKeySwipeTransition setPreviousProgress:];
-[UIKeyboardKeySwipeTransition setStartGeometries:];
-[UIKeyboardKeySwipeTransition setStartKeysOrdered:];
-[UIKeyboardKeySwipeTransition setTransitionKeys:];
-[UIKeyboardKeySwipeTransition startKeysOrdered];
-[UIKeyboardKeySwipeTransition transitionKeys];
```
