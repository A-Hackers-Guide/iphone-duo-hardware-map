# `CAFCustomImageArchive`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 3 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFGetImageArchiveControl",R,N) getImageArchiveControl;
@property (T@"NSString",R,N) identifier;
```

## Class methods

```
+[CAFCustomImageArchive serviceIdentifier];
+[CAFCustomImageArchive observerProtocol];
```

## Instance methods

```
-[CAFCustomImageArchive identifier];
-[CAFCustomImageArchive removeObserver:];
-[CAFCustomImageArchive addObserver:];
-[CAFCustomImageArchive registerObserver:];
-[CAFCustomImageArchive name];
-[CAFCustomImageArchive unregisterObserver:];
-[CAFCustomImageArchive registeredForIdentifier];
-[CAFCustomImageArchive _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCustomImageArchive getImageArchiveControl];
-[CAFCustomImageArchive getImageArchiveWithCompletion:];
-[CAFCustomImageArchive identifierCharacteristic];
-[CAFCustomImageArchive registeredForGetImageArchive];
```
