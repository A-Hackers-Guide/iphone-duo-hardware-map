# `_UISceneBarPositionClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneObserver`, `_UISceneBarPositionClient`
- 3 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"UIWindowScene" _windowScene;
@"_UIWindowSceneTraitOverrideHandle" __traitHandle;
```

## Properties

```
@property (TB,R,N) _systemProvidesVerticalBars;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UISceneBarPositionResolver",R,N) barPositionResolver;
@property (T@"_UISceneBarAlignmentsResolver",R,N) barAlignmentResolver;
@property (T@"_UISceneBarSizeClassResolver",R,N) barSizeClassResolver;
```

## Instance methods

```
-[_UISceneBarPositionClientComponent removeObserver:];
-[_UISceneBarPositionClientComponent scene:didUpdateSettings:];
-[_UISceneBarPositionClientComponent barSizeClassForEdge:orientation:];
-[_UISceneBarPositionClientComponent setScene:];
-[_UISceneBarPositionClientComponent barSizeClassResolver];
-[_UISceneBarPositionClientComponent preferredBarPositionForOrientation:];
-[_UISceneBarPositionClientComponent _systemProvidesVerticalBars];
-[_UISceneBarPositionClientComponent addObserver:];
-[_UISceneBarPositionClientComponent barAlignmentsForOrientation:];
-[_UISceneBarPositionClientComponent barPositionResolver];
-[_UISceneBarPositionClientComponent barAlignmentResolver];
-[_UISceneBarPositionClientComponent _windowSceneDidUpdateEffectiveGeometry:];
```
