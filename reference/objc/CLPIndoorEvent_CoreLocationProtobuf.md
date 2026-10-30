# `CLPIndoorEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 31 instance variables, 60 properties, 102 instance methods, 0 class methods

## Instance variables

```
@"CLPBundleId" _bundleId;
@"CLPCellConnectivityInfo" _cellConnectivity;
@"CLPIndoorCMAttitude" _cmAttitude;
@"CLPIndoorCMPedometer" _cmPedometer;
@"CLPDaemonStatus" _daemonStatus;
@"CLPInertialOdometry" _inertialOdometry;
@"CLPLocation" _location;
@"CLPIndoorMotionActivity" _motionActivity;
@"CLPOutdoorUpdate" _outdoorUpdate;
@"CLPPassKitEvent" _passkitEvent;
@"CLPIndoorPressure" _pressure;
@"CLPProximityAccessoryMetaEvent" _proximityAccessoryMeta;
@"CLPProximityAccessoryMotionEvent" _proximityAccessoryMotion;
@"CLPProximityAlertRaisedEvent" _proximityAlertRaised;
@"CLPProximityGPSTileEvent" _proximityGPSTile;
@"CLPProximityLOIEvent" _proximityLOI;
@"CLPProximityLocationEvent" _proximityLastVisitLocation;
@"CLPProximityMonitoredDeviceCountEvent" _proximityMonitoredDeviceCount;
@"CLPProximityPOITypeEvent" _proximityPOIType;
@"CLPProximityRangeMeasurementEvent" _proximityRangeMeasurement;
@"CLPProximityLocationEvent" _proximityReunionLocation;
@"CLPProximityLocationEvent" _proximityScanLocation;
@"CLPProximityTriggerInfoEvent" _proximityTriggerInfo;
@"CLPProximityVIOPoseEvent" _proximityVIOPose;
@"CLPProximityVehicularStateEvent" _proximityVehicularState;
i _type;
@"CLPLOGENTRYVISIONVIOEstimation" _vioEstimation;
@"CLPLOGENTRYVISIONVLLocalizationResult" _vlLocalizationResult;
@"CLPIndoorWifiScan" _wifiScan;
@"CLPWorkoutUpdateMotionActivity" _workoutUpdateMotionActivity;
{?="type"b1} _has;
```

## Properties

```
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
@property (TB,R,N) hasCmAttitude;
@property (T@"CLPIndoorCMAttitude",&,N,V_cmAttitude) cmAttitude;
@property (TB,R,N) hasCmPedometer;
@property (T@"CLPIndoorCMPedometer",&,N,V_cmPedometer) cmPedometer;
@property (TB,R,N) hasLocation;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasMotionActivity;
@property (T@"CLPIndoorMotionActivity",&,N,V_motionActivity) motionActivity;
@property (TB,R,N) hasPressure;
@property (T@"CLPIndoorPressure",&,N,V_pressure) pressure;
@property (TB,R,N) hasWifiScan;
@property (T@"CLPIndoorWifiScan",&,N,V_wifiScan) wifiScan;
@property (TB,R,N) hasBundleId;
@property (T@"CLPBundleId",&,N,V_bundleId) bundleId;
@property (TB,R,N) hasVioEstimation;
@property (T@"CLPLOGENTRYVISIONVIOEstimation",&,N,V_vioEstimation) vioEstimation;
@property (TB,R,N) hasVlLocalizationResult;
@property (T@"CLPLOGENTRYVISIONVLLocalizationResult",&,N,V_vlLocalizationResult) vlLocalizationResult;
@property (TB,R,N) hasWorkoutUpdateMotionActivity;
@property (T@"CLPWorkoutUpdateMotionActivity",&,N,V_workoutUpdateMotionActivity) workoutUpdateMotionActivity;
@property (TB,R,N) hasInertialOdometry;
@property (T@"CLPInertialOdometry",&,N,V_inertialOdometry) inertialOdometry;
@property (TB,R,N) hasOutdoorUpdate;
@property (T@"CLPOutdoorUpdate",&,N,V_outdoorUpdate) outdoorUpdate;
@property (TB,R,N) hasCellConnectivity;
@property (T@"CLPCellConnectivityInfo",&,N,V_cellConnectivity) cellConnectivity;
@property (TB,R,N) hasPasskitEvent;
@property (T@"CLPPassKitEvent",&,N,V_passkitEvent) passkitEvent;
@property (TB,R,N) hasDaemonStatus;
@property (T@"CLPDaemonStatus",&,N,V_daemonStatus) daemonStatus;
@property (TB,R,N) hasProximityAccessoryMotion;
@property (T@"CLPProximityAccessoryMotionEvent",&,N,V_proximityAccessoryMotion) proximityAccessoryMotion;
@property (TB,R,N) hasProximityAccessoryMeta;
@property (T@"CLPProximityAccessoryMetaEvent",&,N,V_proximityAccessoryMeta) proximityAccessoryMeta;
@property (TB,R,N) hasProximityRangeMeasurement;
@property (T@"CLPProximityRangeMeasurementEvent",&,N,V_proximityRangeMeasurement) proximityRangeMeasurement;
@property (TB,R,N) hasProximityVIOPose;
@property (T@"CLPProximityVIOPoseEvent",&,N,V_proximityVIOPose) proximityVIOPose;
@property (TB,R,N) hasProximityGPSTile;
@property (T@"CLPProximityGPSTileEvent",&,N,V_proximityGPSTile) proximityGPSTile;
@property (TB,R,N) hasProximityPOIType;
@property (T@"CLPProximityPOITypeEvent",&,N,V_proximityPOIType) proximityPOIType;
@property (TB,R,N) hasProximityTriggerInfo;
@property (T@"CLPProximityTriggerInfoEvent",&,N,V_proximityTriggerInfo) proximityTriggerInfo;
@property (TB,R,N) hasProximityLastVisitLocation;
@property (T@"CLPProximityLocationEvent",&,N,V_proximityLastVisitLocation) proximityLastVisitLocation;
@property (TB,R,N) hasProximityScanLocation;
@property (T@"CLPProximityLocationEvent",&,N,V_proximityScanLocation) proximityScanLocation;
@property (TB,R,N) hasProximityReunionLocation;
@property (T@"CLPProximityLocationEvent",&,N,V_proximityReunionLocation) proximityReunionLocation;
@property (TB,R,N) hasProximityLOI;
@property (T@"CLPProximityLOIEvent",&,N,V_proximityLOI) proximityLOI;
@property (TB,R,N) hasProximityMonitoredDeviceCount;
@property (T@"CLPProximityMonitoredDeviceCountEvent",&,N,V_proximityMonitoredDeviceCount) proximityMonitoredDeviceCount;
@property (TB,R,N) hasProximityAlertRaised;
@property (T@"CLPProximityAlertRaisedEvent",&,N,V_proximityAlertRaised) proximityAlertRaised;
@property (TB,R,N) hasProximityVehicularState;
@property (T@"CLPProximityVehicularStateEvent",&,N,V_proximityVehicularState) proximityVehicularState;
```

## Instance methods

```
-[CLPIndoorEvent writeTo:];
-[CLPIndoorEvent typeAsString:];
-[CLPIndoorEvent hasBundleId];
-[CLPIndoorEvent setHasType:];
-[CLPIndoorEvent hasLocation];
-[CLPIndoorEvent location];
-[CLPIndoorEvent mergeFrom:];
-[CLPIndoorEvent setBundleId:];
-[CLPIndoorEvent hasType];
-[CLPIndoorEvent pressure];
-[CLPIndoorEvent StringAsType:];
-[CLPIndoorEvent setType:];
-[CLPIndoorEvent type];
-[CLPIndoorEvent setLocation:];
-[CLPIndoorEvent bundleId];
-[CLPIndoorEvent hash];
-[CLPIndoorEvent copyTo:];
-[CLPIndoorEvent description];
-[CLPIndoorEvent readFrom:];
-[CLPIndoorEvent copyWithZone:];
-[CLPIndoorEvent isEqual:];
-[CLPIndoorEvent motionActivity];
-[CLPIndoorEvent dictionaryRepresentation];
-[CLPIndoorEvent setPressure:];
-[CLPIndoorEvent setMotionActivity:];
-[CLPIndoorEvent hasMotionActivity];
-[CLPIndoorEvent hasPressure];
-[CLPIndoorEvent hasDaemonStatus];
-[CLPIndoorEvent hasPasskitEvent];
-[CLPIndoorEvent hasProximityLOI];
-[CLPIndoorEvent setWorkoutUpdateMotionActivity:];
-[CLPIndoorEvent setCmPedometer:];
-[CLPIndoorEvent cellConnectivity];
-[CLPIndoorEvent cmAttitude];
-[CLPIndoorEvent cmPedometer];
-[CLPIndoorEvent daemonStatus];
-[CLPIndoorEvent hasCellConnectivity];
-[CLPIndoorEvent hasCmAttitude];
-[CLPIndoorEvent hasCmPedometer];
-[CLPIndoorEvent hasInertialOdometry];
-[CLPIndoorEvent hasOutdoorUpdate];
-[CLPIndoorEvent hasProximityAccessoryMeta];
-[CLPIndoorEvent hasProximityAccessoryMotion];
-[CLPIndoorEvent hasProximityAlertRaised];
-[CLPIndoorEvent hasProximityGPSTile];
-[CLPIndoorEvent hasProximityLastVisitLocation];
-[CLPIndoorEvent hasProximityMonitoredDeviceCount];
-[CLPIndoorEvent hasProximityPOIType];
-[CLPIndoorEvent hasProximityRangeMeasurement];
-[CLPIndoorEvent hasProximityReunionLocation];
-[CLPIndoorEvent hasProximityScanLocation];
-[CLPIndoorEvent hasProximityTriggerInfo];
-[CLPIndoorEvent hasProximityVIOPose];
-[CLPIndoorEvent hasProximityVehicularState];
-[CLPIndoorEvent hasVioEstimation];
-[CLPIndoorEvent hasVlLocalizationResult];
-[CLPIndoorEvent hasWifiScan];
-[CLPIndoorEvent hasWorkoutUpdateMotionActivity];
-[CLPIndoorEvent inertialOdometry];
-[CLPIndoorEvent outdoorUpdate];
-[CLPIndoorEvent passkitEvent];
-[CLPIndoorEvent proximityAccessoryMeta];
-[CLPIndoorEvent proximityAccessoryMotion];
-[CLPIndoorEvent proximityAlertRaised];
-[CLPIndoorEvent proximityGPSTile];
-[CLPIndoorEvent proximityLOI];
-[CLPIndoorEvent proximityLastVisitLocation];
-[CLPIndoorEvent proximityMonitoredDeviceCount];
-[CLPIndoorEvent proximityPOIType];
-[CLPIndoorEvent proximityRangeMeasurement];
-[CLPIndoorEvent proximityReunionLocation];
-[CLPIndoorEvent proximityScanLocation];
-[CLPIndoorEvent proximityTriggerInfo];
-[CLPIndoorEvent proximityVIOPose];
-[CLPIndoorEvent proximityVehicularState];
-[CLPIndoorEvent setCellConnectivity:];
-[CLPIndoorEvent setCmAttitude:];
-[CLPIndoorEvent setDaemonStatus:];
-[CLPIndoorEvent setInertialOdometry:];
-[CLPIndoorEvent setOutdoorUpdate:];
-[CLPIndoorEvent setPasskitEvent:];
-[CLPIndoorEvent setProximityAccessoryMeta:];
-[CLPIndoorEvent setProximityAccessoryMotion:];
-[CLPIndoorEvent setProximityAlertRaised:];
-[CLPIndoorEvent setProximityGPSTile:];
-[CLPIndoorEvent setProximityLOI:];
-[CLPIndoorEvent setProximityLastVisitLocation:];
-[CLPIndoorEvent setProximityMonitoredDeviceCount:];
-[CLPIndoorEvent setProximityPOIType:];
-[CLPIndoorEvent setProximityRangeMeasurement:];
-[CLPIndoorEvent setProximityReunionLocation:];
-[CLPIndoorEvent setProximityScanLocation:];
-[CLPIndoorEvent setProximityTriggerInfo:];
-[CLPIndoorEvent setProximityVIOPose:];
-[CLPIndoorEvent setProximityVehicularState:];
-[CLPIndoorEvent setVioEstimation:];
-[CLPIndoorEvent setVlLocalizationResult:];
-[CLPIndoorEvent setWifiScan:];
-[CLPIndoorEvent vioEstimation];
-[CLPIndoorEvent vlLocalizationResult];
-[CLPIndoorEvent wifiScan];
-[CLPIndoorEvent workoutUpdateMotionActivity];
```
