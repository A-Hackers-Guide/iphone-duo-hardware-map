# `TUCallRecordingSession`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUCallRecordingSessionBase`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
i _recordingState;
@"NSString" _destinationBundleIdentifier;
```

## Properties

```
@property (Ti,N,V_recordingState) recordingState;
@property (T@"NSString",&,N,V_destinationBundleIdentifier) destinationBundleIdentifier;
```

## Class methods

```
+[TUCallRecordingSession supportsSecureCoding];
```

## Instance methods

```
-[TUCallRecordingSession encodeWithCoder:];
-[TUCallRecordingSession description];
-[TUCallRecordingSession initWithCoder:];
-[TUCallRecordingSession copyWithZone:];
-[TUCallRecordingSession isEqual:];
-[TUCallRecordingSession setDestinationBundleIdentifier:];
-[TUCallRecordingSession destinationBundleIdentifier];
-[TUCallRecordingSession initWithUUID:state:callUUID:requestUUID:recordingStartedDate:recordingEndedDate:destinationBundleIdentifier:isRedisclosing:];
-[TUCallRecordingSession isEqualToRecordingSession:];
-[TUCallRecordingSession recordingState];
-[TUCallRecordingSession setRecordingState:];
```
