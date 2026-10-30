# `BWCameraLockScreenLaunchAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _completed;
B _prewarmed;
B _ispStreamingStarted;
i _launchError;
```

## Properties

```
@property (TB,N,V_completed) completed;
@property (TB,N,V_prewarmed) prewarmed;
@property (TB,N,V_ispStreamingStarted) ispStreamingStarted;
@property (Ti,N,V_launchError) launchError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWCameraLockScreenLaunchAnalyticsPayload setCompleted:];
-[BWCameraLockScreenLaunchAnalyticsPayload completed];
-[BWCameraLockScreenLaunchAnalyticsPayload eventDictionary];
-[BWCameraLockScreenLaunchAnalyticsPayload init];
-[BWCameraLockScreenLaunchAnalyticsPayload reset];
-[BWCameraLockScreenLaunchAnalyticsPayload eventName];
-[BWCameraLockScreenLaunchAnalyticsPayload launchError];
-[BWCameraLockScreenLaunchAnalyticsPayload prewarmed];
-[BWCameraLockScreenLaunchAnalyticsPayload setLaunchError:];
-[BWCameraLockScreenLaunchAnalyticsPayload ispStreamingStarted];
-[BWCameraLockScreenLaunchAnalyticsPayload setIspStreamingStarted:];
-[BWCameraLockScreenLaunchAnalyticsPayload setPrewarmed:];
```
