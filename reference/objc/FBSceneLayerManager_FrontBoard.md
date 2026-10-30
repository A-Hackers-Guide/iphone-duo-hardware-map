# `FBSceneLayerManager`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSOrderedSet" _layers;
@"NSOrderedSet" _fbsLayers;
@"NSHashTable" _suspendAssertions;
@"NSHashTable" _observers;
@"FBScene" _scene;
B _needsRebuildLayers;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"NSOrderedSet",R,N,V_layers) layers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSceneLayerManager _objc_initiateDealloc];
-[FBSceneLayerManager _observer_didStopTrackingLayers];
-[FBSceneLayerManager _removeSuspendAssertion:];
-[FBSceneLayerManager _initWithScene:];
-[FBSceneLayerManager layers];
-[FBSceneLayerManager _observer_didStartTrackingLayers];
-[FBSceneLayerManager layerWithContextID:];
-[FBSceneLayerManager _suspendUpdatesWithReason:];
-[FBSceneLayerManager identifier];
-[FBSceneLayerManager succinctDescriptionBuilder];
-[FBSceneLayerManager _rebuildLayers];
-[FBSceneLayerManager removeObserver:];
-[FBSceneLayerManager _setLayers:];
-[FBSceneLayerManager add:];
-[FBSceneLayerManager remove:];
-[FBSceneLayerManager _observer_willStartTrackingLayers];
-[FBSceneLayerManager descriptionWithMultilinePrefix:];
-[FBSceneLayerManager _observer_willStopTrackingLayers];
-[FBSceneLayerManager succinctDescription];
-[FBSceneLayerManager addObserver:];
-[FBSceneLayerManager scene];
-[FBSceneLayerManager _observer_sceneLayerManagerWillUpdateLayers];
-[FBSceneLayerManager description];
-[FBSceneLayerManager _observer_sceneLayerManagerDidUpdateLayers];
-[FBSceneLayerManager descriptionBuilderWithMultilinePrefix:];
```
