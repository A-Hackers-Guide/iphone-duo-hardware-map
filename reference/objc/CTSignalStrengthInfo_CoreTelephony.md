# `CTSignalStrengthInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _bars;
@"NSNumber" _displayBars;
@"NSNumber" _maxDisplayBars;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSNumber",&,N,V_bars) bars;
@property (T@"NSNumber",&,N,V_displayBars) displayBars;
@property (T@"NSNumber",&,N,V_maxDisplayBars) maxDisplayBars;
```

## Class methods

```
+[CTSignalStrengthInfo supportsSecureCoding];
```

## Instance methods

```
-[CTSignalStrengthInfo setBars:];
-[CTSignalStrengthInfo ct_shortDescription];
-[CTSignalStrengthInfo setDisplayBars:];
-[CTSignalStrengthInfo maxDisplayBars];
-[CTSignalStrengthInfo ct_shortName];
-[CTSignalStrengthInfo setMaxDisplayBars:];
-[CTSignalStrengthInfo displayBars];
-[CTSignalStrengthInfo bars];
-[CTSignalStrengthInfo encodeWithCoder:];
-[CTSignalStrengthInfo description];
-[CTSignalStrengthInfo initWithCoder:];
-[CTSignalStrengthInfo copyWithZone:];
```
