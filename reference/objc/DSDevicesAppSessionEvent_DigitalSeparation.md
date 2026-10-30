# `DSDevicesAppSessionEvent`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSDate" _endDate;
q _type;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
@property (Tq,R,N,V_type) type;
@property (T@"NSNumber",R,N) duration;
```

## Instance methods

```
-[DSDevicesAppSessionEvent startDate];
-[DSDevicesAppSessionEvent endDate];
-[DSDevicesAppSessionEvent duration];
-[DSDevicesAppSessionEvent type];
-[DSDevicesAppSessionEvent durationString];
-[DSDevicesAppSessionEvent initWithStartDate:endDate:type:];
```
