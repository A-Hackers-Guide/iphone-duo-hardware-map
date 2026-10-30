# `WiFiAwareRadioSchedule`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 12 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"WiFiAwareInterfaceInfo" _interfaceInfo;
B _supportsDualBand;
B _supportsSimultaneousDualBand;
@"WiFiAwareBandSchedule" _band24GHz;
@"WiFiAwareBandSchedule" _band5GHz;
@"NSNumber" _primaryChannel;
@"NSNumber" _secondaryChannel;
@"NSNumber" _infraChannel;
@"NSArray" _preferredChannels;
```

## Properties

```
@property (T@"WiFiAwareInterfaceInfo",R,N) interfaceInfo;
@property (T@"NSString",R,N) interfaceName;
@property (T@"WiFiMACAddress",R,N) interfaceAddr;
@property (TB,R,N) isEnabled;
@property (T@"WiFiAwareBandSchedule",R,N,V_band24GHz) band24GHz;
@property (T@"WiFiAwareBandSchedule",R,N,V_band5GHz) band5GHz;
@property (TB,R,N,V_supportsDualBand) supportsDualBand;
@property (TB,R,N,V_supportsSimultaneousDualBand) supportsSimultaneousDualBand;
@property (T@"NSNumber",R,N,V_primaryChannel) primaryChannel;
@property (T@"NSNumber",R,N,V_secondaryChannel) secondaryChannel;
@property (T@"NSNumber",R,N,V_infraChannel) infraChannel;
@property (T@"NSArray",R,N,V_preferredChannels) preferredChannels;
```

## Class methods

```
+[WiFiAwareRadioSchedule supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareRadioSchedule interfaceName];
-[WiFiAwareRadioSchedule isEnabled];
-[WiFiAwareRadioSchedule encodeWithCoder:];
-[WiFiAwareRadioSchedule description];
-[WiFiAwareRadioSchedule initWithCoder:];
-[WiFiAwareRadioSchedule copyWithZone:];
-[WiFiAwareRadioSchedule preferredChannels];
-[WiFiAwareRadioSchedule band24GHz];
-[WiFiAwareRadioSchedule band5GHz];
-[WiFiAwareRadioSchedule detailedDescriptionWithChangedOptions:previousSchedule:];
-[WiFiAwareRadioSchedule detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:];
-[WiFiAwareRadioSchedule infraChannel];
-[WiFiAwareRadioSchedule initWithInterfaceInfo:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannels:];
-[WiFiAwareRadioSchedule interfaceAddr];
-[WiFiAwareRadioSchedule interfaceInfo];
-[WiFiAwareRadioSchedule primaryChannel];
-[WiFiAwareRadioSchedule secondaryChannel];
-[WiFiAwareRadioSchedule supportsDualBand];
-[WiFiAwareRadioSchedule supportsSimultaneousDualBand];
```
