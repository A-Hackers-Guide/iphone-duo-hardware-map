# `BWNodeInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 23 instance variables, 32 properties, 60 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
B _mediaTypeIsVideo;
B _mediaTypeIsPointCloud;
B _mediaTypeIsSecureVideo;
q _requestedConfigurationID;
I _mediaType;
Q _index;
B _enabled;
B _discardsSampleDataTaggedToBeDropped;
@"BWNode" _node;
@"BWNodeConnection" _connection;
q _liveConfigurationID;
I _numberOfBuffersReceived;
I _numberOfBuffersDropped;
I _numberOfConfigurationDidBecomeLiveMessagesReceived;
I _numberOfConfigurationEndOfDataMessagesReceived;
I _numberOfEndOfDataMessagesReceived;
I _numberOfDataDroppedMessagesReceived;
@"BWNodeInputMediaConfiguration" _primaryMediaConfiguration;
@"BWNodeInputMediaConfiguration" _unspecifiedAttachedMediaConfiguration;
@"NSMutableDictionary" _attachedMediaConfigurations;
@"BWNodeInputMediaProperties" _primaryMediaProperties;
@"NSMutableDictionary" _attachedMediaProperties;
```

## Properties

```
@property (T@"BWFormatRequirements",&,N) formatRequirements;
@property (T@"BWFormat",&,N) format;
@property (T@"BWVideoFormat",R,N) videoFormat;
@property (T@"BWFormat",R,N) liveFormat;
@property (Ti,N) passthroughMode;
@property (TB,N) conversionToPassthroughModeNeverAllowed;
@property (Ti,N) retainedBufferCount;
@property (Ti,N) delayedBufferCount;
@property (Ti,N) indefinitelyHeldBufferCount;
@property (TB,R,N,V_mediaTypeIsVideo) mediaTypeIsVideo;
@property (TB,R,N,V_mediaTypeIsPointCloud) mediaTypeIsPointCloud;
@property (TB,R,N,V_mediaTypeIsSecureVideo) mediaTypeIsSecureVideo;
@property (T@"NSString",C,N,V_name) name;
@property (TI,R,N,V_mediaType) mediaType;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R,N,V_index) index;
@property (TB,N,V_discardsSampleDataTaggedToBeDropped) discardsSampleDataTaggedToBeDropped;
@property (T@"BWNode",R,W,N,V_node) node;
@property (T@"BWNodeConnection",W,N,V_connection) connection;
@property (Tq,N,V_requestedConfigurationID) requestedConfigurationID;
@property (T@"BWNodeInputMediaConfiguration",R,N,V_primaryMediaConfiguration) primaryMediaConfiguration;
@property (T@"NSArray",R,N) specifiedAttachedMediaKeys;
@property (T@"BWNodeInputMediaConfiguration",&,N,V_unspecifiedAttachedMediaConfiguration) unspecifiedAttachedMediaConfiguration;
@property (T@"BWNodeInputMediaProperties",R,N,V_primaryMediaProperties) primaryMediaProperties;
@property (T@"NSArray",R,N) resolvedAttachedMediaKeys;
@property (Tq,R,N,V_liveConfigurationID) liveConfigurationID;
@property (TI,R,N,V_numberOfBuffersReceived) numberOfBuffersReceived;
@property (TI,R,N,V_numberOfBuffersDropped) numberOfBuffersDropped;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWNodeInput initialize];
+[BWNodeInput newSampleDataToBeDroppedMarkerBufferFromSampleBuffer:];
```

## Instance methods

```
-[BWNodeInput _passthroughModeForAttachedMediaKey:];
-[BWNodeInput mediaTypeIsSecureVideo];
-[BWNodeInput resolvedAttachedMediaKeys];
-[BWNodeInput videoFormat];
-[BWNodeInput numberOfBuffersDropped];
-[BWNodeInput primaryMediaProperties];
-[BWNodeInput osStatePropertyList];
-[BWNodeInput liveConfigurationID];
-[BWNodeInput logGraphTimeoutState];
-[BWNodeInput setUnspecifiedAttachedMediaConfiguration:];
-[BWNodeInput initWithMediaType:node:index:];
-[BWNodeInput setRequestedConfigurationID:];
-[BWNodeInput setFormatRequirements:];
-[BWNodeInput unspecifiedAttachedMediaConfiguration];
-[BWNodeInput liveFormat];
-[BWNodeInput mediaTypeIsPointCloud];
-[BWNodeInput initWithMediaType:node:];
-[BWNodeInput mediaPropertiesForAttachedMediaKey:];
-[BWNodeInput specifiedAttachedMediaKeys];
-[BWNodeInput primaryMediaConfiguration];
-[BWNodeInput handleMessage:];
-[BWNodeInput mediaTypeIsVideo];
-[BWNodeInput formatRequirements];
-[BWNodeInput setConversionToPassthroughModeNeverAllowed:];
-[BWNodeInput setPassthroughMode:];
-[BWNodeInput passthroughMode];
-[BWNodeInput conversionToPassthroughModeNeverAllowed];
-[BWNodeInput willDiscardSampleBuffer:];
-[BWNodeInput _clearAllMediaProperties];
-[BWNodeInput setRetainedBufferCount:];
-[BWNodeInput discardsSampleDataTaggedToBeDropped];
-[BWNodeInput delayedBufferCount];
-[BWNodeInput dealloc];
-[BWNodeInput index];
-[BWNodeInput retainedBufferCount];
-[BWNodeInput willKeepSampleBuffer:];
-[BWNodeInput node];
-[BWNodeInput isEnabled];
-[BWNodeInput invalidate];
-[BWNodeInput mediaConfigurationForAttachedMediaKey:];
-[BWNodeInput setMediaConfiguration:forAttachedMediaKey:];
-[BWNodeInput setEnabled:];
-[BWNodeInput connection];
-[BWNodeInput setIndefinitelyHeldBufferCount:];
-[BWNodeInput _setMediaProperties:forAttachedMediaKey:];
-[BWNodeInput indefinitelyHeldBufferCount];
-[BWNodeInput numberOfBuffersReceived];
-[BWNodeInput setConnection:];
-[BWNodeInput description];
-[BWNodeInput setName:];
-[BWNodeInput mediaPropertiesByAttachedMediaKey];
-[BWNodeInput setFormat:];
-[BWNodeInput _passthroughModeForUnspecifiedAttachedMedia];
-[BWNodeInput mediaType];
-[BWNodeInput setDelayedBufferCount:];
-[BWNodeInput requestedConfigurationID];
-[BWNodeInput format];
-[BWNodeInput name];
-[BWNodeInput setDiscardsSampleDataTaggedToBeDropped:];
-[BWNodeInput willKeepSampleBufferWithoutDiscarding:];
```
