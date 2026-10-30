# `CTCellularUsageWorkspaceInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _subscriberTag;
@"NSNumber" _metaDataForHomeCountry;
@"NSNumber" _metaDataForRoaming;
@"NSDate" _billingCycleEndDate;
@"NSDate" _previousBillingCycleDate;
@"NSNumber" _billingCycleSupported;
@"NSNumber" _carrierSpaceSupported;
@"NSString" _workspaceName;
@"NSString" _workspacePath;
```

## Properties

```
@property (T@"NSNumber",R,N,V_subscriberTag) subscriberTag;
@property (T@"NSNumber",R,N,V_metaDataForHomeCountry) metaDataForHomeCountry;
@property (T@"NSNumber",R,N,V_metaDataForRoaming) metaDataForRoaming;
@property (T@"NSDate",R,N,V_billingCycleEndDate) billingCycleEndDate;
@property (T@"NSDate",R,N,V_previousBillingCycleDate) previousBillingCycleDate;
@property (T@"NSNumber",R,N,V_billingCycleSupported) billingCycleSupported;
@property (T@"NSNumber",R,N,V_carrierSpaceSupported) carrierSpaceSupported;
@property (T@"NSString",R,N,V_workspaceName) workspaceName;
@property (T@"NSString",R,N,V_workspacePath) workspacePath;
```

## Class methods

```
+[CTCellularUsageWorkspaceInfo supportsSecureCoding];
```

## Instance methods

```
-[CTCellularUsageWorkspaceInfo encodeWithCoder:];
-[CTCellularUsageWorkspaceInfo description];
-[CTCellularUsageWorkspaceInfo initWithCoder:];
-[CTCellularUsageWorkspaceInfo copyWithZone:];
-[CTCellularUsageWorkspaceInfo billingCycleEndDate];
-[CTCellularUsageWorkspaceInfo billingCycleSupported];
-[CTCellularUsageWorkspaceInfo carrierSpaceSupported];
-[CTCellularUsageWorkspaceInfo initWithSubscriberTag:metaDataForHomeCountry:metaDataForRoaming:billingCycleEndDate:previousBillingCycleDate:billingCycleSupported:carrierSpaceSupported:workspaceName:workspacePath:];
-[CTCellularUsageWorkspaceInfo metaDataForHomeCountry];
-[CTCellularUsageWorkspaceInfo metaDataForRoaming];
-[CTCellularUsageWorkspaceInfo previousBillingCycleDate];
-[CTCellularUsageWorkspaceInfo subscriberTag];
-[CTCellularUsageWorkspaceInfo workspaceName];
-[CTCellularUsageWorkspaceInfo workspacePath];
```
