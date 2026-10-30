# `CAFUInt64Characteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFCharacteristic`
- 1 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAFUInt64Range" _range;
```

## Properties

```
@property (TQ,N) uint64Value;
@property (T@"CAFUInt64Range",R,N,V_range) range;
```

## Class methods

```
+[CAFUInt64Characteristic primaryCharacteristicFormat];
+[CAFUInt64Characteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFUInt64Characteristic range];
-[CAFUInt64Characteristic formattedValue];
-[CAFUInt64Characteristic setUint64Value:];
-[CAFUInt64Characteristic uint64Value];
-[CAFUInt64Characteristic descriptionExtras];
```
