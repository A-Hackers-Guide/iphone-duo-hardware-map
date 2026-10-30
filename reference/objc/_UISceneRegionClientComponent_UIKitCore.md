# `_UISceneRegionClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `FBSSceneObserver`, `_UISceneRegionClient`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _stateCaptureToken;
@"NSMapTable" _identifiedRegions;
@"NSMapTable" _typedRegions;
@"NSMapTable" _typedRegionTokens;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,N) sceneRegions;
```

## Instance methods

```
-[_UISceneRegionClientComponent sceneRegionWithIdentifier:];
-[_UISceneRegionClientComponent debugDescription];
-[_UISceneRegionClientComponent tokenForSceneRegion:];
-[_UISceneRegionClientComponent scene:didUpdateSettings:];
-[_UISceneRegionClientComponent init];
-[_UISceneRegionClientComponent setScene:];
-[_UISceneRegionClientComponent dealloc];
-[_UISceneRegionClientComponent sceneRegionsWithType:];
-[_UISceneRegionClientComponent succinctDescription];
-[_UISceneRegionClientComponent description];
-[_UISceneRegionClientComponent appendDescriptionToStream:];
-[_UISceneRegionClientComponent sceneRegions];
```
