# `CWFWiFiNetworkSharingNetworkMetadata`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _waitingForAssociation;
@"NSDate" _firstSharedDate;
@"NSDate" _mostRecentlySharedDate;
q _askToShareStatus;
@"NSDate" _askToShareStatusUpdatedTimestamp;
@"NSDate" _lastModifiedDate;
```

## Properties

```
@property (TB,V_waitingForAssociation) waitingForAssociation;
@property (T@"NSDate",C,V_firstSharedDate) firstSharedDate;
@property (T@"NSDate",C,V_mostRecentlySharedDate) mostRecentlySharedDate;
@property (Tq,V_askToShareStatus) askToShareStatus;
@property (T@"NSDate",C,V_askToShareStatusUpdatedTimestamp) askToShareStatusUpdatedTimestamp;
@property (T@"NSDate",C,V_lastModifiedDate) lastModifiedDate;
```

## Class methods

```
+[CWFWiFiNetworkSharingNetworkMetadata supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingNetworkMetadata lastModifiedDate];
-[CWFWiFiNetworkSharingNetworkMetadata setLastModifiedDate:];
-[CWFWiFiNetworkSharingNetworkMetadata encodeWithCoder:];
-[CWFWiFiNetworkSharingNetworkMetadata hash];
-[CWFWiFiNetworkSharingNetworkMetadata description];
-[CWFWiFiNetworkSharingNetworkMetadata initWithCoder:];
-[CWFWiFiNetworkSharingNetworkMetadata copyWithZone:];
-[CWFWiFiNetworkSharingNetworkMetadata isEqual:];
-[CWFWiFiNetworkSharingNetworkMetadata firstSharedDate];
-[CWFWiFiNetworkSharingNetworkMetadata askToShareStatus];
-[CWFWiFiNetworkSharingNetworkMetadata askToShareStatusUpdatedTimestamp];
-[CWFWiFiNetworkSharingNetworkMetadata isEqualToWiFiNetworkSharingNetworkMetadata:];
-[CWFWiFiNetworkSharingNetworkMetadata mostRecentlySharedDate];
-[CWFWiFiNetworkSharingNetworkMetadata setAskToShareStatus:];
-[CWFWiFiNetworkSharingNetworkMetadata setAskToShareStatusUpdatedTimestamp:];
-[CWFWiFiNetworkSharingNetworkMetadata setFirstSharedDate:];
-[CWFWiFiNetworkSharingNetworkMetadata setMostRecentlySharedDate:];
-[CWFWiFiNetworkSharingNetworkMetadata setWaitingForAssociation:];
-[CWFWiFiNetworkSharingNetworkMetadata waitingForAssociation];
```
