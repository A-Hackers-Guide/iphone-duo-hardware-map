# `CAFDeepLinkStatusItem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerStatusItem`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"NSString",R,N) contentURLAction;
```

## Class methods

```
+[CAFDeepLinkStatusItem serviceIdentifier];
+[CAFDeepLinkStatusItem observerProtocol];
```

## Instance methods

```
-[CAFDeepLinkStatusItem removeObserver:];
-[CAFDeepLinkStatusItem addObserver:];
-[CAFDeepLinkStatusItem registerObserver:];
-[CAFDeepLinkStatusItem name];
-[CAFDeepLinkStatusItem unregisterObserver:];
-[CAFDeepLinkStatusItem contentURLAction];
-[CAFDeepLinkStatusItem registeredForContentURLAction];
-[CAFDeepLinkStatusItem _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDeepLinkStatusItem contentURLActionCharacteristic];
```
