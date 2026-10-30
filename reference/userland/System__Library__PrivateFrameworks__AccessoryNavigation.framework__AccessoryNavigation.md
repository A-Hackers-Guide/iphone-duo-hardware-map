# `/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 12 classes, 5 protocols, 210 methods, 43 properties

### Class pages

Every class and protocol, with its methods: [`ACCNavigationAccessory`](../objc/ACCNavigationAccessory_AccessoryNavigation.md), [`ACCNavigationAccessoryComponent`](../objc/ACCNavigationAccessoryComponent_AccessoryNavigation.md), [`ACCNavigationAccessoryObjectDetectionComponent`](../objc/ACCNavigationAccessoryObjectDetectionComponent_AccessoryNavigation.md), [`ACCNavigationLaneGuidanceInfo`](../objc/ACCNavigationLaneGuidanceInfo_AccessoryNavigation.md), [`ACCNavigationLaneGuidanceLaneInfo`](../objc/ACCNavigationLaneGuidanceLaneInfo_AccessoryNavigation.md), [`ACCNavigationManeuverUpdateInfo`](../objc/ACCNavigationManeuverUpdateInfo_AccessoryNavigation.md), [`ACCNavigationProvider`](../objc/ACCNavigationProvider_AccessoryNavigation.md), [`ACCNavigationRoadObjectDetectionInfo`](../objc/ACCNavigationRoadObjectDetectionInfo_AccessoryNavigation.md), [`ACCNavigationRoadObjectRoadLaneInfo`](../objc/ACCNavigationRoadObjectRoadLaneInfo_AccessoryNavigation.md), [`ACCNavigationRoadObjectRoadObjectInfo`](../objc/ACCNavigationRoadObjectRoadObjectInfo_AccessoryNavigation.md), [`ACCNavigationRoadObjectRoadSignInfo`](../objc/ACCNavigationRoadObjectRoadSignInfo_AccessoryNavigation.md), [`ACCNavigationRouteGuidanceUpdateInfo`](../objc/ACCNavigationRouteGuidanceUpdateInfo_AccessoryNavigation.md), [`ACCNavigationXPCClientProtocol`](../objc/ACCNavigationXPCClientProtocol_AccessoryNavigation.protocol.md), [`ACCNavigationXPCServerProtocol`](../objc/ACCNavigationXPCServerProtocol_AccessoryNavigation.protocol.md), [`NSCoding`](../objc/NSCoding_AccessoryNavigation.protocol.md), [`NSObject`](../objc/NSObject_AccessoryNavigation.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_AccessoryNavigation.protocol.md)

### Classes

`ACCNavigationAccessory`, `ACCNavigationAccessoryComponent`, `ACCNavigationAccessoryObjectDetectionComponent`, `ACCNavigationLaneGuidanceInfo`, `ACCNavigationLaneGuidanceLaneInfo`, `ACCNavigationManeuverUpdateInfo`, `ACCNavigationProvider`, `ACCNavigationRoadObjectDetectionInfo`, `ACCNavigationRoadObjectRoadLaneInfo`, `ACCNavigationRoadObjectRoadObjectInfo`, `ACCNavigationRoadObjectRoadSignInfo`, `ACCNavigationRouteGuidanceUpdateInfo`

### Protocols

`ACCNavigationXPCClientProtocol`, `ACCNavigationXPCServerProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSMutableDictionary",&,V_componentListInternal) componentListInternal;
@property (T@"NSMutableDictionary",&,V_objectDetectionComponentListInternal) objectDetectionComponentListInternal;
@property (T@"ACCNavigationProvider",R,W,N,V_provider) provider;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (T@"NSDictionary",R) componentList;
@property (TQ,N,V_identifier) identifier;
@property (T@"NSString",&,V_name) name;
@property (TB,N,V_isEnabled) isEnabled;
@property (TQ,N,V_maxLength_CurrentRoadName) maxLength_CurrentRoadName;
@property (TQ,N,V_maxLength_DestinationRoadName) maxLength_DestinationRoadName;
@property (TQ,N,V_maxLength_PostManeuverRoadName) maxLength_PostManeuverRoadName;
@property (TQ,N,V_maxLength_ManeuverDescription) maxLength_ManeuverDescription;
@property (TQ,N,V_maxLength_LaneGuidanceDescription) maxLength_LaneGuidanceDescription;
@property (TB,N,V_requestSourceName) requestSourceName;
@property (TB,N,V_requestSourceSupportsRouteGuidance) requestSourceSupportsRouteGuidance;
@property (TB,N,V_supportsExitInfo) supportsExitInfo;
@property (TB,N,V_supportsLaneGuidance) supportsLaneGuidance;
@property (TB,N,V_supportsTimeZoneOffset) supportsTimeZoneOffset;
@property (TB,N,V_supportsPreconditioning) supportsPreconditioning;
@property (TQ,N,V_maxCapacity_GuidanceManeuver) maxCapacity_GuidanceManeuver;
@property (TQ,N,V_maxCapacity_LaneGuidance) maxCapacity_LaneGuidance;
@property (TQ,V_identifier) identifier;
@property (T@"NSString",&,V_name) name;
@property (TB,V_isEnabled) isEnabled;
@property (T@"NSArray",&,V_supportedTypes) supportedTypes;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCNavigationXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"NSMutableArray",&,N,V_delegates) delegates;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
@property (T@"NSMutableDictionary",&,V_infoDict) infoDict;
```

## Strings (211)

```
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList: %@ updateInfo: %@, accessory=%@, accessory does not exist!
[#Navigation] ERROR: Unknown RoadObjectDetection:RoadLane InfoType %d
%s cannot get server state (%d, %s)
[#Navigation] accessoryNavigationAttached: %@ componentList: %@, accessory=%@
Created log object %s: %s
[#Navigation] ACCNavigationProvider init, _providerUID=%@
[#Navigation] Connecting to XPC server...
[#Navigation] shouldStayConnected: %d
[#Navigation] accessoryNavigationDetached: accessory %@, accessory=%@, no delgate found conforming to protocol
[#Navigation] routeGuidance: %@ maneuverUpdateInfo: %@ componentIdList: %@
[#Navigation] objectDetection: %@ startComponentIdList: %@ objectTypes: %@
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
[#Navigation] ERROR: Unknown ManeuverInfoUpdate InfoType %d
[#Navigation] ERROR: Unknown LaneGuidanceInfoUpdate:LaneInfo InfoType %d
[#Navigation] ERROR: Unknown RoadObjectDetectionInfo infoType %d
[#Navigation] accessoryNavigationStopRouteGuidance: accessory %@, accessory=%@ componentIdList=%@
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList: %@ updateInfo: %@, accessory=%@, no component is enabled!
[#Navigation] routeGuidance: %@ laneGuidanceInfo: %@ componentIdList: %@
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#Navigation] NavigationAccessory objectDetectionComponentIdListIsEnabled: accessoryUID %@, select components, component %@
[#Navigation] ERROR: Unknown RouteGuidnaceUpdate InfoType %d
[#Navigation] detachAllAccessories: allAccessories=%@
[#Navigation] accessoryNavigationDetached: accessory %@, accessory=%@, delegate=%@, notify navigation(object detection) accessory detached
[#Navigation] accessoryNavigationDetached: accessory %@ (%@) does not exist!
[#Navigation] accessoryNavigationStartRouteGuidance: accessory %@, accessory=%@ componentIdList=%@
[#Navigation] accessoryNavigationStopRouteGuidance: accessory %@, accessory=%@ componentIdList=%@, file: %s
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#Navigation] ACCNavigationProvider connectToServer, _providerUID=%@, IS accessoryServer_isServerAvailable()
[#Navigation] accessoryNavigationAttached: accessory %@, accessory=%@ componentList=%@, delegate=%@, notify navigation(object detection) accessory attached
[#Navigation] accessoryNavigationDetached: accessory %@, accessory=%@
Register AvailabilityChangedHandler (%d, %s)
[#Navigation] routeGuidance: %@, _remoteObject nil, _providerUID=%@
[#Navigation] Navigation objectDetectionComponentIdListIsEnabled: accessoryUID %@, componentIDList %@, isEnabled=%d
[#Navigation] XPC connection error!
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
[#Navigation] XPC connection interrupted!
[#Navigation] accessoryNavigationAttached: accessory %@, accessory=%@ componentList=%@, no delegate found conforming to protocol: ACCNavigationProviderObjectDetectionProtocol
[#Navigation] objectDetection: %@, _remoteObject nil, _providerUID=%@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
[#Navigation] ACCNavigationProvider connectToServer, _providerUID=%@
[#Navigation] delegatesImplementing: selector=%s, result delegateList=%@
[#Navigation] accessoryNavigationStartRouteGuidance: accessory %@, accessory=%@ componentList=%@, no delgate found conforming to protocol
[#Navigation] ERROR: Unknown RoadObjectDetection:RoadObject InfoType %d
Unregister AvailabilityChangedHandler (%d, %s)
[#Navigation] %@
[#Navigation] accessoryNavigationStopRouteGuidance: accessory %@, accessory=%@ componentList=%@, delegate=%@
[#Navigation] routeGuidance: %@ updateInfo: %@ componentIdList: %@
Created %d log object(s)!
[#Navigation] XPC connection invalidated!
[#Navigation] Getting remote object...
[#Navigation] Call initConnection to remoteObject=%@
[#Navigation] accessoryNavigationDetached: %@, accessory=%@
[#Navigation] accessoryNavigationDetached: accessory %@, accessory=%@, delegate=%@, notify navigation accessory detached
[#Navigation] accessoryNavigationStartRouteGuidance: accessory %@, accessory=%@ componentList=%@, delegate=%@, options=%llxh
[#Navigation] ERROR: Unknown RouteGuidnaceUpdate CharginStation InfoType %d
[#Navigation] Trying to connect to server...
[#Navigation] ACCNavigationProvider connectToServer, _providerUID=%@, NOT accessoryServer_isServerAvailable()
[#Navigation] accessoryNavigationAttached: accessory %@, accessory=%@ componentList=%@, delegate=%@, notify navigation(route guidance) accessory attached
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
%s did not register for notification (%d, %s), token (%d)
[#Navigation] Server availability changed! State: %d
[#Navigation] objectDetection: %@ stopComponentIdList: %@
[#Navigation] exiting accessoryNavigationStartRouteGuidance: accessory %@, accessory=%@ componentIdList=%@, file: %s
[#Navigation] accessoryNavigationStopRouteGuidance: accessory %@ (%@) does not exist! file: %s
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList: %@ updateInfo: %@
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList: %@ updateInfo: %@, componentList %@, delegateList %@
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList %@, accessory %@, delegate %@, objectDetectionInfo %@
[#Navigation] NavigationAccessory objectDetectionComponentIdListIsEnabled: accessoryUID %@, all components, component %@
[#Navigation] accessoryNavigationAttached: accessory %@, accessory=%@ componentList=%@, no delegate found conforming to protocol: ACCNavigationProviderProtocol
[#Navigation] accessoryNavigationAttached: accessory %@ (%@) already exists! file: %s
[#Navigation] exiting accessoryNavigationAttached: accessory %@, _accessories=%@, accessory.componentListInternal=%@, file: %s
[#Navigation] accessoryNavigationObjectDetection: %@ componentIdList: %@ updateInfo: %@, accessory=%@, no delgate found conforming to protocol
Failed to create os_log_t object %s: %s!
[#Navigation] ERROR: Unknown LaneGuidanceInfoUpdate InfoType %d
[#Navigation] ERROR: Unknown RoadObjectDetection:RoadSign InfoType %d
%s (%d)
%s (%d, %s)
[#Navigation] accessoryNavigationStopRouteGuidance: accessory %@, accessory=%@ componentList=%@, no delgate found conforming to protocol
[#Navigation] NavigationAccessory objectDetectionComponentListForIdList: accessoryUID %@, componentIdList %@, componentList %@
[#Navigation] exiting accessoryNavigationDetached: accessory %@, _accessories=%@, file:%s
[#Navigation] accessoryNavigationStartRouteGuidance: accessory %@ (%@) does not exist! file: %s
_SetupAvailabilityChangedHandlerForServiceEntry
ACCNav_DispComp_ComponentID
ACCNav_RGUpdate_ChargingStationInfo_Power
ACCNav_RODUpdate_RoadSign_Type
ACCNav_LGIUpdate_AccessoryID
ACCNav_RODComp_Name
ACCNav_RODUpdate_RoadObject_LateralAccel
accessoryServer_isServerAvailableForServiceEntry
General
com.apple.accessories.signposts
ACCNav_RODUpdate_RoadLane_TypeLeft
v24@?0@\"ACCNavigationAccessoryComponent\"8^B16
ACCNav_MIUpdate_JunctionType
ACCNav_RODUpdate_EgoYawRate
ACCNav_RODUpdate_RoadSign_LateralOffset
ACCNav_RODUpdate_RoadObject_LateralOffset
%@, 
]
ACCNav_DispComp_Name
ACCNav_MIUpdate_JunctionElementAngle
ACCNav_RODUpdate_RoadSign_ID
<ACCNavigationRoadObjectRoadLaneInfo: ID %@, state %@, type[left %@, right %@], color[left %@, right %@], width %@, curvature[center %@, left %@, right %@]>
ACCNav_RGUpdate_CurrentRoadName
ACCNav_RGUpdate_EstimatedTimeOfArrival
ACCNav_RGUpdate_StopType
<ACCNavigationRoadObjectRoadObjectInfo: ID %@, state %@, type %@, isMoving %@, lateral[offset %@, speed %@, accel %@] forward[offset %@, speed %@, accel %@]>
ACCNav_RODUpdate_RoadLane_CurvatureLeft
com.apple.accessories.navigation
Connection
ACCNav_DispComp_MaxCurRoadNameLength
ACCNav_DispComp_MaxManeuverDescriptionLength
ACCNav_RODUpdate_RoadLane_TypeRight
\"
ACCNav_RGUpdate_DistanceRemainingDisplayUnits
ACCNav_LGIUpdate_LaneInfo
ACCNav_RODUpdate_RoadObject_ForwardAccel
ACCNav_RGUpdate_ChargingStationInfo_Voltage
ACCNav_MIUpdate_DistanceBetweenManeuver
ACCNav_MIUpdate_DistanceBetweenManeuverDisplayUnits
ACCNav_RGUpdate_DestinationName
ACCNav_RGUpdate_ChargingStationInfoList
ACCNav_MIUpdate_ExitInfo
ACCNav_RODUpdate_EgoSpeed
ACCNav_RODUpdate_RoadObject_ForwardOffset
v12@?0B8
null
ACCNav_RGUpdate_LaneGuidanceTotalCount
ACCNav_RGUpdate_SourceName
ACCNav_RGUpdate_LaneGuidanceShowing
ACCNav_MIUpdate_AfterManeuverRoadName
ACCNav_LGIUpdate_LaneInfo_Angle
com.apple.accessories.frameworks
ACCNav_RGUpdate_DepartureBatteryLevel
ACCNav_MIUpdate_ManeuverDescription
ACCNav_MIUpdate_DrivingSide
v8@?0
<ACCNavigationAccessoryComponent - name: %@, identifier: %d, isEnabled: %d>, max_CRN: %d, max_DRN: %d, max_PMRN: %d, max_GM: %d, max_MD: %d, max_LD: %d, max_LG: %d, reqSrcName: %d reqSrcSupportRG: %d, exitInfo: %d, laneGuidance: %d, timeZon
ACCNav_LGIUpdate_LaneInfo_Status
ACCNav_RODUpdate_Timestamp
<ACCNavigationRoadObjectDetectionInfo: componentIDs %@, timestamp %@, egoSpeed %@, egoYawRate %@, roadSign count %lu, roadLane count %lu, roadObject count %lu>
ACCNav_DispComp_MaxMGuidanceManeuverCapacity
ACCNav_RGUpdate_DistanceRemaining
ACCNav_RGUpdate_SourceSupportsRouteGuidance
ACCNav_RGUpdate_DestinationTimeZoneOffsetMinutes
ACCNav_MIUpdate_LinkedLaneGuidanceInfo
ACCNav_RODUpdate_RoadObject
ACCNav_RODUpdate_RoadObject_ID
ACCNav_DispComp_MaxDestinationNameLength
ACCNav_RGUpdate_ArrivalBatteryLevel
ACCNav_RGUpdate_FinalWaypointBatteryLevel
ACCNav_MIUpdate_DistanceBetweenManeuverDisplayString
ACCNav_RODUpdate_RoadObject_IsMoving
com.apple.accessories.navigation.availability-changed
ACCNav_RGUpdate_RouteGuidanceState
ACCNav_LGIUpdate_LaneGuidanceIndex
ACCNav_LGIUpdate_InstructionText
ACCNav_RODUpdate_RoadSign_State
ACCNav_RODUpdate_RoadSign_Value
ACCNav_RODUpdate_RoadObject_LateralSpeed
ACCNav_DispComp_MaxLaneGuidanceDescriptionLength
ACCNav_DispComp_SourceName
ACCNav_RGUpdate_RouteGuidanceBeingShownInApp
ACCNav_MIUpdate_JunctionElementExitAngle
ACCNav_RODUpdate_RoadLane_ColorRight
ACCNav_RODUpdate_RoadSign
ACCNav_RODUpdate_RoadLane_ID
ACCNav_RODUpdate_RoadObject_Type
/Library/Caches/com.apple.xbs/76B1CF77-B43E-4354-A598-AC1F85B56663/TemporaryDirectory.JL1DQp/Sources/CoreAccessories/Apple/Accessory_Frameworks/AccessoryNavigation/ACCNavigationProvider.m
ACCNav_RGUpdate_RouteGuidanceManeuverCurrentList
ACCNav_LGIUpdate_LaneInfo_AngleHighlight
<ACCNavigationAccessoryObjectDetectionComponent - name: %@, identifier: %d, isEnabled: %d>, supportedTypes: %@>
Endpoint
ACCNav_RGUpdate_RouteGuidanceManeuverCount
ACCNav_MIUpdate_Index
ACCNav_RODComp_ComponentID
ACCNav_RODComp_SupportedTypes
ACCNav_DispComp_MaxLaneGuidanceStorageCapacity
ACCNav_MIUpdate_AccessoryID
ACCNav_RODUpdate_ID
Transport
ACCNav_RGUpdate_AccessoryID
ACCNav_RGUpdate_DistanceRemainingToNextManeuver
v12@?0i8
v16@?0@\"NSError\"8
<Undefined>
ACCNav_RODUpdate_RoadSign_ForwardOffset
ACCNav_RODUpdate_RoadLane_State
ACCNav_RODUpdate_RoadLane_CurvatureCenter
<ACCNavigationRoadObjectRoadSignInfo: ID %@, state %@, type %@, value '%@', lateralOffset %@, forwardOffset %@>
!
ACCNav_RGUpdate_TimeRemainingToDestination
ACCNav_RGUpdate_LaneGuidanceCurrentIndex
ACCNav_RODUpdate_RoadLane
ACCNav_RGUpdate_ChargingStationInfo_ConnectorType
ACCNav_DispComp_SourceSupportsRouteGuidance
ACCNav_RGUpdate_DistanceRemainingDisplayString
ACCNav_MIUpdate_ManeuverType
ACCNav_RODUpdate_RoadObject_ForwardSpeed
ACCNav_RGUpdate_DistanceRemainingToNextManeuverDisplayString
ACCNav_RODUpdate_RoadLane_ColorLeft
ACCNav_RODUpdate_RoadLane_Width
ACCNav_RODUpdate_RoadObject_State
ACCNav_RGUpdate_DistanceRemainingToNextManeuverDisplayUnits
ACCNav_RODUpdate_RoadLane_CurvatureRight
ACCNav_RGUpdate_ManeuverState
[ 
%@ 
<ACCNavigationAccessory - %@ components: count=%lu objectDetectionComponents: count=%lu>
ACCNav_DispComp_MaxAfterManeuverRoadNameLength
ACCNav_LGIUpdate_LaneInfo_Index
```
