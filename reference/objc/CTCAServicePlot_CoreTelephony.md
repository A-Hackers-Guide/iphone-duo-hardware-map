# `CTCAServicePlot`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _startsAt;
@"NSDate" _endsAt;
@"NSArray" _readings;
```

## Properties

```
@property (T@"NSDate",&,N,V_startsAt) startsAt;
@property (T@"NSDate",&,N,V_endsAt) endsAt;
@property (T@"NSArray",&,N,V_readings) readings;
```

## Class methods

```
+[CTCAServicePlot supportsSecureCoding];
```

## Instance methods

```
-[CTCAServicePlot encodeWithCoder:];
-[CTCAServicePlot description];
-[CTCAServicePlot initWithCoder:];
-[CTCAServicePlot copyWithZone:];
-[CTCAServicePlot endsAt];
-[CTCAServicePlot readings];
-[CTCAServicePlot setEndsAt:];
-[CTCAServicePlot setReadings:];
-[CTCAServicePlot setStartsAt:];
-[CTCAServicePlot startsAt];
```
