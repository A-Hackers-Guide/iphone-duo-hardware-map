# `/System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay`

iOS 27.2 dyld shared cache image. Version `3187.0.1.0.0`. **[DSC]**

## Linked libraries (10)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`
- `/System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation`
- `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 1 classes, 0 protocols, 29 methods, 7 properties

### Class pages

Every class and protocol, with its methods: [`_CLLocationPlayer`](../objc/_CLLocationPlayer_CoreLocationReplay.md)

### Classes

`_CLLocationPlayer`

### Properties

```
@property (TB,N,GisPlayerActive,V_playerActive) playerActive;
@property (TB,N,GisNotifierARSessionActive,V_notifierARSessionActive) notifierARSessionActive;
@property (TB,N,GisARSessionActive,V_arSessionActive) arSessionActive;
@property (Td,N,V_notifierLastARKitUpdateTime) notifierLastARKitUpdateTime;
@property (T@"CLSimulationManager",&,N,V_simulationManager) simulationManager;
@property (TB,N,GisFusionEnabled,V_fusionEnabled) fusionEnabled;
@property (TB,N,GisSimulationEnabled,V_simulationEnabled) simulationEnabled;
```

## Strings (141)

```
CLVLF,initWithPoints,Unable to initialize transform_vio2enu,machAbsTime,%{public}.3lf
CLVLF,pushARSessionState,sessionState,%{public}d
CLVLF,pushVLLocalizationResult,activated,%{public}d
CLVLF,pushLocation,Unable to construct LocData,machAbsTime,%{public}.3lf
CLVLF,pushLocation,Unable to synchronize VIO,machAbsTime,%{public}.3lf
CLLP,_updateVIOEstimation:,Payload was sent without start notification of current ARsession
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Input does not have valid rawCourse,machAbsTime,%{public}.3f,rawCourseAcc,%{public}.3f
CLVLF,initWithPoints,Unable to compute course in ENU,machAbsTime,%{public}.3lf
CLVLF,checkStateHealth,Location not fused consecutively for last %zu epochs,machAbsTime,%{public}.3lf
CLVLF,checkStateHealth,Location propagated consecutively for last %zu epochs,machAbsTime,%{public}.3lf
CLVLF,reinitWithFrames,filter re-initialized with frames
CLVLF,updateWithCLPoints,Mahalanobis test failed,machAbsTime,%{public}.3lf,forceUpdateNeeded,%{public}d
longitude %.9lf is not valid.
CLLP,setEnableSimulation:,Cannot set a flag while player is active
CLVLF,pushARSessionState,Filter reset,AR session closed,activated,%{public}d
CLVLF,fuseWithPoints,Update skipped,machAbsTime,%{public}.3lf,hasVlfEngaged,%{public}d,hasVlfTimedOut,%{public}d,isDevicestatic,%{public}d,vio2enu,[%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{
CLVLF,propagateAfterSessionEnded,Location propagated,machAbsTime,%{public}.3lf,course,%{public}.3lf,speed,%{public}.3lf
CLVLF,updateWithCLPoints,Invalid measurement,machAbsTime,%{public}.3lf,isVioSynced,%{public}d,isLocEnuValid,%{public}d,isPredictedStateEnuValid,%{public}d
CLVLF,isValid,Invalid VL,confidence lower than the minimum threshold,%f
CLVLF,interpolateVioDataAt,util::binary_find_nearest error,machAbsTime,%{public}.3lf
CLLP,_updateVIOEstimation:,Input estimation is nil
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Input does not have valid rawAltitude,machAbsTime,%{public}.3f,rawVertAcc,%{public}.3f
CLVLF,getFusedLocation,Filter not initialized,machAbsTime,%{public}.3lf,initialized,%{public}d
CLVLFT,fromCLVLLocalizationResult,unable to compute LLA from ECEF
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Input does not have valid rawCoordinate,machAbsTime,%{public}.3f,rawHorzAcc,%{public}.3f
CLVLFT,propagatePositionCovInENU,this should not happen,isPosEnuValid,%d,speedAcc,%.3lf
CLVLF,pushVLLocalizationResult,VL buffer reached its maximum size,machAbsTime,%{public}.3lf,sizeInSec,%{public}.3lf,sizeInMB,%{private}.3lf
#Warning Input latitude = %.9lf is out of possible range
CLVLF,fuseWithPoints,Filter reset,VIO measurements were unacceptable for %{public}.3lf sec,machAbsTime,%{public}.3lf,lastNominalVioMachAbsTime,%{public}.3lf
CLVLF,getFusedLocation,Output,type,%{private}d,timestamp,%{public}.3lf,machtime,%{public}.3lf,machContinuousTime,%{public}.3lf,latitude,%{sensitive}.8lf,longitude,%{sensitive}.8lf,horizontalAccuracy,%{private}.3lf,altitude,%{sensitive}.3lf,
CLVLF,fuseWithFrames,Filter reset,VIO session is re-initialized,machAbsTime,%{public}.3lf,prevOriginTimestamp,%{public}.3lf,currOriginTimestamp,%{public}.3lf
CLVLF,filterUnfusedLocation,Invalid LocData,machAbsTime,%{public}.3lf,currLocIsEnuValid,%{public}d
CLVLF,initWithPoints,Unable to compute course in VIO,machAbsTime,%{public}.3lf
CLVLF,propagateAfterSessionEnded,Filter reset,Propagated LLA invalid,machAbsTime,%{public}.3lf
CLLP,_getFusedLocationFrom:machAbsTime:,Player is inactive - need to start the player first
CLVLF,pushVIOEstimation,VIO buffer reached its maximum size,machAbsTime,%{public}.3lf,sizeInSec,%{public}.3lf,sizeInMB,%{private}.3lf
CLLP,setEnableFusion:,Cannot set a flag while player is active
CLLP,_getFusedLocationFrom:machAbsTime:,Input recordedLocation is nil
CLLP,_updateLocation:locationPrivate:,Manual location fuser reset,machAbsTime,%{public}.3lf
CLVLFT,convertAltitudeWgs84ToMsl,DMA unavailable,Failed to convert altitude
CLVLF,pushLocation,Invalid measurement,machAbsTime,%{public}.3lf,prevMachAbsTime,%{public}.3lf,locationType,%{private}d
CLVLF,propagateAfterSessionEnded,Filter reset,Invalid horzAcc,machAbsTime,%{public}.3lf,propHorzAcc,%{public}.3lf,currHorzAcc,%{public}.3lf
CLVLF,getFusedLocation,Nonsupporting provider,machAbsTime,%{public}.3lf,locationType,%{private}d
CLVLF,pushLocation,LOC buffer reached its maximum size,machAbsTime,%{public}.3lf,sizeInSec,%{public}.3lf,sizeInMB,%{private}.3lf
CLVLF,filterFusedCourse,Course adjusted,machAbsTime,%{public}.3lf,courseDiff,%{public}.3lf
CLVLF,initialize,Computed course and reported course are too different,machAbsTime,%{public}.3lf,courseEnuFromPos,%{private}.3lf,courseEnu,%{private}.3lf
CLVLF,propagateAfterSessionEnded,Filter reset,prev ENU invalid,machAbsTime,%{public}.3lf
CLVLFT,computePositionInENU,altitude unavailable
CLVLF,getFusedLocation,Filter inactive,machAbsTime,%{public}.3lf,activated,%{public}d,lastValidVlf,%{public}.3lf
CLVLF,fuseWithPoints,Filter reset,unhealthy state,machAbsTime,%{public}.3lf
CLVLF,reinitWithFrames,filter still with points init
CLVLF,isValid,Invalid CL,maybe a simulated location
CLVLF,removeAllVioDataExceptLastNSeconds,Called without locking vision buffers
CLVLFT,computeCourseFromPosInENU,this should not happen,isPrevPoseDeterministic,%d,isCurrPoseDeterministic,%d
CLVLF,pushVLLocalizationResult,VL added to queue,machAbsTime,%{public}.3lf
CLVLF,filterUnfusedLocation,Invalid horzAcc,machAbsTime,%{public}.3lf,propHorzAcc,%{public}.3lf,currHorzAcc,%{public}.3lf
CLLP,_updateVLLocalizationResult:,Player is inactive - need to start the player first
CLVLF,pushVIOEstimation,Invalid measurement,machAbsTime,%{public}.3lf,prevMachAbsTime,%{public}.3lf
CLVLFT,computeCourseFromPos,this should not happen,isPrevPoseDeterministic,%d,isCurrPoseDeterministic,%d
CLVLF,pushVIOEstimation,activated,%{public}d
CLVLF,fuseWithPoints,Filter reset,VIO session is re-initialized,machAbsTime,%{public}.3lf,prevOriginTimestamp,%{public}.3lf,currOriginTimestamp,%{public}.3lf
CLVLF,reset,Called without locking vision buffers
CLVLF,fuseWithFrames,Filter reset,unhealthy state,machAbsTime,%{public}.3lf
CLVLF,initWithPoints,Not enough movement,machAbsTime,%{public}.3lf,vioHorzDist,%{private}.3lf,locHorzDist,%{private}.3lf
CLVLF,isValid,Invalid VL,CL-VL vertical distance,%{private}.3lf,vertDistThres,%{private}.3lf
CLVLF,filterUnfusedLocation,Propagate LLA invalid,machAbsTime,%{public}.3lf
CLVLF,filterFusedCourse,Invalid courseAcc,machAbsTime,%{public}.3lf,prevCourseAcc,%{public}.3lf,currCourseAcc,%{public}.3lf
CLVLF,initWithFrames,Unable to convert VLF to LOC,machAbsTime,%{public}.3lf
CLVLF,removeAllVioDataLessThanMachAbsoluteTime,Called without locking vision buffers
Bad index into kkDefenseMappingAgencyTenByTenGeoid.
CLVLFT,convertAltitudeMslToWgs84,DEM unavailable,using DMA und,%{private}f
CLVLFT,convertAltitudeWgs84ToMsl,altitudeWgs84 unavailable
CLVLF,pushVLLocalizationResult,Invalid measurement,machAbsTime,%{public}.3lf,prevMachAbsTime,%{public}.3lf,confidence,%{public}.3lf
CLVLF,fuseWithFrames,Filter reset,VIO measurements were unacceptable for %{public}.3lf sec,machAbsTime,%{public}.3lf,lastNominalVioMachAbsTime,%{public}.3lf
CLVLF,fuseWithFrames,Unable to compute VLF in ENU,machAbsTime,%{public}.3lf
CLVLF,initWithFrames,Invalid measurement,machAbsTime,%{public}.3lf
CLLP,start,Player is already active - nothing to start
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Will use course instead of rawCourse
CLVLFT,convertAltitudeWgs84ToMsl,DEM unavailable,using DMA und,%{private}f
CLVLF,getFusedLocation,Filter reset,diverged,machAbsTime,%{public}.3lf,fusedHorizontalAccuracy,%{private}.3lf,locationHorizontalAccuracy,%{private}.3lf,horzDistToRaw,%{private}.3lf,fusedVerticalAccuracy,%{private}.3lf,locationVerticalAccura
CLVLF,initWithPoints,Unable to compute ENU potisions,machAbsTime,%{public}.3lf
CLVLF,updateWithCLPoints,Filter updated,machAbsTime,%{public}.3lf,vio2enu,[%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf],vio2enu_cov_diag,[%{private}.6lf,%{private}.6lf,%{private}.
CLVLF,isValid,Invalid VL,VL-VIO pitchDiff,%{private}.3lf,pitchDiffThres,%{private}.3lf
CLVLF,extrapolateVioDataAt,Not enough VIO data,machAbsTime,%{public}.3lf
CLVLF,isValid,Invalid VL,CL-VL horizontal distance,%{private}.3lf,horzDistThres,%{private}.3lf
CLVLF,interpolateVioDataAt,mach::SphericalLinearInterpolator::interpolate error,machAbsTime,%{public}.3lf
CLVLF,removeAllVioDataForFirstNSeconds,Called without locking vision buffers
CLVLFT,computePositionInENU,latitude/longitude unavailable
CLVLF,initWithFrames,Filter initialized,machAbsTime,%{public}.3lf,vio2enu,[%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf],vio2enu_cov_diag,[%{private}.6lf,%{private}.6lf,%{private}.
CLVLF,isValid,Invalid VL,VL-VL distance,%{private}.3lf,distThres,%{private}.3lf
CLLP,_updateVIOEstimation:,Player is inactive - need to start the player first
CLLP,_updateVLLocalizationResult,ARSession has timed out without end notification,nowMachAbsTime,%{public}.3lf,lastARKitUpdate,%{public}.3lf
CLVLFT,convertAltitudeMslToWgs84,DMA unavailable,Failed to convert altitude
CLVLF,filterUnfusedLocation,Location propagated,machAbsTime,%{public}.3lf,course,%{public}.3lf,speed,%{public}.3lf
CLVLF,isValid,Invalid VL,Unable to compute ENU from ECEF
CLVLF,removeAllVlfDataForFirstNSeconds,Called without locking vision buffers
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Will use coordinate instead of rawCoordinate
CLVLF,pushARSessionState,Filter reset,AR session started,activated,%{public}d
CLVLF,propagate,Filter propagated,machAbsTime,%{public}.3lf,rotProcNoiseStd,%{public}.3lf,posProcNoiseStd,%{public}.3lf
CLVLF,synchronizeVioDataAt,Called without locking vision buffers
CLVLF,removeAllVlfDataLessThanMachAbsoluteTime,Called without locking vision buffers
CLVLFT,convertAltitudeMslToWgs84,altitudeMsl unavailable
CLVLF,isValid,Invalid VL,inf or nan value in estimates or covariance
CLVLF,isValid,Invalid VL,data class initialized as deterministic
latitude %.9lf is not valid.
CLVLF,pushLocation,Filter reset,this should not happen,machAbsTime,%{public}.3lf,activated,%{public}d,lastValidVlf,%{public}.3lf
CLVLF,fuseWithFrames,Unable to convert VLF to LOC,machAbsTime,%{public}.3lf
CLVLF,initWithPoints,Filter initialized,machAbsTime,%{public}.3lf,vio2enu,[%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf],vio2enu_cov_diag,[%{private}.6lf,%{private}.6lf,%{private}.
CLVLF,updateWithVLPoints,Filter updated,machAbsTime,%{public}.3lf,vio2enu,[%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf,%{private}.3lf],vio2enu_cov_diag,[%{private}.6lf,%{private}.6lf,%{private}.
CLLP,_updateARSessionState:,Player is inactive - need to start the player first
CLLP,_updateVLLocalizationResult:,Input localizationResult is nil
CLVLF,pushVIOEstimation,Unable to construct VioData,machAbsTime,%{public}.3lf,trackingState,%{public}d,inertialState,%{private}p,inertialCovariance,%{private}p
CLVLF,initWithFrames,Unable to compute VLF in ENU,machAbsTime,%{public}.3lf
CLVLF,initWithPoints,Unable to compute delta position in VIO,machAbsTime,%{public}.3lf
CLVLF,isValid,Invalid VL,the diagonal of covarinace is all zero
CLVLF,isValid,Invalid VL,confidence out of range,%f
CLLP,stop,Player is already inactive - nothing to stop
CLLP,_updateVIOEstimation,ARSession has timed out without end notification,nowMachAbsTime,%{public}.3lf,lastARKitUpdate,%{public}.3lf
CLVLF,pushVLLocalizationResult,Unable to construct VlfData,machAbsTime,%{public}.3lf
CLLP,_updateARSessionState:,New session has started without end notification of previous session
CLLP,convertCLLocation:toDaemonLocation:daemonLocationPrivate:,Will use altitude instead of rawAltitude
CLVLF,getFusedLocation,Outdated state,machAbsTime,%{public}.3lf,stateMachAbsTime,%{public}.3lf
CLVLF,updateWithVLPoints,Mahalanobis test failed,machAbsTime,%{public}.3lf,forceUpdateNeeded,%{public}d
CLLP,_updateVLLocalizationResult:,Payload was sent without start notification of current ARSession
this->max_num_rows_ >= A.num_rows_
TransposeDataFootprint
com.apple.locationd.Legacy
Generic_deprecated
lead_dim > 0
operator()
idx >= 0
data_ != __null
idx < num_elements_
v8@?0
com.apple.locationd.Position
Vision
operator=
cnmatrixbase.h
cnmatrix.h
this->max_num_cols_ >= A.num_cols_
vector
```
