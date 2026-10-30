# `CWFMLOLink`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
C _channel;
B _isPrimaryLink;
i _band;
i _width;
i _subchannel;
```

## Properties

```
@property (Ti,N,V_band) band;
@property (TC,N,V_channel) channel;
@property (Ti,N,V_width) width;
@property (Ti,N,V_subchannel) subchannel;
@property (TB,N,V_isPrimaryLink) isPrimaryLink;
```

## Class methods

```
+[CWFMLOLink supportsSecureCoding];
```

## Instance methods

```
-[CWFMLOLink setChannel:];
-[CWFMLOLink channel];
-[CWFMLOLink band];
-[CWFMLOLink setBand:];
-[CWFMLOLink encodeWithCoder:];
-[CWFMLOLink hash];
-[CWFMLOLink description];
-[CWFMLOLink initWithCoder:];
-[CWFMLOLink setWidth:];
-[CWFMLOLink width];
-[CWFMLOLink copyWithZone:];
-[CWFMLOLink isEqual:];
-[CWFMLOLink isEqualToMLOLink:];
-[CWFMLOLink isPrimaryLink];
-[CWFMLOLink setIsPrimaryLink:];
-[CWFMLOLink setSubchannel:];
-[CWFMLOLink subchannel];
```
