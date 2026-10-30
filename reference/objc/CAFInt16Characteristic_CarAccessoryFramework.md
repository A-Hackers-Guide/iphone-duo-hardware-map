# `CAFInt16Characteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFCharacteristic`
- 1 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAFInt16Range" _range;
```

## Properties

```
@property (Ts,N) int16Value;
@property (T@"CAFInt16Range",R,N,V_range) range;
```

## Class methods

```
+[CAFInt16Characteristic primaryCharacteristicFormat];
+[CAFInt16Characteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFInt16Characteristic range];
-[CAFInt16Characteristic formattedValue];
-[CAFInt16Characteristic descriptionExtras];
-[CAFInt16Characteristic int16Value];
-[CAFInt16Characteristic setInt16Value:];
```
