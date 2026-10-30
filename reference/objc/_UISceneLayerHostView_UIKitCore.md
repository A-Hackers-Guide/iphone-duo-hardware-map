# `_UISceneLayerHostView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDirectionalRotationView`
- 9 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"FBSceneLayer" _sceneLayer;
@"UITransformer" _transformer;
@"UIScenePresentationContext" _presentationContext;
B _inheritsSecurity;
B _resizesHostedContext;
B _zombifiesHostedContext;
B _stopsHitTestTransformAccumulation;
B _stopsSecureSuperlayersValidation;
@"UIScenePresentationContext" _currentPresentationContext;
```

## Properties

```
@property (T@"UIScenePresentationContext",&,N,V_currentPresentationContext) currentPresentationContext;
@property (T@"UITransformer",&,N,V_transformer) transformer;
@property (T@"FBSceneLayer",R,N,V_sceneLayer) sceneLayer;
@property (TB,N,V_inheritsSecurity) inheritsSecurity;
@property (TB,N,V_resizesHostedContext) resizesHostedContext;
@property (TB,N,V_zombifiesHostedContext) zombifiesHostedContext;
@property (TB,N,V_stopsHitTestTransformAccumulation) stopsHitTestTransformAccumulation;
@property (TB,N,V_stopsSecureSuperlayersValidation) stopsSecureSuperlayersValidation;
```

## Instance methods

```
-[_UISceneLayerHostView stopsSecureSuperlayersValidation];
-[_UISceneLayerHostView resizesHostedContext];
-[_UISceneLayerHostView stopsHitTestTransformAccumulation];
-[_UISceneLayerHostView setStopsSecureSuperlayersValidation:];
-[_UISceneLayerHostView setStopsHitTestTransformAccumulation:];
-[_UISceneLayerHostView setResizesHostedContext:];
-[_UISceneLayerHostView initWithSceneLayer:];
-[_UISceneLayerHostView hitTest:withEvent:];
-[_UISceneLayerHostView setInheritsSecurity:];
-[_UISceneLayerHostView setZombifiesHostedContext:];
-[_UISceneLayerHostView transformer];
-[_UISceneLayerHostView inheritsSecurity];
-[_UISceneLayerHostView currentPresentationContext];
-[_UISceneLayerHostView sceneLayer];
-[_UISceneLayerHostView setTransformer:];
-[_UISceneLayerHostView setCurrentPresentationContext:];
-[_UISceneLayerHostView initWithFrame:];
-[_UISceneLayerHostView zombifiesHostedContext];
```
