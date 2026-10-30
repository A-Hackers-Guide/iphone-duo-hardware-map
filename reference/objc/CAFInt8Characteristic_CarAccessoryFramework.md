# `CAFInt8Characteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFCharacteristic`
- 1 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CAFInt8Range" _range;
```

## Properties

```
@property (Tc,N) int8Value;
@property (T@"CAFInt8Range",R,N,V_range) range;
```

## Class methods

```
+[CAFInt8Characteristic primaryCharacteristicFormat];
+[CAFInt8Characteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFInt8Characteristic range];
-[CAFInt8Characteristic formattedValue];
-[CAFInt8Characteristic descriptionExtras];
-[CAFInt8Characteristic int8Value];
-[CAFInt8Characteristic setInt8Value:];
```
