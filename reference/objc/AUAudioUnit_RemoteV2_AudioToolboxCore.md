# `AUAudioUnit_RemoteV2`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit_XPC`
- 2 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<AUHostingServiceClient, std::default_delete<AUHostingServiceClient>>=""{?="__ptr_"^{AUHostingServiceClient}}} _service;
@"NSUUID" _auInstanceUUID;
```

## Instance methods

```
-[AUAudioUnit_RemoteV2 requestViewControllerWithCompletionHandler:];
-[AUAudioUnit_RemoteV2 dealloc];
-[AUAudioUnit_RemoteV2 reset];
-[AUAudioUnit_RemoteV2 _setValue:forKey:error:];
-[AUAudioUnit_RemoteV2 _valueForProperty:error:];
-[AUAudioUnit_RemoteV2 auInstanceUUID];
-[AUAudioUnit_RemoteV2 initWithXPCService:componentDescription:instance:instanceUUID:error:];
-[AUAudioUnit_RemoteV2 providesUserInterface];
```
