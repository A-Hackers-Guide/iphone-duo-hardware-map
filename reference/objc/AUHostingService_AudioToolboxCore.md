# `AUHostingService`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUHostingServiceProtocol`
- 4 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"AURemoteHost" _host;
@"NSXPCConnection" _connection;
{AudioComponentDescription="componentType"I"componentSubType"I"componentManufacturer"I"componentFlags"I"componentFlagsMask"I} _componentDescription;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} _instanceUUID;
```

## Class methods

```
+[AUHostingService instancesRespondToSelector:];
+[AUHostingService conformsToProtocol:];
```

## Instance methods

```
-[AUHostingService dealloc];
-[AUHostingService forwardingTargetForSelector:];
-[AUHostingService initWithConnection:];
-[AUHostingService closeHost:];
-[AUHostingService establishConnection:];
-[AUHostingService loadAudioUnitInRemoteHost:config:reply:];
-[AUHostingService retrieveAudioUnitInstanceID:];
```
