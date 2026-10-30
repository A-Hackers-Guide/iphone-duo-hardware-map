# `FigObjectDetectionMetadataGenerator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 31 instance variables, 14 properties, 36 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _regionOfInterest;
I _maxHumanFaces;
B _humanFaceEyeDetectionEnabled;
B _humanFaceSmileDetectionEnabled;
B _humanFaceBlinkDetectionEnabled;
I _maxHumanHeads;
I _maxHumanBodies;
I _maxHumanFullBodies;
I _maxDogBodies;
I _maxDogHeads;
I _maxCatBodies;
I _maxCatHeads;
I _maxSalientObjects;
I _maxSportsBalls;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_queue>" _detectObjectQueue;
B _prepared;
Q _objectDetectionHostTime;
I _objectDetectionInterval;
f _maxMatchCost;
I _previousDetectionsThreshold;
B _objectDetectionIsRunning;
@"NSMutableDictionary" _objectMetadataDictionary;
{?="value"q"timescale"i"flags"I"epoch"q} _objectMetadataDictionaryPTS;
^{OpaqueVTPixelTransferSession=} _pixelTransferInSession;
@"VNSession" _vnSession;
@"NSMutableArray" _figFaceObservations;
@"NSMutableArray" _figHumanBodyObservations;
Q _metadataFaceID;
Q _metadataHumanBodyID;
@"FTBipartiteMatcher" _objectTrackingMatcher;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) regionOfInterest;
@property (TI) maxHumanFaces;
@property (TB) humanFaceEyeDetectionEnabled;
@property (TB) humanFaceSmileDetectionEnabled;
@property (TB) humanFaceBlinkDetectionEnabled;
@property (TI) maxHumanHeads;
@property (TI) maxHumanBodies;
@property (TI) maxHumanFullBodies;
@property (TI) maxDogBodies;
@property (TI) maxDogHeads;
@property (TI) maxCatBodies;
@property (TI) maxCatHeads;
@property (TI) maxSalientObjects;
@property (TI) maxSportsBalls;
```

## Class methods

```
+[FigObjectDetectionMetadataGenerator initialize];
```

## Instance methods

```
-[FigObjectDetectionMetadataGenerator init];
-[FigObjectDetectionMetadataGenerator dealloc];
-[FigObjectDetectionMetadataGenerator unprepare];
-[FigObjectDetectionMetadataGenerator regionOfInterest];
-[FigObjectDetectionMetadataGenerator setRegionOfInterest:];
-[FigObjectDetectionMetadataGenerator setMaxCatHeads:];
-[FigObjectDetectionMetadataGenerator setMaxDogHeads:];
-[FigObjectDetectionMetadataGenerator getCurrentDetectedObjectsAndPTS:];
-[FigObjectDetectionMetadataGenerator getDetectedObjectsForPixelBuffer:pts:];
-[FigObjectDetectionMetadataGenerator humanFaceBlinkDetectionEnabled];
-[FigObjectDetectionMetadataGenerator humanFaceEyeDetectionEnabled];
-[FigObjectDetectionMetadataGenerator humanFaceSmileDetectionEnabled];
-[FigObjectDetectionMetadataGenerator maxCatBodies];
-[FigObjectDetectionMetadataGenerator maxCatHeads];
-[FigObjectDetectionMetadataGenerator maxDogBodies];
-[FigObjectDetectionMetadataGenerator maxDogHeads];
-[FigObjectDetectionMetadataGenerator maxHumanBodies];
-[FigObjectDetectionMetadataGenerator maxHumanFaces];
-[FigObjectDetectionMetadataGenerator maxHumanFullBodies];
-[FigObjectDetectionMetadataGenerator maxHumanHeads];
-[FigObjectDetectionMetadataGenerator maxSalientObjects];
-[FigObjectDetectionMetadataGenerator maxSportsBalls];
-[FigObjectDetectionMetadataGenerator prepareForVideoFormat:];
-[FigObjectDetectionMetadataGenerator processPixelBuffer:pts:];
-[FigObjectDetectionMetadataGenerator processSampleBuffer:];
-[FigObjectDetectionMetadataGenerator setHumanFaceBlinkDetectionEnabled:];
-[FigObjectDetectionMetadataGenerator setHumanFaceEyeDetectionEnabled:];
-[FigObjectDetectionMetadataGenerator setHumanFaceSmileDetectionEnabled:];
-[FigObjectDetectionMetadataGenerator setMaxCatBodies:];
-[FigObjectDetectionMetadataGenerator setMaxDogBodies:];
-[FigObjectDetectionMetadataGenerator setMaxHumanBodies:];
-[FigObjectDetectionMetadataGenerator setMaxHumanFaces:];
-[FigObjectDetectionMetadataGenerator setMaxHumanFullBodies:];
-[FigObjectDetectionMetadataGenerator setMaxHumanHeads:];
-[FigObjectDetectionMetadataGenerator setMaxSalientObjects:];
-[FigObjectDetectionMetadataGenerator setMaxSportsBalls:];
```
