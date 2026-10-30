# `/System/Library/Frameworks/CrashReportExtension.framework/CrashReportExtension`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 145,888 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 35 (Size: 4688)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (18)

- `/System/Library/Frameworks/CrashReportExtension.framework/CrashReportExtension (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation (compatibility version 1.0.0, current version 97.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/swift/libswiftAccelerate.dylib (compatibility version 1.0.0, current version 82.0.0, weak)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftMetal.dylib (compatibility version 1.0.0, current version 383.1.2, weak)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftQuartzCore.dylib (compatibility version 1.0.0, current version 5.0.0, weak)`
- `/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib (compatibility version 1.0.0, current version 919.1.13, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`
- `/usr/lib/swift/libswiftsimd.dylib (compatibility version 1.0.0, current version 25.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 2 protocols)

Classes: `_TtC20CrashReportExtension14CrashedProcess`

Protocols: `_TtP20CrashReportExtension28CrashDataProviderXPCProtocol_`, `_TtP20CrashReportExtension33CrashReporterExtensionXPCProtocol_`

## Strings (55)

```
v32@0:8Q16@?<v@?@\"NSData\">24
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?Q>32
v44@0:8@16i24@28@?36
v32@0:8Q16@?24
v32@0:8@16@?24
v40@0:8@16@24@?32
v24@0:8@?<v@?@\"NSData\">16
v16@?0@\"<OS_xpc_object>\"8
v44@0:8@\"NSXPCListenerEndpoint\"16i24@\"NSArray\"28@?<v@?B>36
v24@0:8@?<v@?@\"<OS_xpc_object>\">16
v32@0:8@\"NSArray\"16@?<v@?@\"NSData\">24
v16@0:8
v24@0:8@?16
v16@?0@\"NSData\"8
v16@?0Q8
@16@0:8
v16@?0@\"NSError\"8
Extension: Ready to receive crash info
Extension: Accepting connection from host
Extension: Received crash connection (exception: %d)
CrashExtensionConfiguration initialized
CrashedProcess XPC error: %s
CrashExtensionFramework
CrashReportExtension.CrashExtensionConfiguration
init()
CrashReportExtension/CrashReportExtension.swift
Fatal error
CrashedProcess: remote object proxy does not conform to CrashDataProviderXPCProtocol
_TtC20CrashReportExtension14CrashedProcess
_TtP20CrashReportExtension33CrashReporterExtensionXPCProtocol_
_TtP20CrashReportExtension28CrashDataProviderXPCProtocol_
_images
_corpsePort
.cxx_destruct
connectTo:exception:codes:reply:
connection
setXPCType:forSelector:argumentIndex:ofReply:
synchronousRemoteObjectProxyWithErrorHandler:
getBinaryImagesWithReply:
getSymbolAddressWithImageName:symbolName:reply:
hostConnection
interfaceWithProtocol:
reason
setExportedInterface:
ext
initWithListenerEndpoint:
sendCorpsePortWithReply:
setRemoteObjectInterface:
symbolicateAddresses:reply:
dealloc
init
invalidate
resume
setExportedObject:
symbolicateAddress:reply:
```
