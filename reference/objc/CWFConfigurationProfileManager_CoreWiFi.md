# `CWFConfigurationProfileManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCProfileConnectionObserver`
- 4 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"MCProfileConnection" _mcProfileConnection;
@"NSMutableSet" _mdmManagedProfileUUIDs;
B _checkInComplete;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _checkInCompleteLock;
```

## Properties

```
@property (TB,D) checkInComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CWFConfigurationProfileManager isNetworkManagedByMDM:];
-[CWFConfigurationProfileManager isDeviceSupervised];
-[CWFConfigurationProfileManager activateWithCompletion:];
-[CWFConfigurationProfileManager init];
-[CWFConfigurationProfileManager profileConnectionDidReceiveProfileListChangedNotification:userInfo:];
-[CWFConfigurationProfileManager invalidate];
-[CWFConfigurationProfileManager checkInComplete];
-[CWFConfigurationProfileManager __completeCheckInWithError:];
-[CWFConfigurationProfileManager __updateCachedMDMManagedProfileUUIDs:];
-[CWFConfigurationProfileManager setCheckInComplete:];
```
