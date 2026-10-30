# `_UIApplicationConfigurationLoader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"UISApplicationInitializationContext" _applicationInitializationContext;
AB _hasRequestedPreload;
```

## Properties

```
@property (T@"UISApplicationInitializationContext",R,N) applicationInitializationContext;
@property (TB,R,N) isFrontBoard;
@property (TB,R,N) usesLocalInitializationContext;
```

## Class methods

```
+[_UIApplicationConfigurationLoader sharedLoader];
```

## Instance methods

```
-[_UIApplicationConfigurationLoader dealloc];
-[_UIApplicationConfigurationLoader usesLocalInitializationContext];
-[_UIApplicationConfigurationLoader _init];
-[_UIApplicationConfigurationLoader startPreloadInitializationContext];
-[_UIApplicationConfigurationLoader _loadInitializationContext];
-[_UIApplicationConfigurationLoader isFrontBoard];
-[_UIApplicationConfigurationLoader applicationInitializationContext];
-[_UIApplicationConfigurationLoader _appInitializationContextFactoryClass];
```
