# `CAMBurstImageSetInternal`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 18 properties, 55 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" dq;
@"NSObject<OS_dispatch_queue>" dq_yuvdump;
@"NSObject<OS_dispatch_semaphore>" sem;
@"NSMutableArray" clusterArray;
i temporalOrder;
i maxNumPendingFrames;
B enableAnalysis;
i dummyAnalysisCount;
B enableFaceCore;
B enableDumpYUV;
@"NSString" burstCoverSelection;
B isAction;
B isPortrait;
@"CAMBurstImageFaceAnalysisContext" faceAnalysisContext;
@"CAMBurstYUVImage" overrideImage;
@"NSDictionary" overrideProps;
@"NSMutableArray" allImageIdentifiers;
@"NSCountedSet" faceIDCounts;
@"NSMutableDictionary" statsByImageIdentifier;
@"NSMutableDictionary" clusterByImageIdentifier;
@"NSString" burstLogFileName;
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq} burstLogFileHandle;
@"CAMBurstActionClassifier" actionClassifier;
i curClusterIndexToProcess;
@"NSMutableArray" bestImageIdentifiersArray;
i _version;
@"NSString" burstId;
@"NSString" _versionString;
```

## Properties

```
@property (T@"NSMutableArray",VclusterArray) clusterArray;
@property (Ti,VtemporalOrder) temporalOrder;
@property (T@"NSCountedSet",VfaceIDCounts) faceIDCounts;
@property (T@"NSMutableArray",VallImageIdentifiers) allImageIdentifiers;
@property (T@"NSMutableDictionary",VstatsByImageIdentifier) statsByImageIdentifier;
@property (T@"NSMutableDictionary",VclusterByImageIdentifier) clusterByImageIdentifier;
@property (T@"NSString",VburstLogFileName) burstLogFileName;
@property (T@"CAMBurstActionClassifier",VactionClassifier) actionClassifier;
@property (Ti,VmaxNumPendingFrames) maxNumPendingFrames;
@property (TB,VenableAnalysis) enableAnalysis;
@property (Ti,VdummyAnalysisCount) dummyAnalysisCount;
@property (TB,VenableFaceCore) enableFaceCore;
@property (TB,VenableDumpYUV) enableDumpYUV;
@property (T@"NSString",VburstCoverSelection) burstCoverSelection;
@property (T@"NSString",&,N,VburstId) burstId;
@property (T@"NSArray",VbestImageIdentifiersArray) bestImageIdentifiersArray;
@property (T@"NSString",V_versionString) versionString;
@property (Ti,V_version) version;
```

## Class methods

```
+[CAMBurstImageSetInternal defaultVersionString];
```

## Instance methods

```
-[CAMBurstImageSetInternal isPortrait];
-[CAMBurstImageSetInternal setVersionString:];
-[CAMBurstImageSetInternal dealloc];
-[CAMBurstImageSetInternal version];
-[CAMBurstImageSetInternal initWithOptions:];
-[CAMBurstImageSetInternal versionString];
-[CAMBurstImageSetInternal setVersion:];
-[CAMBurstImageSetInternal burstId];
-[CAMBurstImageSetInternal addImageFromIOSurface:properties:identifier:completionBlock:];
-[CAMBurstImageSetInternal allImageIdentifiers];
-[CAMBurstImageSetInternal bestImageIdentifiers];
-[CAMBurstImageSetInternal imageClusterForIdentifier:];
-[CAMBurstImageSetInternal isAction];
-[CAMBurstImageSetInternal computeActionSelectionThreshold];
-[CAMBurstImageSetInternal computeEmotion:];
-[CAMBurstImageSetInternal actionClassifier];
-[CAMBurstImageSetInternal addYUVImage:properties:identifier:imageProps:completionBlock:];
-[CAMBurstImageSetInternal bestImageIdentifiersArray];
-[CAMBurstImageSetInternal burstCoverSelection];
-[CAMBurstImageSetInternal burstDocumentDirectory];
-[CAMBurstImageSetInternal burstLogFileName];
-[CAMBurstImageSetInternal clusterArray];
-[CAMBurstImageSetInternal clusterByImageIdentifier];
-[CAMBurstImageSetInternal computeAllImageScores];
-[CAMBurstImageSetInternal computeBeginningVsEndAEMatrixDiffVsAverageAdjacent];
-[CAMBurstImageSetInternal computeCameraTravelDistance];
-[CAMBurstImageSetInternal dummyAnalysisCount];
-[CAMBurstImageSetInternal enableAnalysis];
-[CAMBurstImageSetInternal enableDumpYUV];
-[CAMBurstImageSetInternal enableFaceCore];
-[CAMBurstImageSetInternal faceIDCounts];
-[CAMBurstImageSetInternal findBestImage:useActionScores:];
-[CAMBurstImageSetInternal isFaceDetectionForced];
-[CAMBurstImageSetInternal maxNumPendingFrames];
-[CAMBurstImageSetInternal performEmotionalRejectionOnCluster:];
-[CAMBurstImageSetInternal processClusters:];
-[CAMBurstImageSetInternal selectCoverPhotoFromMultiple:burstSize:];
-[CAMBurstImageSetInternal setActionClassifier:];
-[CAMBurstImageSetInternal setAllImageIdentifiers:];
-[CAMBurstImageSetInternal setBestImageIdentifiersArray:];
-[CAMBurstImageSetInternal setBurstCoverSelection:];
-[CAMBurstImageSetInternal setBurstId:];
-[CAMBurstImageSetInternal setBurstLogFileName:];
-[CAMBurstImageSetInternal setClusterArray:];
-[CAMBurstImageSetInternal setClusterByImageIdentifier:];
-[CAMBurstImageSetInternal setDummyAnalysisCount:];
-[CAMBurstImageSetInternal setEnableAnalysis:];
-[CAMBurstImageSetInternal setEnableDumpYUV:];
-[CAMBurstImageSetInternal setEnableFaceCore:];
-[CAMBurstImageSetInternal setFaceIDCounts:];
-[CAMBurstImageSetInternal setMaxNumPendingFrames:];
-[CAMBurstImageSetInternal setStatsByImageIdentifier:];
-[CAMBurstImageSetInternal setTemporalOrder:];
-[CAMBurstImageSetInternal statsByImageIdentifier];
-[CAMBurstImageSetInternal temporalOrder];
```
