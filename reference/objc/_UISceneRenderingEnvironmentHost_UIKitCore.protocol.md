# `_UISceneRenderingEnvironmentHost` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 16 instance methods, 0 class methods

## Properties

```
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
-[_UISceneRenderingEnvironmentHost screenBrightness];
-[_UISceneRenderingEnvironmentHost setScreenBrightness:];
-[_UISceneRenderingEnvironmentHost removeObserver:];
-[_UISceneRenderingEnvironmentHost horizontalSizeClassResolver];
-[_UISceneRenderingEnvironmentHost activeAppearance];
-[_UISceneRenderingEnvironmentHost setHorizontalSizeClassResolver:];
-[_UISceneRenderingEnvironmentHost setIsCapturingContentForAdditionalRenderingDestination:];
-[_UISceneRenderingEnvironmentHost systemDisplayIdentifier];
-[_UISceneRenderingEnvironmentHost addObserver:];
-[_UISceneRenderingEnvironmentHost preferredScreenBrightness];
-[_UISceneRenderingEnvironmentHost prefersContentProtection];
-[_UISceneRenderingEnvironmentHost setSystemDisplayIdentifier:];
-[_UISceneRenderingEnvironmentHost setVerticalSizeClassResolver:];
-[_UISceneRenderingEnvironmentHost verticalSizeClassResolver];
-[_UISceneRenderingEnvironmentHost setActiveAppearance:];
-[_UISceneRenderingEnvironmentHost isCapturingContentForAdditionalRenderingDestination];
```
