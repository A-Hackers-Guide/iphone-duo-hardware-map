# `PLDuetActivitySchedulerUsageSnapshot`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSDate" _stopDate;
d _numberOfBytesUploadedWiFi;
d _numberOfBytesDownloadedWiFi;
d _numberOfBytesUploadedCell;
d _numberOfBytesDownloadedCell;
@"NSString" _bundleID;
```

## Properties

```
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_stopDate) stopDate;
@property (Td,V_numberOfBytesUploadedWiFi) numberOfBytesUploadedWiFi;
@property (Td,V_numberOfBytesDownloadedWiFi) numberOfBytesDownloadedWiFi;
@property (Td,V_numberOfBytesUploadedCell) numberOfBytesUploadedCell;
@property (Td,V_numberOfBytesDownloadedCell) numberOfBytesDownloadedCell;
@property (T@"NSString",&,V_bundleID) bundleID;
```

## Instance methods

```
-[PLDuetActivitySchedulerUsageSnapshot startDate];
-[PLDuetActivitySchedulerUsageSnapshot setStartDate:];
-[PLDuetActivitySchedulerUsageSnapshot setBundleID:];
-[PLDuetActivitySchedulerUsageSnapshot description];
-[PLDuetActivitySchedulerUsageSnapshot bundleID];
-[PLDuetActivitySchedulerUsageSnapshot stopDate];
-[PLDuetActivitySchedulerUsageSnapshot setNumberOfBytesDownloadedCell:];
-[PLDuetActivitySchedulerUsageSnapshot setNumberOfBytesDownloadedWiFi:];
-[PLDuetActivitySchedulerUsageSnapshot numberOfBytesDownloadedCell];
-[PLDuetActivitySchedulerUsageSnapshot numberOfBytesDownloadedWiFi];
-[PLDuetActivitySchedulerUsageSnapshot numberOfBytesUploadedCell];
-[PLDuetActivitySchedulerUsageSnapshot numberOfBytesUploadedWiFi];
-[PLDuetActivitySchedulerUsageSnapshot setNumberOfBytesUploadedCell:];
-[PLDuetActivitySchedulerUsageSnapshot setNumberOfBytesUploadedWiFi:];
-[PLDuetActivitySchedulerUsageSnapshot setStopDate:];
```
