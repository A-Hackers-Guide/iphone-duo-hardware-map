# `CMDeviceImpact`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _simulated;
q _impactType;
@"NSDate" _date;
d _peakAcceleration;
```

## Properties

```
@property (Tq,R,N,V_impactType) impactType;
@property (T@"NSDate",R,N,V_date) date;
@property (Td,R,N,V_peakAcceleration) peakAcceleration;
@property (TB,R,N,GisSimulated,V_simulated) simulated;
```

## Class methods

```
+[CMDeviceImpact supportsSecureCoding];
```

## Instance methods

```
-[CMDeviceImpact compare:];
-[CMDeviceImpact date];
-[CMDeviceImpact isSimulated];
-[CMDeviceImpact encodeWithCoder:];
-[CMDeviceImpact description];
-[CMDeviceImpact initWithCoder:];
-[CMDeviceImpact impactType];
-[CMDeviceImpact initWithImpactType:peakAcceleration:simulated:date:timestamp:];
-[CMDeviceImpact peakAcceleration];
```
