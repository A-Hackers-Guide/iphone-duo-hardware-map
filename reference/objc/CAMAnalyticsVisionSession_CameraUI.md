# `CAMAnalyticsVisionSession`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAnalyticsEvent`
- 17 instance variables, 19 properties, 49 instance methods, 0 class methods

## Instance variables

```
B __textDetectionEnabled;
B __MRCDetectionEnabled;
B __documentScanningEnabled;
d __startTime;
Q __textButtonPressCount;
Q __qrButtonPressCount;
Q __appClipButtonPressCount;
Q __qrPillPressCount;
Q __appClipPillPressCount;
Q __maxTextRegionCount;
Q __maxQRCodeCount;
Q __maxAppClipCodeCount;
@"NSMutableSet" __pressedQRTypes;
Q __countObservedDocuments;
Q __countDocumentScanningPressCount;
Q __countDocumentScanningCompletedScans;
Q __countDocumentScanningCanceledScans;
```

## Properties

```
@property (TB,R,N,G_isTextDetectionEnabled,V__textDetectionEnabled) _textDetectionEnabled;
@property (TB,R,N,G_isMRCDetectionEnabled,V__MRCDetectionEnabled) _MRCDetectionEnabled;
@property (TB,R,N,G_isDocumentScanningEnabled,V__documentScanningEnabled) _documentScanningEnabled;
@property (Td,N,S_setStartTime:,V__startTime) _startTime;
@property (TQ,N,S_setTextButtonPressCount:,V__textButtonPressCount) _textButtonPressCount;
@property (TQ,N,S_setQRButtonPressCount:,V__qrButtonPressCount) _qrButtonPressCount;
@property (TQ,N,S_setAppClipButtonPressCount:,V__appClipButtonPressCount) _appClipButtonPressCount;
@property (TQ,N,S_setQRPillPressCount:,V__qrPillPressCount) _qrPillPressCount;
@property (TQ,N,S_setAppClipPillPressCount:,V__appClipPillPressCount) _appClipPillPressCount;
@property (TQ,N,S_setMaxTextRegionCount:,V__maxTextRegionCount) _maxTextRegionCount;
@property (TQ,N,S_setMaxQRCodeCount:,V__maxQRCodeCount) _maxQRCodeCount;
@property (TQ,N,S_setMaxAppClipCodeCount:,V__maxAppClipCodeCount) _maxAppClipCodeCount;
@property (T@"NSMutableSet",&,N,S_setPressedMRCTypes:,V__pressedQRTypes) _pressedQRTypes;
@property (TQ,N,S_setCountObservedDocuments:,V__countObservedDocuments) _countObservedDocuments;
@property (TQ,N,S_setCountDocumentScanningPressCount:,V__countDocumentScanningPressCount) _countDocumentScanningPressCount;
@property (TQ,N,S_setCountDocumentScanningCompletedScans:,V__countDocumentScanningCompletedScans) _countDocumentScanningCompletedScans;
@property (TQ,N,S_setCountDocumentScanningCanceleddScans:,V__countDocumentScanningCanceledScans) _countDocumentScanningCanceledScans;
@property (TQ,R,N) totalMRCInteractions;
@property (TQ,R,N) totalTextInteractions;
```

## Instance methods

```
-[CAMAnalyticsVisionSession _startTime];
-[CAMAnalyticsVisionSession publish];
-[CAMAnalyticsVisionSession _isTextDetectionEnabled];
-[CAMAnalyticsVisionSession _setCountObservedDocuments:];
-[CAMAnalyticsVisionSession initWithTextDetectionEnabled:MRCDetectionEnabled:documentScanningEnabled:];
-[CAMAnalyticsVisionSession _pressedQRTypes];
-[CAMAnalyticsVisionSession _isDocumentScanningEnabled];
-[CAMAnalyticsVisionSession _setCountDocumentScanningPressCount:];
-[CAMAnalyticsVisionSession _setCountDocumentScanningCompletedScans:];
-[CAMAnalyticsVisionSession _setPressedMRCTypes:];
-[CAMAnalyticsVisionSession countButtonPressForDocumentScanning];
-[CAMAnalyticsVisionSession _setTextButtonPressCount:];
-[CAMAnalyticsVisionSession _qrPillPressCount];
-[CAMAnalyticsVisionSession _setCountDocumentScanningCanceleddScans:];
-[CAMAnalyticsVisionSession _appClipPillPressCount];
-[CAMAnalyticsVisionSession _analyticsValueForQRTypes:];
-[CAMAnalyticsVisionSession _maxAppClipCodeCount];
-[CAMAnalyticsVisionSession _maxQRCodeCount];
-[CAMAnalyticsVisionSession _countObservedDocuments];
-[CAMAnalyticsVisionSession _setAppClipPillPressCount:];
-[CAMAnalyticsVisionSession countButtonPressForMRC:action:];
-[CAMAnalyticsVisionSession eventName];
-[CAMAnalyticsVisionSession totalTextInteractions];
-[CAMAnalyticsVisionSession _textButtonPressCount];
-[CAMAnalyticsVisionSession countDocumentScanningCanceledScans];
-[CAMAnalyticsVisionSession _setStartTime:];
-[CAMAnalyticsVisionSession totalMRCInteractions];
-[CAMAnalyticsVisionSession _isMRCDetectionEnabled];
-[CAMAnalyticsVisionSession countPillPressForMRC:action:];
-[CAMAnalyticsVisionSession _setMaxQRCodeCount:];
-[CAMAnalyticsVisionSession countObservedDocumentScanning];
-[CAMAnalyticsVisionSession _setMaxAppClipCodeCount:];
-[CAMAnalyticsVisionSession _setAppClipButtonPressCount:];
-[CAMAnalyticsVisionSession countObservedSignficantMRCs:];
-[CAMAnalyticsVisionSession _qrButtonPressCount];
-[CAMAnalyticsVisionSession _maxTextRegionCount];
-[CAMAnalyticsVisionSession _setQRPillPressCount:];
-[CAMAnalyticsVisionSession countDocumentScanningCompletedScans];
-[CAMAnalyticsVisionSession _countMRCTypeForAction:];
-[CAMAnalyticsVisionSession _bucketedCount:];
-[CAMAnalyticsVisionSession _setMaxTextRegionCount:];
-[CAMAnalyticsVisionSession countTextButtonPress];
-[CAMAnalyticsVisionSession _countDocumentScanningCanceledScans];
-[CAMAnalyticsVisionSession _countDocumentScanningCompletedScans];
-[CAMAnalyticsVisionSession _appClipButtonPressCount];
-[CAMAnalyticsVisionSession _setQRButtonPressCount:];
-[CAMAnalyticsVisionSession _countDocumentScanningPressCount];
-[CAMAnalyticsVisionSession _analyticsValueForQRType:];
-[CAMAnalyticsVisionSession countObservedSignficantTextRegionCount:];
```
