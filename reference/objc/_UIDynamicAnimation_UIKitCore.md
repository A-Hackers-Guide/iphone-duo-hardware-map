# `_UIDynamicAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 21 instance methods, 4 class methods

## Instance variables

```
@? _completion;
i _state;
b1 _began;
b1 _running;
b1 _completing;
b1 _yield;
b1 _grouped;
b1 _usesNSTimer;
```

## Properties

```
@property (Ti,R,N) state;
```

## Class methods

```
+[_UIDynamicAnimation _updateAnimations:];
+[_UIDynamicAnimation _updateAnimations:timer:];
+[_UIDynamicAnimation _updateAnimationsWithTimer:];
+[_UIDynamicAnimation dynamicAnimationForView:withInitialValue:velocity:type:anchorPoint:];
```

## Instance methods

```
-[_UIDynamicAnimation _stopAnimation];
-[_UIDynamicAnimation init];
-[_UIDynamicAnimation stop];
-[_UIDynamicAnimation dealloc];
-[_UIDynamicAnimation runWithCompletion:];
-[_UIDynamicAnimation _setGrouped:];
-[_UIDynamicAnimation description];
-[_UIDynamicAnimation _appendDescriptionToString:atLevel:];
-[_UIDynamicAnimation state];
-[_UIDynamicAnimation _animateForInterval:];
-[_UIDynamicAnimation _appendSubclassDescription:atLevel:];
-[_UIDynamicAnimation _callAppliers:additionalEndAppliers:done:];
-[_UIDynamicAnimation _cancelWithAppliers:];
-[_UIDynamicAnimation _completeWithFinished:];
-[_UIDynamicAnimation _isGrouped];
-[_UIDynamicAnimation _isRunning];
-[_UIDynamicAnimation _setShouldYield:];
-[_UIDynamicAnimation _setUsesNSTimer:];
-[_UIDynamicAnimation _shouldYield];
-[_UIDynamicAnimation _usesNSTimer];
-[_UIDynamicAnimation runWithCompletion:forScreen:runLoopMode:];
```
