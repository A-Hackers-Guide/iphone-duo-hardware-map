# `TUCallStartRecordingRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUCallRecordingRequest`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isInitiatedLocally;
q _mode;
```

## Properties

```
@property (Tq,N,V_mode) mode;
@property (TB,N,V_isInitiatedLocally) isInitiatedLocally;
```

## Class methods

```
+[TUCallStartRecordingRequest supportsSecureCoding];
```

## Instance methods

```
-[TUCallStartRecordingRequest setMode:];
-[TUCallStartRecordingRequest encodeWithCoder:];
-[TUCallStartRecordingRequest mode];
-[TUCallStartRecordingRequest description];
-[TUCallStartRecordingRequest initWithCoder:];
-[TUCallStartRecordingRequest copyWithZone:];
-[TUCallStartRecordingRequest initWithCall:];
-[TUCallStartRecordingRequest initWithCall:mode:isInitiatedLocally:];
-[TUCallStartRecordingRequest isInitiatedLocally];
-[TUCallStartRecordingRequest setIsInitiatedLocally:];
```
