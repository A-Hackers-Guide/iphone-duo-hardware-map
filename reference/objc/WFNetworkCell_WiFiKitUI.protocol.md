# `WFNetworkCell` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) title;
@property (T@"NSString",C,N) subtitle;
@property (TB,N) secure;
@property (Tq,N) state;
@property (TQ,N) bars;
@property (TB,N) personalHotspot;
@property (T@"WFHotspotDetails",&,N) hotspotDetails;
@property (TB,N) connectionError;
```

## Instance methods

```
-[WFNetworkCell setBars:];
-[WFNetworkCell setSecure:];
-[WFNetworkCell setState:];
-[WFNetworkCell setConnectionError:];
-[WFNetworkCell subtitle];
-[WFNetworkCell setSubtitle:];
-[WFNetworkCell connectionError];
-[WFNetworkCell bars];
-[WFNetworkCell title];
-[WFNetworkCell setTitle:];
-[WFNetworkCell state];
-[WFNetworkCell secure];
-[WFNetworkCell setPersonalHotspot:];
-[WFNetworkCell personalHotspot];
-[WFNetworkCell hotspotDetails];
-[WFNetworkCell setHotspotDetails:];
```
