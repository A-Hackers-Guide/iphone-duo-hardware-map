# `SRAuthorizationClient`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSensorKitServiceClientAuthorizationListening`
- 9 instance variables, 4 properties, 20 instance methods, 4 class methods

## Instance variables

```
i _registrationToken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _initialAuthLock;
@"NSXPCConnection" _connection;
@"NSMapTable" _listeners;
@"NSMutableDictionary" _actualAuthorizedServices;
@"NSMutableDictionary" _deniedServices;
@"NSMutableDictionary" _lastModifiedTimes;
@"NSNumber" _prerequisites;
@"NSMutableSet" _initialAuthCompleteByBundleId;
```

## Properties

```
@property (T@"NSArray",R,N) legacyResearchStudyBundleIDs;
@property (T@"NSString",R,N) legacyResearchStudyEntitlement;
@property (TB,N) dataCollectionEnabled;
@property (TB,N) firstRunOnboardingCompleted;
```

## Class methods

```
+[SRAuthorizationClient sharedInstance];
+[SRAuthorizationClient initialize];
+[SRAuthorizationClient authClient];
+[SRAuthorizationClient setAuthClient:];
```

## Instance methods

```
-[SRAuthorizationClient addListener:];
-[SRAuthorizationClient removeListener:];
-[SRAuthorizationClient init];
-[SRAuthorizationClient dealloc];
-[SRAuthorizationClient initWithConnection:];
-[SRAuthorizationClient dataCollectionEnabled];
-[SRAuthorizationClient invalidate];
-[SRAuthorizationClient setDataCollectionEnabled:];
-[SRAuthorizationClient setFirstRunOnboardingCompleted:];
-[SRAuthorizationClient addListener:forBundleId:];
-[SRAuthorizationClient authorizedServicesDidChange:deniedServices:prerequisites:lastModifiedTimes:bundleIdentifier:];
-[SRAuthorizationClient authorizedServicesForBundleId:];
-[SRAuthorizationClient completeEnrollmentForBundleId:sensors:];
-[SRAuthorizationClient firstRunOnboardingCompleted];
-[SRAuthorizationClient initialAuthorizationNeededForBundleId:];
-[SRAuthorizationClient initialAuthorizationStateForBundleId:authorizationState:];
-[SRAuthorizationClient legacyResearchStudyBundleIDs];
-[SRAuthorizationClient legacyResearchStudyEntitlement];
-[SRAuthorizationClient reregisterAfterInterruption:effectiveBundleId:];
-[SRAuthorizationClient setInitialAuthorizationCompleteForBundleId:];
```
