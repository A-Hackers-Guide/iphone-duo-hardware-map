# `FigCaptureRecordingSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
q _settingsID;
@"NSURL" _outputURL;
@"NSString" _outputFileType;
{?="value"q"timescale"i"flags"I"epoch"q} _maxDuration;
q _maxFileSize;
q _minFreeDiskSpaceLimit;
```

## Properties

```
@property (Tq,N,V_settingsID) settingsID;
@property (T@"NSURL",C,N,V_outputURL) outputURL;
@property (T@"NSString",C,N,V_outputFileType) outputFileType;
@property (T{?=qiIq},N,V_maxDuration) maxDuration;
@property (Tq,N,V_maxFileSize) maxFileSize;
@property (Tq,N,V_minFreeDiskSpaceLimit) minFreeDiskSpaceLimit;
```

## Class methods

```
+[FigCaptureRecordingSettings supportsSecureCoding];
+[FigCaptureRecordingSettings initialize];
```

## Instance methods

```
-[FigCaptureRecordingSettings setOutputFileType:];
-[FigCaptureRecordingSettings init];
-[FigCaptureRecordingSettings maxDuration];
-[FigCaptureRecordingSettings maxFileSize];
-[FigCaptureRecordingSettings dealloc];
-[FigCaptureRecordingSettings settingsID];
-[FigCaptureRecordingSettings setOutputURL:];
-[FigCaptureRecordingSettings outputFileType];
-[FigCaptureRecordingSettings encodeWithCoder:];
-[FigCaptureRecordingSettings setSettingsID:];
-[FigCaptureRecordingSettings initWithCoder:];
-[FigCaptureRecordingSettings setMaxDuration:];
-[FigCaptureRecordingSettings copyWithZone:];
-[FigCaptureRecordingSettings outputURL];
-[FigCaptureRecordingSettings setMaxFileSize:];
-[FigCaptureRecordingSettings minFreeDiskSpaceLimit];
-[FigCaptureRecordingSettings setMinFreeDiskSpaceLimit:];
```
