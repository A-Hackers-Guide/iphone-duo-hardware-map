# `UIViewKeyframeAnimationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewAnimationState`
- 6 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
d _frameDuration;
d _frameStartTime;
q _calculationMode;
@"NSMutableSet" _keyframeLayers;
@"NSMutableDictionary" _keyframeLayersForCurrentKeyFrameDict;
B _inFrame;
```

## Instance methods

```
-[UIViewKeyframeAnimationState pop];
-[UIViewKeyframeAnimationState _isKeyframeAnimation];
-[UIViewKeyframeAnimationState init];
-[UIViewKeyframeAnimationState _createDeferredAnimationForKey:ignoringKeyFrames:];
-[UIViewKeyframeAnimationState animationForLayer:forKey:forView:];
-[UIViewKeyframeAnimationState addKeyframeWithRelativeStartTime:relativeDuration:animations:];
-[UIViewKeyframeAnimationState cleanupTrackedLayers];
-[UIViewKeyframeAnimationState setupWithDuration:delay:view:options:factory:parentState:start:completion:];
-[UIViewKeyframeAnimationState _updateAnimationFrameWithAnimationProperties:];
```
