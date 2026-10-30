# `FigCaptureImageMotionDetector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
i _width;
i _height;
^i _intRowSum;
^i _intColSum;
{?="rowSums"^^d"colSums"^^d"curIdx"I"count"I"size"I} _imgProj;
^d _tmpSum1;
^d _tmpSum2;
^d _corrArray;
i _rowSumLength;
i _rowSumCapacity;
i _colSumLength;
i _colSumCapacity;
i _processedBufferCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sumROI;
f _stationaryThreshold;
i _maximumSearchRange;
{?="crossCorrelationMaximum"[2f]"maxCorrelationShift"[2i]"frameRingBufferCount"i"frameRingBufferDistance"i"roi"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"isMotionDetected"B"valid"B} _motionStatistics;
```

## Properties

```
@property (T{?=[2f][2i]ii{CGRect={CGPoint=dd}{CGSize=dd}}BB},R,N,V_motionStatistics) motionStatistics;
@property (Tf,N,V_stationaryThreshold) stationaryThreshold;
@property (Ti,R,N,V_maximumSearchRange) maximumSearchRange;
```

## Instance methods

```
-[FigCaptureImageMotionDetector init];
-[FigCaptureImageMotionDetector dealloc];
-[FigCaptureImageMotionDetector initWithWidth:height:];
-[FigCaptureImageMotionDetector initWithWidth:height:maximumSearchRange:frameRingSize:];
-[FigCaptureImageMotionDetector maximumSearchRange];
-[FigCaptureImageMotionDetector motionStatistics];
-[FigCaptureImageMotionDetector processPixelBuffer:];
-[FigCaptureImageMotionDetector resetProcessingState];
-[FigCaptureImageMotionDetector setCentralROIAndGetRect:];
-[FigCaptureImageMotionDetector setRoi:actualROI:];
-[FigCaptureImageMotionDetector setStationaryThreshold:];
-[FigCaptureImageMotionDetector stationaryThreshold];
```
