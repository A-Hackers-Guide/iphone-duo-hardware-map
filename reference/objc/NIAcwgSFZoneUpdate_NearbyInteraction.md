# `NIAcwgSFZoneUpdate`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
c _lastBtRssiValue;
B _ioStateDisplacing;
B _explicitPAITriggered;
B _currentSFInBubble;
S _btConnHandle;
q _currentZone;
```

## Properties

```
@property (Tq,R,N,V_currentZone) currentZone;
@property (TS,R,N,V_btConnHandle) btConnHandle;
@property (Tc,R,N,V_lastBtRssiValue) lastBtRssiValue;
@property (TB,R,N,V_ioStateDisplacing) ioStateDisplacing;
@property (TB,R,N,V_explicitPAITriggered) explicitPAITriggered;
@property (TB,R,N,V_currentSFInBubble) currentSFInBubble;
```

## Class methods

```
+[NIAcwgSFZoneUpdate supportsSecureCoding];
```

## Instance methods

```
-[NIAcwgSFZoneUpdate encodeWithCoder:];
-[NIAcwgSFZoneUpdate description];
-[NIAcwgSFZoneUpdate initWithCoder:];
-[NIAcwgSFZoneUpdate copyWithZone:];
-[NIAcwgSFZoneUpdate currentZone];
-[NIAcwgSFZoneUpdate lastBtRssiValue];
-[NIAcwgSFZoneUpdate btConnHandle];
-[NIAcwgSFZoneUpdate currentSFInBubble];
-[NIAcwgSFZoneUpdate explicitPAITriggered];
-[NIAcwgSFZoneUpdate initWithSFZone:btConnHandle:lastBtRssiValue:ioStateDisplacing:explicitPAITriggered:currentSFInBubble:];
-[NIAcwgSFZoneUpdate ioStateDisplacing];
```
