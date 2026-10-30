# `BIAccessoryEstimateInfo`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _nsuuid;
@"NSString" _deviceName;
@"BIBatteryAnalysisOutput" _estimate;
```

## Properties

```
@property (T@"NSString",&,N,V_nsuuid) nsuuid;
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (T@"BIBatteryAnalysisOutput",&,N,V_estimate) estimate;
```

## Class methods

```
+[BIAccessoryEstimateInfo supportsSecureCoding];
```

## Instance methods

```
-[BIAccessoryEstimateInfo estimate];
-[BIAccessoryEstimateInfo setDeviceName:];
-[BIAccessoryEstimateInfo encodeWithCoder:];
-[BIAccessoryEstimateInfo description];
-[BIAccessoryEstimateInfo initWithCoder:];
-[BIAccessoryEstimateInfo deviceName];
-[BIAccessoryEstimateInfo setEstimate:];
-[BIAccessoryEstimateInfo nsuuid];
-[BIAccessoryEstimateInfo setNsuuid:];
```
