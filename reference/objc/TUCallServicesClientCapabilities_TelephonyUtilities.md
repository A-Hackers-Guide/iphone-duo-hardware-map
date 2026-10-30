# `TUCallServicesClientCapabilities`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _wantsCallDisconnectionOnInvalidation;
B _wantsCallStopStreamingOnInvalidation;
B _wantsFrequencyChangeNotifications;
B _wantsToScreenCalls;
B _wantsCallNotificationsDisabledWhileSuspended;
B _excludeFullNearbyCalls;
@"<TUCallServicesClientCapabilitiesActions>" _delegate;
```

## Properties

```
@property (T@"<TUCallServicesClientCapabilitiesActions>",W,N,V_delegate) delegate;
@property (TB,N,V_wantsCallDisconnectionOnInvalidation) wantsCallDisconnectionOnInvalidation;
@property (TB,N,V_wantsCallStopStreamingOnInvalidation) wantsCallStopStreamingOnInvalidation;
@property (TB,N,V_wantsFrequencyChangeNotifications) wantsFrequencyChangeNotifications;
@property (TB,N,V_wantsToScreenCalls) wantsToScreenCalls;
@property (TB,N,V_wantsCallNotificationsDisabledWhileSuspended) wantsCallNotificationsDisabledWhileSuspended;
@property (TB,N,V_excludeFullNearbyCalls) excludeFullNearbyCalls;
```

## Class methods

```
+[TUCallServicesClientCapabilities supportsSecureCoding];
```

## Instance methods

```
-[TUCallServicesClientCapabilities save];
-[TUCallServicesClientCapabilities setWantsFrequencyChangeNotifications:];
-[TUCallServicesClientCapabilities setWantsCallStopStreamingOnInvalidation:];
-[TUCallServicesClientCapabilities wantsFrequencyChangeNotifications];
-[TUCallServicesClientCapabilities wantsCallStopStreamingOnInvalidation];
-[TUCallServicesClientCapabilities setWantsCallDisconnectionOnInvalidation:];
-[TUCallServicesClientCapabilities wantsToScreenCalls];
-[TUCallServicesClientCapabilities setDelegate:];
-[TUCallServicesClientCapabilities setWantsCallNotificationsDisabledWhileSuspended:];
-[TUCallServicesClientCapabilities encodeWithCoder:];
-[TUCallServicesClientCapabilities delegate];
-[TUCallServicesClientCapabilities description];
-[TUCallServicesClientCapabilities wantsCallDisconnectionOnInvalidation];
-[TUCallServicesClientCapabilities initWithCoder:];
-[TUCallServicesClientCapabilities excludeFullNearbyCalls];
-[TUCallServicesClientCapabilities setExcludeFullNearbyCalls:];
-[TUCallServicesClientCapabilities wantsCallNotificationsDisabledWhileSuspended];
-[TUCallServicesClientCapabilities setWantsToScreenCalls:];
```
