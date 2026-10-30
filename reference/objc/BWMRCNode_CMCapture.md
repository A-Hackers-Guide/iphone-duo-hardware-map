# `BWMRCNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 11 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
^? _createSampleBufferProcessorFunction;
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
@"NSArray" _symbologiesArray;
@"NSArray" _mrcIdentifiers;
q _lastDetectedMRCCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rectOfInterest;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _rectOfInterestLock;
B _hasPendingRectOfInterestUpdate;
B _lowPowerModeEnabled;
@"NSDictionary" _metadataIdentifierToSymbologyDictionary;
@"<BWMetadataDetectedResultsObserver>" _detectedResultsObserver;
```

## Properties

```
@property (T@"<BWMetadataDetectedResultsObserver>",N,V_detectedResultsObserver) detectedResultsObserver;
```

## Class methods

```
+[BWMRCNode initialize];
```

## Instance methods

```
-[BWMRCNode prepareForCurrentConfigurationToBecomeLive];
-[BWMRCNode renderSampleBuffer:forInput:];
-[BWMRCNode init];
-[BWMRCNode dealloc];
-[BWMRCNode setRectOfInterest:];
-[BWMRCNode mrcIdentifiers];
-[BWMRCNode setMrcIdentifiers:];
-[BWMRCNode setLowPowerModeEnabled:];
-[BWMRCNode setDetectedResultsObserver:];
-[BWMRCNode didReachEndOfDataForConfigurationID:input:];
-[BWMRCNode rectOfInterest];
-[BWMRCNode nodeSubType];
-[BWMRCNode detectedResultsObserver];
-[BWMRCNode lowPowerModeEnabled];
-[BWMRCNode nodeType];
```
