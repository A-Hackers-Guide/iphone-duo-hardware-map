# `SRElectrocardiogramSample`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 16 instance methods, 2 class methods

## Instance variables

```
d _time;
d _freq;
@"SRElectrocardiogramSession" _session;
q _lead;
@"NSArray" _data;
```

## Properties

```
@property (T@"NSDate",R,N) date;
@property (T@"NSMeasurement",R,N) frequency;
@property (T@"SRElectrocardiogramSession",R,N,V_session) session;
@property (Tq,R,N,V_lead) lead;
@property (T@"NSArray",R,C,N,V_data) data;
```

## Class methods

```
+[SRElectrocardiogramSample supportsSecureCoding];
+[SRElectrocardiogramSample new];
```

## Instance methods

```
-[SRElectrocardiogramSample frequency];
-[SRElectrocardiogramSample init];
-[SRElectrocardiogramSample data];
-[SRElectrocardiogramSample dealloc];
-[SRElectrocardiogramSample date];
-[SRElectrocardiogramSample encodeWithCoder:];
-[SRElectrocardiogramSample hash];
-[SRElectrocardiogramSample description];
-[SRElectrocardiogramSample initWithCoder:];
-[SRElectrocardiogramSample session];
-[SRElectrocardiogramSample copyWithZone:];
-[SRElectrocardiogramSample isEqual:];
-[SRElectrocardiogramSample initWithHAECGSample:];
-[SRElectrocardiogramSample initWithTimestamp:frequency:session:lead:data:];
-[SRElectrocardiogramSample isEqualToSample:];
-[SRElectrocardiogramSample lead];
```
