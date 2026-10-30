# `WiFiAwareDataPathState`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 11 instance variables, 11 properties, 26 instance methods, 4 class methods

## Instance variables

```
@"WiFiAwareInterfaceInfo" _interfaceInfo;
I _totalSessionCounter;
I _establishedSessionCounter;
I _sessionWith24GOnlyPeerCount;
I _rtmSessionRefCount;
I _rtmSessionWith24GOnlyCount;
I _rtmLowLatencySessionRefCount;
@"NSArray" _ndiInfos;
@"NSArray" _preferredChannelNumbers;
@"NSArray" _preferredChannelClasses;
@"NSArray" _ndiSessionInfos;
```

## Properties

```
@property (T@"WiFiAwareInterfaceInfo",R,N) interfaceInfo;
@property (TI,R,N,V_totalSessionCounter) totalSessionCounter;
@property (TI,R,N,V_establishedSessionCounter) establishedSessionCounter;
@property (TI,R,N,V_sessionWith24GOnlyPeerCount) sessionWith24GOnlyPeerCount;
@property (TI,R,N,V_rtmSessionRefCount) rtmSessionRefCount;
@property (TI,R,N,V_rtmSessionWith24GOnlyCount) rtmSessionWith24GOnlyCount;
@property (TI,R,N,V_rtmLowLatencySessionRefCount) rtmLowLatencySessionRefCount;
@property (T@"NSArray",R,N,V_ndiInfos) ndiInfos;
@property (T@"NSArray",R,N,V_preferredChannelNumbers) preferredChannelNumbers;
@property (T@"NSArray",R,N,V_preferredChannelClasses) preferredChannelClasses;
@property (T@"NSArray",R,N,V_ndiSessionInfos) ndiSessionInfos;
```

## Class methods

```
+[WiFiAwareDataPathState supportsSecureCoding];
+[WiFiAwareDataPathState currentState];
+[WiFiAwareDataPathState queryNANDataPathState];
+[WiFiAwareDataPathState queryNANDataPathState];
```

## Instance methods

```
-[WiFiAwareDataPathState interfaceName];
-[WiFiAwareDataPathState isEnabled];
-[WiFiAwareDataPathState encodeWithCoder:];
-[WiFiAwareDataPathState description];
-[WiFiAwareDataPathState initWithCoder:];
-[WiFiAwareDataPathState copyWithZone:];
-[WiFiAwareDataPathState stringForSessionState:];
-[WiFiAwareDataPathState ndiSessionInfos];
-[WiFiAwareDataPathState descriptionWithChangedOptions:];
-[WiFiAwareDataPathState descriptionWithChangedOptions:forceAllChangedOptions:];
-[WiFiAwareDataPathState establishedSessionCounter];
-[WiFiAwareDataPathState getFormattedDataPathStateDescription];
-[WiFiAwareDataPathState initWithInterfaceInfo:sessionCounters:channelConfig:ndiInfos:ndiSessionInfos:];
-[WiFiAwareDataPathState interfaceAddr];
-[WiFiAwareDataPathState interfaceInfo];
-[WiFiAwareDataPathState mapSessionStateToNumber:];
-[WiFiAwareDataPathState ndiInfos];
-[WiFiAwareDataPathState preferredChannelClasses];
-[WiFiAwareDataPathState preferredChannelNumbers];
-[WiFiAwareDataPathState rtmLowLatencySessionRefCount];
-[WiFiAwareDataPathState rtmSessionRefCount];
-[WiFiAwareDataPathState rtmSessionWith24GOnlyCount];
-[WiFiAwareDataPathState sessionWith24GOnlyPeerCount];
-[WiFiAwareDataPathState stringForQosType:];
-[WiFiAwareDataPathState stringForSecurity:];
-[WiFiAwareDataPathState totalSessionCounter];
```
