# `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

iOS 27.2 dyld shared cache image. Version `231.40.1.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 13 classes, 7 protocols, 176 methods, 56 properties

### Class pages

Every class and protocol, with its methods: [`BIAccessoryEstimateInfo`](../objc/BIAccessoryEstimateInfo_BatteryIntelligence.md), [`BIBatteryAnalysisAccessoryEstimateContainer`](../objc/BIBatteryAnalysisAccessoryEstimateContainer_BatteryIntelligence.md), [`BIBatteryAnalysisClient`](../objc/BIBatteryAnalysisClient_BatteryIntelligence.md), [`BIBatteryAnalysisContainer`](../objc/BIBatteryAnalysisContainer_BatteryIntelligence.md), [`BIBatteryAnalysisManagerClient`](../objc/BIBatteryAnalysisManagerClient_BatteryIntelligence.md), [`BIBatteryAnalysisManagerProtocol`](../objc/BIBatteryAnalysisManagerProtocol_BatteryIntelligence.protocol.md), [`BIBatteryAnalysisOutput`](../objc/BIBatteryAnalysisOutput_BatteryIntelligence.md), [`BIBatteryAnalysisProtocol`](../objc/BIBatteryAnalysisProtocol_BatteryIntelligence.protocol.md), [`BIBatteryAnalysisSharedResources`](../objc/BIBatteryAnalysisSharedResources_BatteryIntelligence.md), [`BIBatteryAnalysisTargetDetails`](../objc/BIBatteryAnalysisTargetDetails_BatteryIntelligence.md), [`BIChargeTimeEstimatorClient`](../objc/BIChargeTimeEstimatorClient_BatteryIntelligence.md), [`BIChargeTimeEstimatorOutput`](../objc/BIChargeTimeEstimatorOutput_BatteryIntelligence.md), [`BIConnectedAccessoryInfo`](../objc/BIConnectedAccessoryInfo_BatteryIntelligence.md), [`BIThermalPredictionClient`](../objc/BIThermalPredictionClient_BatteryIntelligence.md), [`BIThermalPredictionClientProtocol`](../objc/BIThermalPredictionClientProtocol_BatteryIntelligence.protocol.md), [`BIThermalPredictionOutput`](../objc/BIThermalPredictionOutput_BatteryIntelligence.md), [`BIThermalPredictionProtocol`](../objc/BIThermalPredictionProtocol_BatteryIntelligence.protocol.md), [`NSCoding`](../objc/NSCoding_BatteryIntelligence.protocol.md), [`NSObject`](../objc/NSObject_BatteryIntelligence.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_BatteryIntelligence.protocol.md)

### Classes

`BIAccessoryEstimateInfo`, `BIBatteryAnalysisAccessoryEstimateContainer`, `BIBatteryAnalysisClient`, `BIBatteryAnalysisContainer`, `BIBatteryAnalysisManagerClient`, `BIBatteryAnalysisOutput`, `BIBatteryAnalysisSharedResources`, `BIBatteryAnalysisTargetDetails`, `BIChargeTimeEstimatorClient`, `BIChargeTimeEstimatorOutput`, `BIConnectedAccessoryInfo`, `BIThermalPredictionClient`, `BIThermalPredictionOutput`

### Protocols

`BIBatteryAnalysisManagerProtocol`, `BIBatteryAnalysisProtocol`, `BIThermalPredictionClientProtocol`, `BIThermalPredictionProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",&,N,V_nsuuid) nsuuid;
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (T@"BIBatteryAnalysisOutput",&,N,V_estimate) estimate;
@property (T@"BIAccessoryEstimateInfo",&,N,V_estimateInfo) estimateInfo;
@property (Tq,N,V_lastUpdatedMonotonicTime) lastUpdatedMonotonicTime;
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSSet",&,N,V_targets) targets;
@property (T@"NSMutableDictionary",&,N,V_targetOutputs) targetOutputs;
@property (T@"NSMutableDictionary",&,N,V_accessoryEstimates) accessoryEstimates;
@property (T@"NSError",&,N,V_accessoryEstimatesFetchError) accessoryEstimatesFetchError;
@property (TB,N,V_trackAccessoryEstimates) trackAccessoryEstimates;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSMutableSet",&,N,V_notificationTokens) notificationTokens;
@property (T@"<BIBatteryAnalysisDelegate>",W,N,V_delegate) delegate;
@property (T@"BIBatteryAnalysisOutput",&,N,V_estimateObj) estimateObj;
@property (Tq,N,V_lastUpdatedMonotonicTime) lastUpdatedMonotonicTime;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (Td,N,V_estimate) estimate;
@property (Tq,N,V_socAtEstimateTime) socAtEstimateTime;
@property (Tq,N,V_endSOC) endSOC;
@property (Td,N,V_confidenceScore) confidenceScore;
@property (Tq,N,V_additionalInformation) additionalInformation;
@property (T@"NSString",&,N,V_formattedEstimate) formattedEstimate;
@property (TB,N,V_isFirstEstimate) isFirstEstimate;
@property (TB,N,V_isEstimateOverridden) isEstimateOverridden;
@property (T@"NSString",&,N,V_friendlyName) friendlyName;
@property (T@"NSString",&,N,V_notificationName) notificationName;
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (Td,N,V_estimate) estimate;
@property (Tq,N,V_endSOC) endSOC;
@property (Td,N,V_confidenceScore) confidenceScore;
@property (Tq,N,V_additionalInformation) additionalInformation;
@property (T@"NSString",C,N,V_nsuuid) nsuuid;
@property (T@"NSNumber",&,N,V_currentCapacity) currentCapacity;
@property (T@"NSString",C,N,V_friendlyName) friendlyName;
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"BIThermalPredictionOutput",&,V_cachedPrediction) cachedPrediction;
@property (T@"NSError",&,V_cachedError) cachedError;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (Ti,N,V_reconnectToken) reconnectToken;
@property (T@"<BIThermalPredictionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_willHitTLC) willHitTLC;
@property (Td,N,V_confidenceScore) confidenceScore;
```

## Strings (115)

```
com.apple.BatteryIntelligence.BatteryAnalysis
isEstimateOverridden
YES
lastUpdatedMonotonicTime
additionalInformation
a
batteryintelligence
Accessory Identifier
Current Capacity
CHARGE_TIME
TTL
com.apple.batteryintelligence.thermalpredictionclient
XPC connection invalidated
BIBatteryAnalysisClient
BIBatteryAnalysis-Localizable
estimate
<BatteryAnalysisOutput: estimate: %.02f, socAtEstimateTime: %ld, endSOC: %ld, confidenceScore: %.02f, additionalInformation: %ld, formattedEstimate: %@, isFirstEstimate: %@, isEstimateOverridden: %@>
<BIAccessoryEstimateInfo: nsuuid: %@, deviceName: %@, estimate: %@>
BIThermalPredictionClient
endSOC
formattedEstimate
fr
<ChargeTimeEstimatorOutput: estimate: %.02f, endSOC: %ld, confidenceScore: %.02f, additionalInformation: %ld>
com.apple.batteryintelligenced.battery-analysis-client-accessory-estimates
com.apple.batteryintelligenced.batteryanalysisttlupdated
TT80
v20@?0B8@\"NSError\"12
willHitTLC
<BIThermalPredictionOutput: willHitTLC=%d, confidence=%.2f>
v12@?0i8
CHARGE_TIME_GREATER_THAN_THRESHOLD
com.apple.batteryintelligenced.battery-analysis-client-accessory-estimate-update
com.apple.batteryintelligenced.batteryanalysismanager
confidenceScore
v16@?0@\"NSError\"8
nsuuid
<BIBatteryAnalysisContainer: estimate: %@, lastUpdatedMonotonicTime: %ld, Error: %@>
deviceName
com.apple.batteryintelligence.batteryanalysisclient
v24@?0@\"BIBatteryAnalysisOutput\"8@\"NSError\"16
Unknown Device
TimeTo80Notification
CHARGE_TIME_LESS_THAN_THRESHOLD
SLOW_CHARGER
(
v24@?0@\"BIThermalPredictionOutput\"8@\"NSError\"16
%
socAtEstimateTime
BIFrameworkUtilities
com.apple.batteryintelligenced.battery-analysis-client-estimate-for-target
q
v8@?0
Name
v24@?0@\"NSArray\"8@\"NSError\"16
<BIBatteryAnalysisAccessoryEstimateContainer: estimateInfo: %@, lastUpdatedMonotonicTime: %lld ns>
com.apple.batteryintelligence.thermalprediction
isFirstEstimate
NO
Type
com.apple.batteryintelligenced.battery-analysis-client-estimate-update
estimateObj
com.apple.batteryintelligenced.batteryanalysistt80updated
com.apple.batteryintelligence.thermal.reconnect
com.apple.BatteryIntelligenceFramework
BIChargeTimeEstimatorClient
com.apple.batteryintelligenced.batteryanalysisaccessoryestimateupdated
BIBatteryAnalysisManagerClient
com.apple.batteryintelligenced.thermalprediction
Accessory Source
com.apple.batteryintelligenced.batteryanalysis
error
Returning a dummy output: %@
Failed to get power sources: status=%d
Passing the updated estimate to the delegate UpdateEstimateFor method for target %@
Failed to register to get notification for %@ target with status 0x%x
Failed to initialize BIBatteryAnalysisManagerClient.
getConnectedAccessoriesInfo: Returning %lu accessories
BIBatteryAnalysisClient init
Failed to initialize BIBatteryAnalysisClient.
Accessory estimates updated - %lu devices
Wait time exceeded for target %@
Failed to connect to service
Connection interrupted
Re-establishing connection after interruption
XPC error: %@
Established connection to batteryintelligenced.
Connection to service invalidated.
Error executing %@: %@
Accessory estimate tracking not enabled. Initialize with trackAccessoryEstimates:YES
Failed to get power sources list
Skipping accessory - missing required fields
Invalid targets are being used for registration: %@. Valid targets are: %@
Estimate updated for %@ target - output: %@, additional information: %@
Wait time exceeded for accessory estimates
Accessory estimate: %@, additionalInformation: %ld
BIBatteryAnalysisManagerClient init
Failed to connect to batteryintelligenced.
Invalid target: %@, Valid targets are: %@
Client output for accessory estimates - %lu devices
Connection invalidated
Registration error: %@
Connection to service interrupted.
Notification received for accessory estimate update
Failed to register for accessory estimate notifications with status 0x%x
Server error %@
target %@ was not registered at init
Client output for %@ - additional information: %@, output: %@
Notification received %@
Called with nil/empty nsuuid
Accessory estimate for nsuuid %@ is stale (%.0f seconds old, threshold: %.0f seconds)
Error cancelling notification token: %u, result: %d.
Accessory '%@' not found
Passing updated accessory estimates to delegate method
Accessory estimates fetch error: %@
Successfully cancelled notification token: %u.
```
