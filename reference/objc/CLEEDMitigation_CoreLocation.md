# `CLEEDMitigation`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 26 instance methods, 3 class methods

## Instance variables

```
B _newStreamingAllowed;
B _dropStreaming;
B _newUploadAllowed;
q _streamingFPS;
q _streamingBitrate;
q _uploadMigitation;
q _source;
```

## Properties

```
@property (TB,N,V_newStreamingAllowed) newStreamingAllowed;
@property (TB,N,V_dropStreaming) dropStreaming;
@property (Tq,N,V_streamingFPS) streamingFPS;
@property (Tq,N,V_streamingBitrate) streamingBitrate;
@property (TB,N,V_newUploadAllowed) newUploadAllowed;
@property (Tq,N,V_uploadMigitation) uploadMigitation;
@property (Tq,N,V_source) source;
```

## Class methods

```
+[CLEEDMitigation supportsSecureCoding];
+[CLEEDMitigation sourceAsString:];
+[CLEEDMitigation newMitigationFromDict:];
```

## Instance methods

```
-[CLEEDMitigation init];
-[CLEEDMitigation dealloc];
-[CLEEDMitigation setSource:];
-[CLEEDMitigation encodeWithCoder:];
-[CLEEDMitigation description];
-[CLEEDMitigation initWithCoder:];
-[CLEEDMitigation source];
-[CLEEDMitigation anyChangeToNewRequestsComparedTo:];
-[CLEEDMitigation dropStreaming];
-[CLEEDMitigation initWithStreamingAllowed:framerateFps:bitrateKbps:dropStreaming:uploadAllowed:uploadMitigation:source:];
-[CLEEDMitigation needsRequestStateUpdateComparedTo:];
-[CLEEDMitigation newMitigationDict];
-[CLEEDMitigation newStreamingAllowed];
-[CLEEDMitigation newUploadAllowed];
-[CLEEDMitigation setDropStreaming:];
-[CLEEDMitigation setNewStreamingAllowed:];
-[CLEEDMitigation setNewUploadAllowed:];
-[CLEEDMitigation setStreamingBitrate:];
-[CLEEDMitigation setStreamingFPS:];
-[CLEEDMitigation setUploadMigitation:];
-[CLEEDMitigation streamingBitrate];
-[CLEEDMitigation streamingFPS];
-[CLEEDMitigation toCLEEDUploadMitigationString:];
-[CLEEDMitigation updateIfDifferentFrom:];
-[CLEEDMitigation updateWorseMitigationsFrom:];
-[CLEEDMitigation uploadMigitation];
```
