# `CAFVentTypesCharacteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFUInt64Characteristic`
- 0 instance variables, 6 properties, 13 instance methods, 2 class methods

## Properties

```
@property (TQ,N) ventTypesValue;
@property (TB,N) hasWindow;
@property (TB,N) hasUpper;
@property (TB,N) hasLower;
@property (TB,N) hasNeck;
@property (TB,N) hasMiddle;
```

## Class methods

```
+[CAFVentTypesCharacteristic primaryCharacteristicFormat];
+[CAFVentTypesCharacteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFVentTypesCharacteristic formattedValue];
-[CAFVentTypesCharacteristic hasWindow];
-[CAFVentTypesCharacteristic hasMiddle];
-[CAFVentTypesCharacteristic hasNeck];
-[CAFVentTypesCharacteristic hasLower];
-[CAFVentTypesCharacteristic hasUpper];
-[CAFVentTypesCharacteristic setHasLower:];
-[CAFVentTypesCharacteristic setHasMiddle:];
-[CAFVentTypesCharacteristic setHasNeck:];
-[CAFVentTypesCharacteristic setHasUpper:];
-[CAFVentTypesCharacteristic setHasWindow:];
-[CAFVentTypesCharacteristic setVentTypesValue:];
-[CAFVentTypesCharacteristic ventTypesValue];
```
