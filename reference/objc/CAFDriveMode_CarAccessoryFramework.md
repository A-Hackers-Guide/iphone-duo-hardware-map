# `CAFDriveMode`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFModeItems`
- 0 instance variables, 6 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) userVisibleLabelsCharacteristic;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
@property (T@"NSArray",R,N) userVisibleLabels;
@property (TB,R,N) hasUserVisibleLabels;
```

## Class methods

```
+[CAFDriveMode serviceIdentifier];
+[CAFDriveMode observerProtocol];
```

## Instance methods

```
-[CAFDriveMode removeObserver:];
-[CAFDriveMode addObserver:];
-[CAFDriveMode registerObserver:];
-[CAFDriveMode name];
-[CAFDriveMode unregisterObserver:];
-[CAFDriveMode hidden];
-[CAFDriveMode hasHidden];
-[CAFDriveMode registeredForHidden];
-[CAFDriveMode registeredForUserVisibleLabels];
-[CAFDriveMode userVisibleLabels];
-[CAFDriveMode userVisibleLabelsCharacteristic];
-[CAFDriveMode _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDriveMode hasUserVisibleLabels];
-[CAFDriveMode hiddenCharacteristic];
```
