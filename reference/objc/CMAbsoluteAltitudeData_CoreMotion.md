# `CMAbsoluteAltitudeData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 8 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
d _altitudePrivate;
d _altitude;
d _accuracy;
d _precision;
d _absoluteAltitudeAccuracy;
d _absoluteAltitudePrecision;
d _filteredPressure;
q _absoluteAltitudeStatusInfo;
```

## Properties

```
@property (T@"NSNumber",R,N) absoluteAltitude;
@property (Td,R,N,V_absoluteAltitudeAccuracy) absoluteAltitudeAccuracy;
@property (Td,R,N,V_absoluteAltitudePrecision) absoluteAltitudePrecision;
@property (Td,R,N,V_filteredPressure) filteredPressure;
@property (Tq,R,N,V_absoluteAltitudeStatusInfo) absoluteAltitudeStatusInfo;
@property (Td,R,N,V_altitude) altitude;
@property (Td,R,N,V_accuracy) accuracy;
@property (Td,R,N,V_precision) precision;
```

## Class methods

```
+[CMAbsoluteAltitudeData supportsSecureCoding];
```

## Instance methods

```
-[CMAbsoluteAltitudeData precision];
-[CMAbsoluteAltitudeData altitude];
-[CMAbsoluteAltitudeData dealloc];
-[CMAbsoluteAltitudeData absoluteAltitude];
-[CMAbsoluteAltitudeData initWithAltitude:accuracy:precision:filteredPressure:status:timestamp:];
-[CMAbsoluteAltitudeData absoluteAltitudeStatusInfo];
-[CMAbsoluteAltitudeData accuracy];
-[CMAbsoluteAltitudeData encodeWithCoder:];
-[CMAbsoluteAltitudeData description];
-[CMAbsoluteAltitudeData initWithCoder:];
-[CMAbsoluteAltitudeData setAltitudeData:accuracy:precision:filteredPressure:status:];
-[CMAbsoluteAltitudeData absoluteAltitudePrecision];
-[CMAbsoluteAltitudeData copyWithZone:];
-[CMAbsoluteAltitudeData absoluteAltitudeAccuracy];
-[CMAbsoluteAltitudeData filteredPressure];
```
