# `AHTBootLoader`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`](../userland/System__Library__PrivateFrameworks__AppleHIDTransportSupport.framework__AppleHIDTransportSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 33 instance methods, 5 class methods

## Instance variables

```
B _needsRestoreUpdate;
B _supportsMemoryDump;
I _imageTag;
I _service;
I _connect;
I _machPort;
@"NSString" _personality;
@"AHTDevice" _device;
@"AHTInterface" _interface;
@"NSString" _type;
```

## Properties

```
@property (TI,N,V_service) service;
@property (TI,N,V_connect) connect;
@property (TI,N,V_machPort) machPort;
@property (T@"NSString",R,N,V_personality) personality;
@property (T@"AHTDevice",R,N,V_device) device;
@property (T@"AHTInterface",R,N,V_interface) interface;
@property (T@"NSString",R,N,V_type) type;
@property (TI,R,N,V_imageTag) imageTag;
@property (TB,R,N,V_needsRestoreUpdate) needsRestoreUpdate;
@property (TB,R,N,V_supportsMemoryDump) supportsMemoryDump;
```

## Class methods

```
+[AHTBootLoader withService:];
+[AHTBootLoader allBootloaders];
+[AHTBootLoader frameworkToDriverOptions:];
+[AHTBootLoader withDevice:service:];
+[AHTBootLoader withParent:service:];
```

## Instance methods

```
-[AHTBootLoader connect];
-[AHTBootLoader close];
-[AHTBootLoader open:];
-[AHTBootLoader device];
-[AHTBootLoader setService:];
-[AHTBootLoader dealloc];
-[AHTBootLoader personality];
-[AHTBootLoader machPort];
-[AHTBootLoader setConnect:];
-[AHTBootLoader interface];
-[AHTBootLoader type];
-[AHTBootLoader service];
-[AHTBootLoader description];
-[AHTBootLoader isOpen];
-[AHTBootLoader initWithService:];
-[AHTBootLoader setMachPort:];
-[AHTBootLoader updateProperty:property:options:error:];
-[AHTBootLoader destroyMachPort];
-[AHTBootLoader createMachPort:];
-[AHTBootLoader clearMemoryDumps:];
-[AHTBootLoader dispatchSourceForNotification:action:error:];
-[AHTBootLoader getMemoryDumpLevel:error:];
-[AHTBootLoader getMemoryDumps:error:];
-[AHTBootLoader getProperty:property:options:error:];
-[AHTBootLoader getRegistryProperties];
-[AHTBootLoader imageTag];
-[AHTBootLoader initWithParent:service:];
-[AHTBootLoader needsRestoreUpdate];
-[AHTBootLoader overridePersonality:error:];
-[AHTBootLoader overrideProperties:error:];
-[AHTBootLoader reloadProperties:error:];
-[AHTBootLoader setMemoryDumpLevel:error:];
-[AHTBootLoader supportsMemoryDump];
```
