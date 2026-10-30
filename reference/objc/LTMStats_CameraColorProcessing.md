# `LTMStats`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMAlgorithmBase`
- 7 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"LTMStatsCompute" _computeLTMStats;
@"<MTLBuffer>" _localHistBuffer;
@"<MTLBuffer>" _globalHistBuffer;
@"<MTLBuffer>" _globalFaceHistBuffer;
@"<MTLBuffer>" _thumbnailBuffer;
{?="luma"{?="LumShift"I"CoeffAvgY"[3I]"CoeffMaxY"[3I]"AvgYOffset"I}"globalHist"{?="Enable"B"YHistSel"S"StartX"I"StartY"I"EndX"I"EndY"I"Offset"[4I]"Scale"[4f]}"globalFaceHist"[10{?="Enable"B"YHistSel"S"StartX"I"StartY"I"EndX"I"EndY"I"Offset"[4I]"Scale"[4f]}]"localHist"{?="Enable"B"SelInput"I"LocalHistShift"I"StartX"I"StartY"I"EndX"I"EndY"I"StrideX"I"StrideY"I"BlockSizeX"I"BlockSizeY"I"Offset"I"Scale"I"ThreLo"I"ThreHi"I"enableAntiAliasing"B"SubBin"I"ClipValidIdx"B"HistCoeff"[25I]"enableHiResLocalHistogram"B}"thumbnail"{?="StartX"I"StartY"I"EndX"I"EndY"I"BlockSizeX"I"BlockSizeY"I"OffsetX"I"OffsetY"I"genMethod"i"portraitOrientated"B"ThumbAvgRecipNumPix"I"thumbnailMult"I}} _params;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LTMStats purgeResources];
-[LTMStats allocateResources];
-[LTMStats initWithMetalContext:];
-[LTMStats prewarmShaders];
-[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:];
-[LTMStats fillProcHITHStat:with:];
-[LTMStats finishCalculateHITHStatistics:optimized:];
-[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:];
```
