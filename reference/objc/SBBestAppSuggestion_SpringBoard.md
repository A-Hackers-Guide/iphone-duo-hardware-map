# `SBBestAppSuggestion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIconContinuityInfo`
- 0 instance variables, 14 properties, 31 instance methods, 0 class methods

## Properties

```
@property (T@"NSUUID",R,C,N) uniqueIdentifier;
@property (T@"NSString",R,C,N) bundleIdentifier;
@property (T@"NSString",R,C,N) activityType;
@property (T@"NSDate",R,C,N) lastUpdateTime;
@property (T@"NSString",R,C,N) originatingDeviceIdentifier;
@property (T@"NSString",R,C,N) originatingDeviceName;
@property (T@"NSString",R,C,N) originatingDeviceType;
@property (T@"NSString",R,C,N) originatingBundleIdentifier;
@property (T@"NSString",R,C,N) suggestedLocationName;
@property (T@"NSURL",R,C,N) launchURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBestAppSuggestion lastUpdateTime];
-[SBBestAppSuggestion activityType];
-[SBBestAppSuggestion bundleIdentifier];
-[SBBestAppSuggestion uniqueIdentifier];
-[SBBestAppSuggestion originatingDeviceName];
-[SBBestAppSuggestion description];
-[SBBestAppSuggestion launchURL];
-[SBBestAppSuggestion isHandoff];
-[SBBestAppSuggestion originatingBundleIdentifier];
-[SBBestAppSuggestion originatingDeviceType];
-[SBBestAppSuggestion originatingDeviceIdentifier];
-[SBBestAppSuggestion isPrediction];
-[SBBestAppSuggestion isBluetoothAudioPrediction];
-[SBBestAppSuggestion isBluetoothPrediction];
-[SBBestAppSuggestion isFirstWakePrediction];
-[SBBestAppSuggestion isHeadphonesPrediction];
-[SBBestAppSuggestion isLocationBasedSuggestion];
-[SBBestAppSuggestion isLocationPredictionFromSource:];
-[SBBestAppSuggestion isArrivedAtHomePrediction];
-[SBBestAppSuggestion isArrivedAtWorkPrediction];
-[SBBestAppSuggestion isCallContinuitySuggestion];
-[SBBestAppSuggestion isCarPlayPrediction];
-[SBBestAppSuggestion isEligibleForLockScreen];
-[SBBestAppSuggestion isLocallyGeneratedSuggestion];
-[SBBestAppSuggestion isLocationPredictionOfType:];
-[SBBestAppSuggestion isNotificationSuggestion];
-[SBBestAppSuggestion isOpenURLSuggestion];
-[SBBestAppSuggestion isSiriSuggestion];
-[SBBestAppSuggestion launchURLRequiresInboxCopy];
-[SBBestAppSuggestion makeInboxCopyOfLaunchURLToInboxURL:];
-[SBBestAppSuggestion suggestedLocationName];
```
