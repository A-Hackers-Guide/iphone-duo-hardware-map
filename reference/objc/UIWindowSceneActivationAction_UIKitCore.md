# `UIWindowSceneActivationAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAction`
- 3 instance variables, 3 properties, 14 instance methods, 5 class methods

## Instance variables

```
@"<_UIWindowSceneActivator>" __preferredActivator;
@? __configurationProvider;
@"UIAction" __alternateAction;
```

## Properties

```
@property (T@?,C,N,S_setConfigurationProvider:,V__configurationProvider) _configurationProvider;
@property (T@"UIAction",C,N,S_setAlternateAction:,V__alternateAction) _alternateAction;
@property (T@"NSString",C,D,N) title;
```

## Class methods

```
+[UIWindowSceneActivationAction _defaultImage];
+[UIWindowSceneActivationAction _defaultTitle];
+[UIWindowSceneActivationAction actionWithHandler:];
+[UIWindowSceneActivationAction actionWithIdentifier:alternateAction:configurationProvider:];
+[UIWindowSceneActivationAction actionWithTitle:image:identifier:handler:];
```

## Instance methods

```
-[UIWindowSceneActivationAction keepsMenuPresented];
-[UIWindowSceneActivationAction initWithCoder:];
-[UIWindowSceneActivationAction setTitle:];
-[UIWindowSceneActivationAction copyWithZone:];
-[UIWindowSceneActivationAction _alternateAction];
-[UIWindowSceneActivationAction _configurationProvider];
-[UIWindowSceneActivationAction _requestSceneActivation];
-[UIWindowSceneActivationAction _resolveAppearanceToAlternateOrHidden];
-[UIWindowSceneActivationAction _setAlternateAction:];
-[UIWindowSceneActivationAction _setConfigurationProvider:];
-[UIWindowSceneActivationAction _validatedLeafWithTarget:validator:];
-[UIWindowSceneActivationAction _willBePreparedForInitialDisplay:];
-[UIWindowSceneActivationAction initWithTitle:image:identifier:discoverabilityTitle:attributes:alternateAction:configurationProvider:];
-[UIWindowSceneActivationAction initWithTitle:image:identifier:discoverabilityTitle:attributes:state:handler:];
```
