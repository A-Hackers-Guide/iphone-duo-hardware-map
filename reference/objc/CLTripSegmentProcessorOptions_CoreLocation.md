# `CLTripSegmentProcessorOptions`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 23 instance variables, 23 properties, 52 instance methods, 1 class methods

## Instance variables

```
B _runLinearInterpolator;
B _runInertialIntegrator;
B _runMapIntegrator;
B _useXPCServiceForMapQuery;
B _shouldRecordDataInFileForReplay;
B _createSparseDataFromOneHzData;
B _isSimulatedSparseProcessing;
B _isNetworkAccessAllowed;
B _useParticleMapMatcherForSnappingInMapIntegrator;
B _useNonGNSSFixesForRouteReconstruction;
B _runLocationOutlierRejector;
B _isWatch;
B _enableUseWifiInPTS;
B _generateRouteSummary;
d _timeBetweenReconstructedPointsSeconds;
@"NSString" _tripSegmentRecorderLoggingDirectory;
d _maxProcessingTimeInMilliSec;
d _useXPCServiceForVehicularAStarSearch;
Q _windowSizeForLocationOutlierRejector;
Q _stepSizeForLocationOutlierRejector;
d _minDistanceBetweenODVisitsToGenerateTripSegmentMeters;
d _maxTripSegmentDurationSeconds;
Q _externalCallNumber;
```

## Properties

```
@property (TB,R,N,V_runLinearInterpolator) runLinearInterpolator;
@property (TB,R,N,V_runInertialIntegrator) runInertialIntegrator;
@property (TB,R,N,V_runMapIntegrator) runMapIntegrator;
@property (TB,R,N,V_useXPCServiceForMapQuery) useXPCServiceForMapQuery;
@property (TB,R,N,V_shouldRecordDataInFileForReplay) shouldRecordDataInFileForReplay;
@property (TB,R,N,V_createSparseDataFromOneHzData) createSparseDataFromOneHzData;
@property (TB,R,N,V_isNetworkAccessAllowed) isNetworkAccessAllowed;
@property (TB,R,N,V_isSimulatedSparseProcessing) isSimulatedSparseProcessing;
@property (Td,R,N,V_timeBetweenReconstructedPointsSeconds) timeBetweenReconstructedPointsSeconds;
@property (TB,R,N,V_useParticleMapMatcherForSnappingInMapIntegrator) useParticleMapMatcherForSnappingInMapIntegrator;
@property (T@"NSString",R,N,V_tripSegmentRecorderLoggingDirectory) tripSegmentRecorderLoggingDirectory;
@property (TB,R,N,V_useNonGNSSFixesForRouteReconstruction) useNonGNSSFixesForRouteReconstruction;
@property (Td,R,N,V_maxProcessingTimeInMilliSec) maxProcessingTimeInMilliSec;
@property (Td,R,N,V_useXPCServiceForVehicularAStarSearch) useXPCServiceForVehicularAStarSearch;
@property (TB,R,N,V_runLocationOutlierRejector) runLocationOutlierRejector;
@property (TQ,R,N,V_windowSizeForLocationOutlierRejector) windowSizeForLocationOutlierRejector;
@property (TQ,R,N,V_stepSizeForLocationOutlierRejector) stepSizeForLocationOutlierRejector;
@property (TB,R,N,V_isWatch) isWatch;
@property (TB,R,N,V_enableUseWifiInPTS) enableUseWifiInPTS;
@property (Td,R,N,V_minDistanceBetweenODVisitsToGenerateTripSegmentMeters) minDistanceBetweenODVisitsToGenerateTripSegmentMeters;
@property (Td,R,N,V_maxTripSegmentDurationSeconds) maxTripSegmentDurationSeconds;
@property (TQ,R,N,V_externalCallNumber) externalCallNumber;
@property (TB,R,N,V_generateRouteSummary) generateRouteSummary;
```

## Class methods

```
+[CLTripSegmentProcessorOptions supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentProcessorOptions isNetworkAccessAllowed];
-[CLTripSegmentProcessorOptions isWatch];
-[CLTripSegmentProcessorOptions setNetworkAccessAllowed:];
-[CLTripSegmentProcessorOptions init];
-[CLTripSegmentProcessorOptions dealloc];
-[CLTripSegmentProcessorOptions setIsWatch:];
-[CLTripSegmentProcessorOptions encodeWithCoder:];
-[CLTripSegmentProcessorOptions description];
-[CLTripSegmentProcessorOptions initWithCoder:];
-[CLTripSegmentProcessorOptions copyWithZone:];
-[CLTripSegmentProcessorOptions setMaxProcessingTimeInMilliSec:];
-[CLTripSegmentProcessorOptions shouldRecordDataInFileForReplay];
-[CLTripSegmentProcessorOptions createSparseDataFromOneHzData];
-[CLTripSegmentProcessorOptions enableUseWifiInPTS];
-[CLTripSegmentProcessorOptions externalCallNumber];
-[CLTripSegmentProcessorOptions generateRouteSummary];
-[CLTripSegmentProcessorOptions isSimulatedSparseProcessing];
-[CLTripSegmentProcessorOptions maxProcessingTimeInMilliSec];
-[CLTripSegmentProcessorOptions maxTripSegmentDurationSeconds];
-[CLTripSegmentProcessorOptions minDistanceBetweenODVisitsToGenerateTripSegmentMeters];
-[CLTripSegmentProcessorOptions runInertialIntegrator];
-[CLTripSegmentProcessorOptions runLinearInterpolator];
-[CLTripSegmentProcessorOptions runLocationOutlierRejector];
-[CLTripSegmentProcessorOptions runMapIntegrator];
-[CLTripSegmentProcessorOptions setCreateSparseDataFromOneHzData:];
-[CLTripSegmentProcessorOptions setEnableUseWifiInPTS:];
-[CLTripSegmentProcessorOptions setExternalCallNumber:];
-[CLTripSegmentProcessorOptions setGenerateRouteSummary:];
-[CLTripSegmentProcessorOptions setMaxTripSegmentDurationSeconds:];
-[CLTripSegmentProcessorOptions setMinDistanceBetweenODVisitsToGenerateTripSegmentMeters:];
-[CLTripSegmentProcessorOptions setRunInertialIntegrator:];
-[CLTripSegmentProcessorOptions setRunLinearInterpolator:];
-[CLTripSegmentProcessorOptions setRunLocationOutlierRejector:];
-[CLTripSegmentProcessorOptions setRunMapIntegrator:];
-[CLTripSegmentProcessorOptions setSimulatedSparseProcessing:];
-[CLTripSegmentProcessorOptions setStepSizeForLocationOutlierRejector:];
-[CLTripSegmentProcessorOptions setTimeBetweenReconstructedPointsSeconds:];
-[CLTripSegmentProcessorOptions setTripSegmentRecorderLoggingDirectory:];
-[CLTripSegmentProcessorOptions setUseNonGNSSFixesForRouteReconstruction:];
-[CLTripSegmentProcessorOptions setUseParticleMapMatcherForSnappingInMapIntegrator:];
-[CLTripSegmentProcessorOptions setUseXPCService:];
-[CLTripSegmentProcessorOptions setUseXPCServiceForVehicularAStarSearch:];
-[CLTripSegmentProcessorOptions setWindowSizeForLocationOutlierRejector:];
-[CLTripSegmentProcessorOptions setshouldRecordDataInFileForReplay:];
-[CLTripSegmentProcessorOptions stepSizeForLocationOutlierRejector];
-[CLTripSegmentProcessorOptions timeBetweenReconstructedPointsSeconds];
-[CLTripSegmentProcessorOptions tripSegmentRecorderLoggingDirectory];
-[CLTripSegmentProcessorOptions useNonGNSSFixesForRouteReconstruction];
-[CLTripSegmentProcessorOptions useParticleMapMatcherForSnappingInMapIntegrator];
-[CLTripSegmentProcessorOptions useXPCServiceForMapQuery];
-[CLTripSegmentProcessorOptions useXPCServiceForVehicularAStarSearch];
-[CLTripSegmentProcessorOptions windowSizeForLocationOutlierRejector];
```
