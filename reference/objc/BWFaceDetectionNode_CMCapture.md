# `BWFaceDetectionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFanOutNode`
- 35 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _metadataObjectOutput;
@"NSArray" _boxedMetadataOutputs;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rectOfInterest;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _configurationLock;
B _metadataObjectOutputEnabled;
B _boxedMetadataOutputEnabled;
B _emitsEmptyObjectDetectionMetadata;
@"NSSet" _enabledDetectedObjectTypes;
i _lastObjectFaceCount;
i _lastDetectedObjectsCount;
[5I] _localIDsForFaces_BE;
[3I] _localIDsForDetectedHumanBodies_BE;
[3I] _localIDsForDetectedCatHeads_BE;
[3I] _localIDsForDetectedCatBodies_BE;
[3I] _localIDsForDetectedDogHeads_BE;
[3I] _localIDsForDetectedDogBodies_BE;
[3I] _localIDsForDetectedSalientObjects_BE;
@"NSDictionary" _detectionTimingInfoByBoxedOutput;
I _localIDOfDetectedFace_BE;
I _localIDOfDetectedFaceFaceID_BE;
I _localIDOfDetectedFaceBounds_BE;
I _localIDOfDetectedFaceRoll_BE;
I _localIDOfDetectedFaceYaw_BE;
^{OpaqueCMBlockBuffer=} _emptyMetadataSampleData;
{?="value"q"timescale"i"flags"I"epoch"q} _startMarkerBufferPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _prevBoxedFacePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _prevBoxedFaceDur;
{?="value"q"timescale"i"flags"I"epoch"q} _prevBoxedNoFacePTS;
i _lastBoxedFaceCount;
I _recordCollectionAtomIdentifier_BE;
I _collectionItemsAtomIdentifier_BE;
q _previousDetectedFacesTimestamp;
q _previousDetectedObjectsTimestamp;
i _preparedRotationDegrees;
i _liveRotationDegrees;
```

## Properties

```
@property (T@"BWNodeOutput",R,V_metadataObjectOutput) metadataObjectOutput;
@property (T@"NSArray",R,V_boxedMetadataOutputs) boxedMetadataOutputs;
@property (Ti,N,V_preparedRotationDegrees) rotationDegrees;
```

## Class methods

```
+[BWFaceDetectionNode initialize];
```

## Instance methods

```
-[BWFaceDetectionNode setEmitsEmptyObjectDetectionMetadata:];
-[BWFaceDetectionNode emitsEmptyObjectDetectionMetadata];
-[BWFaceDetectionNode renderSampleBuffer:forInput:];
-[BWFaceDetectionNode rotationDegrees];
-[BWFaceDetectionNode dealloc];
-[BWFaceDetectionNode boxedMetadataOutputs];
-[BWFaceDetectionNode setRectOfInterest:];
-[BWFaceDetectionNode hasNonLiveConfigurationChanges];
-[BWFaceDetectionNode metadataObjectOutputEnabled];
-[BWFaceDetectionNode metadataObjectOutput];
-[BWFaceDetectionNode setMetadataObjectOutputEnabled:];
-[BWFaceDetectionNode updateMetadataIdentifiers:rectOfInterest:emitsEmptyObjectDetectionMetadata:];
-[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:];
-[BWFaceDetectionNode setRotationDegrees:];
-[BWFaceDetectionNode didReachEndOfDataForConfigurationID:input:];
-[BWFaceDetectionNode rectOfInterest];
-[BWFaceDetectionNode nodeSubType];
-[BWFaceDetectionNode didSelectFormat:forInput:];
-[BWFaceDetectionNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFaceDetectionNode nodeType];
```
