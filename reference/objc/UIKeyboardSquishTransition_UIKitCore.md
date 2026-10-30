# `UIKeyboardSquishTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardKeyplaneTransition`
- 12 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
d _widthRatio;
d _offsetX;
B _useInteractiveOpacity;
B _disableMeshOptimization;
B _opacityAnimationDirectionForward;
Q _animationType;
@"NSArray" _startGeometries;
@"NSArray" _endGeometries;
@"NSArray" _commonVisibleKeys;
@"CADisplayLink" _opacityAnimationDisplayLink;
d _opacityAnimationBeginTime;
d _previousProgress;
```

## Properties

```
@property (T@"NSArray",&,N,V_startGeometries) startGeometries;
@property (T@"NSArray",&,N,V_endGeometries) endGeometries;
@property (T@"NSArray",&,N,V_commonVisibleKeys) commonVisibleKeys;
@property (T@"CADisplayLink",&,N,V_opacityAnimationDisplayLink) opacityAnimationDisplayLink;
@property (Td,N,V_opacityAnimationBeginTime) opacityAnimationBeginTime;
@property (TB,N,V_opacityAnimationDirectionForward) opacityAnimationDirectionForward;
@property (Td,N,V_previousProgress) previousProgress;
@property (TB,N,V_useInteractiveOpacity) useInteractiveOpacity;
@property (TQ,N,V_animationType) animationType;
@property (TB,N,V_disableMeshOptimization) disableMeshOptimization;
```

## Instance methods

```
-[UIKeyboardSquishTransition updateWithProgress:];
-[UIKeyboardSquishTransition animationType];
-[UIKeyboardSquishTransition dealloc];
-[UIKeyboardSquishTransition setAnimationType:];
-[UIKeyboardSquishTransition removeAllAnimations];
-[UIKeyboardSquishTransition setOpacityAnimationDisplayLink:];
-[UIKeyboardSquishTransition startGeometries];
-[UIKeyboardSquishTransition _allowFacesToAdjoinToAdjacentFaces];
-[UIKeyboardSquishTransition _animationsForEnd];
-[UIKeyboardSquishTransition _animationsForStart];
-[UIKeyboardSquishTransition _updateTransition];
-[UIKeyboardSquishTransition commitTransitionRebuild];
-[UIKeyboardSquishTransition commonVisibleKeys];
-[UIKeyboardSquishTransition disableMeshOptimization];
-[UIKeyboardSquishTransition endGeometries];
-[UIKeyboardSquishTransition geometriesForKeyplane:];
-[UIKeyboardSquishTransition meshTransformForKeyplane:toKeyplane:];
-[UIKeyboardSquishTransition opacityAnimationBeginTime];
-[UIKeyboardSquishTransition opacityAnimationDirectionForward];
-[UIKeyboardSquishTransition opacityAnimationDisplayLink];
-[UIKeyboardSquishTransition previousProgress];
-[UIKeyboardSquishTransition rebuildWithStartKeyplane:startView:endKeyplane:endView:];
-[UIKeyboardSquishTransition setCommonVisibleKeys:];
-[UIKeyboardSquishTransition setDisableMeshOptimization:];
-[UIKeyboardSquishTransition setEndGeometries:];
-[UIKeyboardSquishTransition setOpacityAnimationBeginTime:];
-[UIKeyboardSquishTransition setOpacityAnimationDirectionForward:];
-[UIKeyboardSquishTransition setPreviousProgress:];
-[UIKeyboardSquishTransition setStartGeometries:];
-[UIKeyboardSquishTransition setUseInteractiveOpacity:];
-[UIKeyboardSquishTransition sortedCommonVisibleKeys];
-[UIKeyboardSquishTransition symmetricMeshTransformForKeyplane:];
-[UIKeyboardSquishTransition updateOpacityAnimation:];
-[UIKeyboardSquishTransition useInteractiveOpacity];
```
