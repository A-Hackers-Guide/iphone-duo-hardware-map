# `CAFUInt8Characteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFCharacteristic`
- 1 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAFUInt8Range" _range;
```

## Properties

```
@property (TC,N) uint8Value;
@property (T@"CAFUInt8Range",R,N,V_range) range;
```

## Class methods

```
+[CAFUInt8Characteristic primaryCharacteristicFormat];
+[CAFUInt8Characteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFUInt8Characteristic range];
-[CAFUInt8Characteristic formattedValue];
-[CAFUInt8Characteristic descriptionExtras];
-[CAFUInt8Characteristic setUint8Value:];
-[CAFUInt8Characteristic uint8Value];
```
