# `TUPodcastRecordingSession`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUCallRecordingSessionBase`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _initiatedLocally;
i _recordingState;
```

## Properties

```
@property (Ti,N,V_recordingState) recordingState;
@property (TB,N,GisInitiatedLocally,V_initiatedLocally) initiatedLocally;
```

## Class methods

```
+[TUPodcastRecordingSession supportsSecureCoding];
```

## Instance methods

```
-[TUPodcastRecordingSession encodeWithCoder:];
-[TUPodcastRecordingSession description];
-[TUPodcastRecordingSession initWithCoder:];
-[TUPodcastRecordingSession copyWithZone:];
-[TUPodcastRecordingSession isEqual:];
-[TUPodcastRecordingSession initWithUUID:state:callUUID:requestUUID:recordingStartedDate:recordingEndedDate:isRedisclosing:isInitiatedLocally:];
-[TUPodcastRecordingSession isEqualToPodcastSession:];
-[TUPodcastRecordingSession isInitiatedLocally];
-[TUPodcastRecordingSession recordingState];
-[TUPodcastRecordingSession setInitiatedLocally:];
-[TUPodcastRecordingSession setRecordingState:];
```
