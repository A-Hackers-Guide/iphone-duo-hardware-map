# `CAFCabin`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 23 properties, 37 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) maxACOnCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) maxDefrostOnCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hvacOnCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) compressorOnCharacteristic;
@property (TB,N) maxACOn;
@property (TB,R,N) hasMaxACOn;
@property (TB,R,N) maxACOnDisabled;
@property (TB,R,N) maxACOnInvalid;
@property (TB,R,N) maxACOnRestricted;
@property (TB,N) maxDefrostOn;
@property (TB,R,N) hasMaxDefrostOn;
@property (TB,R,N) maxDefrostOnDisabled;
@property (TB,R,N) maxDefrostOnInvalid;
@property (TB,R,N) maxDefrostOnRestricted;
@property (TB,N) hvacOn;
@property (TB,R,N) hasHvacOn;
@property (TB,R,N) hvacOnDisabled;
@property (TB,R,N) hvacOnInvalid;
@property (TB,N) compressorOn;
@property (TB,R,N) hasCompressorOn;
@property (TB,R,N) compressorOnDisabled;
@property (TB,R,N) compressorOnInvalid;
@property (TB,R,N) compressorOnRestricted;
```

## Class methods

```
+[CAFCabin serviceIdentifier];
+[CAFCabin observerProtocol];
```

## Instance methods

```
-[CAFCabin removeObserver:];
-[CAFCabin addObserver:];
-[CAFCabin registerObserver:];
-[CAFCabin name];
-[CAFCabin unregisterObserver:];
-[CAFCabin hasCompressorOn];
-[CAFCabin maxACOn];
-[CAFCabin hasMaxDefrostOn];
-[CAFCabin compressorOn];
-[CAFCabin hasHvacOn];
-[CAFCabin hasMaxACOn];
-[CAFCabin hvacOn];
-[CAFCabin hvacOnInvalid];
-[CAFCabin maxDefrostOn];
-[CAFCabin registeredForACCompressorOn];
-[CAFCabin registeredForHVACOn];
-[CAFCabin registeredForMaxACOn];
-[CAFCabin registeredForMaxDefrostOn];
-[CAFCabin setCompressorOn:];
-[CAFCabin setHvacOn:];
-[CAFCabin setMaxACOn:];
-[CAFCabin setMaxDefrostOn:];
-[CAFCabin maxACOnDisabled];
-[CAFCabin _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCabin compressorOnCharacteristic];
-[CAFCabin compressorOnDisabled];
-[CAFCabin compressorOnInvalid];
-[CAFCabin compressorOnRestricted];
-[CAFCabin hvacOnCharacteristic];
-[CAFCabin hvacOnDisabled];
-[CAFCabin maxACOnCharacteristic];
-[CAFCabin maxACOnInvalid];
-[CAFCabin maxACOnRestricted];
-[CAFCabin maxDefrostOnCharacteristic];
-[CAFCabin maxDefrostOnDisabled];
-[CAFCabin maxDefrostOnInvalid];
-[CAFCabin maxDefrostOnRestricted];
```
