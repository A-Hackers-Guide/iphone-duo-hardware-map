# `PLBatteryUIResponderService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- Protocols: `PLBatteryUIResponseProtocol`
- 15 instance variables, 19 properties, 53 instance methods, 2 class methods

## Instance variables

```
B _skipPlistWrite;
B _shouldUseMidnightQueryRange;
@"PLBatteryUIResponderService" _responderService;
@"NSMutableArray" _dependencies;
@"NSMutableDictionary" _responseCache;
@"NSMutableDictionary" _sharedUtilityCache;
@"NSString" _requestingService;
@"NSString" _plistCopyDestination;
@"NSMutableDictionary" _resultDictionary;
@"PLXPCResponderOperatorComposition" _queryResponder;
@"NSDictionary" _configuration;
@"NSMutableDictionary" _requestedObjects;
@"NSMutableArray" _executionChain;
@"NSOperationQueue" _operationQueue;
@"NSMutableArray" _orderOfExecution;
```

## Properties

```
@property (T@"NSString",&,V_requestingService) requestingService;
@property (T@"NSString",&,V_plistCopyDestination) plistCopyDestination;
@property (TB,V_skipPlistWrite) skipPlistWrite;
@property (T@"NSMutableDictionary",&,V_resultDictionary) resultDictionary;
@property (T@"PLXPCResponderOperatorComposition",&,V_queryResponder) queryResponder;
@property (T@"NSDictionary",&,V_configuration) configuration;
@property (T@"NSMutableDictionary",&,V_requestedObjects) requestedObjects;
@property (T@"NSMutableArray",&,V_executionChain) executionChain;
@property (T@"NSOperationQueue",&,V_operationQueue) operationQueue;
@property (T@"NSMutableArray",&,V_orderOfExecution) orderOfExecution;
@property (TB,V_shouldUseMidnightQueryRange) shouldUseMidnightQueryRange;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (T@"NSMutableArray",&,V_dependencies) dependencies;
@property (T@"NSMutableDictionary",&,V_responseCache) responseCache;
@property (T@"NSMutableDictionary",&,V_sharedUtilityCache) sharedUtilityCache;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLBatteryUIResponderService load];
+[PLBatteryUIResponderService shouldDisableQueryResponder];
```

## Instance methods

```
-[PLBatteryUIResponderService cleanup];
-[PLBatteryUIResponderService configure:];
-[PLBatteryUIResponderService dependencies];
-[PLBatteryUIResponderService initOperatorDependancies];
-[PLBatteryUIResponderService setConfiguration:];
-[PLBatteryUIResponderService coalesce];
-[PLBatteryUIResponderService configuration];
-[PLBatteryUIResponderService result];
-[PLBatteryUIResponderService orderOfExecution];
-[PLBatteryUIResponderService operationQueue];
-[PLBatteryUIResponderService setDependencies:];
-[PLBatteryUIResponderService setOperationQueue:];
-[PLBatteryUIResponderService run];
-[PLBatteryUIResponderService resultDictionary];
-[PLBatteryUIResponderService setShouldUseMidnightQueryRange:];
-[PLBatteryUIResponderService constructResponseObjectFromType:];
-[PLBatteryUIResponderService convertResponseToLegacyFormat:];
-[PLBatteryUIResponderService createCoalescedBreakdownWithResponse:];
-[PLBatteryUIResponderService demoMode];
-[PLBatteryUIResponderService demoPath];
-[PLBatteryUIResponderService dynamicRangeKeyForLength:bucketSize:];
-[PLBatteryUIResponderService endOfDayWithNow:];
-[PLBatteryUIResponderService endOfHourWithNow:];
-[PLBatteryUIResponderService executionChain];
-[PLBatteryUIResponderService getBreakdownForLength:fromCachedLength:forBucketSize:];
-[PLBatteryUIResponderService getDynamicEndUISOCDrainByBuckets:fromCachedLength:forBucketSize:];
-[PLBatteryUIResponderService getUISOCDrainByBuckets:fromCachedLength:forBucketSize:];
-[PLBatteryUIResponderService getUISOCDrainByBuckets:fromCachedLength:forBucketSize:isDynamicSource:];
-[PLBatteryUIResponderService isOfTypeBreakdownForResponseType:];
-[PLBatteryUIResponderService linkDependencies];
-[PLBatteryUIResponderService plistCopyDestination];
-[PLBatteryUIResponderService possibleRequests];
-[PLBatteryUIResponderService prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:];
-[PLBatteryUIResponderService queryResponder];
-[PLBatteryUIResponderService rangeKeyForLength:bucketSize:];
-[PLBatteryUIResponderService requestedObjects];
-[PLBatteryUIResponderService requestingService];
-[PLBatteryUIResponderService responderService];
-[PLBatteryUIResponderService responseCache];
-[PLBatteryUIResponderService setExecutionChain:];
-[PLBatteryUIResponderService setOrderOfExecution:];
-[PLBatteryUIResponderService setPlistCopyDestination:];
-[PLBatteryUIResponderService setQueryResponder:];
-[PLBatteryUIResponderService setRequestedObjects:];
-[PLBatteryUIResponderService setRequestingService:];
-[PLBatteryUIResponderService setResponderService:];
-[PLBatteryUIResponderService setResponseCache:];
-[PLBatteryUIResponderService setResultDictionary:];
-[PLBatteryUIResponderService setSharedUtilityCache:];
-[PLBatteryUIResponderService setSkipPlistWrite:];
-[PLBatteryUIResponderService sharedUtilityCache];
-[PLBatteryUIResponderService shouldUseMidnightQueryRange];
-[PLBatteryUIResponderService skipPlistWrite];
```
