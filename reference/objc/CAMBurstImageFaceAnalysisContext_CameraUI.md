# `CAMBurstImageFaceAnalysisContext`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" curConfig;
@"NSMutableDictionary" faceIdMapping;
@"NSMutableDictionary" renameMapping;
i faceIdCounter;
@"NSMutableArray" faceInfoArray;
i numFramesNoFaces;
@"FCRFaceDetector" faceDetector;
@"NSMutableArray" faceTimestampArray;
d latestImageTimestamp;
i lastFaceIndex;
B forceFaceDetectionEnable;
i _version;
d timeBlinkDetectionDone;
d timeFaceDetectionDone;
d latestFaceTimestamp;
```

## Properties

```
@property (Td,VtimeFaceDetectionDone) timeFaceDetectionDone;
@property (Td,VtimeBlinkDetectionDone) timeBlinkDetectionDone;
@property (TB,VforceFaceDetectionEnable) forceFaceDetectionEnable;
@property (Td,VlatestFaceTimestamp) latestFaceTimestamp;
@property (Ti,V_version) version;
```

## Instance methods

```
-[CAMBurstImageFaceAnalysisContext dealloc];
-[CAMBurstImageFaceAnalysisContext version];
-[CAMBurstImageFaceAnalysisContext setVersion:];
-[CAMBurstImageFaceAnalysisContext initWithVersion:];
-[CAMBurstImageFaceAnalysisContext addFaceToArray:];
-[CAMBurstImageFaceAnalysisContext calcFaceScores:];
-[CAMBurstImageFaceAnalysisContext addFacesToImageStat:imageSize:];
-[CAMBurstImageFaceAnalysisContext adjustFaceIdsForImageStat:];
-[CAMBurstImageFaceAnalysisContext calculateFaceCoreROI:imageStat:needFaceCore:];
-[CAMBurstImageFaceAnalysisContext calculateFaceFocusInImage:imageStat:];
-[CAMBurstImageFaceAnalysisContext dumpFaceInfoArray];
-[CAMBurstImageFaceAnalysisContext extractFacesFromMetadata:];
-[CAMBurstImageFaceAnalysisContext findFacesInImage:imageStat:];
-[CAMBurstImageFaceAnalysisContext findOverlappingFaceStat:imageStat:];
-[CAMBurstImageFaceAnalysisContext forceFaceDetectionEnable];
-[CAMBurstImageFaceAnalysisContext latestFaceTimestamp];
-[CAMBurstImageFaceAnalysisContext padRoiRect:paddingX:paddingY:];
-[CAMBurstImageFaceAnalysisContext setForceFaceDetectionEnable:];
-[CAMBurstImageFaceAnalysisContext setLatestFaceTimestamp:];
-[CAMBurstImageFaceAnalysisContext setTimeBlinkDetectionDone:];
-[CAMBurstImageFaceAnalysisContext setTimeFaceDetectionDone:];
-[CAMBurstImageFaceAnalysisContext setupFaceDetector];
-[CAMBurstImageFaceAnalysisContext timeBlinkDetectionDone];
-[CAMBurstImageFaceAnalysisContext timeFaceDetectionDone];
```
