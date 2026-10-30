# `CTSweetgumUsageAccountMetrics`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _localDevice;
@"NSString" _networkUsageLabel;
q _deviceType;
@"NSString" _subscriptionStatus;
@"NSString" _planType;
@"NSDate" _billingCycleEndDate;
@"NSArray" _applicablePlans;
```

## Properties

```
@property (T@"NSString",&,N,V_networkUsageLabel) networkUsageLabel;
@property (Tq,N,V_deviceType) deviceType;
@property (TB,N,V_localDevice) localDevice;
@property (T@"NSString",&,N,V_subscriptionStatus) subscriptionStatus;
@property (T@"NSString",&,N,V_planType) planType;
@property (T@"NSDate",&,N,V_billingCycleEndDate) billingCycleEndDate;
@property (T@"NSArray",&,N,V_applicablePlans) applicablePlans;
```

## Class methods

```
+[CTSweetgumUsageAccountMetrics supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumUsageAccountMetrics setDeviceType:];
-[CTSweetgumUsageAccountMetrics init];
-[CTSweetgumUsageAccountMetrics deviceType];
-[CTSweetgumUsageAccountMetrics subscriptionStatus];
-[CTSweetgumUsageAccountMetrics localDevice];
-[CTSweetgumUsageAccountMetrics encodeWithCoder:];
-[CTSweetgumUsageAccountMetrics description];
-[CTSweetgumUsageAccountMetrics initWithCoder:];
-[CTSweetgumUsageAccountMetrics setSubscriptionStatus:];
-[CTSweetgumUsageAccountMetrics isEqual:];
-[CTSweetgumUsageAccountMetrics setLocalDevice:];
-[CTSweetgumUsageAccountMetrics applicablePlans];
-[CTSweetgumUsageAccountMetrics billingCycleEndDate];
-[CTSweetgumUsageAccountMetrics networkUsageLabel];
-[CTSweetgumUsageAccountMetrics planType];
-[CTSweetgumUsageAccountMetrics setApplicablePlans:];
-[CTSweetgumUsageAccountMetrics setBillingCycleEndDate:];
-[CTSweetgumUsageAccountMetrics setNetworkUsageLabel:];
-[CTSweetgumUsageAccountMetrics setPlanType:];
```
