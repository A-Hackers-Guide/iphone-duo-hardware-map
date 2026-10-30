# `AVPlayerInterstitialEventController`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlayerInterstitialEventMonitor`
- 1 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarQueue;
```

## Properties

```
@property (T@"NSArray",C,D) events;
@property (T@"NSBundle",C) localizedStringsBundle;
@property (T@"NSString",C) localizedStringsTableName;
```

## Class methods

```
+[AVPlayerInterstitialEventController interstitialEventControllerWithPrimaryPlayer:];
```

## Instance methods

```
-[AVPlayerInterstitialEventController setEvents:];
-[AVPlayerInterstitialEventController dealloc];
-[AVPlayerInterstitialEventController _resetPlaybackCoordinatorTimelineExpectations];
-[AVPlayerInterstitialEventController cancelCurrentEventWithReason:];
-[AVPlayerInterstitialEventController cancelCurrentEventWithResumptionOffset:];
-[AVPlayerInterstitialEventController initWithPrimaryPlayer:];
-[AVPlayerInterstitialEventController localizedStringsBundle];
-[AVPlayerInterstitialEventController localizedStringsTableName];
-[AVPlayerInterstitialEventController setCurrentRemoteEventSkippableState:];
-[AVPlayerInterstitialEventController setCurrentRemoteEventSkippableState:withLabel:];
-[AVPlayerInterstitialEventController setLocalizedStringsBundle:];
-[AVPlayerInterstitialEventController setLocalizedStringsTableName:];
-[AVPlayerInterstitialEventController skipCurrentEvent];
```
