# `CAMBurstImageStat`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 46 instance variables, 33 properties, 95 instance methods, 0 class methods

## Instance variables

```
f normalizedFocusScore;
f normalizedSigma;
[1024f] colorHistogram;
i numEntries;
[256S] aeMatrix;
i dissimilarity;
d timeReceived;
d timestamp;
^v projectionMemoryBlock;
{FastRegistration_Signatures="piRow"^f"nPiRow"Q"piRowTable"{Projections_meanStdTable="sumTable"^f"sumSqTable"^f}"piCol"^f"nPiCol"Q"piColTable"{Projections_meanStdTable="sumTable"^f"sumSqTable"^f}} projectionSignature;
^{SharpnessGridElement_t=CCf} sharpnessGrid;
i gridWidth;
i gridHeight;
{GridROI_t="startX"i"startY"i"endX"i"endY"i} gridROI;
{GridROI_t="startX"i"startY"i"endX"i"endY"i} smoothedROI;
B hasRegistrationData;
f maxSkewness;
f roiSize;
B exclude;
B AEStable;
B AFStable;
B emotionallyRejected;
B doLimitedSharpnessAndBlur;
B isGarbage;
i orientation;
i AEAverage;
i AETarget;
i temporalOrder;
f avgHorzDiffY;
f blurExtent;
f imageScore;
f actionScore;
f registrationErrorX;
f registrationErrorY;
f registrationErrorIntegral;
f actionClusteringScore;
i numHWFaces;
f tx;
f ty;
i _AEDelta;
i _fullsizeJpegSize;
i _version;
@"NSString" imageId;
@"NSMutableArray" faceStatArray;
^{__IOSurface=} _fullsizeJpegData;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} facesRoiRect;
```

## Properties

```
@property (T@"NSString",VimageId) imageId;
@property (Ti,Vorientation) orientation;
@property (T@"NSMutableArray",VfaceStatArray) faceStatArray;
@property (TB,Vexclude) exclude;
@property (TB,VAEStable) AEStable;
@property (Ti,VAEAverage) AEAverage;
@property (Ti,VAETarget) AETarget;
@property (TB,VAFStable) AFStable;
@property (Ti,VtemporalOrder) temporalOrder;
@property (Tf,VavgHorzDiffY) avgHorzDiffY;
@property (Tf,VblurExtent) blurExtent;
@property (Tf,VimageScore) imageScore;
@property (Tf,VactionScore) actionScore;
@property (Td,VtimeReceived) timeReceived;
@property (Td,Vtimestamp) timestamp;
@property (Tf,VmaxSkewness) maxSkewness;
@property (Tf,VregistrationErrorX) registrationErrorX;
@property (Tf,VregistrationErrorY) registrationErrorY;
@property (Tf,VregistrationErrorIntegral) registrationErrorIntegral;
@property (Tf,VactionClusteringScore) actionClusteringScore;
@property (TB,VhasRegistrationData) hasRegistrationData;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VfacesRoiRect) facesRoiRect;
@property (Ti,VnumHWFaces) numHWFaces;
@property (TB,VemotionallyRejected) emotionallyRejected;
@property (TB,VdoLimitedSharpnessAndBlur) doLimitedSharpnessAndBlur;
@property (Tf,Vtx) tx;
@property (Tf,Vty) ty;
@property (TB,VisGarbage) isGarbage;
@property (Tf,VroiSize) roiSize;
@property (Ti,V_AEDelta) AEDelta;
@property (T^{__IOSurface=},V_fullsizeJpegData) fullsizeJpegData;
@property (Ti,V_fullsizeJpegSize) fullsizeJpegSize;
@property (Ti,V_version) version;
```

## Instance methods

```
-[CAMBurstImageStat setOrientation:];
-[CAMBurstImageStat setTimestamp:];
-[CAMBurstImageStat orientation];
-[CAMBurstImageStat dealloc];
-[CAMBurstImageStat timestamp];
-[CAMBurstImageStat version];
-[CAMBurstImageStat setVersion:];
-[CAMBurstImageStat imageId];
-[CAMBurstImageStat initWithIdentifier:];
-[CAMBurstImageStat setImageId:];
-[CAMBurstImageStat AEDelta];
-[CAMBurstImageStat AEStable];
-[CAMBurstImageStat AFStable];
-[CAMBurstImageStat setActionScore:];
-[CAMBurstImageStat AEAverage];
-[CAMBurstImageStat AETarget];
-[CAMBurstImageStat exclude];
-[CAMBurstImageStat roiSize];
-[CAMBurstImageStat setMaxSkewness:];
-[CAMBurstImageStat actionClusteringScore];
-[CAMBurstImageStat actionScore];
-[CAMBurstImageStat aeMatrix];
-[CAMBurstImageStat allocateMeanStdPingPongBuffers::::];
-[CAMBurstImageStat assignMeanStdBuffers:];
-[CAMBurstImageStat avgHorzDiffY];
-[CAMBurstImageStat blurExtent];
-[CAMBurstImageStat canRegister];
-[CAMBurstImageStat collapseSharpnessGrid];
-[CAMBurstImageStat colorHistogram];
-[CAMBurstImageStat compareImageOrder:];
-[CAMBurstImageStat compareImageStats:];
-[CAMBurstImageStat computeAEMatrix:];
-[CAMBurstImageStat computeAEMatrixDifference:];
-[CAMBurstImageStat computeBlurStatsOnGrid:];
-[CAMBurstImageStat computeFacialFocusScoreSum];
-[CAMBurstImageStat computeImageColorHistogram:];
-[CAMBurstImageStat computeImageData:faceIDCounts:];
-[CAMBurstImageStat computeImageDistance:];
-[CAMBurstImageStat computeImageProjections:];
-[CAMBurstImageStat computeImageSharpnessOnGrid:];
-[CAMBurstImageStat computeRuleOfThreeDistance];
-[CAMBurstImageStat computeScore:];
-[CAMBurstImageStat computeSmilePercentage];
-[CAMBurstImageStat computeSmoothedGridROI:nextStat:];
-[CAMBurstImageStat doLimitedSharpnessAndBlur];
-[CAMBurstImageStat emotionallyRejected];
-[CAMBurstImageStat faceStatArray];
-[CAMBurstImageStat facesRoiRect];
-[CAMBurstImageStat flagAsGarbage];
-[CAMBurstImageStat fullsizeJpegData];
-[CAMBurstImageStat fullsizeJpegSize];
-[CAMBurstImageStat getSharpnessAndBlurLimits];
-[CAMBurstImageStat hasRegistrationData];
-[CAMBurstImageStat imageScore];
-[CAMBurstImageStat isGarbage];
-[CAMBurstImageStat maxSkewness];
-[CAMBurstImageStat numHWFaces];
-[CAMBurstImageStat performRegistration:deltaCol:deltaRow:];
-[CAMBurstImageStat registrationErrorIntegral];
-[CAMBurstImageStat registrationErrorX];
-[CAMBurstImageStat registrationErrorY];
-[CAMBurstImageStat setAEAverage:];
-[CAMBurstImageStat setAEDelta:];
-[CAMBurstImageStat setAEMatrix:];
-[CAMBurstImageStat setAEStable:];
-[CAMBurstImageStat setAETarget:];
-[CAMBurstImageStat setAFStable:];
-[CAMBurstImageStat setActionClusteringScore:];
-[CAMBurstImageStat setAvgHorzDiffY:];
-[CAMBurstImageStat setBlurExtent:];
-[CAMBurstImageStat setDoLimitedSharpnessAndBlur:];
-[CAMBurstImageStat setEmotionallyRejected:];
-[CAMBurstImageStat setExclude:];
-[CAMBurstImageStat setFaceStatArray:];
-[CAMBurstImageStat setFacesRoiRect:];
-[CAMBurstImageStat setFullsizeJpegData:];
-[CAMBurstImageStat setFullsizeJpegSize:];
-[CAMBurstImageStat setHasRegistrationData:];
-[CAMBurstImageStat setImageScore:];
-[CAMBurstImageStat setIsGarbage:];
-[CAMBurstImageStat setNumHWFaces:];
-[CAMBurstImageStat setRegistrationErrorIntegral:];
-[CAMBurstImageStat setRegistrationErrorX:];
-[CAMBurstImageStat setRegistrationErrorY:];
-[CAMBurstImageStat setRoiSize:];
-[CAMBurstImageStat setTemporalOrder:];
-[CAMBurstImageStat setTimeReceived:];
-[CAMBurstImageStat setTx:];
-[CAMBurstImageStat setTy:];
-[CAMBurstImageStat temporalOrder];
-[CAMBurstImageStat timeReceived];
-[CAMBurstImageStat tx];
-[CAMBurstImageStat ty];
-[CAMBurstImageStat updateROI:];
-[CAMBurstImageStat writeGridROI:];
```
