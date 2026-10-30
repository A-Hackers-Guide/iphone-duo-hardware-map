# `AHTLoader`

- Image: [`/System/Library/PrivateFrameworks/AppleHIDTransportSupport.framework/AppleHIDTransportSupport`](../userland/System__Library__PrivateFrameworks__AppleHIDTransportSupport.framework__AppleHIDTransportSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 7 class methods

## Instance variables

```
I _imageTag;
I _loadingGroup;
I _service;
I _connect;
@"NSString" _name;
```

## Properties

```
@property (TI,N,V_service) service;
@property (TI,N,V_connect) connect;
@property (T@"NSString",R,N,V_name) name;
@property (TI,R,N,V_imageTag) imageTag;
@property (TI,R,N,V_loadingGroup) loadingGroup;
```

## Class methods

```
+[AHTLoader allDevices];
+[AHTLoader withService:];
+[AHTLoader bootloaderPropertiesForImageTag:];
+[AHTLoader errorFromAfuKextResult:error:];
+[AHTLoader errorFromKernel:error:];
+[AHTLoader registryPropertiesForService:];
+[AHTLoader withName:];
```

## Instance methods

```
-[AHTLoader connect];
-[AHTLoader close];
-[AHTLoader open:];
-[AHTLoader setService:];
-[AHTLoader dealloc];
-[AHTLoader fullDescription];
-[AHTLoader setConnect:];
-[AHTLoader service];
-[AHTLoader description];
-[AHTLoader name];
-[AHTLoader initWithService:];
-[AHTLoader loadingGroup];
-[AHTLoader imageTag];
-[AHTLoader loadImage:payloadOnly:options:error:];
-[AHTLoader overrideFDR:fdrClass:fdrSubclass:error:];
-[AHTLoader overrideNextLoadOptions:error:];
```
