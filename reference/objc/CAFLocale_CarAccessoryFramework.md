# `CAFLocale`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) languageIdentifierCharacteristic;
@property (T@"NSString",R,N) languageIdentifier;
```

## Class methods

```
+[CAFLocale serviceIdentifier];
+[CAFLocale observerProtocol];
```

## Instance methods

```
-[CAFLocale removeObserver:];
-[CAFLocale languageIdentifier];
-[CAFLocale addObserver:];
-[CAFLocale registerObserver:];
-[CAFLocale name];
-[CAFLocale unregisterObserver:];
-[CAFLocale registeredForLanguageIdentifier];
-[CAFLocale _characteristicDidUpdate:fromGroupUpdate:];
-[CAFLocale languageIdentifierCharacteristic];
```
