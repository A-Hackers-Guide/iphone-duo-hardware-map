# `SRElectrocardiogramData`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
d _val;
Q _flags;
```

## Properties

```
@property (TQ,R,N,V_flags) flags;
@property (T@"NSMeasurement",R,N) value;
```

## Class methods

```
+[SRElectrocardiogramData supportsSecureCoding];
+[SRElectrocardiogramData new];
```

## Instance methods

```
-[SRElectrocardiogramData flags];
-[SRElectrocardiogramData init];
-[SRElectrocardiogramData value];
-[SRElectrocardiogramData encodeWithCoder:];
-[SRElectrocardiogramData hash];
-[SRElectrocardiogramData description];
-[SRElectrocardiogramData initWithCoder:];
-[SRElectrocardiogramData copyWithZone:];
-[SRElectrocardiogramData isEqual:];
-[SRElectrocardiogramData initWithFlags:value:];
-[SRElectrocardiogramData isEqualToECGData:];
```
