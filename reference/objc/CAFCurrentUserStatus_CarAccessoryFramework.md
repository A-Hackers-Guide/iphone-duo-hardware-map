# `CAFCurrentUserStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 15 properties, 27 instance methods, 2 class methods

## Properties

```
@property (T@"CAFDataCharacteristic",R,N) imageCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"NSData",R,N) image;
@property (TB,R,N) hasImage;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Class methods

```
+[CAFCurrentUserStatus serviceIdentifier];
+[CAFCurrentUserStatus observerProtocol];
```

## Instance methods

```
-[CAFCurrentUserStatus removeObserver:];
-[CAFCurrentUserStatus hasImage];
-[CAFCurrentUserStatus addObserver:];
-[CAFCurrentUserStatus registerObserver:];
-[CAFCurrentUserStatus image];
-[CAFCurrentUserStatus name];
-[CAFCurrentUserStatus unregisterObserver:];
-[CAFCurrentUserStatus hidden];
-[CAFCurrentUserStatus buttonAction];
-[CAFCurrentUserStatus setButtonAction:];
-[CAFCurrentUserStatus hasButtonAction];
-[CAFCurrentUserStatus hasHidden];
-[CAFCurrentUserStatus contentURLAction];
-[CAFCurrentUserStatus registeredForButtonAction];
-[CAFCurrentUserStatus registeredForContentURLAction];
-[CAFCurrentUserStatus registeredForHidden];
-[CAFCurrentUserStatus registeredForImage];
-[CAFCurrentUserStatus registeredForUserVisibleLabel];
-[CAFCurrentUserStatus userVisibleLabel];
-[CAFCurrentUserStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCurrentUserStatus buttonActionCharacteristic];
-[CAFCurrentUserStatus contentURLActionCharacteristic];
-[CAFCurrentUserStatus hasContentURLAction];
-[CAFCurrentUserStatus hasUserVisibleLabel];
-[CAFCurrentUserStatus hiddenCharacteristic];
-[CAFCurrentUserStatus imageCharacteristic];
-[CAFCurrentUserStatus userVisibleLabelCharacteristic];
```
