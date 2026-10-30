# `_UISceneRenderingEnvironmentClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UIWindowSceneTraitSource`, `FBSSceneObserver`, `_UISceneRenderingEnvironmentClientInternal`
- 4 instance variables, 12 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _didRealizeUISceneNotificationToken;
B _isInvalidating;
@"_UIWindowSceneTraitProvider" _traitProvider;
@"UIScene<_UISceneUIWindowHosting>" _windowHostingScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,W,N,V_windowHostingScene) _windowHostingScene;
@property (Td,R,N) screenBrightness;
@property (TB,R,N) isCapturingContentForAdditionalRenderingDestination;
@property (T@"NSString",R,C,N) systemDisplayIdentifier;
@property (Td,N) preferredScreenBrightness;
@property (TB,N) prefersContentProtection;
@property (T@"_UIUserInterfaceSizeClassResolver",R,N) horizontalSizeClassResolver;
@property (T@"_UIUserInterfaceSizeClassResolver",R,N) verticalSizeClassResolver;
```

## Instance methods

```
-[_UISceneRenderingEnvironmentClientComponent screenBrightness];
-[_UISceneRenderingEnvironmentClientComponent _windowHostingScene];
-[_UISceneRenderingEnvironmentClientComponent scene:didUpdateSettings:];
-[_UISceneRenderingEnvironmentClientComponent horizontalSizeClassResolver];
-[_UISceneRenderingEnvironmentClientComponent traitOverridesForTraitProvider:];
-[_UISceneRenderingEnvironmentClientComponent setScene:];
-[_UISceneRenderingEnvironmentClientComponent _fbsSceneDidRealizeUIScene:];
-[_UISceneRenderingEnvironmentClientComponent systemDisplayIdentifier];
-[_UISceneRenderingEnvironmentClientComponent preferredScreenBrightness];
-[_UISceneRenderingEnvironmentClientComponent prefersContentProtection];
-[_UISceneRenderingEnvironmentClientComponent verticalSizeClassResolver];
-[_UISceneRenderingEnvironmentClientComponent sceneWillInvalidate:];
-[_UISceneRenderingEnvironmentClientComponent setPreferredScreenBrightness:];
-[_UISceneRenderingEnvironmentClientComponent isCapturingContentForAdditionalRenderingDestination];
-[_UISceneRenderingEnvironmentClientComponent setPrefersContentProtection:];
```
