# `CMSedentaryTimerData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
d fStartDate;
d fFiredDate;
q fAlarmType;
B fDidWake;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) firedDate;
@property (Tq,R,N) alarmType;
@property (TB,R,N) didWake;
```

## Class methods

```
+[CMSedentaryTimerData supportsSecureCoding];
```

## Instance methods

```
-[CMSedentaryTimerData startDate];
-[CMSedentaryTimerData firedDate];
-[CMSedentaryTimerData encodeWithCoder:];
-[CMSedentaryTimerData description];
-[CMSedentaryTimerData initWithCoder:];
-[CMSedentaryTimerData copyWithZone:];
-[CMSedentaryTimerData didWake];
-[CMSedentaryTimerData alarmType];
-[CMSedentaryTimerData initWithStartDate:firedDate:alarmType:didWake:];
```
