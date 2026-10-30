# `WiFiChannel`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _is2_4GHz;
B _is5GHz;
B _is6GHz;
B _isDFS;
B _extensionChannelAbove;
I _channelNumber;
q _bandwidth;
```

## Properties

```
@property (TB,R,N,V_extensionChannelAbove) extensionChannelAbove;
@property (TI,R,N,V_channelNumber) channelNumber;
@property (TB,R,N,V_is2_4GHz) is2_4GHz;
@property (TB,R,N,V_is5GHz) is5GHz;
@property (TB,R,N,V_is6GHz) is6GHz;
@property (TB,R,N,V_isDFS) isDFS;
@property (Tq,R,N,V_bandwidth) bandwidth;
```

## Class methods

```
+[WiFiChannel supportsSecureCoding];
```

## Instance methods

```
-[WiFiChannel isDFS];
-[WiFiChannel is6GHz];
-[WiFiChannel initWithChannelNumber:bandwidth:is2_4GHz:is5GHz:is6GHz:isDFS:extensionChannelAbove:];
-[WiFiChannel encodeWithCoder:];
-[WiFiChannel hash];
-[WiFiChannel description];
-[WiFiChannel initWithCoder:];
-[WiFiChannel extensionChannelAbove];
-[WiFiChannel is2_4GHz];
-[WiFiChannel bandwidth];
-[WiFiChannel copyWithZone:];
-[WiFiChannel isEqual:];
-[WiFiChannel is5GHz];
-[WiFiChannel channelNumber];
```
