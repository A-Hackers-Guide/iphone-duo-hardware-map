# `UISMutableApplicationInitializationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISApplicationInitializationContext`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"UISDisplayContext",&,D,N) displayContext;
@property (T@"UISDisplayContext",&,D,N) mainDisplayContext;
@property (T@"UISDisplayContext",&,D,N) launchDisplayContext;
@property (T@"UISDeviceContext",&,D,N) deviceContext;
@property (T@"UISCompatibilityContext",&,D,N) compatibilityContext;
@property (T@"NSSet",&,D,N) persistedSceneIdentifiers;
@property (T@"FBSSceneIdentityToken",&,D,N) defaultSceneToken;
@property (TB,D,N) supportAppSceneRequests;
```

## Instance methods

```
-[UISMutableApplicationInitializationContext setDeviceContext:];
-[UISMutableApplicationInitializationContext setPersistedSceneIdentifiers:];
-[UISMutableApplicationInitializationContext setDefaultSceneToken:];
-[UISMutableApplicationInitializationContext setSupportAppSceneRequests:];
-[UISMutableApplicationInitializationContext setDisplayContext:];
-[UISMutableApplicationInitializationContext setLaunchDisplayContext:];
-[UISMutableApplicationInitializationContext setMainDisplayContext:];
-[UISMutableApplicationInitializationContext copyWithZone:];
-[UISMutableApplicationInitializationContext setCompatibilityContext:];
```
