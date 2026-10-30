# `_UISceneRenderingEnvironmentHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneObserver`, `_UISceneRenderingEnvironmentHost`
- 1 instance variables, 12 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N) isCapturingContentForAdditionalRenderingDestination;
@property (T@"NSString",C,N) systemDisplayIdentifier;
@property (Td,N) screenBrightness;
@property (Td,R,N) preferredScreenBrightness;
@property (TB,R,N) prefersContentProtection;
@property (Tq,N) activeAppearance;
@property (T@"_UIUserInterfaceSizeClassResolver",&,N) horizontalSizeClassResolver;
@property (T@"_UIUserInterfaceSizeClassResolver",&,N) verticalSizeClassResolver;
```

## Instance methods

```
-[_UISceneRenderingEnvironmentHostComponent screenBrightness];
-[_UISceneRenderingEnvironmentHostComponent setScreenBrightness:];
-[_UISceneRenderingEnvironmentHostComponent removeObserver:];
-[_UISceneRenderingEnvironmentHostComponent horizontalSizeClassResolver];
-[_UISceneRenderingEnvironmentHostComponent setScene:];
-[_UISceneRenderingEnvironmentHostComponent activeAppearance];
-[_UISceneRenderingEnvironmentHostComponent setHorizontalSizeClassResolver:];
-[_UISceneRenderingEnvironmentHostComponent setIsCapturingContentForAdditionalRenderingDestination:];
-[_UISceneRenderingEnvironmentHostComponent systemDisplayIdentifier];
-[_UISceneRenderingEnvironmentHostComponent addObserver:];
-[_UISceneRenderingEnvironmentHostComponent preferredScreenBrightness];
-[_UISceneRenderingEnvironmentHostComponent prefersContentProtection];
-[_UISceneRenderingEnvironmentHostComponent setSystemDisplayIdentifier:];
-[_UISceneRenderingEnvironmentHostComponent setVerticalSizeClassResolver:];
-[_UISceneRenderingEnvironmentHostComponent verticalSizeClassResolver];
-[_UISceneRenderingEnvironmentHostComponent setActiveAppearance:];
-[_UISceneRenderingEnvironmentHostComponent isCapturingContentForAdditionalRenderingDestination];
-[_UISceneRenderingEnvironmentHostComponent scene:didUpdateClientSettings:];
```
