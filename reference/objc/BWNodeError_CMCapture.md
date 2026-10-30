# `BWNodeError`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 8 instance methods, 3 class methods

## Instance variables

```
q _uniqueID;
i _errorCode;
@"NSString" _sourceNodeDescription;
@"BWStillImageSettings" _stillImageSettings;
@"FigCaptureRecordingSettings" _recordingSettings;
@"NSDictionary" _metadata;
```

## Properties

```
@property (Ti,R) errorCode;
@property (T@"NSString",R) sourceNodeDescription;
@property (T@"BWStillImageSettings",R) stillImageSettings;
@property (T@"FigCaptureRecordingSettings",R,V_recordingSettings) recordingSettings;
@property (T@"NSDictionary",R,V_metadata) metadata;
```

## Class methods

```
+[BWNodeError newError:sourceNode:];
+[BWNodeError newError:sourceNode:recordingSettings:];
+[BWNodeError newError:sourceNode:stillImageSettings:metadata:];
```

## Instance methods

```
-[BWNodeError stillImageSettings];
-[BWNodeError errorCode];
-[BWNodeError dealloc];
-[BWNodeError metadata];
-[BWNodeError hash];
-[BWNodeError description];
-[BWNodeError recordingSettings];
-[BWNodeError sourceNodeDescription];
```
