# `CTCellularHealthStatusReport`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
q _diagStatus;
q _anomalyState;
@"NSString" _carrierName;
@"NSString" _learnMoreLink;
@"NSString" _resolutionETA;
q _status;
q _diagCode;
```

## Properties

```
@property (Tq,N,V_diagStatus) diagStatus;
@property (Tq,N,V_anomalyState) anomalyState;
@property (T@"NSString",C,N,V_carrierName) carrierName;
@property (T@"NSString",C,N,V_learnMoreLink) learnMoreLink;
@property (T@"NSString",C,N,V_resolutionETA) resolutionETA;
@property (Tq,N,V_status) status;
@property (Tq,N,V_diagCode) diagCode;
```

## Class methods

```
+[CTCellularHealthStatusReport supportsSecureCoding];
```

## Instance methods

```
-[CTCellularHealthStatusReport carrierName];
-[CTCellularHealthStatusReport setCarrierName:];
-[CTCellularHealthStatusReport status];
-[CTCellularHealthStatusReport encodeWithCoder:];
-[CTCellularHealthStatusReport description];
-[CTCellularHealthStatusReport initWithCoder:];
-[CTCellularHealthStatusReport setStatus:];
-[CTCellularHealthStatusReport copyWithZone:];
-[CTCellularHealthStatusReport anomalyState];
-[CTCellularHealthStatusReport diagCode];
-[CTCellularHealthStatusReport diagStatus];
-[CTCellularHealthStatusReport learnMoreLink];
-[CTCellularHealthStatusReport resolutionETA];
-[CTCellularHealthStatusReport setAnomalyState:];
-[CTCellularHealthStatusReport setDiagCode:];
-[CTCellularHealthStatusReport setDiagStatus:];
-[CTCellularHealthStatusReport setLearnMoreLink:];
-[CTCellularHealthStatusReport setResolutionETA:];
```
