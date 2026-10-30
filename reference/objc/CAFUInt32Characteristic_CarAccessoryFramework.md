# `CAFUInt32Characteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFCharacteristic`
- 1 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAFUInt32Range" _range;
```

## Properties

```
@property (TI,N) uint32Value;
@property (T@"CAFUInt32Range",R,N,V_range) range;
```

## Class methods

```
+[CAFUInt32Characteristic primaryCharacteristicFormat];
+[CAFUInt32Characteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFUInt32Characteristic range];
-[CAFUInt32Characteristic formattedValue];
-[CAFUInt32Characteristic setUint32Value:];
-[CAFUInt32Characteristic uint32Value];
-[CAFUInt32Characteristic descriptionExtras];
```
