# `_ANEClient`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 8 properties, 53 instance methods, 4 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"_ANEDaemonConnection" _fastConn;
B _allowRestrictedAccess;
B _isRootDaemon;
@"_ANEDaemonConnection" _conn;
@"NSArray" _priorityQ;
@"_ANEVirtualClient" _virtualClient;
@"NSMutableDictionary" _connectionsUsedForLoadingModels;
@"NSMutableDictionary" _connections;
```

## Properties

```
@property (T@"_ANEDaemonConnection",R,N,V_conn) conn;
@property (TB,R,N,V_allowRestrictedAccess) allowRestrictedAccess;
@property (T@"_ANEDaemonConnection",R,N) fastConn;
@property (T@"NSArray",R,N,V_priorityQ) priorityQ;
@property (T@"_ANEVirtualClient",R,N,V_virtualClient) virtualClient;
@property (T@"NSMutableDictionary",R,N,V_connectionsUsedForLoadingModels) connectionsUsedForLoadingModels;
@property (T@"NSMutableDictionary",R,N,V_connections) connections;
@property (TB,R,N,V_isRootDaemon) isRootDaemon;
```

## Class methods

```
+[_ANEClient sharedConnection];
+[_ANEClient initialize];
+[_ANEClient new];
+[_ANEClient sharedPrivateConnection];
```

## Instance methods

```
-[_ANEClient allowRestrictedAccess];
-[_ANEClient compileModel:options:qos:error:];
-[_ANEClient isVirtualClient];
-[_ANEClient doUnloadModel:options:qos:error:];
-[_ANEClient evaluateRealTimeWithModel:options:request:error:];
-[_ANEClient isRootDaemon];
-[_ANEClient connections];
-[_ANEClient initWithRestrictedAccessAllowed:];
-[_ANEClient init];
-[_ANEClient updateSourcePathForModelTrackedByHash:to:error:];
-[_ANEClient dealloc];
-[_ANEClient priorityQ];
-[_ANEClient updateCachedModelLocationForModelTrackedByHash:toAppGroup:error:];
-[_ANEClient virtualClient];
-[_ANEClient doEvaluateDirectWithModel:options:request:qos:error:];
-[_ANEClient beginRealTimeTask];
-[_ANEClient unloadRealTimeModel:options:qos:error:];
-[_ANEClient doPrepareChainingWithModel:options:chainingReq:qos:error:];
-[_ANEClient connectionUsedForLoadingModel:];
-[_ANEClient updatePurgeabilityLevelForModelTrackedByHash:to:];
-[_ANEClient mapIOSurfacesWithModel:request:cacheInference:error:];
-[_ANEClient enqueueSetsWithModel:outputSet:options:qos:error:];
-[_ANEClient loadModel:options:qos:error:];
-[_ANEClient unloadModel:options:qos:error:];
-[_ANEClient compiledModelExistsInCacheFor:];
-[_ANEClient conn];
-[_ANEClient endRealTimeTask];
-[_ANEClient prepareChainingWithModel:options:chainingReq:qos:error:];
-[_ANEClient buffersReadyWithModel:inputBuffers:options:qos:error:];
-[_ANEClient sessionHintWithModel:hint:options:report:error:];
-[_ANEClient doLoadModel:options:qos:error:];
-[_ANEClient compiledModelExistsFor:];
-[_ANEClient doEnqueueSetsWithModel:outputSet:options:qos:error:];
-[_ANEClient mapMutableWeightsForModel:andProcedure:mappedWeightsBuffer:size:error:];
-[_ANEClient fastConn];
-[_ANEClient unmapIOSurfacesWithModel:request:];
-[_ANEClient connectionForLoadingModel:options:];
-[_ANEClient loadRealTimeModel:options:qos:error:];
-[_ANEClient unmapMutableWeightsForModel:andProcedure:];
-[_ANEClient syncMutableWeightsForModel:andProcedure:fromOffset:withSize:error:];
-[_ANEClient purgeCompiledModelMatchingHash:];
-[_ANEClient compiledModelExistsMatchingHash:];
-[_ANEClient connectionsUsedForLoadingModels];
-[_ANEClient doLoadModelNewInstance:options:modelInstParams:qos:error:];
-[_ANEClient compiledModelExistsInCacheFor:limitToCurrentProcess:];
-[_ANEClient evaluateWithModel:options:request:qos:error:];
-[_ANEClient fastConnWithoutLock];
-[_ANEClient doBuffersReadyWithModel:inputBuffers:options:qos:error:];
-[_ANEClient reportEvaluateFailure:failureReason:qIdx:];
-[_ANEClient isAnetoolRootDaemonConnection];
-[_ANEClient purgeCompiledModel:];
-[_ANEClient echo:];
-[_ANEClient loadModelNewInstance:options:modelInstParams:qos:error:];
```
