# `_ANEDaemonProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance methods

```
-[_ANEDaemonProtocol loadModelNewInstance:options:modelInstParams:qos:withReply:];
-[_ANEDaemonProtocol updateSourcePathForModelTrackedByHash:to:withReply:];
-[_ANEDaemonProtocol unloadModel:options:qos:withReply:];
-[_ANEDaemonProtocol loadModel:sandboxExtension:options:qos:withReply:];
-[_ANEDaemonProtocol compileModel:sandboxExtension:options:qos:withReply:];
-[_ANEDaemonProtocol prepareChainingWithModel:options:chainingReq:qos:withReply:];
-[_ANEDaemonProtocol purgeCompiledModelMatchingHash:withReply:];
-[_ANEDaemonProtocol compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:];
-[_ANEDaemonProtocol compiledModelExistsMatchingHash:withReply:];
-[_ANEDaemonProtocol compiledModelExistsFor:withReply:];
-[_ANEDaemonProtocol reportTelemetryToPPS:playload:];
-[_ANEDaemonProtocol updatePurgeabilityLevelForModelTrackedByHash:to:withReply:];
-[_ANEDaemonProtocol updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:];
-[_ANEDaemonProtocol purgeCompiledModel:withReply:];
```
