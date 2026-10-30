# `WFHotspotInterface`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFRemoteHotspotSessionDelegate`
- 5 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _scanning;
@"NSSet" _networks;
@"<WFHotspotInterfaceDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"SFRemoteHotspotSession" _hotspotSession;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (TB,N,GisScanning,V_scanning) scanning;
@property (T@"NSSet",&,V_networks) networks;
@property (T@"SFRemoteHotspotSession",&,V_hotspotSession) hotspotSession;
@property (T@"<WFHotspotInterfaceDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFHotspotInterface setScanning:];
-[WFHotspotInterface setNetworks:];
-[WFHotspotInterface isScanning];
-[WFHotspotInterface init];
-[WFHotspotInterface networks];
-[WFHotspotInterface setDelegate:];
-[WFHotspotInterface delegate];
-[WFHotspotInterface setInternalQueue:];
-[WFHotspotInterface internalQueue];
-[WFHotspotInterface session:updatedFoundDevices:];
-[WFHotspotInterface startBrowsing];
-[WFHotspotInterface stopBrowsing];
-[WFHotspotInterface _stopBrowsingRemoveCache:];
-[WFHotspotInterface enableHotspot:error:];
-[WFHotspotInterface hotspotSession];
-[WFHotspotInterface setHotspotSession:];
-[WFHotspotInterface updateNetworksWithHotspots:];
```
