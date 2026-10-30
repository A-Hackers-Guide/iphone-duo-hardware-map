# `_ANEDaemonConnection`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_ANEDaemonProtocol`
- 2 instance variables, 2 properties, 22 instance methods, 3 class methods

## Instance variables

```
B _restricted;
@"NSXPCConnection" _daemonConnection;
```

## Properties

```
@property (T@"NSXPCConnection",R,N,V_daemonConnection) daemonConnection;
@property (TB,R,N,V_restricted) restricted;
```

## Class methods

```
+[_ANEDaemonConnection daemonConnection];
+[_ANEDaemonConnection daemonConnectionRestricted];
+[_ANEDaemonConnection userDaemonConnection];
```

## Instance methods

```
-[_ANEDaemonConnection loadModelNewInstance:options:modelInstParams:qos:withReply:];
-[_ANEDaemonConnection updateSourcePathForModelTrackedByHash:to:withReply:];
-[_ANEDaemonConnection endRealTimeTaskWithReply:];
-[_ANEDaemonConnection init];
-[_ANEDaemonConnection unloadModel:options:qos:withReply:];
-[_ANEDaemonConnection dealloc];
-[_ANEDaemonConnection echo:withReply:];
-[_ANEDaemonConnection initWithMachServiceName:restricted:];
-[_ANEDaemonConnection loadModel:sandboxExtension:options:qos:withReply:];
-[_ANEDaemonConnection compileModel:sandboxExtension:options:qos:withReply:];
-[_ANEDaemonConnection prepareChainingWithModel:options:chainingReq:qos:withReply:];
-[_ANEDaemonConnection purgeCompiledModelMatchingHash:withReply:];
-[_ANEDaemonConnection compiledModelExistsInCacheFor:limitToCurrentProcess:withReply:];
-[_ANEDaemonConnection restricted];
-[_ANEDaemonConnection compiledModelExistsMatchingHash:withReply:];
-[_ANEDaemonConnection beginRealTimeTaskWithReply:];
-[_ANEDaemonConnection compiledModelExistsFor:withReply:];
-[_ANEDaemonConnection reportTelemetryToPPS:playload:];
-[_ANEDaemonConnection updatePurgeabilityLevelForModelTrackedByHash:to:withReply:];
-[_ANEDaemonConnection updateCachedModelLocationForModelTrackedByHash:toAppGroup:withReply:];
-[_ANEDaemonConnection daemonConnection];
-[_ANEDaemonConnection purgeCompiledModel:withReply:];
```
