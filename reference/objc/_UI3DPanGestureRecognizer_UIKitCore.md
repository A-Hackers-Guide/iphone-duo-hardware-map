# `_UI3DPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 3 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
B canPanInZ;
{CAPoint3D=ddd} initial3DLocationInScene;
{CAPoint3D=ddd} current3DLocationInScene;
```

## Properties

```
@property (TB,N,VcanPanInZ) canPanInZ;
@property (T{CAPoint3D=ddd},N,Vinitial3DLocationInScene) initial3DLocationInScene;
@property (T{CAPoint3D=ddd},N,Vcurrent3DLocationInScene) current3DLocationInScene;
@property (TB,N,R) willPanZ;
@property (TB,N,R) isVisionIdiom;
@property (T@"NSArray",N,R) movingTouches;
```

## Instance methods

```
-[_UI3DPanGestureRecognizer touchesEnded:withEvent:];
-[_UI3DPanGestureRecognizer touchesCancelled:withEvent:];
-[_UI3DPanGestureRecognizer touchesBegan:withEvent:];
-[_UI3DPanGestureRecognizer touchesMoved:withEvent:];
-[_UI3DPanGestureRecognizer initWithTarget:action:];
-[_UI3DPanGestureRecognizer isVisionIdiom];
-[_UI3DPanGestureRecognizer _shouldTryToBeginWithEvent:];
-[_UI3DPanGestureRecognizer _didUpdateCentroidWithTouches:event:];
-[_UI3DPanGestureRecognizer canPanInZ];
-[_UI3DPanGestureRecognizer centroid3DOfTouches:excludingEnded:];
-[_UI3DPanGestureRecognizer current3DLocationInScene];
-[_UI3DPanGestureRecognizer handleTouchesEndedWithOldMovingTouches:];
-[_UI3DPanGestureRecognizer initial3DLocationInScene];
-[_UI3DPanGestureRecognizer movingTouches];
-[_UI3DPanGestureRecognizer process3DTouchesMoved:withEvent:];
-[_UI3DPanGestureRecognizer setCanPanInZ:];
-[_UI3DPanGestureRecognizer setCurrent3DLocationInScene:];
-[_UI3DPanGestureRecognizer setInitial3DLocationInScene:];
-[_UI3DPanGestureRecognizer update3DTouchesCentroid:];
-[_UI3DPanGestureRecognizer willPanZ];
```
