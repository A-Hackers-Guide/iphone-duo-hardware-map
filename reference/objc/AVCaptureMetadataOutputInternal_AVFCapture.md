# `AVCaptureMetadataOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 39 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDataOutputDelegateCallbackHelper" delegateCallbackHelper;
@"AVWeakReference" weakReference;
@"NSArray" metadataObjectTypes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} rectOfInterest;
B faceTrackingMetadataObjectTypesAvailable;
q faceTrackingMaxFaces;
B faceTrackingUsesFaceRecognition;
B faceTrackingPlusEnabled;
B faceTrackingSuspended;
f faceTrackingNetworkFailureThresholdMultiplier;
f faceTrackingFailureFieldOfViewModifier;
B attentionDetectionEnabled;
B faceOcclusionDetectionEnabled;
B periocularForFaceIDReadinessEnabled;
B attentionForFaceIDReadinessRequired;
@"AVCaptureFaceIDConfiguration" faceIDConfiguration;
B rawFrameDeliveryEnabled;
@"NSArray" metadataObjectTypesForPerceptionThumbnailChannel;
B perceptionTestModeEnabled;
@"NSDictionary" targetFrameRateByMetadataObjectType;
@"NSArray" deviceProximityDetectionDeviceTypes;
Q lightSourceEstimationAmbientLuminance;
B videoPreviewHistogramMetadataObjectTypesAvailable;
B appClipCodeObjectTypeAvailable;
B textRegionObjectTypeAvailable;
B sceneClassificationObjectTypeAvailable;
B headObjectTypesAvailable;
B humanHandObjectTypeAvailable;
B emitsEmptyObjectDetectionMetadata;
B offlineVideoStabilizationMotionMetadataObjectTypesAvailable;
B cinematicVideoMetadataCaptureSupported;
B continuousAutoFocusTrackingSupported;
@"NSMutableDictionary" previousTwoCMTimesByDetectorType;
B synchronizationEnabledByClient;
B synchronizationEnabledBySynchronizer;
B synchronizationEnabled;
Q maxSynchronizationFrameDelay;
@"NSMutableArray" synchronizedMetadataCollectionsQueue;
@"NSObject<OS_dispatch_source>" synchronizationQueueFlushTimer;
```

## Instance methods

```
-[AVCaptureMetadataOutputInternal init];
-[AVCaptureMetadataOutputInternal dealloc];
```
