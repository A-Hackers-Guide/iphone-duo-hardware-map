# `/System/Library/PrivateFrameworks/CoreGPS.framework/CoreGPS.dylib`

iOS 27.2 dyld shared cache image. Version `367.0.2.0.0`. **[DSC]**

## Linked libraries (19)

- `/usr/lib/libprotobuf.dylib`
- `/usr/lib/libcompression.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libTelephonyUtilDynamic.dylib`
- `/usr/lib/libPCITransport.dylib`
- `/usr/lib/libMobileGestalt.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 4 classes, 3 protocols, 26 methods, 4 properties

### Class pages

Every class and protocol, with its methods: [`NSObject`](../objc/NSObject_CoreGPS.dylib.protocol.md), [`NSXPCListenerDelegate`](../objc/NSXPCListenerDelegate_CoreGPS.dylib.protocol.md), [`_TtC6GPSXPC12GPSXPCClient`](../objc/_TtC6GPSXPC12GPSXPCClient_CoreGPS.dylib.md), [`_TtC6GPSXPC12GPSXPCLogger`](../objc/_TtC6GPSXPC12GPSXPCLogger_CoreGPS.dylib.md), [`_TtC6GPSXPC17ALServiceDelegate`](../objc/_TtC6GPSXPC17ALServiceDelegate_CoreGPS.dylib.md), [`_TtC7CoreGPS13CoreGPSDevice`](../objc/_TtC7CoreGPS13CoreGPSDevice_CoreGPS.dylib.md), [`_TtP6GPSXPC14GPSXPCProtocol_`](../objc/_TtP6GPSXPC14GPSXPCProtocol__CoreGPS.dylib.protocol.md)

### Classes

`_TtC6GPSXPC12GPSXPCClient`, `_TtC6GPSXPC12GPSXPCLogger`, `_TtC6GPSXPC17ALServiceDelegate`, `_TtC7CoreGPS13CoreGPSDevice`

### Protocols

`NSObject`, `NSXPCListenerDelegate`, `_TtP6GPSXPC14GPSXPCProtocol_`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Swift types (5)

`CoreGPS.CoreGPSDevice`, `GPSXPC.ALServiceDelegate:`, `GPSXPC.GPSXPCClient`, `GPSXPC.GPSXPCDataService`, `GPSXPC.GPSXPCLogger`

## Strings (27)

```
client,receive %s
proxyErrorHandler: %s
client,invalidationHandler %@, pid %d exits
service,onInterrupt
service,disconnectHandler,%{public}@
client,interruptionHandler %{public}@
Invalid proxy
serviceName %{public}s started
CoreGPSDevice,init
CoreGPS,isAvailable,default,%{bool,public}d
Connected to xpc service pid: %{public}d
Try connecting xpc service %{public}s
remoteObjectProxyWithErrorHandler failed%{public}@
client,sent %{public}s
service,invalidationHandler,%{public}@
Activated Connection from process:%{public}d, details:(%{public}@)
CoreGPS,useLegacyLibXpc,%{bool,public}d
Entitlement check failed for pid:%{public}d, connection rejected
Entitlement check passed for pid: %{public}d
service,interruptionHandler,%{public}@
New XPC Connection from process:%{public}d, details:(%{public}@)
isAvailable() returned false. Please check this function before using CoreGPS. But inited anyway!!!
CoreGPS,forceAvailable,%{bool,public}d
com.apple.coregps
ForceCoreGPSAvailable
GPSXPC.ALServiceDelegate
init()
```
