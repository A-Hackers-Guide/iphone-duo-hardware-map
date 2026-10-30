# `WiFiUsageChannel`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 19 instance methods, 3 class methods

## Instance variables

```
B _isDFSChannel;
i _band;
Q _channel;
Q _channelFlags;
Q _channelWidth;
```

## Properties

```
@property (TQ,N,V_channel) channel;
@property (TQ,N,V_channelFlags) channelFlags;
@property (Ti,N,V_band) band;
@property (TQ,N,V_channelWidth) channelWidth;
@property (TB,N,V_isDFSChannel) isDFSChannel;
```

## Class methods

```
+[WiFiUsageChannel channelWithBssDetails:];
+[WiFiUsageChannel channelWithChannelInfo:];
+[WiFiUsageChannel channelWithScanChannel:];
```

## Instance methods

```
-[WiFiUsageChannel setChannel:];
-[WiFiUsageChannel channel];
-[WiFiUsageChannel band];
-[WiFiUsageChannel channelFlags];
-[WiFiUsageChannel channelWidth];
-[WiFiUsageChannel setBand:];
-[WiFiUsageChannel isEqualToChannel:];
-[WiFiUsageChannel hash];
-[WiFiUsageChannel description];
-[WiFiUsageChannel copyWithZone:];
-[WiFiUsageChannel setChannelWidth:];
-[WiFiUsageChannel setChannelFlags:];
-[WiFiUsageChannel isEqual:];
-[WiFiUsageChannel initWithChannel:flags:];
-[WiFiUsageChannel initWithChannel:flags:band:width:isDFS:];
-[WiFiUsageChannel initWithChannel:flags:isDFS:];
-[WiFiUsageChannel isDFSChannel];
-[WiFiUsageChannel setIsDFSChannel:];
-[WiFiUsageChannel updateDFSInfoFromSupportedChannels:];
```
